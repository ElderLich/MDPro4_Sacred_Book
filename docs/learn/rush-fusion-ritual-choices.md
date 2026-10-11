# Rush Fusion And Ritual: Let The Player Choose

**Prerequisites:** [Rush summon procedures](rush-summon-procedures) and
[selection and actions](rush-selection-and-actions). **Goal:** build a summon
effect that checks legality without prompting, then lets the player choose a
legal monster and its materials during resolution.

The Rush library already implements those choices. Start with
`RD.CreateFusionEffect` or `RD.CreateRitualEffect`, supply filters matching the
card text, and configure/register the returned Effect. A material procedure on
the monster and the effect that performs its summon are separate pieces.

## A Complete Fusion Spell

`Rush/Scripts/c120196050.lua` is a small complete example. Its material filter
requires face-up materials on the field:

```lua
local cm,m=GetID()
cm.name="融合术"
function cm.initial_effect(c)
	--Activate
	local e1=RD.CreateFusionEffect(c,cm.matfilter)
	e1:SetCategory(CATEGORY_SPECIAL_SUMMON+CATEGORY_FUSION_SUMMON)
	e1:SetType(EFFECT_TYPE_ACTIVATE)
	e1:SetCode(EVENT_FREE_CHAIN)
	c:RegisterEffect(e1)
end
--Activate
function cm.matfilter(c)
	return c:IsFaceup() and c:IsOnField()
end
```

The constructor installs target and operation callbacks; it does not register
the Spell activation itself. The card still sets its category, type, timing
code and registration. `cm` is the card's script table; its name could equally
be `s`.

`cm.matfilter` tests an individual potential material. The chosen Fusion
Monster's own procedure still checks its required names, material count and
other restrictions. The filter does not replace that procedure.

Compare `c120238025.lua`, which calls `RD.CreateFusionEffect(c)` without a
material filter. Omitting the face-up/on-field restriction is a behavior
change, not just a shorter way to write the same card.

## What The Player Sees, And When

| Stage | What the constructor's callbacks do | Player choice |
| --- | --- | --- |
| Target callback, `chk==0` | Check for a legal candidate, material Group and destination zone. | No monster or material selection. |
| Target callback, actual activation | Publish operation information and run any `target_action`. | Only an additional choice explicitly supplied by the card. |
| Operation | Rebuild candidate/material pools using the current state. | Select the monster to summon. |
| Operation, multiple supported routes | Find the routes that can summon that selected monster. | Choose a material-source route when more than one exists. |
| Operation | Select materials satisfying the chosen monster and route. | Select the material Group. |
| Operation | Record materials, move them, and attempt the summon. | Follow any additional card-specific operation. |

You do not need to choose the summon candidate with `Duel.SelectMatchingCard`
inside `chk==0`. Doing so would introduce a prompt during a legality check.
The generated callbacks already make the monster and material choices at the
appropriate stage.

## Three Filters That Answer Different Questions

The first part of the Fusion constructor is:

```lua
RD.CreateFusionEffect(card, matfilter, spfilter, exfilter,
    self_extra_locations, opponent_extra_locations, mat_check, mat_move, ...)
```

| Input | Question it answers |
| --- | --- |
| `matfilter` | Which individual cards from the ordinary material pool are eligible? |
| `spfilter` | Which Extra Deck monsters may this effect summon? |
| `exfilter` plus location masks | Which additional cards can enter the material pool? |
| `mat_check` | Does the selected Group satisfy an extra combined restriction? |
| `mat_move` | Where do the selected materials go? |

The location masks add extra material locations. Zero does not remove the
ordinary material pool. Conversely, adding `LOCATION_GRAVE` without the
appropriate extra-material filter and movement rules does not fully implement
“use monsters from your GY”.

### A Real Combined Restriction

`c120238024.lua` uses this constructor call:

```lua
local e1=RD.CreateFusionEffect(c,cm.matfilter,nil,cm.exfilter,
    LOCATION_GRAVE,0,cm.matcheck,RD.FusionToDeck,nil,nil,cm.limit)
```

Its ordinary-material filter requires a face-up Normal Dragon on the field
that can return to the Deck. Its extra-material filter admits suitable Dragons
from the GY. The Group-level condition is:

```lua
function cm.matcheck(tp,sg,fc)
    return sg:FilterCount(Card.IsOnField,nil)==1
end
```

Exactly one selected material must be on the field. This cannot be expressed
by simply requiring every individual material to be on the field. The helper
also checks the Fusion Monster's own material procedure and usable zone after
the materials leave. `RD.FusionToDeck` supplies the matching material movement.

The complete card additionally has an activation condition and an attack
restriction in `cm.limit`. Copying the constructor call alone would omit those
parts of its text. Read the complete card in the
[Rush Script Explorer](/tools/script-explorer?format=rush&mode=cards&q=120238024).

## A Complete Ritual Spell With Two Candidate Names

`Rush/Scripts/c120280031.lua` permits either of two named Ritual Monsters, with
face-up field materials:

```lua
local cm,m=GetID()
local list={120280002,120280003}
cm.name="仪式法之门"
function cm.initial_effect(c)
	RD.AddCodeList(c,list)
	--Activate
	local e1=RD.CreateRitualEffect(c,RITUAL_ORIGINAL_LEVEL_GREATER,cm.matfilter,cm.spfilter)
	e1:SetCategory(CATEGORY_SPECIAL_SUMMON)
	e1:SetType(EFFECT_TYPE_ACTIVATE)
	e1:SetCode(EVENT_FREE_CHAIN)
	c:RegisterEffect(e1)
end
--Activate
function cm.matfilter(c)
	return c:IsFaceup() and c:IsOnField()
end
function cm.spfilter(c)
	return c:IsCode(list[1],list[2])
end
```

