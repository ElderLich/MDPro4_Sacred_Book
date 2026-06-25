# Source Coverage Notes

This page records how outside topic outlines were converted into original
Sacred Book lessons. They are used as a topic checklist and teaching-quality
benchmark only.

Sacred Book does not copy outside wording and does not use outside simulator
documentation as factual source of truth. Final behavior is checked against
local MDPro3/YGOPro sources, local scripts, local define files, and generated
Sacred Book data.

Editor-tool material is tracked separately as the bridge between card database
setup and Lua scripting.

This audit is section-level. It covers each source topic's headings,
code-pattern topics, and recurring warnings, while replacing non-local helper
names and examples with local MDPro3/YGOPro behavior.

## Coverage Map

| Source topic | Sacred Book equivalent |
| --- | --- |
| Main scripting reference landing page | [Home](/), [Learning Path](/learn/), [First Scripts To Study](/learn/first-scripts), [Beginner Script Ladder](/learn/beginner-script-ladder), and this coverage map organize the beginner route. |
| Structure of a card script | [Structure of a card script](/learn/script-structure) covers file naming, `GetID`, `initial_effect`, callback naming, and reading real scripts. |
| Creation, building, and registration of an effect object | [Creation, building, and registration of an effect object](/learn/effect-object) covers `Effect.CreateEffect`, setters, registration, cloning, labels, label objects, and resets. |
| EFFECT_TYPE constants and templates | [EFFECT_TYPE constants and templates](/learn/effect-types) covers common type flags, type-shape selection, no-op Spell/Trap activation, activated types, trigger source combinations, quick-effect hints, material effects, grant effects, and special target-range modes. |
| Functions for conditions, costs, activation procedures, and resolution | [Conditions, costs, activation procedures, and resolution](/learn/effect-callbacks) plus [Cost, target, and operation lifecycle](/learn/cost-target-operation-lifecycle) cover logical operators, `not` grouping, cost sections, target variants, non-activated targets, values, and resolution rechecks. |
| Activation legality | [Activation legality](/learn/activation-legality) covers `chk==0`, implicit action requirements, optional effects, mandatory effects, `chkc`, and resolution rechecks. |
| Common script errors and debugging | [Common Script Errors And Debugging](/learn/common-script-errors-and-debugging) collects frequent local-script mistakes: nil values, `chk==0`, cost/target/operation desync, targeting versus selecting, relation checks, location masks, `IsFaceupEx`, count limits, resets, continuous ranges, negation types, Group lifetime, and code identity checks. |
| Chain timing and activation windows | [Chain Timing And Activation Windows](/learn/chain-timing-and-activation-windows) covers prompt masks, `EVENT_FREE_CHAIN`, `EVENT_CHAINING`, Spell Speed, Damage Step flags, `Duel.CheckTiming`, and Chain-solving watcher effects. |
| Activated effects | [Activated effects](/learn/activated-effects) covers Chain Link flow, common activated types, optional and mandatory triggers, Spell/Trap activation, and the activation/resolution split. |
| Filters, Card objects, and Group objects | [Filters, Card Objects, and Group Objects](/learn/filters-and-groups) covers filter arguments, matching vs targeting, Groups, filtering, selecting, iterating, membership, and counts. |
| Min/Max-stat card selection | [Min/Max Stat Card Selection](/learn/min-max-stat-selection) covers `Group.GetMinGroup`, `Group.GetMaxGroup`, tied groups, returned numeric values, custom scoring functions, and activation-vs-resolution selection. |
| List of functions that move cards across locations | [Functions that move cards across locations](/learn/moving-cards) covers movement APIs, effect-vs-cost able-to checks, operation-info categories, destroy checks, release/discard/control helpers, targeting/non-targeting patterns, Special Summons, equip, `MoveToField`, `SendtoExtraP`, returns, reason flags, and the local replacement for non-local `Duel.RemoveCards`. |
| Effects that apply continuously | [Effects That Apply Continuously](/learn/continuous-effects) covers single, field, equip, Xyz Material, player-affecting, event-watching, and temporary continuous effects. |
| Tutorial for scripting a simple continuous effect | [Continuous stat modifiers](/learn/continuous-stat-modifiers) gives the focused ATK/DEF tutorial for self, field, equip, material, temporary, and cloned modifiers. |
| Equip Spell | [Equip Spells and Equip Cards](/learn/equip-spells) covers manual Equip Spell activation, the local `Auxiliary.AddEquipSpellEffect` helper, equip rules, equip limits, `EFFECT_TYPE_EQUIP`, monsters equipped by effects, activated effects on Equip Cards, previous equip targets, card targets, summon-then-equip patterns, existing-card equip prechecks, and stepped equip. |
| Field Spell | [Field Spells](/learn/field-spells) covers Field Spell activation shape, `LOCATION_FZONE`, Field Zone replacement, activating/placing Field Spells from the Deck, environment checks, counters, and common pitfalls. |
| Recovering LP and inflicting effect damage | [LP Recovery and Effect Damage](/learn/lp-recovery-and-damage) covers fixed amounts, resolution-calculated amounts, target-player data, target-based recovery, stepped LP changes, event-value amounts, event-count vs resolution-count amounts, `BreakEffect` sequencing, categories, operation info, and return values. |
| Methods for affecting cards | [Methods for Affecting Cards](/learn/affecting-cards) acts as the outcome router for immediate actions, continuous changes, negation, stat/property changes, control, equip, and review checks. |
| Subarchetype | [Archetypes and Set Codes](/learn/archetypes-and-setcodes) covers IDs, `IsSetCard`, multiple set-code checks, subarchetype bit structure, listed-card and listed-set helpers, original-code checks, and common filter patterns. |
| DataEditorX | [Card Data and Script Wiring](/learn/card-data-and-script-wiring) covers `cards.cdb` `datas`/`texts` fields, ID-to-script matching, card text versus script strings, type bits, category labels, set codes, alias, and prompt-string API links. |

## Conversion Answer

The source topics listed above have Sacred Book equivalents.
That does not mean they are finished forever. They are converted as original
MDPro3/YGOPro lessons, with outside material used only as a coverage checklist.
Where outside material uses non-local examples or helper names, Sacred Book
should replace them with local YGOPro examples from `ygopro-scripts`, local
define files, generated API pages, and core behavior.

Future passes should keep splitting large subjects into focused lessons instead
of pouring every detail into one page. The broad navigation shape should be:

