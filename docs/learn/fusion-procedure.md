# Fusion Procedure Guide

Fusion scripting has two halves that beginners often mix together:

1. The Fusion Monster declares what counts as its Fusion Materials.
2. A Spell, Trap, monster effect, or procedure effect collects materials and
   performs the Fusion Summon.

Those halves meet at `Card.CheckFusionMaterial` and
`Duel.SelectFusionMaterial`. The Fusion Monster's material procedure tells the
core what combinations are legal; the effect that Summons it decides where the
materials may come from and how those materials move.

For a guided walkthrough of the actual player prompts, optional summons,
Chain Material routes, and changing material availability, continue with
[Fusion Summon Choices](fusion-summon-choices).

## The Two Layers

| Layer | Where it usually lives | What it does |
| --- | --- | --- |
| Fusion Monster material requirement | The Fusion Monster script in `initial_effect` | Registers `EFFECT_FUSION_MATERIAL` with helpers such as `aux.AddFusionProcCode2` or `aux.AddFusionProcFunRep`. |
| Fusion Summon effect | A Spell/Trap/monster effect that Summons from the Extra Deck | Gathers material candidates, checks Fusion Monsters, lets the player choose materials, moves them, and Special Summons with `SUMMON_TYPE_FUSION`. |

If a Fusion Monster has no material procedure, generic Fusion Spells cannot know
how to Summon it. If a Fusion Spell has no Summon operation, the Fusion Monster
material procedure will never be used.

## Fusion Monster Material Procedures

Fusion Monsters normally start by enabling their proper-Summon rule, then
registering a material procedure:

```lua
function s.initial_effect(c)
    c:EnableReviveLimit()
    aux.AddFusionProcFunRep(c,s.ffilter,2,true)
end

function s.ffilter(c)
    return c:IsFusionAttribute(ATTRIBUTE_DARK)
        and c:IsOnField()
        and not c:IsType(TYPE_TOKEN)
end
```

Starving Venom Fusion Dragon (`c41209827.lua`) uses that pattern. Its material
helper means "2 DARK monsters on the field, excluding Tokens." The helper
registers an `EFFECT_TYPE_SINGLE` effect with `EFFECT_FUSION_MATERIAL`; it does
not perform a Summon by itself.

For fixed names, local scripts use code helpers:

```lua
function c10248389.initial_effect(c)
    c:EnableReviveLimit()
    aux.AddFusionProcCode2(c,97023549,11460577,false,false)
end
```

The common material-definition helpers are:

| Helper | Use it when the material text says... |
| --- | --- |
| [`aux.AddFusionProcCode2`](/api/functions/Auxiliary/AddFusionProcCode2) | Two specific card names. |
| [`aux.AddFusionProcCode3`](/api/functions/Auxiliary/AddFusionProcCode3) / [`Code4`](/api/functions/Auxiliary/AddFusionProcCode4) | Three or four specific card names. |
| [`aux.AddFusionProcFun2`](/api/functions/Auxiliary/AddFusionProcFun2) | One material matching filter A plus one material matching filter B. |
| [`aux.AddFusionProcFunRep`](/api/functions/Auxiliary/AddFusionProcFunRep) | A fixed number of materials all matching the same filter. |
| [`aux.AddFusionProcFunRep2`](/api/functions/Auxiliary/AddFusionProcFunRep2) | A variable number of materials matching one filter. |
| [`aux.AddFusionProcMix`](/api/functions/Auxiliary/AddFusionProcMix) | A custom list of fixed code/filter slots. |
| [`aux.AddFusionProcMixRep`](/api/functions/Auxiliary/AddFusionProcMixRep) | Fixed slots plus a repeated variable slot. |
| [`aux.AddFusionProcShaddoll`](/api/functions/Auxiliary/AddFusionProcShaddoll) | The local Shaddoll two-material pattern. |

Many helpers accept `sub` and `insf`:

| Parameter | Meaning |
| --- | --- |
| `sub` | Allows Fusion Substitute material checks when the procedure supports them. |
| `insf` | Allows the procedure check with no material group, used by Instant Fusion-style handling. |

Most beginner scripts should copy the `sub` and `insf` values from a close local
Fusion Monster. The flags affect legality in the material condition, not only
the player prompt.

## Fusion-Specific Material Checks

Inside Fusion Material filters, prefer Fusion-aware card checks:

```lua
return c:IsFusionSetCard(0x9d)
```

Fusion material identity is not always the same as ordinary identity. The core
has functions such as:

- [`Card.IsFusionCode`](/api/functions/Card/IsFusionCode)
- [`Card.IsFusionSetCard`](/api/functions/Card/IsFusionSetCard)
- [`Card.IsFusionType`](/api/functions/Card/IsFusionType)
- [`Card.IsFusionAttribute`](/api/functions/Card/IsFusionAttribute)

Those checks can see Fusion-only code, set, type, and Attribute changes. For
Fusion Material text, they are usually safer than ordinary `IsCode`,
`IsSetCard`, `IsType`, or `IsAttribute`.

The lower-level legality check is
[`Card.IsCanBeFusionMaterial`](/api/functions/Card/IsCanBeFusionMaterial). It
answers whether a candidate card may be used as Fusion Material for a Fusion
Monster and Summon type. Material procedures call it internally, and manual
Fusion effects often use it before adding unusual material locations.

## A Standard Fusion Spell Flow

Polymerization (`c24094653.lua`) is the clean local model for a standard Fusion
Spell. It activates like an ordinary Spell, but the target and operation do the
Fusion work.

The target branch checks whether a Fusion Monster can be Summoned:

```lua
function c24094653.filter2(c,e,tp,m,f,chkf)
    return c:IsType(TYPE_FUSION) and (not f or f(c))
        and c:IsCanBeSpecialSummoned(e,SUMMON_TYPE_FUSION,tp,false,false)
        and c:CheckFusionMaterial(m,nil,chkf)
end

function c24094653.target(e,tp,eg,ep,ev,re,r,rp,chk)
    if chk==0 then
        local chkf=tp
        local mg1=Duel.GetFusionMaterial(tp)
        local res=Duel.IsExistingMatchingCard(c24094653.filter2,tp,
            LOCATION_EXTRA,0,1,nil,e,tp,mg1,nil,chkf)
        if not res then
            local ce=Duel.GetChainMaterial(tp)
            if ce~=nil then
                local fgroup=ce:GetTarget()
                local mg2=fgroup(ce,e,tp)
                local mf=ce:GetValue()
                res=Duel.IsExistingMatchingCard(c24094653.filter2,tp,
                    LOCATION_EXTRA,0,1,nil,e,tp,mg2,mf,chkf)
            end
        end
        return res
    end
    Duel.SetOperationInfo(0,CATEGORY_SPECIAL_SUMMON,nil,1,tp,LOCATION_EXTRA)
end
```

The important pieces are:

| Piece | Job |
| --- | --- |
| `chkf=tp` | Tells the Fusion Material check to respect the player's Extra Monster Zone and Main Monster Zone availability. |
| [`Duel.GetFusionMaterial`](/api/functions/Duel/GetFusionMaterial) | Gets the player's normal Fusion Material pool. |
| [`Card.CheckFusionMaterial`](/api/functions/Card/CheckFusionMaterial) | Asks the chosen Fusion Monster's registered material procedure whether the pool can satisfy it. |
| [`Duel.GetChainMaterial`](/api/functions/Duel/GetChainMaterial) | Optional fallback for Chain Material-style effects. |
| `f` / `mf` | Extra Chain Material filter supplied by the Chain Material effect. |

The target branch does not move cards. It only proves that at least one legal
Fusion Summon is currently possible.

## Operation Order

The operation branch repeats the Fusion search at resolution, because the field
may have changed after activation:

```lua
local mg1=Duel.GetFusionMaterial(tp):Filter(c24094653.filter1,nil,e)
local sg1=Duel.GetMatchingGroup(c24094653.filter2,tp,
    LOCATION_EXTRA,0,nil,e,tp,mg1,nil,chkf)
```

Then it selects the Fusion Monster, selects the materials, records them, moves
them, and Summons:

```lua
local mat1=Duel.SelectFusionMaterial(tp,tc,mg1,nil,chkf)
tc:SetMaterial(mat1)
Duel.SendtoGrave(mat1,REASON_EFFECT+REASON_MATERIAL+REASON_FUSION)
Duel.BreakEffect()
Duel.SpecialSummon(tc,SUMMON_TYPE_FUSION,tp,tp,false,false,POS_FACEUP)
tc:CompleteProcedure()
```

Keep that order:

1. [`Duel.SelectFusionMaterial`](/api/functions/Duel/SelectFusionMaterial)
   asks the player for a legal material group.
2. [`Card.SetMaterial`](/api/functions/Card/SetMaterial) records the materials
   on the Fusion Monster.
3. The material movement function sends, banishes, or returns the materials
   with `REASON_EFFECT+REASON_MATERIAL+REASON_FUSION`.
4. [`Duel.BreakEffect`](/api/functions/Duel/BreakEffect) separates the material
   movement and summon in effect timing; it is not merely a visual pause.
