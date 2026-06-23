# Pendulum Procedure Guide

Pendulum scripts are two cards in one file: a monster script plus the behavior
the same card has while it is in a Pendulum Zone. The normal starting point is
[`aux.EnablePendulumAttribute`](/api/functions/Auxiliary/EnablePendulumAttribute).
It registers the shared Pendulum Summon procedure and, by default, the simple
activation effect that lets the player activate the Pendulum Monster from the
hand as a Spell.

Most of your script work then falls into one of three lanes: Pendulum Zone
effects, monster effects, and effects that place or move Pendulum Cards.

## The Three Jobs

| Job | Where it usually lives | What it does |
| --- | --- | --- |
| Pendulum Summon procedure | Each Pendulum Monster script | Registers an `EFFECT_SPSUMMON_PROC_G` from `LOCATION_PZONE` with `SUMMON_TYPE_PENDULUM`. |
| Pendulum Zone effects | The same card script, usually after the helper call | Uses `SetRange(LOCATION_PZONE)` for effects that apply while the card is in a Pendulum Zone. |
| Placement and special cases | Monster effects, Spell/Trap effects, or Special Summon Monster scripts | Moves cards to a Pendulum Zone, checks scales, grants extra Pendulum Summons, or completes revive-limit procedure handling. |

For an ordinary Pendulum Monster, start with the procedure helper. Then add the
Pendulum Zone effects and monster effects as separate `Effect.CreateEffect`
blocks.

## Standard Pendulum Pattern

Junoldo the Shadespirit Power Patron (`c10266279.lua`) shows the regular shape:

```lua
function s.initial_effect(c)
    aux.EnablePendulumAttribute(c)

    local e1=Effect.CreateEffect(c)
    e1:SetDescription(aux.Stringid(id,0))
    e1:SetCategory(CATEGORY_DRAW+CATEGORY_HANDES_SELF+CATEGORY_DESTROY)
    e1:SetType(EFFECT_TYPE_FIELD+EFFECT_TYPE_TRIGGER_O)
    e1:SetProperty(EFFECT_FLAG_DELAY)
    e1:SetCode(EVENT_SPSUMMON_SUCCESS)
    e1:SetRange(LOCATION_PZONE)
    e1:SetCountLimit(1,id)
    e1:SetCondition(s.drcon)
    e1:SetTarget(s.drtg)
    e1:SetOperation(s.drop)
    c:RegisterEffect(e1)
end
```

Read that as:

| Piece | Meaning |
| --- | --- |
| `aux.EnablePendulumAttribute(c)` | Makes the card usable as a Pendulum Card and gives it the shared Pendulum Summon procedure. |
| `SetRange(LOCATION_PZONE)` | Makes the effect apply only while the card is in a Pendulum Zone. |
| `EFFECT_TYPE_FIELD+EFFECT_TYPE_TRIGGER_O` | Watches a game event from the Pendulum Zone and may activate when its condition is met. |

Pendulum Zone effects are not all the same type. They can be continuous field
effects, optional triggers, Ignition Effects, Quick Effects, or activation
effects, depending on the card text. The shared detail is the range:
`LOCATION_PZONE`.

## What EnablePendulumAttribute Builds

Local `procedure.lua` creates the Pendulum Summon procedure like this:

```lua
local e1=Effect.CreateEffect(c)
e1:SetDescription(1163)
e1:SetType(EFFECT_TYPE_FIELD)
e1:SetCode(EFFECT_SPSUMMON_PROC_G)
e1:SetProperty(EFFECT_FLAG_CANNOT_DISABLE+EFFECT_FLAG_UNCOPYABLE)
e1:SetRange(LOCATION_PZONE)
e1:SetCondition(Auxiliary.PendCondition)
e1:SetOperation(Auxiliary.PendOperation)
e1:SetValue(SUMMON_TYPE_PENDULUM)
c:RegisterEffect(e1)
```

This is a rule procedure, not an activated effect. It does not create a Chain
Link. The core asks the condition whether a Pendulum Summon is available, then
the operation lets the player choose the monsters to Summon.

The same helper also registers a global Draw Phase Start reset the first time a
Pendulum procedure is enabled:

```lua
Auxiliary.PendulumChecklist=0
```