| Classification area | Sacred Book split |
| --- | --- |
| Monster Cards: Normal, Ritual, Fusion, Synchro, Xyz, Pendulum, Link, Special Summon Monsters | Keep general script foundations in [Learning Path](/learn/). [Ritual Procedure Guide](/learn/ritual-procedure), [Fusion Procedure Guide](/learn/fusion-procedure), [Synchro Procedure Guide](/learn/synchro-procedure), [Xyz Procedure Guide](/learn/xyz-procedure), [Link Procedure Guide](/learn/link-procedure), [Pendulum Procedure Guide](/learn/pendulum-procedure), [Special Summon-only Monster Guide](/learn/special-summon-only-monsters), and [Tribute Summon Materials](/learn/tribute-summon-materials) now cover the main procedure families and Tribute-material variants. |
| Monster subtypes: Gemini, Toon, Union, Spirit | [Gemini Monsters](/learn/gemini-monsters), [Toon Monsters](/learn/toon-monsters), [Union Monsters](/learn/union-monsters), and [Spirit Monsters](/learn/spirit-monsters) now split these subtype topics into focused guides with local constants, helper patterns, reset behavior, and local examples. |
| Spell Cards: Normal, Continuous, Equip, Field, Quick-Play, Ritual | [Spell Card Patterns](/learn/spell-card-patterns) now covers Normal, Continuous, Quick-Play, and Ritual Spell activation shapes; [Quick-Play Spells](/learn/quick-play-spells), [Equip Spells and Equip Cards](/learn/equip-spells), [Field Spells](/learn/field-spells), and [Ritual Procedure Guide](/learn/ritual-procedure) are focused child pages. |
| Trap Cards: Normal, Continuous, Counter | [Trap Card Patterns](/learn/trap-card-patterns) now separates Normal Trap activation, Continuous Trap face-up effects, hand/set-turn exceptions, and Counter Trap/Spell Speed 3 patterns. [Normal And Continuous Traps](/learn/normal-and-continuous-traps) and [Counter Traps](/learn/counter-traps) provide the focused follow-up guides. |
| Effects that affect cards | [Methods for Affecting Cards](/learn/affecting-cards) now routes to focused child pages: [Functions that move cards across locations](/learn/moving-cards), [Continuous stat modifiers](/learn/continuous-stat-modifiers), [Equip Spells and Equip Cards](/learn/equip-spells), [Counters](/learn/counters), [Negation and Immunity](/learn/negation-and-immunity), [Control Change](/learn/control-change), and [Battle Position Effects](/learn/battle-position-effects). |
| Effects that affect players | [LP Recovery and Effect Damage](/learn/lp-recovery-and-damage), [Player-Targeted Effects](/learn/player-targeted-effects), [Player Restrictions](/learn/player-restrictions), and [Draw, Hand, And Deck Effects](/learn/draw-hand-and-deck-effects) now split player-target data, LP changes, player locks, and draw/hand/Deck patterns into focused pages. |
| Effect metadata, categories, properties, hint timing, and client prompts | [Categories, Properties, And Hint Timing](/learn/categories-properties-and-hints) now splits category labels, operation info, targeting flags, Damage Step flags, single-range flags, oath/cannot-disable flags, prompt timing, and `HINTMSG_*` selection hints into a focused learner page. [Client UI And Prompt Behavior](/learn/client-ui-and-prompt-behavior) expands the prompt layer with `Duel.Hint`, `SetHintTiming`, `SetOperationInfo`, opponent notices, target prompts, resolution choices, and invisible/awkward effect troubleshooting. |
| Chain timing, prompt windows, and response legality | [Chain Timing And Activation Windows](/learn/chain-timing-and-activation-windows) now separates hint timing from legality, explains `EVENT_FREE_CHAIN` versus `EVENT_CHAINING`, records local Spell Speed behavior, and shows Damage Step response patterns. |
| Spell and Trap timing specializations | [Quick-Play Spells](/learn/quick-play-spells), [Normal And Continuous Traps](/learn/normal-and-continuous-traps), and [Counter Traps](/learn/counter-traps) now split the broad Spell/Trap classification into practical timing, targeting, exception, negation, reset, and leave-field workflows. |
| Selection helpers and Group/Card handling | [Filters, Card Objects, and Group Objects](/learn/filters-and-groups) covers the basic filter and Group model; [Selection And Group Handling](/learn/selection-and-group-handling) now covers official targets, resolution choices, selecting from existing Groups, subgroup checks, `SelectUnselect`, Group lifetime, iteration, and rechecks before acting. |
| Reset flags, temporary effects, and duration | [Reset Flags And Effect Duration](/learn/reset-flags-and-duration) now centralizes `Effect.SetReset`, phase resets, event resets, `RESETS_STANDARD`, reset counts, player restrictions, card-bound temporary effects, flag lifetimes, and manual reset APIs. |
| Debugging and common mistakes | [Common Script Errors And Debugging](/learn/common-script-errors-and-debugging) now gives a focused troubleshooting pass that links existing lessons together without turning them into one large appendix. |

## 2026-06-24 Source Re-Audit

The archive was re-read as a curriculum and teaching-quality pass, not only a
topic checklist. The main lesson from the source topics is that beginners
need a visible curve before the full reference library: read a script, study a
few complete effects, then branch into targeting, Groups, card types, and
outcomes.

Sacred Book now routes that curve through [Home](/), [Learning Path](/learn/),
[First Scripts To Study](/learn/first-scripts), and
[Beginner Script Ladder](/learn/beginner-script-ladder). The first-scripts page
uses local scripts for Pot of Greed (`c55144522.lua`), Mystical Space Typhoon
(`c5318639.lua`), Book of Moon (`c14087893.lua`), Banner of Courage
(`c10012614.lua`), and Fissure (`c97169186.lua`). The ladder page extends that
into complete small script shapes.

| Source signal | Sacred Book action |
| --- | --- |
| Main page emphasizes a start route before topic browsing. | Home and Learn now expose a shorter beginner curve and route into [Beginner Script Ladder](/learn/beginner-script-ladder) before the full lesson library. |
| Single-filter targeting spends time on `chkc`, target counts, operation info, and resolution wording. | [Targeting flow](/learn/targeting-flow) now expands `chkc`, local target-redirection examples, `min,max`, and relation/current-state rechecks. |
| Single-filter selection separates matching-card selection from official targets. | [First Scripts To Study](/learn/first-scripts) and [Selection And Group Handling](/learn/selection-and-group-handling) reinforce targeting versus resolution selection with local scripts. |
| Min/Max-stat card selection uses tied min/max groups. | [Min/Max Stat Card Selection](/learn/min-max-stat-selection) now documents `Group.GetMinGroup`, `Group.GetMaxGroup`, tie handling, returned values, custom scoring functions, and targeting variants with local scripts. |
| Equip Spell material includes non-local helper names. | [Equip Spells and Equip Cards](/learn/equip-spells) now names the local `Auxiliary.AddEquipSpellEffect` route and points to local scripts for normal, summon-then-equip, existing-card equip, previous-target, and stepped equip flows. |
| Movement page includes non-local movement names. | [Functions that move cards across locations](/learn/moving-cards) uses local `Duel.GetControl`, `Duel.Remove`, `Duel.SendtoExtraP`, and related local APIs, and explicitly excludes non-local `Duel.RemoveCards`. |

Non-local function names that were intentionally not copied as local facts:

| Non-local name | Local Sacred Book handling |
| --- | --- |
| `Duel.GetTargetCards` | Use `Duel.GetTargetsRelateToChain()` or `Duel.GetChainInfo(0,CHAININFO_TARGET_CARDS):Filter(Card.IsRelateToEffect,nil,e)`. |
| `Duel.Control` | Use local [`Duel.GetControl`](/api/functions/Duel/GetControl). |
| `Duel.Exile`, `Duel.RemoveCards` | Use local [`Duel.Remove`](/api/functions/Duel/Remove). |
| `aux.AddEquipProcedure` and related `aux.Equip*` helpers | Use local [`Auxiliary.AddEquipSpellEffect`](/api/functions/Auxiliary/AddEquipSpellEffect), [`Duel.Equip`](/api/functions/Duel/Equip), and `EFFECT_EQUIP_LIMIT` patterns. |
| Shorthand selection names such as `Duel.Select` | Use local `Duel.SelectMatchingCard`, `Duel.SelectTarget`, `Group.Select`, or `Group.FilterSelect` depending on the state being created. |