If both named monsters exist in the Extra Deck and each has a valid material
solution, the player can choose either. If only one has valid materials, the
candidate Group contains only that one. You do not need a separate option menu
containing the two names.

The constructor's `type` argument controls how the required total is derived
and compared. The other filters and callbacks have the same broad roles as
Fusion's, but they run the Rush Ritual material checker.

### Exact Totals And At-Least Totals

| Mode family | Requirement taken from the Ritual Monster | Material values used by the checker |
| --- | --- | --- |
| `RITUAL_ORIGINAL_LEVEL_*` | Original Level | `Card.GetRitualLevel(material, ritual_monster)` |
| `RITUAL_CURRENT_LEVEL_*` | Current Level | `Card.GetRitualLevel(material, ritual_monster)` |
| `RITUAL_ORIGINAL_ATTACK_*` | Base ATK | Current material ATK in the final Group sum check |
| `RITUAL_CURRENT_ATTACK_*` | Current ATK | Current material ATK in the final Group sum check |

`*_EQUAL` requires an exact sum; `*_GREATER` uses the core's at-least sum check
and the helper's no-unnecessary-material constraints. The name “original”
describes which value of the Ritual Monster sets the requirement. It does not
mean “read every material's printed stat”.

For a real exact-Level example, `c120287036.lua` uses
`RITUAL_ORIGINAL_LEVEL_EQUAL`, a Fiend material filter and two permitted monster
names. Its post-operation callback also checks whether a material was
previously in Maximum mode. Material identity and history can matter after
the total has been satisfied.

## Cancellation Returns To An Earlier Choice

In the standard constructor flow, monster selection is not offered as an
optional yes/no action. A failed or canceled Fusion material selection returns
to monster selection; Ritual material selection similarly returns `nil` on
cancellation and the executor returns to its monster-selection step.

The lower-level executors have an optional `cancelable` flag for the monster
choice. With that flag enabled, canceling the monster choice returns `nil` to
the caller. This is a different boundary from canceling the material Group.
Do not delete the helper's retry loop or reinterpret every cancellation as a
success with zero materials.

## Alternative Materials And Alternative Routes

These are two different features supported by the pinned library:

- **Alternatives for one Fusion material slot:** `RD.AddFusionProcedure` can
  accept a table containing card codes or predicates for one slot. The slot
  matches any listed alternative. A table does not mean “use every listed
  card”; separate arguments create separate slots.
- **Another material-source route:** Fusion checks `EFFECT_CHAIN_MATERIAL`;
  Ritual checks its custom `EFFECT_RITUAL_MATERIAL`. A supporting effect can
  provide a different material pool and movement operation. If multiple routes
  support the chosen monster, the executor asks which route to use.

For example, `c120300052.lua` supplies a Ritual material route for a particular
Ritual Spell. It can add suitable Galaxy monsters from the GY, then uses
`RD.RitualToDeck` as that route's movement operation. It is not permission for
every Ritual Spell to use any GY monster.

An illustrative Fusion slot declaration is:

```lua
-- Hypothetical material requirement: (code_a OR code_b) + code_c.
RD.AddFusionProcedure(c,false,false,{code_a,code_b},code_c)
```

Here the two explicit Booleans avoid the helper's overloaded-argument shifting.
Choose substitute and alternate-summon permissions from the actual monster's
text; this fragment illustrates slot structure rather than declaring a real
card's ruling.

## Callback Arguments And Return Values

The constructors return an **Effect**, not a summoned monster. Their extra
operation callback receives the usual eight effect arguments followed by
`materials, summon_card`:

```lua
function s.after_summon(e,tp,eg,ep,ev,re,r,rp,materials,summon_card)
    -- Inspect the selected materials or apply this card's follow-up.
end
```

The internal `ExecuteFusionSummon` and `ExecuteRitualSummon` functions return
`summon_card, materials` in the opposite order. In this snapshot they call
`Duel.SpecialSummon` but do not return or test its numeric count. Receiving a
Card from those executors is not a verified positive summon result. A custom
follow-up must check the state it requires rather than assuming every returned
Card is now successfully on the field.

`operation_action` runs after an executor returns for a viable route.
`limit_action` runs after cleanup even when no viable candidate remains during
resolution. Put unconditional resolution restrictions and success-dependent
follow-ups in the appropriate callback. Avoid saving a temporary material
Group for a later event without following the engine's Group lifetime rules.

::: warning Pinned direct Ritual-wrapper limitation
`RD.RitualSummon` and `RD.CanRitualSummon` read `card.ritual_mat_filter`, but
their parameter/local lists do not define `card`. They have no direct callsites
in the imported card corpus and normally error at that access. Use the
`RD.CreateRitualEffect` pattern above; do not introduce a global `card` variable
as a workaround. The vendored upstream code is preserved unchanged.
:::

## Verify The Choice Flow

Test one candidate, two candidates with different material requirements, no
legal material solution, a full field that materials would free, cancellation
at each supported selection stage, and a changed-state resolution that no
longer has a viable candidate. For extra material routes, test the source
restriction and the correct material destination separately.

Continue with [Special Summons and result types](rush-special-summon-results).
Source contracts: [CreateFusionEffect](/rush/api/functions/RushDuel/CreateFusionEffect),
[CreateRitualEffect](/rush/api/functions/RushDuel/CreateRitualEffect),
[ExecuteFusionSummon](/rush/api/functions/RushDuel/ExecuteFusionSummon), and
[ExecuteRitualSummon](/rush/api/functions/RushDuel/ExecuteRitualSummon).
