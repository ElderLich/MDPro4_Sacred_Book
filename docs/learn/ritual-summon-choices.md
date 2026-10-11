# Ritual Summon Choices

**Before this lesson:** read [Ritual Procedures](ritual-procedure).
**Goal:** understand monster selection, legal material groups, backing out to
choose again, and optional effects around a Ritual Summon.

These are the standard helpers in `Utilities/procedure.lua`. The
[Rush Ritual helper](rush-summon-procedures#ritual-match-the-rush-data-convention)
has a different interface and data convention.

## Start With A Complete, Small Spell

This tutorial Ritual Spell summons one Ritual Monster from the hand
using materials whose Ritual Levels exactly equal that monster's original
Level. Create a matching database entry with `TYPE_SPELL+TYPE_RITUAL` and a
script with that card's ID.

```lua
local s,id=GetID()

function s.initial_effect(c)
    aux.AddRitualProcEqual(c)
end
```

The omitted filter allows any Ritual Monster that
[`aux.AddRitualProcEqual`](/api/functions/Auxiliary/AddRitualProcEqual) finds legal.
It does not bypass that monster's summon or material restrictions. For a
named family, pass a filter: [Super Soldier Ritual
(`14094090`)](/examples/cards/14094090) uses
`aux.AddRitualProcEqual(c,c14094090.ritual_filter)` and restricts the candidate
Ritual Monsters to set `0x10cf`.

Test the tutorial with two Ritual Monsters in hand. Only monsters for which a
legal material set and summon destination exist should be offered. Choosing
one of them then determines the material-selection rules.

## Follow The Choice Loop

[`RitualUltimateTarget`](/api/functions/Auxiliary/RitualUltimateTarget) checks whether a summon exists at activation. It does
not commit a particular Ritual Monster or material set. At resolution,
[`RitualUltimateOperation`](/api/functions/Auxiliary/RitualUltimateOperation) follows this loop:

1. Rebuild the material pool and the eligible Ritual Monster choices.
2. Ask the player to choose one Ritual Monster.
3. Filter the materials for that exact monster, excluding the monster itself.
4. Ask the player to choose a valid material subgroup.
5. If that selection returns `nil`, go back to step 1.
6. Otherwise, record and move the materials, then summon the chosen monster.

The actual material-selection block is:

```lua
-- Bounded excerpt from RitualUltimateOperation:
-- mg is filtered for tc; lv is the selected monster's requirement.
Auxiliary.GCheckAdditional=Auxiliary.RitualCheckAdditional(tc,lv,greater_or_equal)
mat=mg:SelectSubGroup(tp,Auxiliary.RitualCheck,true,1,lv,tp,tc,lv,greater_or_equal)
Auxiliary.GCheckAdditional=nil
```

The next statement in the source is
`if not mat then goto RitualUltimateSelectStart end`. That label is **before**
the material-pool and monster-selection steps. The helper clears the temporary
group hook before going back.

::: tip Back means “choose again”
The `true` argument enables cancellation of this material selection. The
surrounding code decides what cancellation means. Here it returns to monster
choice without paying or releasing anything. Changing the `goto` to `return`
would let the player abandon the resolving Ritual effect instead.
:::

Compare [Sonic Tracker (`17888577`)](/examples/cards/17888577): its manual
operation uses the same backtracking pattern, then stores the selected
materials' total Level before releasing them. This is why a manual procedure
must preserve more than just the final `SpecialSummon` call.

## A Legal Material Set Is More Than A Total

[`aux.RitualCheck`](/api/functions/Auxiliary/RitualCheck) checks the destination's space **after the chosen materials
leave**, the required total, the Ritual Monster's `mat_group_check`, and any
active `aux.RCheckAdditional` hook. A full field is not automatically illegal
if releasing a selected monster makes room.

The helper also filters ordinary materials with
`Card.IsCanBeRitualMaterial(candidate,chosenMonster)` and applies the chosen
monster's `mat_filter` when it has one. A candidate may be valid for Ritual
Monster A and invalid for Ritual Monster B.

With ordinary Level values and no other restrictions, the distinction between
the two common modes looks like this:

| Requirement | Selected material Levels | Total check |
| --- | --- | --- |
| Exactly 8 | 4 + 4 | Can satisfy the exact total. |
| Exactly 8 | 4 + 5 | Cannot satisfy the exact total. |
| 8 or more | 4 + 5 | Can satisfy the required total. |
| 8 or more | 8 + 1 | The extra material is unnecessary; preserve the helper's material-selection restrictions. |

Do not replace the material predicate with `g:GetSum(Card.GetLevel)>=lv`.
Materials use `Card.GetRitualLevel(material,ritualMonster)`, which can encode
alternative values. Zone availability and card-specific restrictions also
remain part of the answer.

The ordinary helper compares against the Ritual Monster's **original** Level;
the `2` variants use its **current** Level. That choice changes the required
total, not the fact that materials use `GetRitualLevel`.

## Three Independent Filters

Here is the first-effect registration from [Revendread Origin
(`94666032`)](/examples/cards/94666032), renamed to `s` and bounded to its Ritual
effect. Its separate GY protection effect is omitted.

```lua
local s,id=GetID()

function s.initial_effect(c)
    aux.AddCodeList(c,4388680)
    aux.AddRitualProcGreater2(c,s.ritualFilter,
        LOCATION_HAND+LOCATION_GRAVE,s.graveMaterialFilter)
end

function s.ritualFilter(c)
    return c:IsSetCard(0x106)
end

function s.graveMaterialFilter(c)
    return c:IsRace(RACE_ZOMBIE)
end
```

Read the arguments separately:

| Argument | Question |
| --- | --- |
| `s.ritualFilter` | Which Ritual Monsters may be summoned? |
| `LOCATION_HAND+LOCATION_GRAVE` | Where may the Ritual Monster be selected from? |
| `s.graveMaterialFilter` | Which extra GY monsters may be considered as materials? |
| The next optional `mat_filter` argument | How should the ordinary material pool be restricted? |

Allowing the Ritual Monster to come from the GY does not automatically allow
GY materials. Supplying GY material does not automatically allow the Ritual
Monster to be summoned from the GY. The helper's extra-GY path checks Level,
Monster type, and ability to banish; `ReleaseRitualMaterial` handles that
material route. Do not replace it with ordinary `Duel.Release`.

For an unusual source of the **summoned monster**, [Stars Align Above the Shrine
(`15306543`)](/examples/cards/15306543) uses `LOCATION_DECK` in paired
`RitualUltimateTarget`/`RitualUltimateOperation` factories, with a separate
field-material filter. Its other effects and restrictions still matter.

For unusual **material**, [Nekroz Kaleidoscope
(`51124303`)](/examples/cards/51124303) can select an Extra Deck monster and
send it to the GY rather than release it. It can also summon a Group of Ritual
Monsters. That manual procedure is not reproduced by changing only
`summon_location` on a one-monster helper.

## Choosing A Mode At Activation

[Mitsurugi Magatama (`76725398`)](/examples/cards/76725398) lets the player choose
between a destruction route and a Ritual route. Its target callback calculates
whether each route is currently legal, then presents only the available modes.

This is the bounded option-selection fragment, after `b1` and `b2` have been
computed from the card's complete legality checks:

```lua
local op=aux.SelectFromOptions(tp,
    {b1,aux.Stringid(id,1),1},
    {b2,aux.Stringid(id,2),2}
)
```

[`aux.SelectFromOptions`](/api/functions/Auxiliary/SelectFromOptions) uses the
final entry in each option as its stable returned value. If only the
Ritual choice remains, its result is still `2`; it does not become mode `1`
because it is the first visible row. The real script stores the chosen mode
in `e:SetLabel`, adjusts categories and targeting properties for that route,
and resolves the matching branch later.

The Ritual branch invokes the helper **factory**, then its returned callback:

```lua
-- Bounded excerpt inside the selected Ritual resolution branch:
aux.RitualUltimateOperation(s.ritual_filter,Card.GetLevel,"Greater",
    LOCATION_HAND,nil,s.mfilter)(e,tp,eg,ep,ev,re,r,rp)
```

Do not choose a different mode at resolution just because its materials now
look better. Recheck the chosen mode's resources instead. The selected mode
is a decision made at activation; its Ritual Monster and materials are later
decisions made by that branch.

## Optional Follow-Up Work And Callback Limits

[Recette de Viande (`14166715`)](/examples/cards/14166715) supplies an
`extra_operation` callback to offer its position-changing follow-up. Its first
guard is `if not tc or not tc:IsCode(53618197) then return end`, and it checks
for applicable opposing monsters before asking `SelectYesNo`.

In the local helper, `extra_operation` runs after the main operation block
**even if no Ritual Monster was selected**. Treat `tc` and `mat` as possibly
missing. The callback being invoked is not a Boolean success report from
`Duel.SpecialSummon`; if bespoke behavior needs that exact result, preserve
the summon-result check in a suitable manual operation.

Two related settings are easy to misread:

- `pause=true` delays **registration of the effect** so the script can adjust
  it, as [Mitsurugi Mirror (`49721684`)](/examples/cards/49721684) does before
  adding a count limit. It does not pause gameplay or enable cancellation.
- `extra_target` runs after the helper's `chk==0` branch has already returned.
  Use it for activation-time announcements or bookkeeping. It cannot add a
  missing activation-legality test to that branch.

## Recheck At Resolution

The helper recollects both ordinary and extra GY materials on each pass through
the choice loop. If the intended monster or its resources disappear before
resolution, the current candidate search decides what remains legal. Avoid
storing an activation-time material Group and treating it as a confirmed
selection.

For manual extensions, keep target and operation filters consistent, clean up
temporary `aux.GCheckAdditional` hooks on every path, and move materials only
after the player confirms a legal set. Read the chosen materials' values before
moving them if the later effect needs their former state.

## Practice And Review

| Test state | Expected behavior to verify |
| --- | --- |
| Two Ritual Monsters are legal | Choose either; material legality follows that chosen monster. |
| Cancel material selection | Return to monster choice without releasing cards. |
| Full field with a legal field material | The checker can account for the zone freed by that material. |
| Only a GY Ritual Monster is allowed | `summon_location` enables it; this alone grants no GY material access. |
| A material is removed before resolution | The old material pool is discarded and legality is rebuilt. |
| Only option 2 is legal | Its stable returned value remains `2`. |
| Follow-up is optional or has no candidate | Declining it or lacking candidates does not undo the Ritual Summon. |
| No Ritual Monster survives the resolution check | The follow-up callback handles missing `tc` without an error. |

Continue with [Fusion Summon Choices](fusion-summon-choices) to compare this
backtracking flow with separate normal/Chain Material routes.

## Source Trail

- `Utilities/procedure.lua`: `RitualUltimateTarget`, `RitualUltimateFilter`,
  `RitualUltimateOperation`, `RitualCheck`, `RitualCheckAdditional`.
- `Utilities/utility.lua`: `SelectFromOptions`.
- `Scripts/c17888577.lua`: manual backtracking and material-value capture.
- `Scripts/c94666032.lua`, `c15306543.lua`, `c51124303.lua`: distinct monster
  sources, GY material, and Extra Deck material.
- `Scripts/c76725398.lua`, `c14166715.lua`, `c49721684.lua`: mode choice,
  optional follow-up, and deferred registration.