## Forever Pass Rule

Do not mark a source topic as fully covered until its headings,
examples, tables, warnings, edge notes, and special cases have either:

- an original Sacred Book equivalent,
- a stronger local MDPro3/YGOPro replacement example, or
- a documented reason for exclusion.

Outside examples should be treated as lesson prompts only. Replace them with
local examples from `ygopro-scripts`, local define files, generated API data,
or verified core behavior. When a source topic is too broad, split the coverage
across focused Sacred Book pages rather
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
- Quick-Play Spell, Counter Trap, and Normal/Continuous Trap behavior was
  checked against local scripts and generated API pages. Examples include
  Mystical Space Typhoon (`c5318639.lua`), Book of Moon (`c14087893.lua`),
  Solemn Judgment (`c41420027.lua`), Solemn Strike (`c40605147.lua`), Divine
  Wrath (`c49010598.lua`), Dark Bribe (`c77538567.lua`), Chaos Trap Hole
  (`c11593137.lua`), Infinite Impermanence (`c10045474.lua`), Trap Trick
  (`c80101899.lua`), Cyberdark Invasion (`c1157683.lua`), Mind Scan
  (`c34298391.lua`), and Call of the Haunted (`c97077563.lua`).
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
- `Auxiliary.AddSynchroProcedure` and `Auxiliary.AddSynchroMixProcedure` in
  local `procedure.lua` register `EFFECT_SPSUMMON_PROC` effects from the Extra
  Deck with `SUMMON_TYPE_SYNCHRO`. Standard procedure targets use
  `Duel.CheckSynchroMaterial`, `Duel.SelectSynchroMaterial`,
  `Duel.CheckTunerMaterial`, and `Duel.SelectTunerMaterial`; operations call
  `Card.SetMaterial` and send the chosen group to the GY with
  `REASON_MATERIAL+REASON_SYNCHRO`.
- `Auxiliary.AddXyzProcedure` and `Auxiliary.AddXyzProcedureLevelFree` in local
  `procedure.lua` register `EFFECT_SPSUMMON_PROC` effects from the Extra Deck
  with `SUMMON_TYPE_XYZ`. Standard procedure checks and targets use
  `Duel.CheckXyzMaterial`, `Duel.SelectXyzMaterial`, `Card.SetMaterial`, and
  `Duel.Overlay`; operations send existing Xyz Materials under ordinary
  material cards to the GY by `REASON_RULE` before overlaying the selected
  cards.
- `Duel.GetRitualMaterial`, `Duel.GetRitualMaterialEx`, and
  `Duel.ReleaseRitualMaterial` are bound in `ygopro-core\libduel.cpp`;
  `Card.IsCanBeRitualMaterial` is bound in `ygopro-core\libcard.cpp`.
- `Duel.GetFusionMaterial`, `Duel.SelectFusionMaterial`, and
  `Duel.SetFusionMaterial` are bound in `ygopro-core\libduel.cpp`;
  `Card.IsCanBeFusionMaterial` and `Card.CheckFusionMaterial` are bound in
  `ygopro-core\libcard.cpp`.
- `Duel.SynchroSummon`, `Duel.GetSynchroMaterial`,
  `Duel.SetSynchroMaterial`, `Duel.CheckSynchroMaterial`,
  `Duel.SelectSynchroMaterial`, `Duel.CheckTunerMaterial`, and
  `Duel.SelectTunerMaterial` are bound in `ygopro-core\libduel.cpp`;
  `Card.IsSynchroSummonable`, `Card.IsCanBeSynchroMaterial`,
  `Card.GetSynchroLevel`, and `Card.GetHandSynchro` are bound or declared in
  the local core/define sources.
- `Duel.XyzSummon`, `Duel.CheckXyzMaterial`, `Duel.SelectXyzMaterial`, and
  `Duel.Overlay` are bound in `ygopro-core\libduel.cpp`;
  `Card.IsXyzSummonable`, `Card.IsCanBeXyzMaterial`, `Card.IsCanOverlay`,
  `Card.GetOverlayGroup`, and `Card.RemoveOverlayCard` are bound or declared in
  the local core/define sources.
- Local `ygopro-core\operations.cpp` maps `SUMMON_TYPE_RITUAL` to
  `REASON_RITUAL` for material event handling.
- Local `ygopro-core\operations.cpp` maps `SUMMON_TYPE_FUSION` to
  `REASON_FUSION` for material event handling.
- Local `ygopro-core\operations.cpp` maps `SUMMON_TYPE_XYZ` to `REASON_XYZ`
  for material event handling.
- `Card.IsSetCard` is bound in `ygopro-core\libcard.cpp`; set-code matching is
  implemented through the local core set-code comparison in `card_data.h`.
- Activation lifecycle quality pass checked the source activation,
  activation-legality, and callback pages against local scripts:
  `c6172122.lua` for Red-Eyes Fusion activation restrictions,
  `c10443957.lua` for Damage Step negation legality, `c102380.lua` for
  inherent Special Summon callback shapes and mandatory trigger targeting, and
  `utility.lua` for the local `aux.dscon` Damage Step helper.
- Script examples were checked against local files in
  `D:\Programs\GitHub\ygopro-scripts`.
- Link procedure behavior was checked against local `procedure.lua`,
  `libduel.cpp`, `libcard.cpp`, `operations.cpp`, and
  `ygopro-scripts-define\def.lua`: `Auxiliary.AddLinkProcedure` registers an
  Extra Deck `EFFECT_SPSUMMON_PROC` with `SUMMON_TYPE_LINK`, Link material
  selection uses `Group.CheckWithSumEqual(Auxiliary.GetLinkCount,lc:GetLink(),#sg,#sg)`,
  and the operation records materials with `Card.SetMaterial` before sending
  them to the GY with `REASON_MATERIAL+REASON_LINK`. `Card.IsLinkSummonable`
  and `Duel.LinkSummon` are core bindings and both reject Damage Step use.
- Pendulum procedure behavior was checked against local `procedure.lua`,
  `libduel.cpp`, `libcard.cpp`, `operations.cpp`, and local scripts:
  `Auxiliary.EnablePendulumAttribute` registers a `LOCATION_PZONE`
  `EFFECT_SPSUMMON_PROC_G` with `SUMMON_TYPE_PENDULUM`, uses
  `Auxiliary.PendCondition` and `Auxiliary.PendOperation`, and by default
  registers a hand `EFFECT_TYPE_ACTIVATE` effect unless `reg` is false.
  Candidate checks use the current left and right scales, hand and face-up
  Extra Deck Pendulum locations, `Duel.GetLocationCountFromEx`, and the shared
  Pendulum checklist reset at Draw Phase start. `Duel.MoveToField` accepts
  `LOCATION_PZONE` by mapping it through Spell & Trap Zone placement with a
  Pendulum Zone flag.
