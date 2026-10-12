# Rush Duel Scripting

**Prerequisites:** [Lua Essentials](lua-essentials) and
[Effect Callbacks](effect-callbacks). **Goal:** read a complete Rush effect,
separate its requirement from its resolution, and use the `RD` helpers correctly.

Rush scripts still use Cards, Effects, Groups, and the `Duel` API. This project's
Rush implementation adds a Lua rules layer and helper library. Learn that layer
before adapting an OCG/TCG script.

## Choose The Right Layer

| Layer | What it owns |
| --- | --- |
| `rush_cards.cdb` | Rush names, text, IDs, type bits, stats, and prompt strings. |
| `Rush/Scripts/c<ID>.lua` | The imported behavior of an individual Rush card. |
| `Rush/Utilities/RD*.lua` | Shared requirements, actions, rules, and summon procedures. |
| `Card`, `Effect`, `Group`, `Duel` | The underlying engine operations used by those helpers. |
| MDPro4's Rush mode and bootstrap | Loading and initializing the Rush environment for a duel. |

In the imported upstream `special.lua`, the `RD*.lua` files load first,
`RD = RushDuel` supplies the short alias, and `Auxiliary.PreloadUds()` calls
`RD.Init()`. MDPro4 packages these through its own Rush bootstrap in
`Data/rush_scripts.zip`. Its local host selects Rush mode and installs the
session hook. A card's `initial_effect` should register that card's effects;
it should not call `RD.Init()` again.

