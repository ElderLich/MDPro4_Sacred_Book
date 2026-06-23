# Xyz Procedure Guide

Xyz scripts are built around overlaying materials, not sending them to the GY.
The Xyz Monster registers a Summon procedure in the Extra Deck, that procedure
selects legal materials, and the operation records those cards as material
before placing them under the Xyz Monster with `Duel.Overlay`.

Effects can also tell a player to Xyz Summon during resolution. Those effects
should still ask the Xyz Monster's registered procedure whether the current
material group is legal.

## The Three Jobs

| Job | Where it usually lives | What it does |
| --- | --- | --- |
| Xyz Monster procedure | The Xyz Monster script in `initial_effect` | Registers an `EFFECT_SPSUMMON_PROC` in the Extra Deck with `SUMMON_TYPE_XYZ`. |
| Effect that performs an Xyz Summon | A Spell, Trap, or monster effect | Checks [`Card.IsXyzSummonable`](/api/functions/Card/IsXyzSummonable), then calls [`Duel.XyzSummon`](/api/functions/Duel/XyzSummon). |
| Xyz Material effects | Usually on the Xyz Monster after it is on the field | Read, add, or detach Xyz Materials with overlay APIs. |

For a normal Xyz Monster, start with the first job. The procedure is what tells
the engine which materials can become Xyz Materials for that monster.

## Standard Xyz Procedure

Number 39: Utopia (`c84013237.lua`) shows the classic "2 Level 4 monsters"
shape:

```lua
function s.initial_effect(c)
    aux.AddXyzProcedure(c,nil,4,2)
    c:EnableReviveLimit()
end
```

Read that as:

| Piece | Meaning |
| --- | --- |
| `aux.AddXyzProcedure` | Registers the Xyz Summon procedure on the Extra Deck monster. |
| `nil` | No extra material filter; any legal material with the required Xyz Level can be used. |
| `4` | Required material Level. Xyz scripts often call this Xyz Level because effects can change what Level a card provides for Xyz Summons. |
| `2` | Minimum material count. Because `maxct` is omitted, the maximum is also `2`. |
| `c:EnableReviveLimit()` | Marks the Xyz Monster as needing a proper Summon before it can be revived by normal revive effects. |

The helper compares the materials' Xyz Levels, not the Xyz Monster's Rank
directly. The two often match in card text, but they are not the same concept in
script.

## Helper Arguments

The standard helper is:

```lua
aux.AddXyzProcedure(c,f,lv,ct,alterf,alterdesc,maxct,alterop)
```

| Argument | Meaning |
| --- | --- |
| `c` | The Xyz Monster receiving the procedure. |
| `f` | Optional material filter. `nil` means no extra family, Type, Attribute, or name restriction. |
| `lv` | Required material Xyz Level. |
| `ct` | Minimum material count. |
| `alterf` | Optional filter for a one-card alternate Xyz Summon route. |
| `alterdesc` | Prompt text id for choosing the alternate route. Usually `aux.Stringid(id,n)`. |
| `maxct` | Optional maximum material count. Defaults to `ct`. |
| `alterop` | Optional check/apply callback for the alternate route. |

For "2 or more Level 8 monsters", local scripts commonly pass a high maximum:

```lua
aux.AddXyzProcedure(c,nil,8,2,nil,nil,99)
```

That pattern appears in Number 1: Infection Buzzking (`c10666000.lua`). The
helper still applies zone checks, material restrictions, and any runtime
minimum/maximum overrides from `Duel.XyzSummon`.

## What The Helper Builds

Local `procedure.lua` creates a Special Summon procedure:

```lua
local e1=Effect.CreateEffect(c)
e1:SetDescription(1165)
e1:SetType(EFFECT_TYPE_FIELD)
e1:SetCode(EFFECT_SPSUMMON_PROC)
e1:SetProperty(EFFECT_FLAG_CANNOT_DISABLE+EFFECT_FLAG_UNCOPYABLE)
e1:SetRange(LOCATION_EXTRA)
e1:SetCondition(Auxiliary.XyzCondition(f,lv,ct,maxct,alterf,alterdesc,alterop))
e1:SetTarget(Auxiliary.XyzTarget(f,lv,ct,maxct,alterf,alterdesc,alterop))
e1:SetOperation(Auxiliary.XyzOperation(f,lv,ct,maxct,alterf,alterdesc,alterop))
e1:SetValue(SUMMON_TYPE_XYZ)
c:RegisterEffect(e1)
```

