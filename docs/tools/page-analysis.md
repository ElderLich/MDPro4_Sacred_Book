# Downloaded Tutorial Coverage

This page records how the downloaded YGOPRO Scripting Wiki tutorial pages in
`C:\Users\Shanalotte\Desktop\New folder (2)` were analyzed for Sacred Book.
They are used as a topic checklist and teaching-quality benchmark only.

Sacred Book does not copy their wording and does not use EDO/Project Ignis
documentation as factual source of truth. Final behavior is checked against
local MDPro3/YGOPro sources, local scripts, local define files, and generated
Sacred Book data.

The downloaded editor-tool page is excluded from this tutorial-equivalent pass.

## Coverage Map

| Downloaded tutorial topic | Sacred Book equivalent |
| --- | --- |
| Main scripting-wiki landing page | [Home](/), [Learning Path](/learn/), and this coverage map organize the beginner route. |
| Structure of a card script | [Structure of a card script](/learn/script-structure) covers file naming, `GetID`, `initial_effect`, callback naming, and reading real scripts. |
| Creation, building, and registration of an effect object | [Creation, building, and registration of an effect object](/learn/effect-object) covers `Effect.CreateEffect`, setters, registration, cloning, labels, label objects, and resets. |
| EFFECT_TYPE constants and templates | [EFFECT_TYPE constants and templates](/learn/effect-types) covers common type flags, activated types, continuous types, combinations, material effects, and grant effects. |
| Functions for conditions, costs, activation procedures, and resolution | [Conditions, costs, activation procedures, and resolution](/learn/effect-callbacks) plus [Cost, target, and operation lifecycle](/learn/cost-target-operation-lifecycle). |
| Activation legality | [Activation legality](/learn/activation-legality) covers `chk==0`, implicit action requirements, optional effects, mandatory effects, `chkc`, and resolution rechecks. |
| Activated effects | [Activated effects](/learn/activated-effects) covers Chain Link flow, common activated types, optional and mandatory triggers, Spell/Trap activation, and the activation/resolution split. |
| Filters, Card objects, and Group objects | [Filters, Card Objects, and Group Objects](/learn/filters-and-groups) covers filter arguments, matching vs targeting, Groups, filtering, selecting, iterating, membership, and counts. |
| List of functions that move cards across locations | [Functions that move cards across locations](/learn/moving-cards) covers movement APIs, able-to checks, targeting/non-targeting patterns, Special Summons, equip, `MoveToField`, returns, and reason flags. |
| Effects that apply continuously | [Effects That Apply Continuously](/learn/continuous-effects) covers single, field, equip, Xyz Material, player-affecting, event-watching, and temporary continuous effects. |
| Tutorial for scripting a simple continuous effect | [Continuous stat modifiers](/learn/continuous-stat-modifiers) gives the focused ATK/DEF tutorial for self, field, equip, material, temporary, and cloned modifiers. |
| Equip Spell | [Equip Spells and Equip Cards](/learn/equip-spells) covers manual Equip Spell activation, `Auxiliary.AddEquipSpellEffect`, equip limits, `EFFECT_TYPE_EQUIP`, monsters equipped by effects, and stepped equip. |
| Recovering LP and inflicting effect damage | [LP Recovery and Effect Damage](/learn/lp-recovery-and-damage) covers fixed amounts, resolution-calculated amounts, target-player data, target-based recovery, stepped LP changes, categories, and return values. |
| Methods for affecting cards | [Methods for Affecting Cards](/learn/affecting-cards) acts as the outcome router for immediate actions, continuous changes, negation, stat/property changes, control, equip, and review checks. |
| Subarchetype | [Archetypes and Set Codes](/learn/archetypes-and-setcodes) covers IDs, `IsSetCard`, multiple set-code checks, subarchetype bit structure, listed cards, and alternate codes. |

## Verification Notes

Several details were verified directly against local MDPro3/YGOPro sources:

- `Duel.Damage`, `Duel.Recover`, `Duel.RDComplete`, `Duel.Equip`, and
  `Duel.EquipComplete` are bound in `ygopro-core\libduel.cpp` and documented in
  `ygopro-scripts-define\def.lua`.
- `Duel.Damage` and `Duel.Recover` return the actual changed LP value and clamp
  negative input amounts to `0` in the local core binding.
- `Auxiliary.AddEquipSpellEffect` in local `utility.lua` creates the normal
  Equip Spell activation shape and registers `EFFECT_EQUIP_LIMIT`.
- `Card.IsSetCard` is bound in `ygopro-core\libcard.cpp`; set-code matching is
  implemented through the local core set-code comparison in `card_data.h`.
- Script examples were checked against local files in
  `D:\Programs\GitHub\ygopro-scripts`.

## Ongoing Standard

Future learning pages should continue this style:

- Use downloaded pages only to notice topics and teaching gaps.
- Rewrite explanations in Sacred Book's own words.
- Prefer local script-backed examples over invented snippets.
- Mark inferred behavior clearly when the local core does not prove it.
- Keep API signatures and generated function docs as the exact reference layer.
