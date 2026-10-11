# Rush Special Summons And Result Types

**Prerequisites:** [selection and actions](rush-selection-and-actions) and
[Rush summon procedures](rush-summon-procedures). **Goal:** distinguish a
summoning effect from a registered hand procedure, give the player a legal
choice, and interpret counts, booleans, Cards and Groups correctly.

## A Complete Effect: Silver's Cry

`Rush/Scripts/c120102010.lua` demonstrates a normal effect Special Summon from
the GY. The imported card also restricts activation by its tracked card name:

```lua
local cm,m=GetID()
local list={120102010}
cm.name="银龙的轰咆"
function cm.initial_effect(c)
	RD.AddCodeList(c,list)
	--Activate
	local e1=Effect.CreateEffect(c)
	e1:SetCategory(CATEGORY_SPECIAL_SUMMON+CATEGORY_GRAVE_SPSUMMON)
	e1:SetType(EFFECT_TYPE_ACTIVATE)
	e1:SetCode(EVENT_FREE_CHAIN)
	e1:SetCondition(cm.condition)
	e1:SetTarget(cm.target)
	e1:SetOperation(cm.activate)
	c:RegisterEffect(e1)
end
--Activate
function cm.spfilter(c,e,tp)
	return c:IsType(TYPE_NORMAL) and c:IsRace(RACE_DRAGON) and RD.IsCanBeSpecialSummoned(c,e,tp,POS_FACEUP)
end
function cm.condition(e,tp,eg,ep,ev,re,r,rp)
	return RD.IsPlayerNoActivateInThisTurn(tp,list[1])
end
function cm.target(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.GetMZoneCount(tp)>0
		and Duel.IsExistingMatchingCard(cm.spfilter,tp,LOCATION_GRAVE,0,1,nil,e,tp) end
	Duel.SetOperationInfo(0,CATEGORY_SPECIAL_SUMMON,nil,1,tp,LOCATION_GRAVE)
end
function cm.activate(e,tp,eg,ep,ev,re,r,rp)
	RD.SelectAndSpecialSummon(aux.NecroValleyFilter(cm.spfilter),tp,LOCATION_GRAVE,0,1,1,nil,e,POS_FACEUP)
end
```

The filter checks **both card identity and summon legality**. The target
callback separately checks capacity. Neither check chooses a monster. During
resolution, the helper rebuilds the candidate Group, the player chooses one,
and the helper performs the summon.

`aux.NecroValleyFilter` wraps the GY selection filter in the operation, matching
the source's GY handling. The card's other activation restriction depends on
the Rush bootstrap's tracking. Copy the whole behavior required by your card;
a category flag alone does not supply those checks.

## Match The Filter To The Later Summon

`RD.IsCanBeSpecialSummoned(c,e,tp,position)` is a **predicate**. It calls:

```lua
c:IsCanBeSpecialSummoned(e,0,tp,false,false,position)
```

It performs an ordinary effect-summon check with neither summoning-condition
nor revive-limit bypass. It does not reserve a zone. A positive result does not
turn an improperly summoned Fusion/Ritual monster in the GY into a legal revival.

`RD.SelectAndSpecialSummon` is an **action**. It checks the destination's
available Monster Zones, caps the maximum choice by that count, selects cards
and calls `Duel.SpecialSummon` with summon type `0`. Supply the per-card
legality filter yourself; the helper's capacity check does not provide it.

Unlike `RD.SelectAndDoAction`, the specialized summon helper supplies extra
arguments to its filter:

```lua
filter(candidate, e, tp, position, break_effect, target_player)
```

A filter such as Silver's Cry's accepts only `candidate,e,tp`; Lua ignores the
extra arguments. This is why reusing a filter in the general action wrapper,
which supplies only `candidate`, can produce missing-argument errors.

### Summoning To The Other Player's Field

The helper's final `target_player` changes the destination, while `tp` remains
the selecting/summoning player. Match that destination in the native legality
check if your effect uses it:

```lua
function s.spfilter(c,e,tp,position,break_effect,target_player)
    return c:IsCanBeSpecialSummoned(e,0,tp,false,false,
        position,target_player or tp)
end
```

The short `RD.IsCanBeSpecialSummoned` wrapper has no destination-player
argument, so it does not express this different-destination check. Keep your
card's own race, Level, type and other restrictions in the filter as well.

## Optional Summoning Is Still An Operation

`RD.CanSelectAndSpecialSummon` adds a yes/no prompt before selection. It does
not mean “return whether a summon is possible”. Place it in the operation,
and use a separate capacity/existence check for `chk==0`.

```lua
-- Resolution fragment; str2 contains this card's optional-action question.
local summoned = RD.CanSelectAndSpecialSummon(
    aux.Stringid(id,1), aux.NecroValleyFilter(s.spfilter),
    tp, LOCATION_GRAVE, 0, 1, 1, nil, e, POS_FACEUP)

if summoned > 0 then
    -- A branch whose prerequisite is at least one successful summon.
end
```

The player can decline. If they accept and then cancel the card selection,
the helper returns to the yes/no prompt. Too few candidates, inadequate
capacity or declining the action produces numeric `0`.

