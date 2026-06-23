# Activation Legality

Activation legality is the part of a script that answers: "May this effect be
activated right now?"

Most of that work happens in `condition`, `cost`, and `target`. The important
habit is to separate legality checks from resolution. A legal activation can
still resolve without doing anything if its target disappears or a required
zone closes.

## The Legality Flow

For an activated effect, the engine checks roughly this shape:

1. Is the effect type/timing available?
2. Is the handler in the right place?
3. Does `condition` return true?
4. Can the `cost` be paid with `chk==0`?
5. Does `target` return true with `chk==0`?
6. If activated, pay cost and select targets.
7. Later, resolve the operation.

This is why target and cost callbacks must be careful: the check branch is not
the same as the real activation branch.

## `chk==0`

In target and cost functions, `chk==0` means the engine is asking if activation
is legal. Do not pay costs or move cards in this branch.

```lua
function s.target(e,tp,eg,ep,ev,re,r,rp,chk)
    if chk==0 then
        return Duel.IsExistingMatchingCard(s.filter,tp,LOCATION_MZONE,0,1,nil)
    end
    Duel.SetOperationInfo(0,CATEGORY_DESTROY,nil,1,tp,LOCATION_MZONE)
end
```

The non-check branch is where you select targets, announce operation info, or
store labels that the operation will read.

## Common Legality Questions

| Question | Typical check |
| --- | --- |
| Is the handler in the right place? | `SetRange`, `c:IsLocation(...)` |
| Is the phase right? | `Duel.IsMainPhase()`, `Duel.IsBattlePhase()`, `Duel.IsPhase(...)` |
| Is a card available? | `Duel.IsExistingMatchingCard(...)` |
| Can the card be targeted? | `Duel.IsExistingTarget(...)` and the `chkc` branch |
| Can the player perform the action? | `Duel.IsPlayerCanDraw(...)`, `Duel.GetLocationCount(...)` |
| Can the cost be paid? | `Duel.CheckLPCost(...)`, `Duel.CheckReleaseGroup(...)` |
| Can the monster be Special Summoned? | `c:IsCanBeSpecialSummoned(...)`, `Duel.GetLocationCount(...)` |
| Is the effect once per turn? | `SetCountLimit(...)` |

## Explicit vs Implicit Requirements

Card text usually gives explicit requirements before the colon. Those are good
condition/cost/target checks. Some legality requirements are implicit in the
action instead:

| Intended action | Implicit legality check |
| --- | --- |
| Draw cards. | `Duel.IsPlayerCanDraw(...)` |
| Special Summon. | `Duel.GetLocationCount(...)` and `Card.IsCanBeSpecialSummoned(...)` |
| Add to hand. | a filter with `Card.IsAbleToHand` or the relevant able-to helper |
| Banish. | a filter with `Card.IsAbleToRemove` or `Card.IsAbleToRemoveAsCost` |
| Equip. | an available target plus legal equip state/checks |
| Inflict damage or recover LP. | target player/amount can be announced, and any card-dependent amount has a legal source |

Do not put every implicit action check into `condition`. Conditions should
answer timing and event questions. Action availability usually belongs in
`target` or `cost`, because those callbacks already have the `chk==0` check
branch.

## What Is Not A Condition

Some phrases in card text are handled by effect setup instead of a Condition
callback.

| Text or rule shape | Usual script home |
| --- | --- |
| "Once per turn", "once per Duel", shared once-per-turn wording | [`Effect.SetCountLimit`](/api/functions/Effect/SetCountLimit) |
| "(Quick Effect)" | [`Effect.SetType`](/api/functions/Effect/SetType) with `EFFECT_TYPE_QUICK_O` or `EFFECT_TYPE_QUICK_F` |
| "during the Damage Step" or "even during damage calculation" | [`Effect.SetProperty`](/api/functions/Effect/SetProperty) with Damage Step flags |
| costs and activation restrictions | the `cost` callback, using `chk==0` for checks and the real branch for applying restrictions |

The Condition callback still handles fine timing details. For example, an
ATK/DEF modifier that is legal in the Damage Step but not after damage
calculation can pair `EFFECT_FLAG_DAMAGE_STEP` with a phase check:

```lua
e1:SetProperty(EFFECT_FLAG_DAMAGE_STEP)
e1:SetCondition(aux.dscon)
```

In the local `utility.lua`, `aux.dscon` returns true outside the Damage Phase
and during the Damage Phase before [`Duel.IsDamageCalculated`](/api/functions/Duel/IsDamageCalculated)
becomes true. Effects that are also legal during damage calculation use
`EFFECT_FLAG_DAMAGE_CAL` as well, and should still keep any card-specific
timing checks in their condition.

## Damage Step Legality

Damage Step scripting is a common source of accidental legality bugs. The setup
flags open the timing window; the condition decides whether this specific effect
should be allowed at the current point inside that window.

Cyber Dragon Infinity (`c10443957.lua`) shows the shape for a negation Quick
Effect:

```lua
e3:SetType(EFFECT_TYPE_QUICK_O)
e3:SetCode(EVENT_CHAINING)
e3:SetProperty(EFFECT_FLAG_DAMAGE_STEP+EFFECT_FLAG_DAMAGE_CAL)
e3:SetCondition(c10443957.discon)

function c10443957.discon(e,tp,eg,ep,ev,re,r,rp)
    return not e:GetHandler():IsStatus(STATUS_BATTLE_DESTROYED)
        and Duel.IsChainNegatable(ev)
end
```