- Special Summon-only procedure behavior was checked against local
  `libcard.cpp`, `operations.cpp`, `ygopro-scripts-define\def.lua`,
  `utility.lua`, and local scripts: `Card.EnableReviveLimit` registers
  `EFFECT_REVIVE_LIMIT`, successful rule Special Summon procedures set
  `STATUS_PROC_COMPLETE`, `Card.CompleteProcedure` sets the same status for
  effect-driven proper Summons, and movement to the hand or Deck clears that
  status. Local examples checked include Black Luster Soldier - Envoy of the
  Beginning (`c72989439.lua`), Blue-Eyes Alternative White Dragon
  (`c38517737.lua`), Dark Armed Dragon (`c65192027.lua`), Judgment Dragon
  (`c57774843.lua`), Lava Golem (`c102380.lua`), Flowerdino
  (`c10851853.lua`), The Winged Dragon of Ra - Immortal Phoenix
  (`c10000090.lua`), and the Drytron shared helper block in `utility.lua`.
- Tribute Summon material behavior was checked against local `field.cpp`,
  `playerop.cpp`, `operations.cpp`, `card.cpp`, `libcard.cpp`,
  `libduel.cpp`, `constant.lua`, and `ygopro-scripts-define\def.lua`:
  ordinary Tribute candidates receive `release_param=1`, cards affected by
  `EFFECT_DOUBLE_TRIBUTE` receive `release_param=2`, and
  `Duel.GetTributeCount` may differ from the number of cards in
  `Duel.GetTributeGroup`. `EFFECT_TRIPLE_TRIBUTE` is marked `N/A` locally and
  commented out in the core header, so Egyptian God Slime-style "treated as 3
  Tributes" behavior is documented as a custom Summon/Set procedure. Local
  examples checked include Kaiser Sea Horse (`c17444133.lua`), Double Coston
  (`c44436472.lua`), The First Monarch (`c8522996.lua`), Egyptian God Slime
  (`c42166000.lua`), Slifer the Sky Dragon (`c10000020.lua`), Simorgh, Bird of
  Divinity (`c14989021.lua`), Amarylease (`c18988391.lua`), Simorgh, Bird of
  Ancestry (`c86489182.lua`), Hardened Armed Dragon (`c68473226.lua`), and
  Mausoleum of the Emperor (`c80921533.lua`).
- Counter behavior was checked against local `card.cpp`, `libcard.cpp`,
  `libduel.cpp`, `operations.cpp`, `playerop.cpp`, `processor.cpp`,
  `effect.h`, `card.h`, `constant.lua`, and `ygopro-scripts-define\def.lua`.
  `Card.EnableCounterPermit` creates a single-card `EFFECT_COUNTER_PERMIT`,
  `Card.SetCounterLimit` creates `EFFECT_COUNTER_LIMIT`, `Card.AddCounter`
  checks whether the card is still affected by the resolving reason effect,
  `singly=true` can add only the amount that fits under a counter limit, and
  field-wide `Duel.RemoveCounter` uses the internal counter-selection
  processor. The local core exposes `Duel.IsCanAddCounter` as a player-level
  placement check, not a replacement for `Card.IsCanAddCounter`. Local examples
  checked include Defender, the Magical Knight (`c2525268.lua`), Magical
  Abductor (`c10239627.lua`), Servant of Endymion (`c92559258.lua`), The Kaiju
  Files (`c11163040.lua`), Arcane Barrier (`c17896384.lua`), The World Legacy
  (`c92562411.lua`), Power of the Guardians (`c1118137.lua`), and Magical
  Citadel of Endymion (`c39910367.lua`).
- Monster subtype behavior was checked against local `constant.lua`,
  `procedure.lua`, `utility.lua`, `common.h`, `effect.h`, `card.cpp`,
  `libcard.cpp`, `libduel.cpp`, `operations.cpp`, and local scripts. Gemini
  behavior uses `TYPE_DUAL`, `SUMMON_TYPE_DUAL`,
  `EFFECT_DUAL_SUMMONABLE`, `EFFECT_DUAL_STATUS`,
  `Auxiliary.EnableDualAttribute`, and `Card.EnableDualState`; local examples
  checked include Gemini Soldier (`c68366996.lua`), Gemini Ablation
  (`c80758812.lua`), Gemini Booster (`c18096222.lua`), and Geminize Lord
  Golknight (`c72305034.lua`). Toon behavior was verified as pattern-driven:
  the local sources define `TYPE_TOON` but no shared `EnableToon` helper was
  found; local examples checked include Toon Black Luster Soldier
  (`c28711704.lua`), Blue-Eyes Toon Dragon (`c53183600.lua`), Toon Dragon
  Egger (`c38369349.lua`), Toon Dark Magician (`c21296502.lua`), Toon Kingdom
  (`c43175858.lua`), and Comic Hand (`c33453260.lua`). Union behavior was
  checked through `Auxiliary.EnableUnionAttribute`,
  `Auxiliary.CheckUnionEquip`, `Auxiliary.SetUnionState`,
  `Card.CheckUnionTarget`, and `Card.GetUnionCount`; local examples include
  Union Driver (`c99249638.lua`), Union Pilot (`c89357740.lua`), and Union
  Hangar (`c66399653.lua`). Spirit behavior was checked through
  `Auxiliary.EnableSpiritReturn`, the shared Spirit return condition/target
  helpers, `EFFECT_SPIRIT_DONOT_RETURN`, and `EFFECT_SPIRIT_MAYNOT_RETURN`;
  local examples include Yata Mirror (`c1200843.lua`), Kusanagi Sword
  (`c48716139.lua`), Shinobaroness Peacock (`c25415052.lua`), and Shinobird
  Power Spot (`c9553721.lua`).
- Player-affecting behavior was checked against local `libduel.cpp`,
  `libeffect.cpp`, `effect.h`, `constant.lua`,
  `ygopro-scripts-define\def.lua`, and local scripts. `Duel.SetTargetPlayer`,
  `Duel.SetTargetParam`, `Duel.GetChainInfo`, `Duel.Draw`,
  `Duel.DiscardHand`, `Duel.DiscardDeck`, `Duel.ConfirmDecktop`,
  `Duel.GetDecktopGroup`, `Duel.SortDecktop`, `Duel.ShuffleDeck`, and
  `Duel.ShuffleHand` are local bindings. Player restrictions were checked
  through `EFFECT_FLAG_PLAYER_TARGET`, `Effect.SetTargetRange`,
  `Duel.RegisterEffect`, `EFFECT_CANNOT_DRAW`, `EFFECT_CANNOT_SUMMON`,
  `EFFECT_CANNOT_SPECIAL_SUMMON`, `EFFECT_CANNOT_ACTIVATE`,
  `EFFECT_CANNOT_BP`, `EFFECT_SKIP_DP`, `EFFECT_CANNOT_TO_HAND`, and
  `EFFECT_CANNOT_DISCARD_HAND`. Local examples checked include Pot of Greed
  (`c55144522.lua`), Masked Sorcerer (`c10189126.lua`), Lava Golem
  (`c102380.lua`), Truth Reinforce (`c10118318.lua`), Ancient Gear Beast
  (`c10509340.lua`), Protector of the Sanctuary (`c24221739.lua`), Greed
  Goblin (`c425934.lua`), Deck Lockdown (`c1149109.lua`), Offerings to the
  Doomed (`c19230407.lua`), That Grass Looks Greener (`c11110587.lua`),
  Sunlight Unicorn (`c10321588.lua`), Sylvan Sprout (`c10753491.lua`), and
  Junoldo the Shadespirit Power Patron (`c10266279.lua`).
