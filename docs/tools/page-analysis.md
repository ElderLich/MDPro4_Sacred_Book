# Page Analysis

This is the working analysis of the downloaded YGOPRO Scripting Wiki pages in `C:\Users\Shanalotte\Desktop\New folder (2)`. These pages are used as a depth benchmark only. Sacred Book should not copy their wording or import EDO/ProjectIgnis assumptions; every final explanation should be rewritten from MDPro3/YGOPro behavior, local scripts, `ygopro-core`, `Define/`, `Utilities/`, and `cards.cdb`.

## What The Pages Teach Well

- They teach concepts before listing functions.
- They show the shape of real callback code instead of only giving signatures.
- They explain why similar functions differ, such as matching vs targeting and check vs select.
- They warn about common mistakes, such as paying costs during legality checks or forgetting relation checks during resolution.
- They group API functions by workflow: building effects, checking activation legality, selecting cards, iterating Groups, moving cards, and applying continuous effects.

## Sacred Book Coverage Map

| Downloaded page | Sacred Book response |
| --- | --- |
| `Structure of a card script` | Expand `/learn/script-structure` with complete script anatomy, `GetID`, `initial_effect`, callback naming, and a tiny complete MDPro3 card script. |
| `Creation, building, and registration, of an effect object` | Expand `/learn/effect-object` and deepen pages for `Effect.CreateEffect`, `Effect.Set*`, and `Card.RegisterEffect`. |
| `EFFECT TYPE constants and templates` | Expand `/learn/effect-types` with MDPro3 examples for single, field, activate, ignition, trigger, quick, continuous, and procedure effects. |
| `Functions for conditions, costs, activation procedures, and resolution of an effect` | Expand `/learn/effect-callbacks`; add deep API guides for `Effect.SetCondition`, `Effect.SetCost`, `Effect.SetTarget`, and `Effect.SetOperation`. |
| `Activation legality` | Expand `/learn/activation-legality`; connect legality checks to `chk==0`, target availability, cost availability, once-per-turn counts, and response windows. |
| `Using filters to handle Card and Group Objects` | Expand `/learn/filters-and-groups`; add deep API guides for matching, targeting, Group iteration, filtering, selecting, and counting. |
| `List of functions that move cards across locations` | Expand `/learn/moving-cards`; add movement pages for `Duel.SendtoGrave`, `Duel.SendtoHand`, `Duel.SendtoDeck`, `Duel.Remove`, `Duel.Destroy`, and `Duel.SpecialSummon`. |
| `Activated effects` | Add a focused lesson for activated effects from registration through resolution, with one normal Spell/Trap style example and one monster ignition/trigger example. |
| `Effects that apply continuously` | Add a focused lesson for continuous effects, including handler-only effects, field effects, equipped-card effects, and Xyz Material effects. |
| `Methods for affecting cards` | Add a guide that groups common Card/Duel operations by outcome: destroy, send, banish, return, change ATK/DEF, negate, equip, and change control. |
| `Subarchetype` | Expand `/learn/archetypes-and-setcodes` with set-code matching, sub-set behavior, and script examples using `Card.IsSetCard`. |

## Current Learning Pass

The first original learning-pass pages now cover script structure, effect object creation, effect types, callbacks, activation legality, filters/groups, movement functions, continuous effects, methods for affecting cards, and archetypes/set codes. These pages are intentionally tutorial-level; deeper function-specific examples continue to live on generated API pages.

## Function Page Standard

Important function pages should eventually include:

- A short summary that reads naturally.
- The exact MDPro3/YGOPro signature.
- Parameter and return notes.
- A `How To Use It` section with the common workflow.
- A small Lua example in local script style.
- A pitfall or distinction when the function is often confused with another one.
- Links to related function pages and real cards using the function.

## First Implementation Batch

The first generated `How To Use It` sections focus on the pages with the highest script usage and the most tutorial value:

- `Duel.IsExistingMatchingCard`
- `Duel.SelectMatchingCard`
- `Duel.IsExistingTarget`
- `Duel.SelectTarget`
- `Duel.GetFirstTarget`
- `Duel.GetMatchingGroup`
- `Duel.SpecialSummon`
- `Card.IsCanBeSpecialSummoned`
- `Effect.SetCost`
- `Effect.SetTargetRange`
- `Card.IsCode`
- `Group.Filter`
- `Group.Select`
- `Group.IsExists`
- `Group.GetFirst`
- `Group.GetNext`