5. [`Duel.SpecialSummon`](/api/functions/Duel/SpecialSummon) uses
   `SUMMON_TYPE_FUSION`.
6. [`Card.CompleteProcedure`](/api/functions/Card/CompleteProcedure) marks the
   monster as properly Fusion Summoned.

The local core maps `SUMMON_TYPE_FUSION` to `REASON_FUSION` for material event
handling. The explicit `REASON_FUSION` flag in the movement call is still the
local script pattern for Fusion Material movement.

## Using The Local Fusion Effect Helper

`procedure.lua` also provides a configurable helper for Fusion Summon effects:
[`Auxiliary.AddFusionEffectProcUltimate`](/api/functions/Auxiliary/AddFusionEffectProcUltimate).

It creates an activation effect whose default behavior is close to
Polymerization:

- `params.mat_location` defaults to `LOCATION_HAND+LOCATION_MZONE`;
- `params.mat_filter` defaults to `Auxiliary.FMaterialFilter`, which checks
  `Card.IsCanBeFusionMaterial`;
- `params.mat_operation` defaults to sending materials to the GY with
  `REASON_EFFECT+REASON_MATERIAL+REASON_FUSION`;
- `params.grave_operation` defaults to banishing GY materials;
- `params.deck_operation` and `params.extra_operation` default to the main
  material operation unless overridden;
- `params.reg=false` returns the effect without registering it.

The smaller wrapper
[`Auxiliary.AddFusionEffectProc`](/api/functions/Auxiliary/AddFusionEffectProc)
fills the common `filter`, `mat_location`, `mat_filter`, and `mat_operation`
fields before calling the ultimate helper.

Many current local card scripts write the Fusion flow manually, especially older
or highly custom Fusion Spells. The helper is still useful for new scripts when
the card text matches its parameter table.

## Deck And Extra Material

Deck Fusion cards add another material group before checking the Extra Deck.
Red-Eyes Fusion (`c6172122.lua`) and Branded Fusion (`c44362883.lua`) both use
the same local shape:

```lua
local mg1=Duel.GetFusionMaterial(tp)
local mg2=Duel.GetMatchingGroup(s.filter0,tp,LOCATION_DECK,0,nil)
mg1:Merge(mg2)
```

Their Deck material filters still check Fusion-material legality and movement:

```lua
function s.filter0(c)
    return c:IsType(TYPE_MONSTER)
        and c:IsCanBeFusionMaterial()
        and c:IsAbleToGrave()
end
```

Deck Fusion cards usually need extra legality checks. Red-Eyes Fusion uses
`aux.FCheckAdditional` to require a "Red-Eyes" material, and Branded Fusion uses
it to require a material with the listed code and at most two materials:

```lua
function c44362883.fcheck(tp,sg,fc)
    return sg:GetCount()<=2 and sg:IsExists(Card.IsFusionCode,1,nil,68468459)
end
```

`aux.FCheckAdditional` is a temporary global hook. Set it only around the
Fusion Material check or selection that needs it, then clear it immediately.

## Different Material Movement

Not all Fusion effects send materials to the GY. The local helper has default
material operations for common movement choices:

| Operation | Movement |
| --- | --- |
| `Auxiliary.FMaterialToGrave` | `Duel.SendtoGrave(mat,REASON_EFFECT+REASON_MATERIAL+REASON_FUSION)` |
| `Auxiliary.FMaterialRemove` | `Duel.Remove(mat,POS_FACEUP,REASON_EFFECT+REASON_MATERIAL+REASON_FUSION)` |
| `Auxiliary.FMaterialToDeck` | `Duel.SendtoDeck(mat,nil,2,REASON_EFFECT+REASON_MATERIAL+REASON_FUSION)` |

Manual scripts follow the same idea. Choose movement based on card text, and
make sure the candidate material filter matches that movement. A card that will
banish materials should check `IsAbleToRemove`; a card that sends materials to
the GY should check `IsAbleToGrave`.

## Chain Material

Polymerization-style scripts include a Chain Material fallback:

```lua
local ce=Duel.GetChainMaterial(tp)
if ce~=nil then
    local fgroup=ce:GetTarget()
    local mg2=fgroup(ce,e,tp)
    local mf=ce:GetValue()
    res=Duel.IsExistingMatchingCard(s.filter2,tp,LOCATION_EXTRA,0,1,nil,
        e,tp,mg2,mf,chkf)
end
```

If the selected Fusion Monster is Summoned through that Chain Material path, the
script does not move the materials itself. It calls the Chain Material
operation:

```lua
local mat2=Duel.SelectFusionMaterial(tp,tc,mg2,nil,chkf)
local fop=ce:GetOperation()
fop(ce,e,tp,tc,mat2)
```

For beginner scripts, keep the Chain Material block intact when copying a
standard Fusion Spell. Removing only half of it can make activation checks and
resolution disagree.

## Contact Fusion

Contact Fusion is related, but it is not the same as a normal Fusion Spell. The
local helper [`Auxiliary.AddContactFusionProcedure`](/api/functions/Auxiliary/AddContactFusionProcedure)
registers a Special Summon procedure on the Fusion Monster. Its material filter
uses `Card.IsCanBeFusionMaterial(fc,SUMMON_TYPE_SPECIAL)`, and its operation
uses a material operation such as sending materials to the Deck.

That deserves its own focused guide later. For this page, the key distinction is
simple: normal Fusion effects Summon with `SUMMON_TYPE_FUSION`; Contact Fusion
procedures are custom Special Summon procedures that still use Fusion Material
checks.

## Common Pitfalls

| Mistake | Better habit |
| --- | --- |
| Writing a Fusion Spell before the Fusion Monsters have material procedures. | Put `EnableReviveLimit` and an `AddFusionProc...` helper on the Fusion Monster first. |
| Using ordinary `IsCode` or `IsSetCard` inside Fusion Material filters. | Prefer `IsFusionCode`, `IsFusionSetCard`, `IsFusionType`, and `IsFusionAttribute` for Fusion Material identity. |
| Moving materials before `SetMaterial`. | Call `tc:SetMaterial(mat)` before sending, banishing, or returning the materials. |
| Sending materials without `REASON_MATERIAL+REASON_FUSION`. | Include `REASON_EFFECT+REASON_MATERIAL+REASON_FUSION` unless a local source-backed card pattern says otherwise. |
| Reusing the target-branch material group in the operation. | Rebuild and re-filter the material group at resolution. |
| Forgetting immunity checks in the operation. | Filter ordinary materials with `not c:IsImmuneToEffect(e)` or a local equivalent before selecting them. |
| Leaving `aux.FCheckAdditional` set. | Set it around the relevant check or selection, then clear it immediately. |
| Treating Contact Fusion as a normal `SUMMON_TYPE_FUSION` Spell. | Use the local Contact Fusion procedure pattern and `SUMMON_TYPE_SPECIAL` material checks. |

## Useful API Pages

- [`Auxiliary.AddFusionEffectProcUltimate`](/api/functions/Auxiliary/AddFusionEffectProcUltimate)
- [`Auxiliary.AddFusionEffectProc`](/api/functions/Auxiliary/AddFusionEffectProc)
- [`Auxiliary.AddFusionProcCode2`](/api/functions/Auxiliary/AddFusionProcCode2)
- [`Auxiliary.AddFusionProcFunRep`](/api/functions/Auxiliary/AddFusionProcFunRep)
- [`Auxiliary.AddFusionProcMix`](/api/functions/Auxiliary/AddFusionProcMix)
- [`Auxiliary.AddContactFusionProcedure`](/api/functions/Auxiliary/AddContactFusionProcedure)
- [`Duel.GetFusionMaterial`](/api/functions/Duel/GetFusionMaterial)
- [`Duel.SelectFusionMaterial`](/api/functions/Duel/SelectFusionMaterial)
- [`Duel.SetFusionMaterial`](/api/functions/Duel/SetFusionMaterial)
- [`Duel.GetChainMaterial`](/api/functions/Duel/GetChainMaterial)
- [`Card.CheckFusionMaterial`](/api/functions/Card/CheckFusionMaterial)
- [`Card.IsCanBeFusionMaterial`](/api/functions/Card/IsCanBeFusionMaterial)
- [`Card.IsFusionCode`](/api/functions/Card/IsFusionCode)
- [`Card.IsFusionSetCard`](/api/functions/Card/IsFusionSetCard)
- [`Card.IsFusionType`](/api/functions/Card/IsFusionType)
- [`Card.IsFusionAttribute`](/api/functions/Card/IsFusionAttribute)
- [`Card.SetMaterial`](/api/functions/Card/SetMaterial)
- [`Card.CompleteProcedure`](/api/functions/Card/CompleteProcedure)
- [`Duel.SendtoGrave`](/api/functions/Duel/SendtoGrave)
- [`Duel.Remove`](/api/functions/Duel/Remove)
- [`Duel.SendtoDeck`](/api/functions/Duel/SendtoDeck)
- [`Duel.SpecialSummon`](/api/functions/Duel/SpecialSummon)
