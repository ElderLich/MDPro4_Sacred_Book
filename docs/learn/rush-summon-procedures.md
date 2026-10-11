# Rush Maximum, Fusion, And Ritual

**Prerequisite:** [Rush Duel Scripting](rush-duel-scripting).
**Goal:** identify which helper registers a monster's procedure and which
effect actually performs a summon. These examples describe the imported Rush
library; use its [function reference](/rush/api/functions/) alongside them.

After this overview, follow [Fusion and Ritual player choices](rush-fusion-ritual-choices)
for complete summoning effects, candidate/material selection and cancellation.
[Special Summons and result types](rush-special-summon-results) covers revival
effects, hand procedures and safe follow-up checks.

## Maximum: Center And Side Pieces

The [center card `120150002`](/examples/rush-cards/120150002) registers its two named partners and 3500
Maximum ATK:

```lua
-- Inside the center card's initial_effect(c):
RD.AddCodeList(c,{120150001,120150003})
RD.AddMaximumProcedure(c,3500,120150001,120150003)
```

[`RD.AddMaximumProcedure(card,max_atk,left_code,right_code)`](/rush/api/functions/RushDuel/AddMaximumProcedure) registers the hand
summon procedure, Maximum ATK, and the field occupancy effect. In this library,
the side pieces are represented internally as overlay materials of the center
card. The procedure also marks Maximum mode. That representation explains why
side-piece effects use an XMaterial effect type even though the card is not an
Xyz Monster.

The [left piece `120150001`](/examples/rush-cards/120150001) contains this registration shape:

```lua
e1:SetType(EFFECT_TYPE_XMATERIAL+EFFECT_TYPE_IGNITION)
e1:SetRange(LOCATION_MZONE)
e1:SetLabel(id)
e1:SetCondition(s.condition)
```

The label carries the side piece's identity for Rush used-effect tracking.
Keep the complete condition from the real card: this left piece also checks
LP, pays a hand cost, and rechecks the center's relation before changing ATK.

### Two Different Maximum Checks

| Helper | Input and implementation |
| --- | --- |
| `RD.MaximumMode(e)` | Takes an **Effect**, gets its handler, and checks `EFFECT_MAXIMUM_MODE` plus a nonempty overlay group. Suitable for `SetCondition`. |
| `RD.IsMaximumMode(c)` | Takes a **Card**, checks the Monster Zone, `SUMMON_TYPE_MAXIMUM`, and a nonempty overlay group. |
| `RD.IsPreviousMaximumMode(c)` | Checks Maximum type, summon type, and the previous overlay count for a leaving-field context. |

The first two are not interchangeable spellings. Their marker and summon-type
checks differ, which matters for effects that put a monster into Maximum mode
without following the ordinary summon procedure.

::: warning Data and procedure must agree
`TYPE_MAXIMUM` is `0x8000` in the imported library and MDPro3. That bit alone
does not create the three-piece procedure. Register the center's procedure,
use the actual left/right IDs, and test the three scripts together.
:::

## Fusion: Declare Materials, Then Supply A Summoning Effect

Imported [card `120102001`](/examples/rush-cards/120102001) is a compact material declaration:

```lua
local s,id=GetID()
local materials={120102002,120145007}

function s.initial_effect(c)
    RD.AddCodeList(c,materials)
    RD.AddFusionProcedure(c,materials[1],materials[2])
end
```

`RD.AddCodeList` records the named cards as metadata. [`RD.AddFusionProcedure`](/rush/api/functions/RushDuel/AddFusionProcedure)
registers the Fusion material procedure; it does not activate a Spell or summon
the monster immediately.

The full helper has optional Boolean `sub` and `insf` arguments before the
material declarations. When those positions contain material values instead
of Booleans, this library shifts them into the material list and defaults the
options to true. Read a matching source example before inserting a Boolean:
it changes how the later arguments are interpreted.

On the effect that performs the Fusion Summon,
`RD.CreateFusionEffect(...)` builds target/operation callbacks and returns an
Effect object. The card still supplies its category, activation type, timing,
and registration. Use the Rush helpers for Rush materials; do not substitute
the standard `aux.AddFusionProc...` or `Fusion.*` APIs solely because the names
look similar.

## Ritual: Match The Rush Data Convention

The imported library supports Ritual Monsters in the Extra Deck. It uses a
Fusion bit in their database type for that placement and
`RD.AddRitualProcedure(c)` registers an effect removing the Fusion type at
runtime. This is a compatibility convention of this Rush implementation.

For [card `120280030`](/examples/rush-cards/120280030), the Ritual Spell's structure is:

```lua
local s,id=GetID()

function s.initial_effect(c)
    RD.AddCodeList(c,{120280001})
    local e1=RD.CreateRitualEffect(c,RITUAL_ORIGINAL_LEVEL_GREATER,nil,s.spfilter)
    e1:SetCategory(CATEGORY_SPECIAL_SUMMON)
    e1:SetType(EFFECT_TYPE_ACTIVATE)
    e1:SetCode(EVENT_FREE_CHAIN)
    c:RegisterEffect(e1)
end

function s.spfilter(c)
    return c:IsCode(120280001)
end
```

Here `nil` leaves the optional material filter unset. `s.spfilter` restricts the
monster being summoned. The helper builds the legality and resolution logic;
the card registers the activation effect around it.

Compare [card `120280031`](/examples/rush-cards/120280031): it adds a material filter requiring face-up cards on
the field. Copying only its destination-monster filter would lose that
requirement. The library also has original/current Level and ATK variants;
choose the constant that matches the text and inspect the material checker
instead of replacing it with an ordinary sum over Levels.

## A Test Route For Advanced Cards

| Mechanic | States to compare |
| --- | --- |
| Maximum | All three correct pieces; a missing piece; two copies of one side; center alone; Maximum mode created by an effect. |
| Side-piece effects | Each side's condition and cost; separate used-effect tracking; center leaving or changing state. |
| Fusion | Correct named materials; an invalid material; replacement/substitute permissions; occupied zones; resolution after the available material changes. |
| Ritual | Correct Extra Deck monster; wrong name; valid/invalid material total; hand versus field material restrictions; the actual material destination. |

Follow the real card through all three layers: database, card script, then
helper. A successful summon animation does not prove that the material
restrictions or later revival behavior are correct.

## Source Trail

Read `Rush/Utilities/RDMaximum.lua`, `RDCondition.lua`, `RDFusion.lua`, and
`RDRitual.lua`, with `Rush/Scripts/c120150001.lua`, `c120150002.lua`,
`c120102001.lua`, `c120280030.lua`, and `c120280031.lua`.
