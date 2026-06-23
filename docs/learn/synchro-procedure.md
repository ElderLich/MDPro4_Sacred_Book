# Synchro Procedure Guide

Synchro scripts are usually split into two different jobs. The Synchro Monster
script registers the procedure that says which materials are legal. A separate
card effect may later tell a player to perform a Synchro Summon, but that
effect still asks the Synchro Monster's own procedure whether the Summon can be
performed.

This is different from most Fusion and Ritual scripts. A Fusion Spell or Ritual
Spell often owns the material selection flow. A normal Synchro Monster usually
owns its own Summon procedure from the Extra Deck.

## The Two Layers

| Layer | Where it usually lives | What it does |
| --- | --- | --- |
| Synchro Monster procedure | The Synchro Monster script in `initial_effect` | Registers an `EFFECT_SPSUMMON_PROC` in the Extra Deck with `SUMMON_TYPE_SYNCHRO`. |
| Effect that performs a Synchro Summon | A Spell, Trap, or monster effect | Checks [`Card.IsSynchroSummonable`](/api/functions/Card/IsSynchroSummonable), then calls [`Duel.SynchroSummon`](/api/functions/Duel/SynchroSummon). |
| Custom Synchro-like Special Summon | A very specific card script | Uses `SUMMON_TYPE_SYNCHRO` with manual `SpecialSummonStep`/`CompleteProcedure` handling. Copy a close local script when you need this. |

For most Synchro Monsters, begin with the first layer. The procedure is what
lets the engine answer "can this monster be properly Synchro Summoned right
now?"

## Standard Synchro Procedure

Salamangreat Burst Gryphon (`c10140443.lua`) uses the most common shape:

```lua
function s.initial_effect(c)
    c:EnableReviveLimit()
    aux.AddSynchroProcedure(c,nil,aux.NonTuner(nil),1)
end
```

Read that as:

| Piece | Meaning |
| --- | --- |
| `c:EnableReviveLimit()` | Marks the monster as a proper-Summon monster. After it is properly Synchro Summoned, it can be revived by later effects that allow it. |
| `nil` as the first filter | Any legal Tuner is accepted. |
| `aux.NonTuner(nil)` | The remaining materials must be non-Tuners. |
| `1` | At least one non-Tuner material is required. |
| omitted `maxc` | The helper caps the non-Tuner count by the Synchro Monster's Level minus 1. |

The helper does not just store a label. It creates a field Summon procedure on
the Synchro Monster while it is in the Extra Deck.

## Tuner And Non-Tuner Filters

The standard helper is:

```lua
aux.AddSynchroProcedure(c,f1,f2,minc,maxc)
```

| Argument | Meaning |
| --- | --- |
| `c` | The Synchro Monster receiving the procedure. |
| `f1` | Optional filter for the Tuner material. `nil` means any legal Tuner. |
| `f2` | Optional filter for non-Tuner materials. Use [`aux.NonTuner`](/api/functions/Auxiliary/NonTuner) when you need the non-Tuner slot. |
| `minc` | Minimum number of non-Tuner materials. |
| `maxc` | Optional maximum number of non-Tuner materials. If omitted, the helper caps it by the Synchro Monster's Level. |

Use the local helper filters instead of hand-testing `TYPE_TUNER` in your own
procedure filters:

| Pattern | Use |
| --- | --- |
| [`aux.Tuner(nil)`](/api/functions/Auxiliary/Tuner) | A filter for any card treated as a Tuner for this Synchro Monster. |
| `aux.Tuner(Card.IsSetCard,0x2)` | A Tuner that also belongs to a specific set. |
| [`aux.NonTuner(nil)`](/api/functions/Auxiliary/NonTuner) | A filter for any card treated as a non-Tuner for this Synchro Monster. |
| `aux.NonTuner(Card.IsAttribute,ATTRIBUTE_FIRE)` | A non-Tuner with an extra requirement. |

Those helpers call [`Card.IsTuner`](/api/functions/Card/IsTuner) and
[`Card.IsNotTuner`](/api/functions/Card/IsNotTuner) with the Synchro Monster
context. That matters for cards whose Tuner status is changed by an effect.

Turbo Cannon (`c13574687.lua`) shows a listed-Tuner pattern:

```lua
aux.AddMaterialCodeList(c,6142213)
aux.AddSynchroProcedure(c,aux.FilterBoolFunction(Card.IsCode,6142213),aux.NonTuner(nil),1,1)
c:EnableReviveLimit()
```

`AddMaterialCodeList` records the listed material for text/helper checks. The
Summon procedure still comes from `AddSynchroProcedure`: the first filter
requires card `6142213`, and `1,1` means exactly one non-Tuner.

## What The Helper Builds