::: tip Verify the environment first
An “attempt to index a nil value” on `RD` points to a missing rules/helper load.
The card database's Rush label alone does not initialize the duel. See
[Card Database](../guides/card-database#rush-card-data-and-runtime-rules).
:::

## A Complete First Example: Mystic Dealer

Imported [card `120105006`](/examples/rush-cards/120105006) sends one Spellcaster from the hand to the GY as its
requirement, then draws one card. This is its effect structure with the script
table renamed from `cm` to `s` for consistency with the other lessons:

```lua
local s,id=GetID()

function s.initial_effect(c)
    local e1=Effect.CreateEffect(c)
    e1:SetDescription(aux.Stringid(id,0))
    e1:SetCategory(CATEGORY_DRAW)
    e1:SetType(EFFECT_TYPE_IGNITION)
    e1:SetProperty(EFFECT_FLAG_PLAYER_TARGET)
    e1:SetRange(LOCATION_MZONE)
    e1:SetCost(s.cost)
    e1:SetTarget(s.target)
    e1:SetOperation(s.operation)
    c:RegisterEffect(e1)
end

function s.costfilter(c)
    return c:IsRace(RACE_SPELLCASTER) and c:IsAbleToGraveAsCost()
end
s.cost=RD.CostSendHandToGrave(s.costfilter,1,1)

function s.target(e,tp,eg,ep,ev,re,r,rp,chk)
    if chk==0 then return Duel.IsPlayerCanDraw(tp,1) end
    RD.TargetDraw(tp,1)
end

function s.operation(e,tp,eg,ep,ev,re,r,rp)
    RD.Draw()
end
```

Trace it in four steps:

1. `CostSendHandToGrave` **returns a callback**. The engine later invokes that
   callback to check and pay the requirement. `1,1` requires exactly one card.
2. `IsAbleToGraveAsCost` asks about paying a cost, so the filter matches the
   helper's `REASON_COST` action.
3. `RD.TargetDraw(tp,1)` stores the player and draw count on the Chain and
   announces the operation. The earlier `chk==0` branch checks draw legality.
4. `RD.Draw()` reads that stored player/count and calls `Duel.Draw` with
   `REASON_EFFECT` when resolving.

The target callback here targets a **player**. It never selects a card target.
Its name does not imply `EFFECT_FLAG_CARD_TARGET`.

## Helper Shapes

Read the helper's implementation or [Rush reference](/rush/api/functions/)
before deciding whether to call it during initialization or resolution.

| Shape | Example | Correct use |
| --- | --- | --- |
| Callback factory | [`RD.CostSendDeckTopToGrave(1)`](/rush/api/functions/RushDuel/CostSendDeckTopToGrave) | Pass its returned function to `SetCost`. |
| Immediate action | [`RD.TargetDraw(tp,1)`](/rush/api/functions/RushDuel/TargetDraw) | Call inside the target callback after `chk==0`. |
| Resolution action | [`RD.Draw()`](/rush/api/functions/RushDuel/Draw) | Call inside the operation; compare its numeric result if later actions depend on it. |
| Condition taking an Effect | [`RD.MaximumMode(e)`](/rush/api/functions/RushDuel/MaximumMode) | Pass `RD.MaximumMode` to `SetCondition`. |
| Predicate taking a Card | [`RD.IsSummonTurn(c)`](/rush/api/functions/RushDuel/IsSummonTurn) | Call with the Card while evaluating a condition. |

For example, this is valid **inside `initial_effect(c)`**:

```lua
e1:SetCost(RD.CostSendDeckTopToGrave(1))
```

This helper already checks `Duel.IsPlayerCanDiscardDeckAsCost(tp,1)` in its
`chk==0` branch and performs `Duel.DiscardDeck(tp,1,REASON_COST)` when paying.
It does not also draw a card; drawing belongs to the operation.

## A Requirement Can Include A Condition

Some requirements describe a game state rather than an action to pay. For
example, imported `c120101001.lua` checks that the monster was Normal Summoned
this turn and that its controller has at most one monster:

```lua
function s.condition(e,tp,eg,ep,ev,re,r,rp)
    return RD.IsSummonTurn(e:GetHandler())
        and Duel.GetFieldGroupCount(tp,LOCATION_MZONE,0)<=1
end
```

`RD.IsSummonTurn` checks the Normal Summon reason, status, and a flag registered
by the Rush rules layer. `RD.IsSpecialSummonTurn` is a different helper. Choose
the one that matches the card text instead of treating “summoned” as one broad
test.

## Rules Already Provided By The Rush Layer

The imported `RDRule.lua` implements draw-to-five behavior, a three-column
field, additional Normal Summons, skipped Standby/Main Phase 2, and its Rush
activation restrictions. Its draw formula is
`math.max(1,5-currentHandCount)`, so a hand of five or more draws one card.

It also tracks used monster effects through card flags, including separate
labels for Maximum side pieces. Follow comparable Rush cards before adding
`SetCountLimit(1,id)`: an OCG/TCG card-name limit can impose a different
restriction on multiple copies. `RD.Init()` also overrides `Duel.BreakEffect`
with an empty function in this implementation. Do not assume an OCG/TCG timing
recipe has identical behavior after copying it into Rush.

These describe the **imported implementation**, not a replacement for a card's
text or rulings. Test the actual packaged runtime used by the game.

## Test This Example

| Setup | Expected observation |
| --- | --- |
| One Spellcaster in hand; drawing is legal. | Offer the effect, send exactly one qualifying card as cost, draw one on resolution. |
| No qualifying card in hand. | Do not offer the effect. |
| A restriction prevents sending that card as cost. | That card must not pay the requirement. |
| A restriction prevents drawing. | Do not offer the effect even when the hand contains a valid cost. |
| The same monster already used its effect this turn. | Check the Rush rules layer's used-effect restriction. |
| A second copy is on the field. | Verify its own activation separately; do not silently impose a shared OCG/TCG name limit. |

Next, read [Maximum, Fusion, and Ritual](rush-summon-procedures). For a helper
you do not recognize, open the [Rush function reference](/rush/api/functions/)
and follow its source before adapting a larger script.

## Source Trail

This lesson follows the imported `Rush/Utilities/special.lua`, `RDRule.lua`,
`RDCost.lua`, `RDTarget.lua`, and `RDCondition.lua`, plus
`Rush/Scripts/c120105006.lua` and `c120101001.lua`. The game wiring was checked
against MDPro4's `RushDuelScripts.cs` and `Card.IsRushDuelCard()`.
