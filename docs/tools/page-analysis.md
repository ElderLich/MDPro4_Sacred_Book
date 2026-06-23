# Downloaded Tutorial Coverage

This page records how the downloaded YGOPRO Scripting Wiki tutorial pages in
`C:\Users\Shanalotte\Desktop\New folder (2)` were analyzed for Sacred Book.
They are used as a topic checklist and teaching-quality benchmark only.

Sacred Book does not copy their wording and does not use EDO/Project Ignis
documentation as factual source of truth. Final behavior is checked against
local MDPro3/YGOPro sources, local scripts, local define files, and generated
Sacred Book data.

The downloaded editor-tool page is excluded from this tutorial-equivalent pass.

This audit is section-level. It covers each downloaded scripting page's
headings, code-pattern topics, and recurring warnings, while replacing
simulator-specific helper names and examples with local MDPro3/YGOPro behavior.

## Coverage Map

| Downloaded tutorial topic | Sacred Book equivalent |
| --- | --- |
| Main scripting-wiki landing page | [Home](/), [Learning Path](/learn/), and this coverage map organize the beginner route. |
| Structure of a card script | [Structure of a card script](/learn/script-structure) covers file naming, `GetID`, `initial_effect`, callback naming, and reading real scripts. |
| Creation, building, and registration of an effect object | [Creation, building, and registration of an effect object](/learn/effect-object) covers `Effect.CreateEffect`, setters, registration, cloning, labels, label objects, and resets. |
| EFFECT_TYPE constants and templates | [EFFECT_TYPE constants and templates](/learn/effect-types) covers common type flags, no-op Spell/Trap activation, activated types, Flip Effects, quick-effect hints, combinations, material effects, and grant effects. |
| Functions for conditions, costs, activation procedures, and resolution | [Conditions, costs, activation procedures, and resolution](/learn/effect-callbacks) plus [Cost, target, and operation lifecycle](/learn/cost-target-operation-lifecycle) cover logical operators, `not` grouping, cost sections, target variants, non-activated targets, values, and resolution rechecks. |
| Activation legality | [Activation legality](/learn/activation-legality) covers `chk==0`, implicit action requirements, optional effects, mandatory effects, `chkc`, and resolution rechecks. |
| Activated effects | [Activated effects](/learn/activated-effects) covers Chain Link flow, common activated types, optional and mandatory triggers, Spell/Trap activation, and the activation/resolution split. |
| Filters, Card objects, and Group objects | [Filters, Card Objects, and Group Objects](/learn/filters-and-groups) covers filter arguments, matching vs targeting, Groups, filtering, selecting, iterating, membership, and counts. |
| List of functions that move cards across locations | [Functions that move cards across locations](/learn/moving-cards) covers movement APIs, effect-vs-cost able-to checks, destroy checks, release/discard/control helpers, targeting/non-targeting patterns, Special Summons, equip, `MoveToField`, `SendtoExtraP`, returns, and reason flags. |
| Effects that apply continuously | [Effects That Apply Continuously](/learn/continuous-effects) covers single, field, equip, Xyz Material, player-affecting, event-watching, and temporary continuous effects. |
| Tutorial for scripting a simple continuous effect | [Continuous stat modifiers](/learn/continuous-stat-modifiers) gives the focused ATK/DEF tutorial for self, field, equip, material, temporary, and cloned modifiers. |
| Equip Spell | [Equip Spells and Equip Cards](/learn/equip-spells) covers manual Equip Spell activation, `Auxiliary.AddEquipSpellEffect`, equip rules, equip limits, `EFFECT_TYPE_EQUIP`, monsters equipped by effects, activated effects on Equip Cards, previous equip targets, card targets, summon-then-equip patterns, and stepped equip. |
| Field Spell | [Field Spells](/learn/field-spells) covers Field Spell activation shape, `LOCATION_FZONE`, Field Zone replacement, activating/placing Field Spells from the Deck, environment checks, counters, and common pitfalls. |
| Recovering LP and inflicting effect damage | [LP Recovery and Effect Damage](/learn/lp-recovery-and-damage) covers fixed amounts, resolution-calculated amounts, target-player data, target-based recovery, stepped LP changes, event-value amounts, conjuncted effects, event-count vs resolution-count amounts, categories, and return values. |
| Methods for affecting cards | [Methods for Affecting Cards](/learn/affecting-cards) acts as the outcome router for immediate actions, continuous changes, negation, stat/property changes, control, equip, and review checks. |
| Subarchetype | [Archetypes and Set Codes](/learn/archetypes-and-setcodes) covers IDs, `IsSetCard`, multiple set-code checks, subarchetype bit structure, listed cards, and alternate codes. |