Local `procedure.lua` builds an `EFFECT_SPSUMMON_PROC` effect:

```lua
local e1=Effect.CreateEffect(c)
e1:SetDescription(1164)
e1:SetType(EFFECT_TYPE_FIELD)
e1:SetCode(EFFECT_SPSUMMON_PROC)
e1:SetProperty(EFFECT_FLAG_CANNOT_DISABLE+EFFECT_FLAG_UNCOPYABLE)
e1:SetRange(LOCATION_EXTRA)
e1:SetCondition(Auxiliary.SynCondition(f1,f2,minc,maxc))
e1:SetTarget(Auxiliary.SynTarget(f1,f2,minc,maxc))
e1:SetOperation(Auxiliary.SynOperation(f1,f2,minc,maxc))
e1:SetValue(SUMMON_TYPE_SYNCHRO)
c:RegisterEffect(e1)
```

That means a normal Synchro Summon is not activated as a Chain Link. The engine
checks this Special Summon procedure while the card is in the Extra Deck, asks
the target branch to select materials, and then lets the operation branch move
those materials.

The helper also refuses the procedure for a face-up Pendulum Synchro Monster in
the Extra Deck. That check is directly in `Auxiliary.SynCondition`.

## Material Legality

The standard target branch delegates the hard work to the core Synchro helpers:

| Situation | Local helper used |
| --- | --- |
| Checking whether the Summon can happen | [`Duel.CheckSynchroMaterial`](/api/functions/Duel/CheckSynchroMaterial) |
| Selecting ordinary Synchro Materials | [`Duel.SelectSynchroMaterial`](/api/functions/Duel/SelectSynchroMaterial) |
| Checking with a required Tuner material | [`Duel.CheckTunerMaterial`](/api/functions/Duel/CheckTunerMaterial) |
| Selecting with a required Tuner material | [`Duel.SelectTunerMaterial`](/api/functions/Duel/SelectTunerMaterial) |

The material pool starts from [`Duel.GetSynchroMaterial`](/api/functions/Duel/GetSynchroMaterial).
Local `procedure.lua` then filters candidates through
[`Card.IsCanBeSynchroMaterial`](/api/functions/Card/IsCanBeSynchroMaterial).

Level math uses [`Card.GetSynchroLevel`](/api/functions/Card/GetSynchroLevel),
not always the card's visible Level. Some cards provide alternate Synchro
Levels. If you write custom checks, use the same value the procedure uses or
your target branch can say "yes" while the actual Summon says "no."

## Operation Order

The standard operation branch is short:

```lua
local g=e:GetLabelObject()
c:SetMaterial(g)
Duel.SendtoGrave(g,REASON_MATERIAL+REASON_SYNCHRO)
g:DeleteGroup()
```

The target branch stored the selected group on the procedure effect. The
operation branch records it as the Synchro Monster's material group, sends the
materials to the GY with Synchro material reason flags, and releases the kept
Group object.

Do not put `Duel.SpecialSummon` inside this operation. For an
`EFFECT_SPSUMMON_PROC`, the core is already performing the rule Summon around
the procedure's condition, target, and operation.

## Mixed Synchro Procedures

Some Synchro Monsters do not fit "1 Tuner + one or more non-Tuners." Use:

```lua
aux.AddSynchroMixProcedure(c,f1,f2,f3,f4,minc,maxc,gc)
```

| Argument | Meaning |
| --- | --- |
| `f1`, `f2`, `f3` | Up to three fixed one-card material filters. Pass `nil` for unused fixed slots. |
| `f4` | Repeated variable material filter. |
| `minc`, `maxc` | Minimum and maximum count for the repeated `f4` materials. |
| `gc` | Optional final group check. Use it for custom restrictions that need the whole selected group. |

Crystron Quariongandrax (`c13455674.lua`) needs two or more Tuners plus one
non-Tuner:

```lua
aux.AddSynchroMixProcedure(c,aux.NonTuner(nil),nil,nil,aux.Tuner(nil),2,99)
c:EnableReviveLimit()
```

Here the fixed slot is one non-Tuner. The repeated slot is a Tuner, with at
least two copies. The local helper caps impossible maximum counts during its
own check, so scripts often pass a high number such as `99` for "as many as the
Summon can legally use."

The mixed helper checks several details that are easy to miss in a hand-written
script:

- the exact Synchro Level total with `Card.GetSynchroLevel`
- mandatory Synchro Materials through `EFFECT_MUST_BE_SMATERIAL`
- Extra Monster Zone and Main Monster Zone availability through
  `Duel.GetLocationCountFromEx`
- hand Synchro rules through [`Card.GetHandSynchro`](/api/functions/Card/GetHandSynchro)
  and [`Auxiliary.SynMixHandCheck`](/api/functions/Auxiliary/SynMixHandCheck)