Like other Extra Deck rule procedures, this is not activated as a Chain Link.
The core checks the procedure, the target branch selects materials, and the
operation branch overlays them.

The helper refuses its procedure for a face-up Pendulum Xyz Monster in the
Extra Deck. That check is directly in `Auxiliary.XyzCondition`.

## Material Legality

The ordinary material pool is the player's Monster Zone:

```lua
mg=Duel.GetFieldGroup(tp,LOCATION_MZONE,0)
```

If an effect calls `Duel.XyzSummon` with a material group, the helper uses that
group instead. The core helpers do the normal Xyz material check and selection:

| Task | Local function |
| --- | --- |
| Check whether a legal group exists | [`Duel.CheckXyzMaterial`](/api/functions/Duel/CheckXyzMaterial) |
| Let the player choose Xyz Materials | [`Duel.SelectXyzMaterial`](/api/functions/Duel/SelectXyzMaterial) |
| Check a specific Xyz Monster from an effect | [`Card.IsXyzSummonable`](/api/functions/Card/IsXyzSummonable) |
| Confirm a card can be Xyz Material | [`Card.IsCanBeXyzMaterial`](/api/functions/Card/IsCanBeXyzMaterial) |
| Test a material's Xyz Level | [`Card.IsXyzLevel`](/api/functions/Card/IsXyzLevel) |

Local procedure code also handles:

- mandatory Xyz Materials through `EFFECT_MUST_BE_XMATERIAL`
- cards that require a minimum Xyz Material count through `EFFECT_XYZ_MIN_COUNT`
- double-material effects through `EFFECT_DOUBLE_XMATERIAL`
- Extra Monster Zone and Main Monster Zone availability through
  `Duel.GetLocationCountFromEx`

There is a local implementation caveat in `procedure.lua`: the standard helper
has special support for double-material effects, while the Level-free helper
has a comment saying `EFFECT_DOUBLE_XMATERIAL` is not supported there.

## Operation Order

The ordinary operation does three important things:

```lua
local mg=e:GetLabelObject()

-- Existing Xyz Materials under the chosen materials are sent to the GY by rule.
local sg=Group.CreateGroup()
for tc in aux.Next(mg) do
    sg:Merge(tc:GetOverlayGroup())
end
Duel.SendtoGrave(sg,REASON_RULE)

c:SetMaterial(mg)
Duel.Overlay(c,mg)
mg:DeleteGroup()
```

The exact local code uses `Auxiliary.Next` and has extra branches for alternate
procedures and double-material effects, but the beginner idea is the same:

1. Existing Xyz Materials under ordinary material cards are moved to the GY by
   rule.
2. The selected cards are recorded as the new Xyz Monster's materials with
   [`Card.SetMaterial`](/api/functions/Card/SetMaterial).
3. The selected cards are overlaid under the Xyz Monster with
   [`Duel.Overlay`](/api/functions/Duel/Overlay).

Do not send the selected Xyz Materials to the GY in a normal Xyz procedure.
They become Xyz Materials under the Xyz Monster.

## Detaching Xyz Materials

Number 39: Utopia uses a standard detach-as-cost pattern:

```lua
function s.atkcost(e,tp,eg,ep,ev,re,r,rp,chk)
    if chk==0 then
        return e:GetHandler():CheckRemoveOverlayCard(tp,1,REASON_COST)
    end
    e:GetHandler():RemoveOverlayCard(tp,1,1,REASON_COST)
end
```

Use [`Card.CheckRemoveOverlayCard`](/api/functions/Card/CheckRemoveOverlayCard)
in the `chk==0` branch, then
[`Card.RemoveOverlayCard`](/api/functions/Card/RemoveOverlayCard) in the real
cost branch. The card method removes Xyz Materials from that Xyz Monster and
returns the number actually removed.

Use the reason that matches the text:

| Text shape | Reason |
| --- | --- |
| "detach 1 material; ..." as a cost | `REASON_COST` |
| "detach 1 material, then ..." during resolution | `REASON_EFFECT` |

To read materials without detaching them, use
[`Card.GetOverlayGroup`](/api/functions/Card/GetOverlayGroup) or
[`Card.GetOverlayCount`](/api/functions/Card/GetOverlayCount). Utopia's
self-destroy effect checks:

```lua
return Duel.GetAttackTarget()==c and c:GetOverlayCount()==0
```

## Alternate One-Card Xyz Routes

Some Xyz Monsters can be Xyz Summoned by using one specific Xyz Monster you
control as material. Cyber Dragon Infinity (`c10443957.lua`) has both a normal
procedure and an alternate one-card route:

```lua
aux.AddXyzProcedure(c,s.mfilter,6,3,s.ovfilter,aux.Stringid(id,0),3,s.xyzop)
```

The normal route is three Level 6 LIGHT Machine monsters:

```lua
function s.mfilter(c)
    return c:IsRace(RACE_MACHINE) and c:IsAttribute(ATTRIBUTE_LIGHT)
end
```

The alternate route looks for a face-up Cyber Dragon Nova:

```lua
function s.ovfilter(c)
    return c:IsFaceup() and c:IsCode(58069384)
end
```

The optional `alterop` callback is used as both a check and an apply step:

```lua
function s.xyzop(e,tp,chk)
    if chk==0 then return Duel.GetFlagEffect(tp,id)==0 end
    Duel.RegisterFlagEffect(tp,id,RESET_PHASE+PHASE_END,EFFECT_FLAG_OATH,1)
end
```

The helper calls this with `chk==0` while checking whether the alternate route
is legal, and with `chk==1` after the player selects that route. The local
operation also moves the selected Xyz Monster's existing Xyz Materials under
the new Xyz Monster before overlaying the selected monster itself.

## Level-Free Xyz Procedures

Some Xyz Monsters do not use the ordinary "same Level" material check. Use:

```lua
aux.AddXyzProcedureLevelFree(c,f,gf,minc,maxc,alterf,alterdesc,alterop)
```

Number F0: Utopic Future (`c65305468.lua`) is a local example:

```lua
c:EnableReviveLimit()
aux.AddXyzProcedureLevelFree(c,s.mfilter,s.xyzcheck,2,2)

function s.mfilter(c,xyzc)
    return c:IsXyzType(TYPE_XYZ) and not c:IsSetCard(0x48)
end

function s.xyzcheck(g)
    return g:GetClassCount(Card.GetRank)==1
end
```

Here `mfilter` chooses the material kind, while `xyzcheck` checks the whole
selected group. The group check requires all selected Xyz Monsters to have the
same Rank. It does not compare material Levels.

The Level-free helper still filters through `Card.IsCanBeXyzMaterial`, checks
Monster Zone availability, supports `EFFECT_XYZ_MIN_COUNT`, and uses the same
overlay operation style as the standard helper.

## Effects That Xyz Summon

Gagaga Magician - Gagaga Magic (`c12908094.lua`) shows an effect that Special
Summons two monsters, then Xyz Summons using exactly those monsters.

The filter asks Extra Deck Xyz Monsters whether the temporary group is legal:

```lua
function s.xyzfilter(c,g)
    return c:IsSetCard(0x8f,0x54,0x59,0x82,0x206f,0x6d,0x48,0x107e,0x207e)
        and c:IsXyzSummonable(g,2,2)
end
```

After both monsters are Special Summoned and still face-up in the Monster Zone,
the operation rechecks and performs the Xyz Summon:

```lua
local g=Group.FromCards(c,tc)
if Duel.SpecialSummon(g,0,tp,tp,false,false,POS_FACEUP)==2
    and g:IsExists(Card.IsLocation,2,nil,LOCATION_MZONE)
    and g:IsExists(Card.IsFaceup,2,nil) then
    Duel.AdjustAll()
    local xyzg=Duel.GetMatchingGroup(s.xyzfilter,tp,LOCATION_EXTRA,0,nil,g)
    if xyzg:GetCount()>0 then
        Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_SPSUMMON)
        local xyz=xyzg:Select(tp,1,1,nil):GetFirst()
        Duel.XyzSummon(tp,xyz,g)
    end
end
```

The important habit is the recheck. The target branch can prove that a Summon
is possible before resolution, but the operation still needs the actual
face-up monsters on the field before it calls `Duel.XyzSummon`.

`Duel.XyzSummon` is for effects that perform a rule Xyz Summon. It sets the
core's temporary material group and count limits, then the selected Xyz
Monster's registered procedure handles selection and overlaying.

## Adding Cards As Xyz Material

Adding a card as Xyz Material after the Xyz Monster is already on the field is
not the same as performing an Xyz Summon.

Cyber Dragon Infinity has an Ignition Effect that targets a face-up Attack
Position monster and attaches it:

```lua
function s.filter(c)
    return c:IsPosition(POS_FACEUP_ATTACK) and c:IsCanOverlay()
end

function s.operation(e,tp,eg,ep,ev,re,r,rp)
    local c=e:GetHandler()
    local tc=Duel.GetFirstTarget()
    if c:IsRelateToEffect(e) and tc:IsRelateToEffect(e) and not tc:IsImmuneToEffect(e) then
        local og=tc:GetOverlayGroup()
        if og:GetCount()>0 then
            Duel.SendtoGrave(og,REASON_RULE)
        end
        Duel.Overlay(c,Group.FromCards(tc))
    end
end
```

The target must pass [`Card.IsCanOverlay`](/api/functions/Card/IsCanOverlay).
If that target already has Xyz Materials, the local script sends those existing
materials to the GY by rule before overlaying the target itself.

## Common Pitfalls

| Mistake | Better habit |
| --- | --- |
| Forgetting `EnableReviveLimit` on an Xyz Monster. | Put it near the Xyz procedure in `initial_effect`. |
| Treating the helper's `lv` argument as the Xyz Monster's Rank. | Read it as the required material Xyz Level. |
| Expecting `ct` alone to mean "or more." | Pass `maxct` when the material count can vary. |
| Sending selected Xyz Materials to the GY in the procedure. | Record them with `SetMaterial`, then overlay them with `Duel.Overlay`. |
| Using `Duel.Overlay` and assuming that makes a proper Xyz Summon. | Use a registered procedure or `Duel.XyzSummon` for proper Xyz Summons. |
| Detaching in a cost with `REASON_EFFECT`. | Use `REASON_COST` in cost branches and `REASON_EFFECT` only for resolution detach. |
| Skipping the `chk==0` overlay-removal check. | Use `CheckRemoveOverlayCard` before `RemoveOverlayCard`. |
| Forgetting that `RemoveOverlayCard` returns the actual removed count. | Check the return when the rest of the operation depends on detaching successfully. |
| Reusing a target-branch material group after resolution changes. | Rebuild and recheck the group in the operation before `Duel.XyzSummon`. |
| Using Level-free procedures for double-material effects. | Local `procedure.lua` comments that `EFFECT_DOUBLE_XMATERIAL` is not supported in the Level-free helper. |

## Useful API Pages

- [`Auxiliary.AddXyzProcedure`](/api/functions/Auxiliary/AddXyzProcedure)
- [`Auxiliary.AddXyzProcedureLevelFree`](/api/functions/Auxiliary/AddXyzProcedureLevelFree)
- [`Auxiliary.XyzCondition`](/api/functions/Auxiliary/XyzCondition)
- [`Auxiliary.XyzTarget`](/api/functions/Auxiliary/XyzTarget)
- [`Auxiliary.XyzOperation`](/api/functions/Auxiliary/XyzOperation)
- [`Auxiliary.XyzAlterFilter`](/api/functions/Auxiliary/XyzAlterFilter)
- [`Auxiliary.CheckXyz2XMaterial`](/api/functions/Auxiliary/CheckXyz2XMaterial)
- [`Duel.CheckXyzMaterial`](/api/functions/Duel/CheckXyzMaterial)
- [`Duel.SelectXyzMaterial`](/api/functions/Duel/SelectXyzMaterial)
- [`Duel.XyzSummon`](/api/functions/Duel/XyzSummon)
- [`Duel.Overlay`](/api/functions/Duel/Overlay)
- [`Duel.GetOverlayGroup`](/api/functions/Duel/GetOverlayGroup)
- [`Duel.GetOverlayCount`](/api/functions/Duel/GetOverlayCount)
- [`Duel.RemoveOverlayCard`](/api/functions/Duel/RemoveOverlayCard)
- [`Card.IsXyzSummonable`](/api/functions/Card/IsXyzSummonable)
- [`Card.IsCanBeXyzMaterial`](/api/functions/Card/IsCanBeXyzMaterial)
- [`Card.IsCanOverlay`](/api/functions/Card/IsCanOverlay)
- [`Card.IsXyzLevel`](/api/functions/Card/IsXyzLevel)
- [`Card.IsXyzType`](/api/functions/Card/IsXyzType)
- [`Card.GetOverlayGroup`](/api/functions/Card/GetOverlayGroup)
- [`Card.GetOverlayCount`](/api/functions/Card/GetOverlayCount)
- [`Card.CheckRemoveOverlayCard`](/api/functions/Card/CheckRemoveOverlayCard)
- [`Card.RemoveOverlayCard`](/api/functions/Card/RemoveOverlayCard)
- [`Card.SetMaterial`](/api/functions/Card/SetMaterial)
- [`Group.GetClassCount`](/api/functions/Group/GetClassCount)