## Conversion Answer

The downloaded wiki/tutorial pages listed above have Sacred Book equivalents.
That does not mean they are finished forever. They are converted as original
MDPro3/YGOPro lessons, with the external page used as a coverage checklist.
Where a downloaded page used EDO-style examples or helper names, Sacred Book
should replace them with local YGOPro examples from `ygopro-scripts`, local
define files, generated API pages, and core behavior.

Future passes should keep splitting large subjects into focused lessons instead
of pouring every detail into one page. The broad navigation shape should be:

| Classification area | Sacred Book split |
| --- | --- |
| Monster Cards: Normal, Ritual, Fusion, Synchro, Xyz, Pendulum, Link, Special Summon Monsters | Keep general script foundations in [Learning Path](/learn/). [Ritual Procedure Guide](/learn/ritual-procedure) and [Fusion Procedure Guide](/learn/fusion-procedure) now cover the first two procedure families; Synchro, Xyz, Link, Pendulum, and Special Summon-only guides remain next. |
| Monster subtypes: Gemini, Toon, Union, Spirit | Add subtype guides only after the core procedure pages, because each subtype needs its own rule hooks, reset patterns, and local examples. |
| Spell Cards: Normal, Continuous, Equip, Field, Quick-Play, Ritual | [Spell Card Patterns](/learn/spell-card-patterns) now covers Normal, Continuous, Quick-Play, and Ritual Spell activation shapes; [Equip Spells and Equip Cards](/learn/equip-spells), [Field Spells](/learn/field-spells), and [Ritual Procedure Guide](/learn/ritual-procedure) are focused child pages. |
| Trap Cards: Normal, Continuous, Counter | [Trap Card Patterns](/learn/trap-card-patterns) now separates Normal Trap activation, Continuous Trap face-up effects, hand/set-turn exceptions, and Counter Trap/Spell Speed 3 patterns. |
| Effects that affect cards | Expand [Methods for Affecting Cards](/learn/affecting-cards) into focused child pages for stat changes, immunity/negation, control changes, position changes, equip relationships, and location movement. |
| Effects that affect players | Keep LP changes in [LP Recovery and Effect Damage](/learn/lp-recovery-and-damage), then add player restrictions, draw/hand/deck access restrictions, and player-targeted effects as separate pages. |

## Forever Pass Rule

Do not mark a downloaded tutorial page as fully covered until its headings,
examples, tables, warnings, edge notes, and special cases have either:

- an original Sacred Book equivalent,
- a stronger local MDPro3/YGOPro replacement example, or
- a documented reason for exclusion.

External examples that mention another simulator should be treated as lesson
prompts only. Replace them with local examples from `ygopro-scripts`, local
define files, generated API data, or verified core behavior. When a downloaded
page is too broad, split the coverage across focused Sacred Book pages rather
than hiding every detail in one long guide.

## Verification Notes

Several details were verified directly against local MDPro3/YGOPro sources:

- `Duel.Damage`, `Duel.Recover`, `Duel.RDComplete`, `Duel.Equip`, and
  `Duel.EquipComplete` are bound in `ygopro-core\libduel.cpp` and documented in
  `ygopro-scripts-define\def.lua`.
