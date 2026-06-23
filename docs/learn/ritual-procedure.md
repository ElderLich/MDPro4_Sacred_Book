# Ritual Procedure Guide

Ritual scripts look like Spell scripts from the outside, but their resolution
does several Summon-procedure jobs at once: find a Ritual Monster, check that
materials can be used for that exact monster, make the material total legal,
move the materials, Special Summon with `SUMMON_TYPE_RITUAL`, and mark the
monster as properly Summoned.

Most ordinary Ritual Spells should start with the local helpers in
`procedure.lua`. Manual Ritual scripts are still important, but they are for
card text that changes the material source, Summons more than one monster, sends
materials instead of releasing them, or applies extra behavior that does not fit
the helper.

## Helper Or Manual Script

| Need | Local pattern |
| --- | --- |
| A named Ritual Spell that can Ritual Summon one listed monster with equal-or-higher material Levels. | Use [`aux.AddRitualProcGreaterCode`](/api/functions/Auxiliary/AddRitualProcGreaterCode). |
| A Ritual Spell that can Ritual Summon a filtered group of Ritual Monsters with equal-or-higher material Levels. | Use [`aux.AddRitualProcGreater`](/api/functions/Auxiliary/AddRitualProcGreater). |
| A Ritual Spell that needs the material total to exactly equal the Ritual Monster's Level. | Use [`aux.AddRitualProcEqual`](/api/functions/Auxiliary/AddRitualProcEqual) or [`aux.AddRitualProcEqualCode`](/api/functions/Auxiliary/AddRitualProcEqualCode). |
| A Ritual Spell that checks the Ritual Monster's current Level instead of original Level. | Use the `2` variants, such as [`aux.AddRitualProcGreater2`](/api/functions/Auxiliary/AddRitualProcGreater2) or [`aux.AddRitualProcEqual2`](/api/functions/Auxiliary/AddRitualProcEqual2). |
| A Ritual Spell that needs Graveyard extras, material filters, delayed registration, or post-Summon work. | Use [`aux.AddRitualProcUltimate`](/api/functions/Auxiliary/AddRitualProcUltimate) directly or through one of the wrappers. |
| A Ritual Spell that sends Extra Deck material, Summons multiple monsters, or uses a custom resource such as ATK instead of Level. | Write a manual target and operation, usually copying the shape of a close local script. |

The wrappers are thin. They choose a Level function, choose exact vs
greater-or-equal checking, and pass the rest to
`Auxiliary.AddRitualProcUltimate`.

## Small Helper Examples

The simplest local Ritual Spell is a one-line procedure. Doriado's Blessing
(`c23965037.lua`) registers an equal-or-higher Ritual Summon for one monster
code:

```lua
function c23965037.initial_effect(c)
    aux.AddRitualProcGreaterCode(c,99414168)
end
```

That one call creates the activation effect, checks hand material, checks field
material, asks the player to choose a matching Ritual Monster, releases the
selected materials, and Special Summons the monster as a Ritual Summon.

Cycle of the World (`c14094090.lua`) uses a filter instead of a single listed
code, and requires exact Levels:

```lua
function c14094090.initial_effect(c)
    aux.AddRitualProcEqual(c,c14094090.ritual_filter)
end

function c14094090.ritual_filter(c)
    return c:IsType(TYPE_RITUAL) and c:IsSetCard(0x10cf)
end
```

Recette de Viande (`c14166715.lua`) shows a helper with post-Summon behavior.
The local script uses `AddRitualProcGreater2`, checks the Ritual Monster's
current Level, and passes an `extra_operation` callback:

```lua
aux.AddRitualProcGreater2(c,s.filter,LOCATION_HAND,nil,nil,false,s.extraop)
```

Use that last style when the Ritual Summon itself is standard but the card must
do something after a successful Summon.

## What The Main Helper Builds

`Auxiliary.AddRitualProcUltimate` creates a normal Spell activation effect:

```lua
local e1=Effect.CreateEffect(c)
e1:SetCategory(CATEGORY_SPECIAL_SUMMON)
e1:SetType(EFFECT_TYPE_ACTIVATE)
e1:SetCode(EVENT_FREE_CHAIN)
e1:SetTarget(Auxiliary.RitualUltimateTarget(...))
e1:SetOperation(Auxiliary.RitualUltimateOperation(...))
c:RegisterEffect(e1)
```