- Card-affecting negation, immunity, control, and position behavior was
  checked against local `constant.lua`, `utility.lua`,
  `ygopro-scripts-define\def.lua`, generated API pages, and local scripts.
  Chain negation examples include Cyber Dragon Infinity (`c10443957.lua`),
  Infinite Impermanence (`c10045474.lua`), and Effect Veiler
  (`c97268402.lua`). Immunity and protection examples include The Winged
  Dragon of Ra - Immortal Phoenix (`c10000090.lua`) and Toon Kingdom
  (`c43175858.lua`). Control examples include Change of Heart (`c4031928.lua`),
  Mind Control (`c37520316.lua`), Mind Castlin (`c12172567.lua`), Enemy
  Controller (`c98045062.lua`), and Comic Hand (`c33453260.lua`). Position
  examples include Book of Moon (`c14087893.lua`), Enemy Controller
  (`c98045062.lua`), Cosmic Slicer Zer'oll (`c1487805.lua`), Wattsquirrel
  (`c12296376.lua`), and Knight Dragolich (`c88724332.lua`).
- Effect metadata behavior was checked against local `effect.h`,
  `constant.lua`, `libeffect.cpp`, `libduel.cpp`,
  `ygopro-scripts-define\def.lua`, generated API pages, and local scripts.
  `Effect.SetProperty` preserves internal property flags and stores the
  optional second property word, `Effect.SetHintTiming` copies the first
  timing mask to the opponent timing when the second argument is omitted, and
  `Duel.SetOperationInfo` stores category-specific operation data for Chain
  response checks. Local examples checked include Book of Moon
  (`c14087893.lua`), Infinite Impermanence (`c10045474.lua`), Cyber Dragon
  Infinity (`c10443957.lua`), Snipe Hunter (`c84290642.lua`), Time Magic
  Hammer (`c10960419.lua`), Salamandra with Chain (`c62091148.lua`), Pot of
  Greed (`c55144522.lua`), and Lava Golem (`c102380.lua`).
- Chain timing and activation-window behavior was checked against local
  `field.h`, `effect.cpp`, `libeffect.cpp`, `libduel.cpp`,
  `processor.cpp`, `constant.lua`, generated constants, and local scripts.
  `Effect.SetHintTiming` stores controller/opponent prompt masks and copies
  the first mask when the second argument is omitted; `field::check_hint_timing`
  interprets those masks relative to the handler player. `Duel.CheckTiming`
  checks the current core hint masks for either player. `effect::get_speed`
  returns Spell Speed 1 for trigger/ignition effects, 2 for Quick Effects and
  Quick-Play Spell activations, 2 for ordinary Trap activations, and 3 for
  Counter Trap activations. The local `Duel.IsChainNegatable` binding currently
  returns true for the checked Chain Link, so Sacred Book documents it as a
  compatibility/intention check rather than a full legality condition. Damage
  Step and damage calculation activation filtering was checked against
  `EFFECT_FLAG_DAMAGE_STEP` and `EFFECT_FLAG_DAMAGE_CAL` in `effect.cpp` and
  `processor.cpp`. Local examples checked include Book of Moon
  (`c14087893.lua`), Infinite Impermanence (`c10045474.lua`), and Cyber Dragon
  Infinity (`c10443957.lua`).
- Selection and Group-handling behavior was checked against local
  `libduel.cpp`, `libgroup.cpp`, `utility.lua`, generated API pages, and local
  scripts. `Duel.SelectMatchingCard` returns a selected Group without creating
  Chain target relations; `Duel.SelectTarget` requires a current Chain, records
  target cards, and creates relations for non-continuous effects; local
  `Group.SelectSubGroup` is implemented in `utility.lua` and uses
  `Duel.GrabSelectedCard` plus subgroup checks; `Group.SelectUnselect` exposes
  add/remove/cancel selection flow; and `Group.KeepAlive`/`Group.DeleteGroup`
  manage Groups stored beyond the current callback. Local examples checked
  include Book of Moon (`c14087893.lua`), Rescue Hedgehog (`c99742859.lua`),
  Neo-Daedalus (`c10485110.lua`), Lava Golem (`c102380.lua`), and local
  procedure helpers in `procedure.lua`.
- Min/Max selection, archetype/set-code, and effect-type template refinements
  were checked against generated API pages and local scripts. `c96470883.lua`
  and `c97169186.lua` cover tied min/max Groups and resolution choices;
  `c10796448.lua` and `c99075257.lua` cover returned numeric values;
  `c45950291.lua` covers a target-filter alternative for an extreme Rank
  check; `c10186633.lua`, `c12908094.lua`, and `c10000040.lua` cover listed
  metadata, multi-set checks, `aux.gfcheck`, and `IsOriginalCodeRule`; and
  `c99229085.lua` plus `c10604644.lua` cover Xyz Material activated effects and
  `EFFECT_TYPE_FIELD+EFFECT_TYPE_GRANT`.
- Reset behavior was checked against local `effect.h`, `constant.lua`,
  `libeffect.cpp`, `libcard.cpp`, `libduel.cpp`, and
  `ygopro-scripts-define\def.lua`. `Effect.SetReset`,
  `Card.RegisterFlagEffect`, and `Duel.RegisterFlagEffect` all treat reset
  count `0` as `1`; phase resets without `RESET_SELF_TURN` or
  `RESET_OPPO_TURN` receive both turn-side flags. Local examples checked
  include Infinite Impermanence (`c10045474.lua`), Effect Veiler
  (`c97268402.lua`), Lava Golem (`c102380.lua`), Truth Reinforce
  (`c10118318.lua`), Dragon Master Magia (`c12381100.lua`), and the draw-skip
  option in `c967928.lua`.
- Common debugging patterns were checked against local scripts and generated API
  pages. Book of Moon (`c14087893.lua`) is used as the target/relation baseline;
  Rescue Hedgehog (`c99742859.lua`) and X-Saber Perina (`c9978697.lua`) cover
  stored Groups, End Phase cleanup, and `IsRelateToChain`; Holactie
  (`c10000040.lua`) covers `IsOriginalCodeRule` and procedure Group lifetime;
  Cyber Dragon Infinity (`c10443957.lua`), Chow Chow Chan (`c99902789.lua`),
  and Dark-Imprisoning Mirror (`c99735427.lua`) cover activation negation,
  resolving-effect negation, and lingering disable effects; Banner of Courage
  (`c10012614.lua`) covers `SetRange` plus `SetTargetRange`; Sphere Mode
  (`c10000080.lua`) covers reset counts and guarded `GetFirst()` results.
- Client UI and prompt behavior was checked against local `libduel.cpp`,
  `libeffect.cpp`, `constant.lua`, generated API pages, and local scripts.
  Book of Moon (`c14087893.lua`) and Mystical Space Typhoon (`c5318639.lua`)
  cover selection prompts and operation info; Infinite Impermanence
  (`c10045474.lua`) covers opponent-side hint timing and zone highlights;
  Cyberdark Invasion (`c1157683.lua`) covers opponent option notices and
  target-vs-resolution choices; Trap Trick (`c80101899.lua`) covers sequential
  prompts; Pot of Greed (`c55144522.lua`) covers player target data.
- Beginner Script Ladder examples were checked against local scripts and then
  rewritten in modern `local s,id=GetID()` style for teaching. The ladder uses
  Pot of Greed (`c55144522.lua`), Mystical Space Typhoon (`c5318639.lua`),
  Black Hole (`c53129443.lua`), Fissure (`c97169186.lua`), Banner of Courage
  (`c10012614.lua`), Marron (`c11548522.lua`), Book of Moon (`c14087893.lua`),
  and Mirror Force (`c44095762.lua`).