- Tuner limits returned by materials
- the Flower Cardian alternate Synchro Level path used by local scripts

That is why custom Synchro procedures should start from `AddSynchroProcedure`
or `AddSynchroMixProcedure` whenever possible.

## Effects That Synchro Summon

Some effects instruct a player to Synchro Summon during resolution. Those
effects do not need to rebuild every Synchro rule by hand. They find a legal
Synchro Monster with `Card.IsSynchroSummonable`, then call
`Duel.SynchroSummon`.

Hop Ear Squadron (`c1980574.lua`) is a compact local example. Its target branch
checks that the hand monster can be Special Summoned first, then builds a
temporary material group from itself and the chosen face-up monster:

```lua
function s.synfilter(c,tp,mc)
    local mg=Group.FromCards(c,mc)
    return c:IsFaceup()
        and Duel.IsExistingMatchingCard(Card.IsSynchroSummonable,tp,LOCATION_EXTRA,0,1,nil,nil,mg)
end
```

After Hop Ear Squadron is Special Summoned and the target is rechecked, the
operation rebuilds the group and asks the Extra Deck again:

```lua
local mg=Group.FromCards(c,tc)
local g=Duel.GetMatchingGroup(Card.IsSynchroSummonable,tp,LOCATION_EXTRA,0,nil,nil,mg)
if g:GetCount()>0 then
    Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_SPSUMMON)
    local sg=g:Select(tp,1,1,nil)
    Duel.SynchroSummon(tp,sg:GetFirst(),nil,mg)
end
```

The fourth argument, `mg`, restricts the Summon to that material group. The
player still chooses the final Synchro Monster from legal options, and the
chosen monster's registered procedure still controls the exact material rules.

When you script this pattern, recheck at resolution. A target that was legal
when the Chain Link was activated may leave the field, turn face-down, or stop
being usable as Synchro Material.

## Advanced Manual Synchro Summons

A few card effects Special Summon a monster and mark that Summon as a Synchro
Summon without running a normal material-selection procedure at that moment.
Accel Synchro Stardust Dragon (`c30983281.lua`) has a local example:

```lua
tc:SetMaterial(nil)
if Duel.SpecialSummonStep(tc,SUMMON_TYPE_SYNCHRO,tp,tp,false,false,POS_FACEUP) then
    -- temporary effects are applied here
    tc:CompleteProcedure()
end
Duel.SpecialSummonComplete()
```

Use this only when the card text and local script pattern really call for it.
If actual materials are being consumed, record them with
[`Card.SetMaterial`](/api/functions/Card/SetMaterial) before moving them, use
the proper `REASON_MATERIAL+REASON_SYNCHRO` flags, and call
[`Card.CompleteProcedure`](/api/functions/Card/CompleteProcedure) after the
Special Summon succeeds.

The same Accel Synchro Stardust Dragon script also shows a full material-group
check for a later Synchro Summon:

```lua
function s.syncheck(g,tp,syncard)
    return aux.SynMixHandCheck(g,tp,syncard)
        and syncard:IsSynchroSummonable(nil,g,#g-1,#g-1)
end
```

It uses [`Auxiliary.SynGroupCheckLevelAddition`](/api/functions/Auxiliary/SynGroupCheckLevelAddition)
around `Group.CheckSubGroup` so the player is not offered material groups that
cannot reach the Synchro Monster's Level.

## Material Memory After The Summon

Effects often care which cards were used as Synchro Material. Salamangreat
Burst Gryphon uses `EFFECT_MATERIAL_CHECK` to remember whether a copy of itself
was used:

```lua
local e1=Effect.CreateEffect(c)
e1:SetType(EFFECT_TYPE_SINGLE)
e1:SetCode(EFFECT_MATERIAL_CHECK)
e1:SetValue(s.check)
c:RegisterEffect(e1)

function s.check(e,c)
    if c:GetMaterial():IsExists(Card.IsCode,1,nil,id) then
        e:SetLabel(1)
    else
        e:SetLabel(0)
    end
end
```

The later trigger checks both the Summon type and the label:

```lua
function s.regcon(e,tp,eg,ep,ev,re,r,rp)
    local c=e:GetHandler()
    return c:IsSummonType(SUMMON_TYPE_SYNCHRO)
        and e:GetLabelObject():GetLabel()==1
end
```

This is safer than trying to inspect materials long after the Summon, because
the script records the answer at the material-check timing.

## Custom Synchro Material Providers

[`Duel.SetSynchroMaterial`](/api/functions/Duel/SetSynchroMaterial) is not the
normal standard-procedure storage path. Standard `Auxiliary.SynTarget` keeps the
selected group on the procedure effect, then `Auxiliary.SynOperation` reads it.