The flags say the effect may be offered in the Damage Step and during damage
calculation. The condition still rejects a handler already marked with
`STATUS_BATTLE_DESTROYED` and checks whether the current Chain Link can be
negated with [`Duel.IsChainNegatable`](/api/functions/Duel/IsChainNegatable).
That pattern is local-script-backed; the exact real-card timing still depends
on the effect's official text and rulings.

## Costs Can Apply Restrictions

Some effects have an activation restriction that must be checked before
activation and then applied immediately once the effect is activated. Red-Eyes
Fusion (`c6172122.lua`) is a local example:

```lua
function c6172122.cost(e,tp,eg,ep,ev,re,r,rp,chk)
    if chk==0 then
        return Duel.GetActivityCount(tp,ACTIVITY_SUMMON)==0
            and Duel.GetActivityCount(tp,ACTIVITY_SPSUMMON)==0
    end
    local e1=Effect.CreateEffect(e:GetHandler())
    e1:SetType(EFFECT_TYPE_FIELD)
    e1:SetCode(EFFECT_CANNOT_SUMMON)
    e1:SetProperty(EFFECT_FLAG_PLAYER_TARGET+EFFECT_FLAG_OATH)
    e1:SetTargetRange(1,0)
    e1:SetReset(RESET_PHASE+PHASE_END)
    Duel.RegisterEffect(e1,tp)
end
```

The `chk==0` branch only asks whether the player already Summoned this turn.
The real branch registers the oath-style restriction. Do not register that
restriction during `chk==0`; the engine may call the check branch without the
player actually activating the effect.

## Optional Effects Should Have A Legal Outcome

Optional activated effects should normally be unavailable if they cannot make a
legal attempt. For example, a search effect should check that a matching card
exists and can be added to the hand.

```lua
function s.thfilter(c)
    return c:IsSetCard(0x123) and c:IsAbleToHand()
end

function s.thtg(e,tp,eg,ep,ev,re,r,rp,chk)
    if chk==0 then
        return Duel.IsExistingMatchingCard(s.thfilter,tp,LOCATION_DECK,0,1,nil)
    end
    Duel.SetOperationInfo(0,CATEGORY_TOHAND,nil,1,tp,LOCATION_DECK)
end
```

The operation may still fail if the Deck changes before resolution. Legality
only proves that the activation was valid when chosen.

When an effect will free a zone as part of its cost or procedure, count that
freed zone. Local scripts commonly use helpers such as
[`Duel.GetMZoneCount`](/api/functions/Duel/GetMZoneCount) when the cards to
leave the Monster Zone are already known. A plain
[`Duel.GetLocationCount`](/api/functions/Duel/GetLocationCount) check can be
too strict for effects that Tribute, release, or move their own monster before
placing another card.

## Mandatory Effects Still Resolve Carefully

Mandatory trigger effects normally activate when their event happens, even if
some later action may no longer be possible. Their check branch is often broad:

```lua
function s.mandtarg(e,tp,eg,ep,ev,re,r,rp,chk)
    if chk==0 then return true end
    Duel.SetOperationInfo(0,CATEGORY_DAMAGE,nil,0,1-tp,500)
end
```

The operation still checks the current state before applying an action. A
mandatory trigger is not permission to skip resolution checks.

## Target Rechecks With `chkc`

Targeting effects often include a `chkc` branch. It tells the client whether a
manually chosen card is a legal target for this effect.

```lua
function s.target(e,tp,eg,ep,ev,re,r,rp,chk,chkc)
    if chkc then
        return chkc:IsControler(tp) and chkc:IsLocation(LOCATION_MZONE)
            and s.filter(chkc)
    end
    if chk==0 then
        return Duel.IsExistingTarget(s.filter,tp,LOCATION_MZONE,0,1,nil)
    end
    Duel.SelectTarget(tp,s.filter,tp,LOCATION_MZONE,0,1,1,nil)
end
```

The `chkc` branch should match the same target rules used by
`Duel.SelectTarget`.

## Resolution Is Separate

Legal activation does not guarantee successful resolution. Cards may move, be
flipped face-down, become unaffected, or stop being related to the effect.

```lua
local tc=Duel.GetFirstTarget()
if tc and tc:IsRelateToEffect(e) then
    Duel.Destroy(tc,REASON_EFFECT)
end
```

Use activation checks to make the effect legal. Use resolution checks to keep it
correct after the game state changes.

## Common Mistakes

| Mistake | Safer pattern |
| --- | --- |
| Paying cost during `chk==0`. | Only return whether the cost can be paid, then pay later. |
| Using `SelectMatchingCard` for an effect that targets. | Use `SelectTarget` and relation checks. |
| Forgetting zone checks for Special Summons or setting cards. | Check `Duel.GetLocationCount` or the relevant summon legality function. |
| Assuming a target is still valid at resolution. | Check `tc and tc:IsRelateToEffect(e)`. |
| Announcing a category that the operation does not perform. | Match `SetCategory` and `SetOperationInfo` to the real action. |

Relevant API pages:

- [`Effect.SetType`](/api/functions/Effect/SetType)
- [`Effect.SetProperty`](/api/functions/Effect/SetProperty)
- [`Effect.SetCountLimit`](/api/functions/Effect/SetCountLimit)
- [`Duel.IsDamageCalculated`](/api/functions/Duel/IsDamageCalculated)
- [`Duel.IsChainNegatable`](/api/functions/Duel/IsChainNegatable)
- [`Card.IsStatus`](/api/functions/Card/IsStatus)
- [`Duel.GetActivityCount`](/api/functions/Duel/GetActivityCount)
- [`Duel.RegisterEffect`](/api/functions/Duel/RegisterEffect)