- `Duel.MoveToField` is bound in `ygopro-core\libduel.cpp`; the binding accepts
  `LOCATION_FZONE` and maps it to the Field Zone's Spell & Trap Zone slot.
- `Effect.SetType` in `ygopro-core\libeffect.cpp` normalizes
  `EFFECT_TYPE_ACTIVATE` into field activation handling and gives the effect
  the normal hand, Spell & Trap Zone, and Field Zone activation range.
- `effect::get_speed` in `ygopro-core\effect.cpp` makes Quick-Play Spell
  activations Spell Speed 2, ordinary Trap activations Spell Speed 2, and
  Counter Trap activations Spell Speed 3.
- `effect::get_required_handorset_effects` in `ygopro-core\effect.cpp` checks
  same-turn Set activation and hand-activation exceptions for Traps and
  Quick-Play Spells.
- `Duel.Damage` and `Duel.Recover` return the actual changed LP value and clamp
  negative input amounts to `0` in the local core binding.
- `Auxiliary.AddEquipSpellEffect` in local `utility.lua` creates the normal
  Equip Spell activation shape and registers `EFFECT_EQUIP_LIMIT`.
- `Auxiliary.AddRitualProcUltimate` and its wrappers in local `procedure.lua`
  create Ritual Spell activation effects, gather Ritual Materials with
  `Duel.GetRitualMaterial`, filter them through `Card.IsCanBeRitualMaterial`,
  release them with `Duel.ReleaseRitualMaterial`, Special Summon with
  `SUMMON_TYPE_RITUAL`, and call `CompleteProcedure`.
- `Auxiliary.AddFusionProc...` helpers in local `procedure.lua` register
  Fusion Monster material requirements through `EFFECT_FUSION_MATERIAL`, while
  Fusion Summon effects use `Duel.GetFusionMaterial`,
  `Card.CheckFusionMaterial`, `Duel.SelectFusionMaterial`, `Card.SetMaterial`,
  material movement with `REASON_FUSION`, `Duel.SpecialSummon` with
  `SUMMON_TYPE_FUSION`, and `CompleteProcedure`.
- `Duel.GetRitualMaterial`, `Duel.GetRitualMaterialEx`, and
  `Duel.ReleaseRitualMaterial` are bound in `ygopro-core\libduel.cpp`;
  `Card.IsCanBeRitualMaterial` is bound in `ygopro-core\libcard.cpp`.
- `Duel.GetFusionMaterial`, `Duel.SelectFusionMaterial`, and
  `Duel.SetFusionMaterial` are bound in `ygopro-core\libduel.cpp`;
  `Card.IsCanBeFusionMaterial` and `Card.CheckFusionMaterial` are bound in
  `ygopro-core\libcard.cpp`.
- Local `ygopro-core\operations.cpp` maps `SUMMON_TYPE_RITUAL` to
  `REASON_RITUAL` for material event handling.
- Local `ygopro-core\operations.cpp` maps `SUMMON_TYPE_FUSION` to
  `REASON_FUSION` for material event handling.
- `Card.IsSetCard` is bound in `ygopro-core\libcard.cpp`; set-code matching is
  implemented through the local core set-code comparison in `card_data.h`.
- Activation lifecycle quality pass checked the downloaded activation,
  activation-legality, and callback pages against local scripts:
  `c6172122.lua` for Red-Eyes Fusion activation restrictions,
  `c10443957.lua` for Damage Step negation legality, `c102380.lua` for
  inherent Special Summon callback shapes and mandatory trigger targeting, and
  `utility.lua` for the local `aux.dscon` Damage Step helper.
- Script examples were checked against local files in
  `D:\Programs\GitHub\ygopro-scripts`.

## Quality Pass Log