That checklist is how the shared helper remembers whether each player has used
their regular Pendulum Summon for the turn.

By default, the helper also registers the simple "activate this Pendulum Card
from the hand" effect:

```lua
local e2=Effect.CreateEffect(c)
e2:SetDescription(1160)
e2:SetType(EFFECT_TYPE_ACTIVATE)
e2:SetCode(EVENT_FREE_CHAIN)
e2:SetRange(LOCATION_HAND)
c:RegisterEffect(e2)
```

Pass `false` as the second argument when the card should not receive that
default hand activation effect:

```lua
aux.EnablePendulumAttribute(c,false)
```

Supreme King Z-ARC (`c13331639.lua`) uses that pattern. It still needs the
Pendulum Summon procedure and Pendulum Zone effects, but it is placed into a
Pendulum Zone by its own effect instead of being activated from the hand as a
regular Pendulum Card.

## Pendulum Zone Effects

Use `LOCATION_PZONE` for effects that belong to the Pendulum Zone:

```lua
local e1=Effect.CreateEffect(c)
e1:SetType(EFFECT_TYPE_FIELD)
e1:SetRange(LOCATION_PZONE)
e1:SetCode(EFFECT_CANNOT_SPECIAL_SUMMON)
e1:SetProperty(EFFECT_FLAG_PLAYER_TARGET+EFFECT_FLAG_CANNOT_DISABLE+EFFECT_FLAG_CAN_FORBIDDEN)
e1:SetTargetRange(1,0)
e1:SetTarget(s.splimit)
c:RegisterEffect(e1)
```

D/D Savant Kepler (`c11609969.lua`) uses this kind of effect to restrict
Pendulum Summons, then another Pendulum Zone effect to update its scales during
the Standby Phase.

Even though the core stores Pendulum Zone cards inside the Spell & Trap Zone
structure internally, scripts should still use the Pendulum Zone API for
Pendulum-specific checks:

| Need | Use |
| --- | --- |
| Effect only applies in a Pendulum Zone | `SetRange(LOCATION_PZONE)` |
| Read the left or right Pendulum Zone card | `Duel.GetFieldCard(tp,LOCATION_PZONE,0)` or `Duel.GetFieldCard(tp,LOCATION_PZONE,1)` |
| Count Pendulum Zone cards | `Duel.GetFieldGroupCount(tp,LOCATION_PZONE,0)` |
| Check whether a Pendulum Zone is open | `Duel.CheckLocation(tp,LOCATION_PZONE,0)` or `Duel.CheckLocation(tp,LOCATION_PZONE,1)` |
| Move a Pendulum Card to a Pendulum Zone | `Duel.MoveToField(tc,tp,tp,LOCATION_PZONE,POS_FACEUP,true)` |

Use `LOCATION_SZONE` for ordinary Spell & Trap Zone effects. Use
`LOCATION_PZONE` when the card text or mechanic specifically means a Pendulum
Zone.

## Scale Checks

The shared Pendulum Summon condition reads the left Pendulum Zone card as the
procedure handler and the right Pendulum Zone card as the partner scale:

```lua
local rpz=Duel.GetFieldCard(tp,LOCATION_PZONE,1)
local lscale=c:GetLeftScale()
local rscale=rpz:GetRightScale()
if lscale>rscale then lscale,rscale=rscale,lscale end
```

Then each candidate monster must have a Level strictly between the two scales:

```lua
lv>lscale and lv<rscale
```

The endpoints are not included. With scales 1 and 8, Level 2 through Level 7
can pass the scale check; Level 1 and Level 8 cannot.

Performapal Popperup (`c11481610.lua`) shows the same manual pattern in a Spell
effect. It reads both Pendulum Zone cards, swaps the values if needed, then
checks hand monsters against `lv>lsc and lv<rsc`.

Use the current scale getters when runtime scale changes matter:

```lua
local lpz=Duel.GetFieldCard(tp,LOCATION_PZONE,0)
local rpz=Duel.GetFieldCard(tp,LOCATION_PZONE,1)
if not lpz or not rpz then return false end

local lscale=lpz:GetLeftScale()
local rscale=rpz:GetRightScale()
if lscale>rscale then lscale,rscale=rscale,lscale end
```