The local helper defaults `summon_location` to `LOCATION_HAND`. That means a
plain helper Ritual Spell looks for the Ritual Monster in your hand unless a
script passes another location.

The important arguments are:

| Argument | Meaning |
| --- | --- |
| `filter` | Which Ritual Monsters this Spell can Summon. Code wrappers build this from `Card.IsCode`. |
| `level_function` | Which value the material total is compared against, usually `Card.GetOriginalLevel` or `Card.GetLevel`. |
| `greater_or_equal` | `"Greater"` for equal-or-higher material totals, `"Equal"` for exact totals. |
| `summon_location` | Where the Ritual Monster may be selected from. Defaults to hand. |
| `grave_filter` | Optional extra GY material group. The helper merges it into the material pool and later uses Ritual-material movement rules. |
| `mat_filter` | Optional filter applied to the material pool before selection. |
| `pause` | If true, the helper returns the effect without registering it. Scripts can adjust or clone it first. |
| `extra_target` | Optional callback run during the target branch for extra categories or checks. |
| `extra_operation` | Optional callback run after the Ritual Summon operation. |

## Target Branch

The target branch answers "can this Ritual Spell legally be activated now?"

The local helper follows this shape:

1. Collect basic Ritual Materials with
   [`Duel.GetRitualMaterial(tp)`](/api/functions/Duel/GetRitualMaterial).
2. Optionally filter that material group with `mat_filter`.
3. Optionally collect extra GY materials with `grave_filter`.
4. Search for a Ritual Monster that passes
   [`Auxiliary.RitualUltimateFilter`](/api/functions/Auxiliary/RitualUltimateFilter).
5. Set operation info for `CATEGORY_SPECIAL_SUMMON`, and `CATEGORY_REMOVE` if
   GY material will be banished by the Ritual material flow.
6. Run `extra_target` if the script supplied one.

`Auxiliary.RitualUltimateFilter` checks more than the visible card name. It
requires a Ritual Monster, applies the script's `filter`, checks
[`Card.IsCanBeSpecialSummoned`](/api/functions/Card/IsCanBeSpecialSummoned) with
`SUMMON_TYPE_RITUAL`, filters materials through
[`Card.IsCanBeRitualMaterial`](/api/functions/Card/IsCanBeRitualMaterial), and
then verifies that some subgroup can satisfy the required material total.

Because this is only the target branch, it should not move cards. It only proves
that the action is currently possible and records public Chain information.

## Material Checks

The material group from `Duel.GetRitualMaterial` is only the starting pool.
After a Ritual Monster is chosen, the script must still filter by that monster:

```lua
mg=mg:Filter(Card.IsCanBeRitualMaterial,tc,tc)
if tc.mat_filter then
    mg=mg:Filter(tc.mat_filter,tc,tp)
else
    mg:RemoveCard(tc)
end
```

That local pattern prevents materials that are blocked for the chosen Ritual
Monster from appearing in the final selection. The helper also respects a Ritual
Monster's optional `mat_filter` and `mat_group_check` callbacks when scripts
define them.

The material total is checked with Group helpers:

| Helper mode | Local check |
| --- | --- |
| Greater-or-equal | [`Group.CheckWithSumGreater`](/api/functions/Group/CheckWithSumGreater) over `Card.GetRitualLevel`. |
| Exact | [`Group.CheckWithSumEqual`](/api/functions/Group/CheckWithSumEqual) over `Card.GetRitualLevel`. |
| Player selection | [`Group.SelectSubGroup`](/api/functions/Group/SelectSubGroup) with `Auxiliary.RitualCheck`. |

`Card.GetRitualLevel` is used for the material cards. The helper's
`level_function` is used for the Ritual Monster being Summoned. That is why
`AddRitualProcGreater` and `AddRitualProcEqual` use the Ritual Monster's
original Level, while the `2` variants use its current Level.

Local `procedure.lua` also handles cards with additional Ritual material Levels.
Those extra Level values are stored in the high and low halves of the
`GetRitualLevel` result. You usually do not unpack that value yourself; let the
helper's `RitualCheckAdditional` logic do it unless you are writing a special
manual procedure.

## Operation Branch

The operation branch repeats the important checks because the game state may
have changed while the Chain waited to resolve. The local helper re-collects
materials, asks the player to choose the Ritual Monster, filters the material
pool for that monster, lets the player choose a legal subgroup, and then
performs the Summon:

```lua
tc:SetMaterial(mat)
Duel.ReleaseRitualMaterial(mat)
Duel.BreakEffect()
Duel.SpecialSummon(tc,SUMMON_TYPE_RITUAL,tp,tp,false,true,POS_FACEUP)
tc:CompleteProcedure()
```

The order matters:

1. [`Card.SetMaterial`](/api/functions/Card/SetMaterial) records which cards
   were used as material.
2. [`Duel.ReleaseRitualMaterial`](/api/functions/Duel/ReleaseRitualMaterial)
   moves standard Ritual Materials with Ritual-specific handling.
3. [`Duel.BreakEffect`](/api/functions/Duel/BreakEffect) creates the visible
   "then" pause used by many Summon procedures.
4. [`Duel.SpecialSummon`](/api/functions/Duel/SpecialSummon) uses
   `SUMMON_TYPE_RITUAL`.
5. [`Card.CompleteProcedure`](/api/functions/Card/CompleteProcedure) marks the
   Ritual Monster as properly Summoned.

For multi-Summon procedures, local scripts use
[`Duel.SpecialSummonStep`](/api/functions/Duel/SpecialSummonStep) and
[`Duel.SpecialSummonComplete`](/api/functions/Duel/SpecialSummonComplete)
instead of one direct `Duel.SpecialSummon` call.

## Manual Ritual Scripts

Manual Ritual scripts should still look like the helper internally:

```lua
function s.target(e,tp,eg,ep,ev,re,r,rp,chk)
    if chk==0 then
        local mg=Duel.GetRitualMaterial(tp)
        return Duel.IsExistingMatchingCard(aux.RitualUltimateFilter,tp,
            LOCATION_HAND,0,1,nil,s.ritual_filter,e,tp,mg,nil,
            Card.GetLevel,"Greater")
    end
    Duel.SetOperationInfo(0,CATEGORY_SPECIAL_SUMMON,nil,1,tp,LOCATION_HAND)
end

function s.activate(e,tp,eg,ep,ev,re,r,rp)
    local mg=Duel.GetRitualMaterial(tp)
    local tg=Duel.SelectMatchingCard(tp,aux.RitualUltimateFilter,tp,
        LOCATION_HAND,0,1,1,nil,s.ritual_filter,e,tp,mg,nil,
        Card.GetLevel,"Greater")
    local tc=tg:GetFirst()
    if not tc then return end

    mg=mg:Filter(Card.IsCanBeRitualMaterial,tc,tc)
    if tc.mat_filter then
        mg=mg:Filter(tc.mat_filter,tc,tp)
    end

    local lv=tc:GetLevel()
    aux.GCheckAdditional=aux.RitualCheckAdditional(tc,lv,"Greater")
    local mat=mg:SelectSubGroup(tp,aux.RitualCheck,true,1,lv,tp,tc,lv,"Greater")
    aux.GCheckAdditional=nil
    if not mat then return end

    tc:SetMaterial(mat)
    Duel.ReleaseRitualMaterial(mat)
    Duel.BreakEffect()
    if Duel.SpecialSummonStep(tc,SUMMON_TYPE_RITUAL,tp,tp,false,true,POS_FACEUP) then
        tc:CompleteProcedure()
    end
    Duel.SpecialSummonComplete()
end
```

This is close to the local Sonic Tracker pattern. It is useful when a card
needs to change the Ritual Monster after selection, store material values, or
apply a lasting effect to the Summoned monster.

When you write a manual procedure, keep the target branch and operation branch
in sync. A common beginner mistake is to prove one material rule in `target`,
then use a slightly different rule in `activate`.

## Nonstandard Material Movement

Not every Ritual Spell releases every material. Nekroz Kaleidoscope
(`c51124303.lua`) can use a monster from the Extra Deck as the full material.
The local script checks the Extra Deck card as Ritual Material, records it with
`SetMaterial`, then sends it to the GY with Ritual material reason flags instead
of calling `Duel.ReleaseRitualMaterial`:

```lua
tc:SetMaterial(mat)
if not mc:IsLocation(LOCATION_EXTRA) then
    Duel.ReleaseRitualMaterial(mat)
else
    Duel.SendtoGrave(mat,REASON_EFFECT+REASON_MATERIAL+REASON_RITUAL)
end
Duel.BreakEffect()
Duel.SpecialSummon(tc,SUMMON_TYPE_RITUAL,tp,tp,false,true,POS_FACEUP)
tc:CompleteProcedure()
```