`Duel.SetSynchroMaterial` appears in local custom material-provider scripts
such as Flower Cardian Peony with Butterfly (`c57261568.lua`) and Flower
Cardian Willow with Calligrapher (`c89818984.lua`). Those scripts register
`EFFECT_SYNCHRO_MATERIAL_CUSTOM`, build a custom group, and then store the
chosen group for the core to use:

```lua
local g=Group.FromCards(c)
local mg=Duel.GetSynchroMaterial(tp):Filter(s.synfilter,c,syncard,c,f)
-- custom selection loop
Duel.SetSynchroMaterial(g)
```

Treat that as an advanced extension point. For ordinary Synchro Monsters and
ordinary effects that Synchro Summon, use the procedure helpers and
`Duel.SynchroSummon`.

## Common Pitfalls

| Mistake | Better habit |
| --- | --- |
| Forgetting `EnableReviveLimit` on a Synchro Monster. | Put `EnableReviveLimit` near the Synchro procedure in `initial_effect`. |
| Testing only `TYPE_TUNER` in material filters. | Use `aux.Tuner`, `aux.NonTuner`, `Card.IsTuner`, or `Card.IsNotTuner` with the Synchro Monster context. |
| Manually summing `GetLevel()` for custom checks. | Use `Card.GetSynchroLevel` or the local helper checks. |
| Moving Synchro Materials with plain effect reasons. | Standard procedures send with `REASON_MATERIAL+REASON_SYNCHRO`. |
| Calling `Duel.SpecialSummon` inside an `EFFECT_SPSUMMON_PROC` operation. | Let the rule procedure move materials only; the core handles the Summon around it. |
| Checking one material group in `target` and using another in `operation`. | Rebuild and recheck the group at resolution, especially for effects like Hop Ear Squadron. |
| Forgetting `CompleteProcedure` in manual Synchro-style Special Summons. | Call it after a successful `SpecialSummonStep` or `SpecialSummon` when the Summon is meant to be proper. |
| Ignoring hand Synchro and mandatory material rules in mixed custom checks. | Reuse `AddSynchroMixProcedure`, `SynMixHandCheck`, and local group-check helpers. |
| Treating `Duel.SetSynchroMaterial` as the standard helper's material movement call. | Reserve it for custom material-provider effects; standard helper operations store and move the selected group themselves. |

## Useful API Pages

- [`Auxiliary.AddSynchroProcedure`](/api/functions/Auxiliary/AddSynchroProcedure)
- [`Auxiliary.AddSynchroProcedure2`](/api/functions/Auxiliary/AddSynchroProcedure2)
- [`Auxiliary.AddSynchroMixProcedure`](/api/functions/Auxiliary/AddSynchroMixProcedure)
- [`Auxiliary.Tuner`](/api/functions/Auxiliary/Tuner)
- [`Auxiliary.NonTuner`](/api/functions/Auxiliary/NonTuner)
- [`Auxiliary.SynMixHandCheck`](/api/functions/Auxiliary/SynMixHandCheck)
- [`Auxiliary.SynGroupCheckLevelAddition`](/api/functions/Auxiliary/SynGroupCheckLevelAddition)
- [`Duel.GetSynchroMaterial`](/api/functions/Duel/GetSynchroMaterial)
- [`Duel.CheckSynchroMaterial`](/api/functions/Duel/CheckSynchroMaterial)
- [`Duel.SelectSynchroMaterial`](/api/functions/Duel/SelectSynchroMaterial)
- [`Duel.CheckTunerMaterial`](/api/functions/Duel/CheckTunerMaterial)
- [`Duel.SelectTunerMaterial`](/api/functions/Duel/SelectTunerMaterial)
- [`Duel.SynchroSummon`](/api/functions/Duel/SynchroSummon)
- [`Duel.SetSynchroMaterial`](/api/functions/Duel/SetSynchroMaterial)
- [`Card.IsSynchroSummonable`](/api/functions/Card/IsSynchroSummonable)
- [`Card.IsCanBeSynchroMaterial`](/api/functions/Card/IsCanBeSynchroMaterial)
- [`Card.GetSynchroLevel`](/api/functions/Card/GetSynchroLevel)
- [`Card.GetHandSynchro`](/api/functions/Card/GetHandSynchro)
- [`Card.SetMaterial`](/api/functions/Card/SetMaterial)
- [`Card.CompleteProcedure`](/api/functions/Card/CompleteProcedure)
- [`Group.CheckSubGroup`](/api/functions/Group/CheckSubGroup)
- [`Group.CheckWithSumEqual`](/api/functions/Group/CheckWithSumEqual)