[`Card.GetLeftScale`](/api/functions/Card/GetLeftScale) and
[`Card.GetRightScale`](/api/functions/Card/GetRightScale) return modified
current values while the card is in a Pendulum Zone. D/D Savant Kepler updates
both scales with `EFFECT_UPDATE_LSCALE` and `EFFECT_UPDATE_RSCALE`, so current
scale reads are the right habit for live gameplay checks.

Use [`Card.GetOriginalLeftScale`](/api/functions/Card/GetOriginalLeftScale) and
[`Card.GetOriginalRightScale`](/api/functions/Card/GetOriginalRightScale) only
when the text specifically cares about printed/original scale values.

## Pendulum Summon Candidate Pool

The shared helper builds the possible locations from the zones the player can
use:

```lua
local loc=0
if Duel.GetLocationCount(tp,LOCATION_MZONE)>0 then
    loc=loc+LOCATION_HAND
end
if Duel.GetLocationCountFromEx(tp,tp,nil,TYPE_PENDULUM)>0 then
    loc=loc+LOCATION_EXTRA
end
```

That means:

| Source | Why it may be included |
| --- | --- |
| Hand | There is at least one usable Monster Zone for monsters from the hand. |
| Extra Deck | There is at least one legal zone for a face-up Pendulum Monster from the Extra Deck. |

The candidate itself still has to pass `Auxiliary.PConditionFilter`. The local
helper checks that the card:

- is in the hand, or is face-up and is a Pendulum Monster
- has a Level between the two active scales
- can be Special Summoned with `SUMMON_TYPE_PENDULUM`
- is not forbidden
- can be included under the regular or extra Pendulum Summon count currently
  being used

Local `procedure.lua` also checks `c.pendulum_level` before falling back to
`c:GetLevel()`. That is a procedure-backed compatibility hook for cards whose
Pendulum Summon Level is stored on the card table instead of coming from the
ordinary Level getter.

## Selection And Resolution

Pendulum Summon selection has to respect three counts:

| Count | Local variable | Meaning |
| --- | --- | --- |
| Main Monster Zone count for hand monsters | `ft1` | How many selected cards may come from the hand. |
| Extra Deck summon count for face-up Extra Deck Pendulum Monsters | `ft2` | How many selected cards may come from the Extra Deck. |
| Total usable Monster Zones | `ft` | The total size limit for the selected group. |

The helper uses `Auxiliary.PendOperationCheck(ft1,ft2,ft)` as a
`Group.SelectSubGroup` check. It splits the candidate group into Extra Deck and
non-Extra Deck cards, then refuses selections that exceed any of those three
limits.

Inside the normal shared procedure, the operation does not call
`Duel.SpecialSummon` directly. It merges the selected cards into the group
given by the core:

```lua
sg:Merge(g)
```

The core's `EFFECT_SPSUMMON_PROC_G` path then filters the group again, handles
Special Summon costs, assigns `SUMMON_TYPE_PENDULUM`, moves each selected
monster to the Monster Zone, and announces the Summons.

When you are writing a normal Pendulum Monster, let
`aux.EnablePendulumAttribute` handle that flow. Do not try to duplicate it with
a manual `Duel.SpecialSummon` call.

## Extra Pendulum Summons

The shared helper tracks the regular once-per-turn Pendulum Summon in
`Auxiliary.PendulumChecklist`. At the start of each Draw Phase,
`Auxiliary.PendulumReset` clears the checklist.

If the regular Pendulum Summon has already been used, the helper only allows a
new Pendulum Summon if the player is affected by an
`EFFECT_EXTRA_PENDULUM_SUMMON` effect. When both a regular and an extra
Pendulum Summon are available, the operation offers the player a choice. If an
extra effect is chosen, the helper calls that effect's value filter and then
uses its count limit with:

```lua
ce:UseCountLimit(tp)
```

Pendulum Evolution (`c55795155.lua`) shows a scripted extra Pendulum Summon. It
temporarily registers an `EFFECT_EXTRA_PENDULUM_SUMMON`, reads both Pendulum
Zones, builds the candidate locations, reuses `aux.PConditionFilter`, and uses
`aux.PendOperationCheck` for selection limits.