That is a card-specific movement rule, not the default Ritual procedure. For a
normal Ritual Spell, use `Duel.ReleaseRitualMaterial`.

Drytron-style scripts are another reason to go manual. The local scripts use
[`Duel.GetRitualMaterialEx`](/api/functions/Duel/GetRitualMaterialEx) and an ATK
based value helper so material adequacy is not only "sum Levels." Treat those as
advanced templates and copy from a close local card when the printed text is
similar.

## Summon Type And Later Effects

The Summon call should use `SUMMON_TYPE_RITUAL`. Other effects can then check
[`Card.IsSummonType`](/api/functions/Card/IsSummonType) to ask whether the
monster was Ritual Summoned.

The local core also maps `SUMMON_TYPE_RITUAL` to `REASON_RITUAL` for material
events. That matters for cards that care how they became material.

`CompleteProcedure` is separate from `SUMMON_TYPE_RITUAL`. The Summon type says
what kind of Summon happened; `CompleteProcedure` marks the monster's proper
Summon procedure as complete for later rule checks.

## Common Pitfalls

| Mistake | Better habit |
| --- | --- |
| Using `Duel.GetRitualMaterial` and immediately selecting from it. | Filter the group with `Card.IsCanBeRitualMaterial` after the Ritual Monster is known. |
| Using `Duel.Release` for ordinary Ritual Materials. | Use `Duel.ReleaseRitualMaterial` so Ritual material movement rules apply. |
| Forgetting `SetMaterial`. | Call `tc:SetMaterial(mat)` before moving the materials. |
| Forgetting `CompleteProcedure`. | Call `tc:CompleteProcedure()` after the Ritual Summon succeeds. |
| Checking only material Levels in `target`. | Also check a Summonable Ritual Monster, Monster Zone availability, and the chosen monster's material restrictions. |
| Mixing original-Level and current-Level helpers accidentally. | Use non-`2` helpers for original Level, `2` helpers for current Level. |
| Copying a manual Ritual script without the operation recheck. | Rebuild the material group and confirm the chosen cards are still legal at resolution. |
| Letting the Ritual Monster become its own material by accident. | Follow the helper pattern: apply `tc.mat_filter` when present, otherwise remove `tc` from the material group. |

## Useful API Pages

- [`Auxiliary.AddRitualProcUltimate`](/api/functions/Auxiliary/AddRitualProcUltimate)
- [`Auxiliary.AddRitualProcGreater`](/api/functions/Auxiliary/AddRitualProcGreater)
- [`Auxiliary.AddRitualProcGreaterCode`](/api/functions/Auxiliary/AddRitualProcGreaterCode)
- [`Auxiliary.AddRitualProcEqual`](/api/functions/Auxiliary/AddRitualProcEqual)
- [`Auxiliary.AddRitualProcEqualCode`](/api/functions/Auxiliary/AddRitualProcEqualCode)
- [`Auxiliary.RitualUltimateFilter`](/api/functions/Auxiliary/RitualUltimateFilter)
- [`Duel.GetRitualMaterial`](/api/functions/Duel/GetRitualMaterial)
- [`Duel.GetRitualMaterialEx`](/api/functions/Duel/GetRitualMaterialEx)
- [`Duel.ReleaseRitualMaterial`](/api/functions/Duel/ReleaseRitualMaterial)
- [`Card.IsCanBeRitualMaterial`](/api/functions/Card/IsCanBeRitualMaterial)
- [`Card.GetRitualLevel`](/api/functions/Card/GetRitualLevel)
- [`Card.SetMaterial`](/api/functions/Card/SetMaterial)
- [`Card.CompleteProcedure`](/api/functions/Card/CompleteProcedure)
- [`Duel.SpecialSummon`](/api/functions/Duel/SpecialSummon)
- [`Duel.SpecialSummonStep`](/api/functions/Duel/SpecialSummonStep)
- [`Duel.SpecialSummonComplete`](/api/functions/Duel/SpecialSummonComplete)
- [`Group.CheckWithSumEqual`](/api/functions/Group/CheckWithSumEqual)
- [`Group.CheckWithSumGreater`](/api/functions/Group/CheckWithSumGreater)
- [`Group.SelectSubGroup`](/api/functions/Group/SelectSubGroup)