| Date | Downloaded page cluster | Sacred Book updates |
| --- | --- | --- |
| 2026-06-23 | Activation lifecycle: activated effects, activation legality, and condition/cost/target/operation callbacks | Expanded [Conditions, Costs, Activation Procedures, and Resolution](/learn/effect-callbacks), [Activation Legality](/learn/activation-legality), [Activated Effects](/learn/activated-effects), and [Cost, Target, And Operation Lifecycle](/learn/cost-target-operation-lifecycle) with event-condition signatures, Damage Step legality, Quick Effect negation checks, activation restrictions, Red-Eyes Fusion and Cyber Dragon Infinity examples, and API links for the referenced functions. |
| 2026-06-23 | Foundation forever pass: effect objects, filters/groups, movement, continuous effects, stat modifiers, and LP effects | Expanded [Creation, building, and registration of an effect object](/learn/effect-object), [Filters, Card Objects, and Group Objects](/learn/filters-and-groups), [Functions that move cards across locations](/learn/moving-cards), [Effects That Apply Continuously](/learn/continuous-effects), [Continuous stat modifiers](/learn/continuous-stat-modifiers), and [LP Recovery and Effect Damage](/learn/lp-recovery-and-damage) with setter-shape maps, target-range modes, property flags, subgroup selection, movement routing, local dynamic value examples, pure LP activation checks, stepped LP examples, and API links. |
| 2026-06-23 | Equip and Field Spell strict pass | Expanded [Equip Spells and Equip Cards](/learn/equip-spells) with activation-shape differences, core equip housekeeping, non-applying equip modifiers, lost-target triggers, and summon-then-equip notes. Added [Field Spells](/learn/field-spells) as a focused local-source guide because the Field Spell downloaded page is not present in the current archive folder. |
| 2026-06-23 | Spell and Trap classification expansion | Added [Spell Card Patterns](/learn/spell-card-patterns) for Normal, Continuous, Quick-Play, and Ritual Spell activation shapes, and [Trap Card Patterns](/learn/trap-card-patterns) for Normal, Continuous, and Counter Trap scripting. Local examples include Pot of Greed, Monster Reborn, Mystical Space Typhoon, Transonic Bird, Infinite Impermanence, Trap Trick, Cyberdark Invasion, and Chaos Trap Hole. |
| 2026-06-23 | Ritual procedure expansion | Added [Ritual Procedure Guide](/learn/ritual-procedure) with helper selection, `AddRitualProcUltimate` internals, target/operation flow, material subgroup checks, `SetMaterial`, `ReleaseRitualMaterial`, `SUMMON_TYPE_RITUAL`, `CompleteProcedure`, manual Sonic Tracker-style flow, Nekroz Kaleidoscope nonstandard material movement, and API links. |
| 2026-06-23 | Fusion procedure expansion | Added [Fusion Procedure Guide](/learn/fusion-procedure) with Fusion Monster material procedures, Fusion-specific material identity checks, Polymerization flow, Deck Fusion examples, Chain Material fallback, material movement operations, Contact Fusion distinction, and API links. |

## Intentional Rewrites

Some downloaded sections referenced helper APIs or simulator behavior that are
not the local MDPro3/YGOPro source of truth. Those sections were rewritten as
local equivalents instead of imported directly:

- Equip procedure material is documented through local
  `Auxiliary.AddEquipSpellEffect`, `Duel.Equip`, `EFFECT_EQUIP_LIMIT`, and equip
  target APIs instead of EDO-only helper names.
- Field Spell material was reconstructed from local scripts and core behavior
  because no downloaded `Field Spell - YGOPRO Scripting Wiki.html` file exists
  in the current archive folder.
- Movement-table entries that used non-local function names were translated to
  local APIs such as `Duel.GetControl` and `Duel.SendtoExtraP`.
- Examples sourced from external repositories were replaced with local-script
  style snippets and local behavior notes.

## Ongoing Standard

Future learning pages should continue this style:

- Use downloaded pages only to notice topics and teaching gaps.
- Rewrite explanations in Sacred Book's own words.
- Prefer local script-backed examples over invented snippets.
- Mark inferred behavior clearly when the local core does not prove it.
- Keep API signatures and generated function docs as the exact reference layer.