That script performs its own `Duel.SpecialSummon` because the Spell effect is
not the standard Pendulum Monster procedure. For ordinary Pendulum Monsters,
prefer the shared helper and let the core perform the group procedure.

## Moving Cards To A Pendulum Zone

Use `Duel.CheckLocation` before activating an effect that must place a card in
a Pendulum Zone:

```lua
function s.pentg(e,tp,eg,ep,ev,re,r,rp,chk)
    if chk==0 then
        return Duel.CheckLocation(tp,LOCATION_PZONE,0)
            or Duel.CheckLocation(tp,LOCATION_PZONE,1)
    end
end
```

Then recheck relation and move the card during resolution:

```lua
function s.penop(e,tp,eg,ep,ev,re,r,rp)
    local c=e:GetHandler()
    if c:IsRelateToEffect(e) then
        Duel.MoveToField(c,tp,tp,LOCATION_PZONE,POS_FACEUP,true)
    end
end
```

Supreme King Z-ARC uses exactly this pattern after it is destroyed face-up from
the Monster Zone. Chronograph Sorcerer (`c12289247.lua`) and Astrograph
Sorcerer, the Star Magician (`c48171151.lua`) use the same movement function
to place selected Pendulum Cards from the hand or Deck into a Pendulum Zone.

The local core accepts `LOCATION_PZONE` in `Duel.MoveToField`. Internally it
maps the destination to the Spell & Trap Zone with a Pendulum Zone flag, then
lets the player choose an open Pendulum Zone. If no Pendulum Zone is usable,
the core sends the card to the GY by rule and the move does not succeed.

Advanced placement effects can pass the optional seventh `zone` argument. For
Pendulum Zone moves, the low bits are used:

| Zone argument | Pendulum Zone allowed |
| --- | --- |
| omitted or `0xff` | either Pendulum Zone |
| `0x1` | left Pendulum Zone only |
| `0x2` | right Pendulum Zone only |
| `0x3` | either Pendulum Zone |

Most local scripts omit the seventh argument and let the player choose any
available Pendulum Zone.

## Revive-Limit Pendulum Summonable Monsters

Some Pendulum Monsters are also Special Summon Monsters. They need revive-limit
handling, but their text may still allow them to be Pendulum Summoned from a
specific location.

Odd-Eyes Revolution Dragon (`c16306932.lua`) uses:

```lua
aux.EnablePendulumAttribute(c)
aux.EnableReviveLimitPendulumSummonable(c,LOCATION_HAND)
```

The second helper does three things in local `procedure.lua`:

1. Calls `c:EnableReviveLimit()`.
2. Stores the allowed Pendulum Summon locations as `psummonable_location`.
3. Registers a continuous `EVENT_SPSUMMON_SUCCESS` effect that calls
   `c:CompleteProcedure()` if the card was Pendulum Summoned.

That is why the Pendulum condition can pass special `nocheck` and `nolimit`
values into `IsCanBeSpecialSummoned` only when
`Auxiliary.PendulumSummonableBool(c)` says the card is in one of its allowed
locations.

Use this helper for Special Summon Monsters that are allowed to be Pendulum
Summoned despite having revive-limit rules. Do not call `CompleteProcedure`
manually for every ordinary Pendulum Monster.

## Scale-Based Effects

Some cards do not perform a Pendulum Summon but still inspect scales.
Pendulum Scale (`c17885118.lua`) requires two cards in your Pendulum Zones,
reads the left card's left scale and the right card's right scale, then chooses
different outcomes based on the absolute difference:

```lua
local tc1=Duel.GetFieldCard(tp,LOCATION_PZONE,0)
local tc2=Duel.GetFieldCard(tp,LOCATION_PZONE,1)
local scl1=tc1:GetLeftScale()
local scl2=tc2:GetRightScale()
local dif=math.abs(scl1-scl2)
```

This is a good pattern for effects that care about the active Pendulum Scale
pair but are not themselves Pendulum Summons. Guard that both Pendulum Zones
are occupied before reading the cards, then use the scale getters that match
the text.

## Common Pitfalls