- The first custom-card walkthrough combines local Pot of Greed
  (`c55144522.lua`) target-player draw storage with Book of Moon
  (`c14087893.lua`) targeting and position-change rechecks. `Duel.ChangePosition`
  return behavior was checked against the generated API page before documenting
  the draw-after-success pattern.
- The DataEditorX follow-up guide was checked against local `cards.cdb` schema,
  `DataEditorX\Core\Card.cs`, `DataEditorX\Core\DataBase.cs`,
  `DataEditForm.cs`, `cardinfo_english.txt`, local `utility.lua`
  `Auxiliary.Stringid`, local `ygopro-core\card.cpp` set-code behavior, and
  generated API pages for identity and prompt functions.
- Script Explorer card text search and filters are generated from local
  `cards.cdb`, local scripts, generated API calls, and local `TYPE_*` /
  `CATEGORY_*` constants. The generated public records now include card text,
  card-type labels, and operation category labels for the Vue explorer.
- The second archive audit pass for effect setup and activation flow was
  checked against local `libeffect.cpp`, generated Effect/Duel API pages, and
  local scripts. Cyber Dragon Infinity (`c10443957.lua`) covers `SetCode` as
  both an `EFFECT_*` rule and an `EVENT_*` Quick Effect timing, Lava Golem
  (`c102380.lua`) covers Special Summon procedure target-range/callback shapes
  and mandatory phase triggers, `c10002346.lua` covers continuous field values
  plus destroy-replacement watcher callbacks, Red-Eyes Fusion (`c6172122.lua`)
  covers activation restrictions in cost callbacks, and `c10000030.lua` covers
  legal-mode checks with `SetLabel`/`GetLabel`.
- The filters and all-Group action refinement was checked against generated
  Duel/Group API pages and local scripts. Mirror Force (`c44095762.lua`) covers
  pure one-card filters and all matching opponent Attack Position monsters;
  Black Hole (`c53129443.lua`) covers the non-targeting "all monsters" Group
  action shape where the target branch announces the current Group and the
  operation rebuilds the Group at resolution.
- The movement and LP/damage follow-up pass was checked against local
  `ygopro-scripts-define\def.lua`, generated API pages, and local scripts.
  Movement-family notes use local `Duel.GetLocationCount`,
  `Duel.GetLocationCountFromEx`, `Card.IsForbidden`, `Card.CheckUniqueOnField`,
  `Duel.MoveToField`, `Duel.ReturnToField`, and `Duel.GetControl` behavior.
  Local examples include Time Magic Hammer (`c10960419.lua`) for temporary
  banish plus `Duel.ReturnToField`, Dark Dream Mirror (`c1050355.lua`) for Field
  Zone `Duel.MoveToField`, and Hyper Psychic Blaster/Assault Mode
  (`c37169670.lua`) for a stepped damage/recovery batch finished by
  `Duel.RDComplete()`.
- The 2026-06-25 common-effect-pattern follow-up rechecked the source Equip,
  movement, and LP pages against local `utility.lua`, `constant.lua`,
  `ygopro-scripts-define\def.lua`, generated API pages, and local scripts. This
  pass verified `Auxiliary.AddEquipSpellEffect`, `Duel.EquipComplete`,
  `Duel.RDComplete`, `Duel.BreakEffect`, the absence of local
  `Duel.RemoveCards`, and the local `CATEGORY_EQUIP` comment that limits it to
  effects equipping their own card.
- The continuous-effect refinement was checked against local scripts,
  generated Effect API pages, and `constant.lua`. Banner of Courage
  (`c10012614.lua`) covers a simple face-up Spell field stat effect; Gachi
  Gachi Gantetsu (`c10002346.lua`) covers dynamic `SetValue` plus a continuous
  destroy-replacement watcher; Prankscale (`c10282757.lua`) covers temporary
  field stat and attack restrictions registered during resolution; Salamangreat
  Burst Gryphon (`c10140443.lua`) covers a temporary player-target Special
  Summon restriction; and Slifer the Sky Dragon (`c10000020.lua`) covers
  affected-card/controller-derived stat values and `EFFECT_SET_*` style
  temporary stat changes.
- The Equip and Field Spell follow-up was checked against local
  `utility.lua`, `constant.lua`, and scripts. Crystal Release (`c10004783.lua`)
  covers the inline Equip Spell pattern and Continuous Spell placement;
  Favorite Hero (`c11881272.lua`) covers an Equip Spell that activates a Field
  Spell while its own trigger remains in the Spell & Trap Zone; Fleur de
  Fleuret (`c10204849.lua`) covers Summon-then-equip flow and temporary equip
  limits; Sacred Noble Knight of King Artorigus (`c10613952.lua`) covers
  stepped `Duel.Equip(..., true)` plus `Duel.EquipComplete()`; Charles'
  Saga (`c11802691.lua`) covers `CheckEquipTarget`, `CheckUniqueOnField`, and
  `IsForbidden` prechecks; Last Resort (`c97970833.lua`) covers activating a
  Field Spell from the Deck; and Summer (`c97254001.lua`) covers placing a
  Field Spell without activating it.

## Quality Pass Log