The non-optional `SelectAndSpecialSummon` uses a non-cancelable card selection.
Both helpers return the actual `Duel.SpecialSummon` count. Their internal
wrapper also handles the pinned library's face-down confirmation rules.

## A Procedure Is Registered, Not Executed Here

The complete imported `c120272033.lua` (The Tricky) has a different shape:

```lua
local cm,m=GetID()
cm.name="诡术师"
function cm.initial_effect(c)
	--Special Summon Procedure
	RD.AddHandToGraveSpecialSummonProcedure(c,aux.Stringid(m,0),cm.spconfilter,1)
end
--Special Summon Procedure
function cm.spconfilter(c)
	return c:IsAbleToGraveAsCost()
end
```

`RD.AddHandToGraveSpecialSummonProcedure` registers an
`EFFECT_SPSUMMON_PROC` in the hand. It returns the registered Effect, not a
summon count. The engine later offers the procedure when its requirements are
met; calling the helper in `initial_effect` does not summon the card immediately.

The generated procedure has three distinct steps:

1. **Condition:** check a usable zone and enough matching other hand cards.
2. **Target/selection:** select exactly the required count with cancellation
   allowed. Retain the chosen Group with `KeepAlive` and store it on the Effect.
3. **Operation:** send that Group with `REASON_SPSUMMON`, then delete the retained
   Group. This is the reason used by this procedure even though its supplied
   legality filter is `Card.IsAbleToGraveAsCost`.

Cancellation returns false from the procedure's target callback before its
payment operation runs. A reveal-hand procedure is a different helper
(`AddHandConfirmSpecialSummonProcedure`), with its own filter and reveal/shuffle
operation. Do not replace one with the other solely because both summon from hand.

For a beginner, use the matching public procedure helper. The retained Group
and its cleanup are part of the contract; copying only `GetMatchingGroup` and
`SendtoGrave` into a new procedure loses its selection and lifetime handling.

## Movement Helpers Can Return Booleans

`RD.SendToHandAndExists` is commonly used for a follow-up after recovering a
card. For example, `c120109025.lua` checks it before giving its still-related,
face-up handler an ATK increase. The check is Boolean:

```lua
if RD.SendToHandAndExists(g,e,tp,REASON_EFFECT) then
    -- The movement was nonzero; the optional operated-Group check passed.
end
```

By default, that does not prove that every selected card entered the hand.
When the follow-up requires at least one card to end up in the hand, supply
an operated-Group predicate and count:

```lua
local reached_hand = RD.SendToHandAndExists(g,e,tp,REASON_EFFECT,
    RD.Filter(Card.IsLocation,LOCATION_HAND),1,nil)
if reached_hand then
    -- At least one operated card is now in the hand.
end
```

The helper filters Rush-specific protection, includes Maximum components,
moves the cards and handles relevant opponent confirmations. Its `player`
argument provides protection/confirmation context; the native movement uses
`nil` for the hand destination, preserving owner-based routing.

::: warning The reason argument is not a general movement switch
In this snapshot, `reason` is passed to the Rush protection check, but the
actual `Duel.SendtoHand` call uses `REASON_EFFECT` unconditionally. Do not use
this helper to implement a cost by merely passing `REASON_COST`.
:::

## Keep These Return Shapes Separate

| Call | Result | Correct interpretation |
| --- | --- | --- |
| `RD.IsCanBeSpecialSummoned(...)` | Boolean | A per-card legality check, with no action or zone reservation. |
| `RD.SelectAndSpecialSummon(...)` | Number | Actual core summon count; compare with `> 0`. |
| `RD.CanSelectAndSpecialSummon(...)` | Number | Actual count, or `0` for declined/unavailable actions. |
| `RD.SendToHandAndExists(...)` | Boolean | Movement and optional operated-Group predicate succeeded. |
| `RD.AddHandToGraveSpecialSummonProcedure(...)` | Effect | A registered procedure, not an immediate summon. |
| `RD.ExecuteFusionSummon(...)` / `RD.ExecuteRitualSummon(...)` | Card and Group, or `nil` on permitted cancellation | Chosen candidate and materials; these wrappers do not verify/return the core summon count. |

If a later effect needs the actual cards operated on, capture the relevant
Group before another operation replaces that engine result. A number tells you
how many; it does not contain the Card objects. Follow the shared
[Group-handling lesson](selection-and-group-handling) before retaining a Group
across callbacks.

## Test The Boundary Conditions

Check no legal candidate, one candidate, multiple choices, no usable zone,
a permitted versus improperly summoned revival, and the exact destination and
position used by the summon. For an optional action, test decline and cancel.
For the hand procedure, cancel before payment and confirm no card was sent.

For a movement follow-up, distinguish partial movement from every card reaching
the required destination. Compare the predicate/count you need with what the
helper actually returns before adding the next branch.

Continue with [Fusion and Ritual player choices](rush-fusion-ritual-choices).
Reference: [SelectAndSpecialSummon](/rush/api/functions/RushDuel/SelectAndSpecialSummon),
[CanSelectAndSpecialSummon](/rush/api/functions/RushDuel/CanSelectAndSpecialSummon),
[SendToHandAndExists](/rush/api/functions/RushDuel/SendToHandAndExists), and
[the hand procedure](/rush/api/functions/RushDuel/AddHandToGraveSpecialSummonProcedure).