| Mistake | Better habit |
| --- | --- |
| Forgetting `aux.EnablePendulumAttribute(c)` on a normal Pendulum Monster. | Put it near the top of `initial_effect`, before Pendulum Zone and monster effects. |
| Adding a custom activation effect but leaving the default helper activation in place. | Use `aux.EnablePendulumAttribute(c,false)` when the card should not get the default hand activation effect. |
| Using `LOCATION_SZONE` for a Pendulum Zone effect. | Use `LOCATION_PZONE` for Pendulum Zone effects and Pendulum Zone checks. |
| Treating scale endpoints as legal Levels. | Check Levels strictly between the two scales: `lv>low_scale and lv<high_scale`. |
| Assuming the left scale is always lower. | Read both scales and swap them before comparing Levels. |
| Trying to Pendulum Summon face-down cards from the Extra Deck. | The shared helper only accepts face-up Pendulum Monsters from the Extra Deck path. |
| Checking only total Monster Zone space. | Respect hand capacity, face-up Extra Deck capacity, and total usable Monster Zones. |
| Calling `Duel.SpecialSummon` inside an ordinary Pendulum Monster's procedure. | Let `aux.EnablePendulumAttribute` and the core group procedure resolve the Summon. |
| Moving a card to a Pendulum Zone without checking open zones. | Use `Duel.CheckLocation(tp,LOCATION_PZONE,0/1)` before activation and relation checks during resolution. |
| Forgetting revive-limit completion for Special Summon Monsters that can be Pendulum Summoned. | Use `aux.EnableReviveLimitPendulumSummonable(c,loc)` for that specific pattern. |

## Useful API Pages

- [`Auxiliary.EnablePendulumAttribute`](/api/functions/Auxiliary/EnablePendulumAttribute)
- [`Auxiliary.PendCondition`](/api/functions/Auxiliary/PendCondition)
- [`Auxiliary.PendOperation`](/api/functions/Auxiliary/PendOperation)
- [`Auxiliary.PendOperationCheck`](/api/functions/Auxiliary/PendOperationCheck)
- [`Auxiliary.PendulumReset`](/api/functions/Auxiliary/PendulumReset)
- [`Auxiliary.PendulumSummonableBool`](/api/functions/Auxiliary/PendulumSummonableBool)
- [`Auxiliary.EnableReviveLimitPendulumSummonable`](/api/functions/Auxiliary/EnableReviveLimitPendulumSummonable)
- [`Auxiliary.PSSCompleteProcedure`](/api/functions/Auxiliary/PSSCompleteProcedure)
- [`Card.GetLeftScale`](/api/functions/Card/GetLeftScale)
- [`Card.GetRightScale`](/api/functions/Card/GetRightScale)
- [`Card.GetOriginalLeftScale`](/api/functions/Card/GetOriginalLeftScale)
- [`Card.GetOriginalRightScale`](/api/functions/Card/GetOriginalRightScale)
- [`Card.GetCurrentScale`](/api/functions/Card/GetCurrentScale)
- [`Card.IsCanBeSpecialSummoned`](/api/functions/Card/IsCanBeSpecialSummoned)
- [`Card.EnableReviveLimit`](/api/functions/Card/EnableReviveLimit)
- [`Card.CompleteProcedure`](/api/functions/Card/CompleteProcedure)
- [`Card.IsSummonType`](/api/functions/Card/IsSummonType)
- [`Duel.GetFieldCard`](/api/functions/Duel/GetFieldCard)
- [`Duel.GetFieldGroup`](/api/functions/Duel/GetFieldGroup)
- [`Duel.GetFieldGroupCount`](/api/functions/Duel/GetFieldGroupCount)
- [`Duel.CheckLocation`](/api/functions/Duel/CheckLocation)
- [`Duel.GetLocationCount`](/api/functions/Duel/GetLocationCount)
- [`Duel.GetLocationCountFromEx`](/api/functions/Duel/GetLocationCountFromEx)
- [`Duel.GetUsableMZoneCount`](/api/functions/Duel/GetUsableMZoneCount)
- [`Duel.MoveToField`](/api/functions/Duel/MoveToField)
- [`Duel.SpecialSummon`](/api/functions/Duel/SpecialSummon)
- [`Effect.UseCountLimit`](/api/functions/Effect/UseCountLimit)
- [`Group.SelectSubGroup`](/api/functions/Group/SelectSubGroup)
