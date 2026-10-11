# Rush Selection, Actions, And Temporary Stats

**Prerequisites:** [Rush requirements and resolution](rush-duel-scripting) and
[Filters and Groups](filters-and-groups). **Goal:** choose cards during
resolution, distinguish optional actions from legality checks, and give a
monster a temporary ATK change with the correct lifetime.

The names `RD.SelectAndDoAction`, `RD.CanSelectAndDoAction`, and
`RD.AttachAtkDef` appear throughout the Rush corpus. Their short names hide
three decisions you still need to make: **when to choose**, **what the callback
returns**, and **when a created modifier expires**.

## Choose The Phase Before The Helper

| Task | Appropriate tool | Does it ask or change anything? |
| --- | --- | --- |
| Check whether at least one legal card exists during `chk==0` | `Duel.IsExistingMatchingCard` | No selection or action. |
| Choose cards now and perform an action | `RD.SelectAndDoAction` | Selects a Group and calls your action immediately. |
| Offer an optional action, then choose cards | `RD.CanSelectAndDoAction` | Asks yes/no, selects, then calls your action. |
| Select activation targets that must be tracked through the chain | The engine's [targeting flow](targeting-flow) | Establishes a target relation and requires the corresponding resolution checks. |

`CanSelectAndDoAction` is an optional **operation**, not a `Can…` legality
predicate. Calling either action helper in `chk==0` can prompt or perform an
action while the engine is merely checking whether the effect is legal.

These two helpers use `Duel.GetMatchingGroup` and ordinary Group selection.
They do not call `Duel.SelectTarget` or store activation targets. A function
passed to `e:SetTarget(...)` can just check legality; its name alone does not
make the effect target a card.

## Complete Example: Wind Spirit's Protection

Card `120105011` sends one hand card to the GY as its requirement, then gives
one face-up Spellcaster you control 1000 ATK until the end of the turn. This is
the complete imported script from `Rush/Scripts/c120105011.lua`:

```lua
local cm,m=GetID()
cm.name="风精的加护"
function cm.initial_effect(c)
	--Activate
	local e1=Effect.CreateEffect(c)
	e1:SetCategory(CATEGORY_ATKCHANGE)
	e1:SetType(EFFECT_TYPE_ACTIVATE)
	e1:SetCode(EVENT_FREE_CHAIN)
	e1:SetCost(cm.cost)
	e1:SetTarget(cm.target)
	e1:SetOperation(cm.activate)
	c:RegisterEffect(e1)
end
--Activate
function cm.filter(c)
	return c:IsFaceup() and c:IsRace(RACE_SPELLCASTER)
end
cm.cost=RD.CostSendHandToGrave(Card.IsAbleToGraveAsCost,1,1)
function cm.target(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.IsExistingMatchingCard(cm.filter,tp,LOCATION_MZONE,0,1,nil) end
end
function cm.activate(e,tp,eg,ep,ev,re,r,rp)
	RD.SelectAndDoAction(aux.Stringid(m,1),cm.filter,tp,LOCATION_MZONE,0,1,1,nil,function(g)
		RD.AttachAtkDef(e,g:GetFirst(),1000,0,RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END)
	end)
end
```

`cm` is this card's script table and `m` is its passcode, like `s,id` in other
lessons. Its Chinese `cm.name` string is retained from upstream; the English
display name comes from the database.

| Stage | What the script does |
| --- | --- |
| Register the effect | Defines a Spell activation with cost, target-check and operation callbacks. |
| Check and pay the requirement | The cost factory supplies a callback that sends one legal hand card to the GY. |
| Check activation legality | `Duel.IsExistingMatchingCard` verifies that a face-up Spellcaster exists. No monster is selected here. |
| Resolve | Builds a fresh matching Group and chooses exactly one monster from the controller's Monster Zones. |
| Apply the result | The action callback takes that monster and registers its temporary +1000 ATK modifier. |

The operation uses the current field state. If no eligible face-up Spellcaster
remains at that point, the action helper finds too few candidates and does not
call the callback. It does not try to recover a previously targeted card: no
activation target was stored.

The prompt uses `aux.Stringid(m,1)`, which reads string slot `str2` for this
passcode. In the supplied English database that slot says “Select the monster:
increase ATK”. Match prompt indexes to the strings you enter in DataEditorX.

## Read The Selection Arguments

The call in the example has this shape:

```lua
RD.SelectAndDoAction(hint, filter, tp,
    self_locations, opponent_locations, min, max, excluded, action)
```

`LOCATION_MZONE,0` searches only your Monster Zones. `1,1` requires exactly
one choice. The `nil` exclusion means no card is excluded. The upstream
parameter is spelled `expect`; it is the excluded Card or Group, not an
expected result.

The public wrapper calls `filter(card)` and `action(selected_group)` without
extra arguments. Capture `e`, `tp`, or other state in a closure when needed;
the example's anonymous action captures `e`. For a predicate needing a fixed
argument, [RD.Filter](/rush/api/functions/RushDuel/Filter) can compose it:

```lua
local machine = RD.Filter(Card.IsRace, RACE_MACHINE)
-- machine(c) now calls Card.IsRace(c, RACE_MACHINE).
```

Always put the relevant legality restrictions in the filter. The action helper
does not automatically add `IsAbleToGrave`, `IsDestructable`, race, face-up, or
other checks for your intended operation.

## Optional Actions Still Perform Work