| Date | Source topic cluster | Sacred Book updates |
| --- | --- | --- |
| 2026-06-25 | Equip, movement, and LP common-effect pattern pass | Refined [Equip Spells and Equip Cards](/learn/equip-spells) with local helper naming, equip-shape routing, and script-reading examples. Refined [Functions That Move Cards Across Locations](/learn/moving-cards) with local `Duel.Remove` replacement guidance, operation-info categories, `CATEGORY_EQUIP` caution, and movement example scripts. Refined [LP Recovery and Effect Damage](/learn/lp-recovery-and-damage) with amount-source routing, `Duel.BreakEffect` sequencing, and local LP example scripts. Added a common-effect pattern entry point to Home and Learn. |
| 2026-06-25 | DataEditorX and custom-card data wiring | Added [Card Data and Script Wiring](/learn/card-data-and-script-wiring) as the beginner bridge from a Lua file to `cards.cdb`: `datas`/`texts`, ID/file matching, `aux.Stringid`, type bits, database category labels, set codes, alias, and first-card database checklist. Updated Home, Learn, the sidebar generator, roadmap, and source notes. |
| 2026-06-24 | Script Explorer and first custom script practice | Expanded [Script Explorer](/tools/script-explorer) with card text search, a dedicated text mode, card-type and category filters, featured-only filtering, type/category result chips, and card-text snippets. Added [Write Your First Custom Card](/learn/first-custom-card) and practice exercises under [Beginner Script Ladder](/learn/beginner-script-ladder). |
| 2026-06-24 | Beginner route and navigation audit | Added [Beginner Script Ladder](/learn/beginner-script-ladder) as a concrete sequence of complete small scripts for draw, targeting, non-targeting Groups, Min/Max stat selection, continuous modifiers, mandatory triggers, Quick-Play prompts, and Trap responses. Updated Home, Learn, the VitePress sidebar, and the site generator sidebar source. Confirmed every `docs/learn` page is linked from both the Learn index and sidebar. |
| 2026-06-24 | Min/Max selection, subarchetypes, and effect-type templates | Added [Min/Max Stat Card Selection](/learn/min-max-stat-selection) as a focused guide for tied min/max Groups, returned values, custom scoring functions, activation-vs-resolution selection, and targeting variants. Refined [Archetypes and Set Codes](/learn/archetypes-and-setcodes) with identity-check choices, listed-card metadata, listed-set helpers, original-code checks, and practical filter patterns. Refined [EFFECT_TYPE Constants and Templates](/learn/effect-types) with type-shape selection, trigger source combinations, Xyz Material activated effects, grant effects, and special `SetTargetRange` modes. |
| 2026-06-24 | Equip and Field Spell follow-up | Refined [Equip Spells and Equip Cards](/learn/equip-spells) with activation target-vs-equip-limit guidance, nonstandard equip prechecks, and stepped equip examples. Refined [Field Spells](/learn/field-spells) with handler-range guidance and the activate-vs-place distinction for Field Spells moved through other effects. |
| 2026-06-24 | Continuous effects and stat modifiers follow-up | Refined [Effects That Apply Continuously](/learn/continuous-effects) with a setter build order, `SetTargetRange` card-vs-player modes, and a quick diagnosis table. Refined [Continuous Stat Modifiers](/learn/continuous-stat-modifiers) with `UPDATE`/`SET`/`SET_FINAL` stat-code guidance and value-callback player-reference notes. |
| 2026-06-24 | Movement functions and LP recovery/damage follow-up | Refined [Functions That Move Cards Across Locations](/learn/moving-cards) with destination-vs-field movement families, zone/field-placement legality checks, and temporary banish return handling. Refined [LP Recovery and Effect Damage](/learn/lp-recovery-and-damage) with a local mixed damage/recovery stepped batch example and clearer sequential-vs-stepped guidance. |
| 2026-06-24 | Filters, single-filter selection/targeting, and all-Group actions | Refined [Filters, Card Objects, and Group Objects](/learn/filters-and-groups) with a pure-filter rule, and expanded [Methods for Affecting Cards](/learn/affecting-cards) with local Black Hole and Mirror Force templates for non-targeting all-cards-in-a-Group operations. |
| 2026-06-24 | Effect setup and activation-flow refinement | Refined [Creation, Building, and Registration of an Effect Object](/learn/effect-object), [Cost, Target, And Operation Lifecycle](/learn/cost-target-operation-lifecycle), [Activation Legality](/learn/activation-legality), and [Effects That Apply Continuously](/learn/continuous-effects) with a local-verified `SetType`/`SetCode` meaning map, callback signature cheat sheet, mandatory-part versus optional-follow-up legality notes, and continuous `SetTarget`/`SetValue` callback roles. |
| 2026-06-24 | Archive curriculum re-audit and first scripts | Reworked [Home](/) and [Learning Path](/learn/) around a shorter beginner curve, added [First Scripts To Study](/learn/first-scripts) with local walkthroughs for draw, targeting, prompt timing, continuous field effects, and min/max stat selection, expanded [Targeting Flow](/learn/targeting-flow) with `chkc`, `min,max`, local `Duel.GetTargetsRelateToChain` handling, and resolution wording rechecks, and expanded [Selection And Group Handling](/learn/selection-and-group-handling) with `Group.GetMinGroup` / `Group.GetMaxGroup`. |
| 2026-06-24 | Client UI and prompt behavior | Added [Client UI And Prompt Behavior](/learn/client-ui-and-prompt-behavior) as a focused guide for `Duel.Hint`, `HINT_SELECTMSG`, `SetHintTiming`, `SetOperationInfo`, target prompts, resolution choices, opponent-side prompts, `HINT_OPSELECTED`, `HINT_ZONE`, and troubleshooting legal effects that feel invisible or awkward in the client. |
| 2026-06-24 | Spell and Trap focused follow-ups | Added [Quick-Play Spells](/learn/quick-play-spells), [Counter Traps](/learn/counter-traps), and [Normal And Continuous Traps](/learn/normal-and-continuous-traps) as focused guides for Spell Speed 2 activation flow, Spell Speed 3 Counter Trap negation families, Normal Trap exceptions, Continuous Trap `LOCATION_SZONE` effects, reset behavior, and leave-field cleanup. |
| 2026-06-24 | Home and debugging entry point | Improved [Home](/) as a compact learning portal with a clearer Start Learning path and stronger Learn/API/Examples/Script Explorer/Roadmap cards. Added [Common Script Errors And Debugging](/learn/common-script-errors-and-debugging) as a focused troubleshooting guide backed by local scripts and generated API links. |
| 2026-06-24 | Chain timing and activation windows | Added [Chain Timing And Activation Windows](/learn/chain-timing-and-activation-windows) as a focused guide for prompt masks, free-chain windows, Chain responses, Spell Speed, Damage Step and damage calculation flags, opponent-side prompts, `Duel.CheckTiming`, `Duel.IsChainNegatable`, and Chain-solving watchers. |
| 2026-06-24 | Local script-source refresh and new utility/card behavior | Imported the local `ygopro-scripts` changes from `d25c0eed5^..06ccc5a99` into `Scripts/` and `Utilities/`. Added function documentation for `Auxiliary.EnableMulcharmyGlobalCheck` and its internal watcher, added reviewed English for `EFFECT_REVEAL_ONFIELD`, and added the [Mind Scan case study](/examples/mind-scan) for the new Continuous Trap reveal/declared-name negation pattern. `EFFECT_REVEAL_ONFIELD` behavior was checked against local `ygopro-core\effect.h`, `card.cpp`, and `effect.cpp`; Mind Scan card facts were supplied from the Yugipedia entry because the card is not yet in local `cards.cdb`. |
| 2026-06-24 | Reset flags, temporary effects, and duration | Added [Reset Flags And Effect Duration](/learn/reset-flags-and-duration) as a central lifetime guide. It explains card-bound temporary resets, `RESETS_STANDARD`, player/Duel restrictions, phase turn-side flags, reset counts, current-phase pitfalls, flag-effect lifetimes, manual resets, local examples, and API links. |
| 2026-06-24 | Selection helpers and Group/Card handling | Added [Selection And Group Handling](/learn/selection-and-group-handling) as a practical follow-up to filters and Groups. It explains target selection versus resolution selection, selecting from existing Groups, subgroup legality/selection, `SelectUnselect`, `KeepAlive`/`DeleteGroup`, iteration patterns, and resolution rechecks with local examples and API links. |
| 2026-06-24 | Categories, properties, hint timing, and client UI behavior | Added [Categories, Properties, And Hint Timing](/learn/categories-properties-and-hints) as a focused effect-metadata guide. It explains category labels versus real actions, operation info for known and unresolved actions, official card/player target flags, Damage Step properties, `EFFECT_FLAG_SINGLE_RANGE`, continuous target flags, oath/cannot-disable flags, `SetHintTiming`, and selection prompts with local examples and API links. |
| 2026-06-24 | Effects that affect cards expansion | Added [Negation and Immunity](/learn/negation-and-immunity), [Control Change](/learn/control-change), and [Battle Position Effects](/learn/battle-position-effects) as focused card-affecting guides. These split Chain negation, lingering disable, immunity, targeting/destruction protection, take-control, swap-control, equip-based control, position changes, forced positions, and position locks with local examples and API links. |
| 2026-06-24 | Effects that affect players expansion | Added [Player-Targeted Effects](/learn/player-targeted-effects), [Player Restrictions](/learn/player-restrictions), and [Draw, Hand, And Deck Effects](/learn/draw-hand-and-deck-effects) as focused player-effect guides. These split target-player Chain data, player/action locks, draw legality, hand discard, Deck-top reveal/sort, and Deck-to-GY patterns with local examples and API links. |
| 2026-06-23 | Monster subtype expansion | Added focused [Gemini Monsters](/learn/gemini-monsters), [Toon Monsters](/learn/toon-monsters), [Union Monsters](/learn/union-monsters), and [Spirit Monsters](/learn/spirit-monsters) guides instead of folding subtype rules into a broad monster page. Each guide uses local constants, helper behavior, API links, and examples from local scripts. |
| 2026-06-23 | Activation lifecycle: activated effects, activation legality, and condition/cost/target/operation callbacks | Expanded [Conditions, Costs, Activation Procedures, and Resolution](/learn/effect-callbacks), [Activation Legality](/learn/activation-legality), [Activated Effects](/learn/activated-effects), and [Cost, Target, And Operation Lifecycle](/learn/cost-target-operation-lifecycle) with event-condition signatures, Damage Step legality, Quick Effect negation checks, activation restrictions, Red-Eyes Fusion and Cyber Dragon Infinity examples, and API links for the referenced functions. |
| 2026-06-23 | Foundation forever pass: effect objects, filters/groups, movement, continuous effects, stat modifiers, and LP effects | Expanded [Creation, building, and registration of an effect object](/learn/effect-object), [Filters, Card Objects, and Group Objects](/learn/filters-and-groups), [Functions that move cards across locations](/learn/moving-cards), [Effects That Apply Continuously](/learn/continuous-effects), [Continuous stat modifiers](/learn/continuous-stat-modifiers), and [LP Recovery and Effect Damage](/learn/lp-recovery-and-damage) with setter-shape maps, target-range modes, property flags, subgroup selection, movement routing, local dynamic value examples, pure LP activation checks, stepped LP examples, and API links. |
| 2026-06-23 | Equip and Field Spell strict pass | Expanded [Equip Spells and Equip Cards](/learn/equip-spells) with activation-shape differences, core equip housekeeping, non-applying equip modifiers, lost-target triggers, and summon-then-equip notes. Added [Field Spells](/learn/field-spells) as a focused local-source guide because no Field Spell source topic was present in the archive folder. |
| 2026-06-23 | Spell and Trap classification expansion | Added [Spell Card Patterns](/learn/spell-card-patterns) for Normal, Continuous, Quick-Play, and Ritual Spell activation shapes, and [Trap Card Patterns](/learn/trap-card-patterns) for Normal, Continuous, and Counter Trap scripting. Local examples include Pot of Greed, Monster Reborn, Mystical Space Typhoon, Transonic Bird, Infinite Impermanence, Trap Trick, Cyberdark Invasion, and Chaos Trap Hole. |
| 2026-06-23 | Ritual procedure expansion | Added [Ritual Procedure Guide](/learn/ritual-procedure) with helper selection, `AddRitualProcUltimate` internals, target/operation flow, material subgroup checks, `SetMaterial`, `ReleaseRitualMaterial`, `SUMMON_TYPE_RITUAL`, `CompleteProcedure`, manual Sonic Tracker-style flow, Nekroz Kaleidoscope nonstandard material movement, and API links. |
| 2026-06-23 | Fusion procedure expansion | Added [Fusion Procedure Guide](/learn/fusion-procedure) with Fusion Monster material procedures, Fusion-specific material identity checks, Polymerization flow, Deck Fusion examples, Chain Material fallback, material movement operations, Contact Fusion distinction, and API links. |
| 2026-06-23 | Synchro procedure expansion | Added [Synchro Procedure Guide](/learn/synchro-procedure) with standard and mixed Synchro procedures, Tuner/non-Tuner filters, helper internals, Level and material legality, Hop Ear Squadron effect-driven Synchro Summon flow, Accel Synchro Stardust Dragon manual Synchro-style Summon notes, material memory checks, custom Synchro material providers, and API links. |
| 2026-06-23 | Xyz procedure expansion | Added [Xyz Procedure Guide](/learn/xyz-procedure) with standard Xyz procedures, Xyz Level checks, variable material counts, overlay operation order, detach costs, alternate one-card Xyz routes, Level-free Xyz procedures, effect-driven Xyz Summons, adding cards as Xyz Material, and API links. |
| 2026-06-23 | Link procedure expansion | Added [Link Procedure Guide](/learn/link-procedure) with standard Link procedures, Link Rating count rules, material pool and extra-material checks, operation order, effect-driven Link Summons, fixed-material and opponent-material examples, linked-zone APIs, material memory, and API links. |
| 2026-06-23 | Pendulum procedure expansion | Added [Pendulum Procedure Guide](/learn/pendulum-procedure) with `EnablePendulumAttribute`, default and custom Pendulum activation patterns, Pendulum Zone effects, scale reads and updates, hand/face-up Extra Deck candidate pools, regular and extra Pendulum Summon handling, `MoveToField` Pendulum Zone placement, revive-limit Pendulum Summonable monsters, and API links. |
| 2026-06-23 | Special Summon-only monster expansion | Added [Special Summon-only Monster Guide](/learn/special-summon-only-monsters) with revive limits, `EFFECT_SPSUMMON_PROC`, procedure target/operation patterns, Blue-Eyes Alternative reveal flow, condition-only procedures, `EFFECT_SPSUMMON_CONDITION`, opponent-field procedures, `EFFECT_SPSUMMON_COST`, effect-driven proper Summons, `nocheck`/`nolimit`, and API links. |
| 2026-06-23 | Tribute Summon material expansion | Added [Tribute Summon Materials](/learn/tribute-summon-materials) with cards treated as multiple Tributes, `release_param`, Egyptian God Slime's local custom procedure, ordinary three-Tribute procedures, Tribute-reduction effects, Tribute limits, material memory, local examples, and API links. |
| 2026-06-23 | Counter mechanics expansion | Added [Counters](/learn/counters) with counter permits, limits, `singly` additions, card-vs-field removal, removal replacement, counter events, lifecycle/reset behavior, local examples, API links, and a corrected learner note for `Duel.IsCanAddCounter`. |

## Intentional Rewrites

Some source sections referenced helper APIs or simulator behavior that are
not the local MDPro3/YGOPro source of truth. Those sections were rewritten as
local equivalents instead of imported directly:

- Equip procedure material is documented through local
  `Auxiliary.AddEquipSpellEffect`, `Duel.Equip`, `EFFECT_EQUIP_LIMIT`, and equip
  target APIs instead of non-local helper names.
- Field Spell material was reconstructed from local scripts and core behavior
  because no Field Spell source topic was present in the archive folder.
- Movement-table entries that used non-local function names were translated to
  local APIs such as `Duel.GetControl` and `Duel.SendtoExtraP`.
- Examples sourced from external repositories were replaced with local-script
  style snippets and local behavior notes.

## Ongoing Standard

Future learning pages should continue this style:

- Use source topics only to notice topics and teaching gaps.
- Rewrite explanations in Sacred Book's own words.
- Prefer local script-backed examples over invented snippets.
- Mark inferred behavior clearly when the local core does not prove it.
- Keep API signatures and generated function docs as the exact reference layer.