Here is a resolution fragment for a hypothetical effect that optionally sends
one of your monsters to the GY. Provide the question in this card's `str3`
slot before using `aux.Stringid(id,2)`:

```lua
local moved = RD.CanSelectAndDoAction(
    aux.Stringid(id,2), HINTMSG_TOGRAVE,
    Card.IsAbleToGrave, tp, LOCATION_MZONE, 0, 1, 1, nil,
    function(g)
        return Duel.SendtoGrave(g, REASON_EFFECT)
    end)

if moved > 0 then
    -- Continue a branch that requires a successful send.
end
```

The helper first checks whether enough candidates exist. If they do, it asks
yes/no. Declining returns `0` without calling the action. Accepting opens the
card selection; canceling that selection returns to the yes/no question.

Put this fragment in the operation callback, at the point where the card text
offers the choice. Use a separate existence check for activation legality.

## A Callback Chooses Its Own Return Contract

The action helpers return your callback's results unchanged. They return
numeric `0` when they do not call the callback. They do not invent a selected
count or a success boolean.

| Action callback | Helper result after selection |
| --- | --- |
| `function(g) return Duel.SendtoGrave(g,REASON_EFFECT) end` | The movement count returned by the engine. |
| `function(g) return #g end` | Selected-card count, which says nothing about a subsequent action succeeding. |
| `function(g) RD.AttachAtkDef(...) end` | No return values; assigning one result produces `nil`. |

The real Wind Spirit's Protection script ignores the action helper's result,
which is appropriate: `RD.AttachAtkDef` returns no values. Do not turn it into
`if RD.AttachAtkDef(...) then ... end` and expect that branch to report success.

Lua treats numeric `0` as true. For the movement-count example, use `moved > 0`,
not `if moved then`. That numeric comparison is safe there because the callback
explicitly returns a count and the no-action path returns `0`. It would fail
for a callback that returns nothing.

## Give Temporary Stats An Explicit Lifetime

[RD.AttachAtkDef](/rush/api/functions/RushDuel/AttachAtkDef) takes the source
Effect, receiving Card, ATK delta, DEF delta, reset mask, and optional `forced`
flag. The example passes `1000,0`: create an ATK update and skip the DEF branch.
Passing `nil` also skips a stat branch; negative numbers lower the stat.

DEF updates additionally require `RD.IsCanChangeDef(card)`. In this snapshot
the exact predicate is `card:IsDefenseAbove(0) and not RD.IsMaximumMode(card)`:
the core must recognize a valid, nonnegative DEF value, and the card must not
be in Maximum mode. A Link Monster fails the core DEF check even outside
Maximum mode. The ATK branch is independent, so an
eligible ATK modifier can still be registered when the DEF branch is skipped.

The helper delegates to `RD.CreateSingleEffect`. It adds **no automatic reset**
when you omit `reset`. The example supplies both kinds of lifetime boundary:

```lua
RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END
```

- `RESET_EVENT+RESETS_STANDARD` clears the attached modifier across the usual
  card-state changes, such as leaving the field or being Set face-down.
- `RESET_PHASE+PHASE_END` expires it at the End Phase if it is still attached.

Leave `forced` omitted for normal effect-immunity handling. It is forwarded to
`Card.RegisterEffect`; it is not an “apply a larger ATK change” option.
Registration and final stat calculation can be affected by other effects, and
`AttachAtkDef` does not return a success report. See
[Reset Flags And Effect Duration](reset-flags-and-duration) for other lifetimes.

## Option Menus Return Values, Not Always Indexes

[RD.SelectOption](/rush/api/functions/RushDuel/SelectOption) accepts option
tables `{available, description, value}`. Unlike the engine's zero-based
`Duel.SelectOption` menu result, it returns your supplied value, or the option's
original one-based position when that value is omitted.

```lua
local choice = RD.SelectOption(tp,
    {false, aux.Stringid(id,0)},
    {true,  aux.Stringid(id,1)})
-- Only the second original option is available: choice is 2, not 0 or 1.

local action = RD.SelectOption(tp,
    {can_draw,    aux.Stringid(id,0), 10},
    {can_recover, aux.Stringid(id,1), 20})
if action == 10 then
    -- Draw branch.
elseif action == 20 then
    -- Recover branch.
end
```

Here `can_draw` and `can_recover` stand for legality booleans you calculate
before opening the menu. No available options returns `nil`; one available
option is announced automatically. Internally `value or index` supplies the
default, so an explicit `false` also falls back to the index, while `0` is
preserved. Prefer explicit numeric branch values when optional entries change
the visible menu.

## Check Your Implementation

For the complete ATK example, verify an ordinary activation, an unpaid
requirement, a field with no face-up Spellcaster, and a controlled test state
where no eligible monster remains when the operation runs. Then check the End Phase reset and
the receiving monster leaving the field early.

For an optional action, test accepting, declining, canceling the card selection,
and having no candidates. Confirm that `chk==0` never opens a selection prompt
and that your result test matches the callback's actual return type.

Continue with [Rush summon procedures](rush-summon-procedures), or inspect the
source-backed contracts for [SelectAndDoAction](/rush/api/functions/RushDuel/SelectAndDoAction)
and [CanSelectAndDoAction](/rush/api/functions/RushDuel/CanSelectAndDoAction).
The implementations are pinned in `Rush/Utilities/RDAction.lua`,
`RDFunction.lua`, `RDAttach.lua`, `RDBase.lua`, and `RDCondition.lua`.
