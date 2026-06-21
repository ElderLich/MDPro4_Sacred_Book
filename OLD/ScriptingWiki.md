# 📚 Combined YGOPro/MDPro3 Scripting Wiki

## Part 1 — User Draft (Original ScriptingWiki.md)

````markdown
# 🧠 Koishi-style Yu-Gi-Oh! Scripting Guide (YGOPro Percy / MDPro3)

> A deep, structured reference and how-to manual for scripting custom Yu-Gi-Oh! cards using Koishi-style Lua.  
> Synthesized from the [YGOPro Scripting Wiki](https://ygoproscripting.miraheze.org/wiki/Main_Page), real card scripts, and expert review.

---

## 📚 Table of Contents

1. [Introduction](#introduction)  
2. [Structure of a Card Script](#structure-of-a-card-script)  
3. [Effect Creation & Registration](#effect-creation--registration)  
4. [Effect Types, Categories & Constants](#effect-types-categories--constants)  
5. [Effect Flags Explained](#effect-flags-explained)  
6. [Condition, Cost, Target, Operation](#condition-cost-target-operation)  
7. [Card Filters, Groups & Selection](#card-filters-groups--selection)  
8. [Trigger Types: `O` vs `F`](#trigger-types-o-vs-f)  
9. [Timing and Activation Legality](#timing-and-activation-legality)  
10. [Necrovalley Filter: When to Use It](#necrovalley-filter-when-to-use-it)  
11. [Common Patterns (Koishi-style Templates)](#common-patterns-koishi-style-templates)  
12. [Do's and Don'ts](#dos-and-donts)  
13. [Advanced Notes](#advanced-notes)  
14. [Useful References](#useful-references)

---

## 🧩 Introduction

**Koishi-style scripting** is the modern standard for MDPro3/YGOPro Lua effects. It is modular, consistent, and designed for compatibility with automatic parser systems and custom simulators.

Compared to Edo-style, it uses `Effect.CreateEffect`, standardized function declarations, and clear separation of `cost`, `target`, and `operation`.

---

## 🔧 Structure of a Card Script

Every card script starts like this:

```lua
--Card Name
local s,id=GetID()

function s.initial_effect(c)
  -- Effect registration goes here
end
````

* `GetID()` dynamically assigns `id` and creates a namespace `s`
* Avoid global function definitions like `function c12345678.initial_effect()`

---

## ⚙️ Effect Creation & Registration

```lua
local e1=Effect.CreateEffect(c)
e1:SetType(EFFECT_TYPE_SINGLE)
e1:SetCode(EFFECT_UPDATE_ATTACK)
e1:SetValue(500)
c:RegisterEffect(e1)
```

* Always create effects with `Effect.CreateEffect`
* Always attach them to the card with `RegisterEffect`

---

## 🎭 Effect Types, Categories & Constants

### Effect Types (from `constant.lua`)

| Type                     | Description                        |
| ------------------------ | ---------------------------------- |
| `EFFECT_TYPE_SINGLE`     | Applies only to the card           |
| `EFFECT_TYPE_TRIGGER_O`  | Optional trigger                   |
| `EFFECT_TYPE_TRIGGER_F`  | Mandatory trigger                  |
| `EFFECT_TYPE_IGNITION`   | Activatable during your Main Phase |
| `EFFECT_TYPE_CONTINUOUS` | Always active (state-based)        |
| `EFFECT_TYPE_QUICK_O`    | Optional quick effect              |

### Categories

These determine how the engine handles effect resolution:

* `CATEGORY_TOHAND`
* `CATEGORY_SPECIAL_SUMMON`
* `CATEGORY_TOGRAVE`
* `CATEGORY_DESTROY`
* `CATEGORY_REMOVE`

---

## 🚩 Effect Flags Explained

| Flag                        | Purpose                                                            |
| --------------------------- | ------------------------------------------------------------------ |
| `EFFECT_FLAG_DELAY`         | Makes trigger use “If” rather than “When” (prevents missed timing) |
| `EFFECT_FLAG_CARD_TARGET`   | Required when the effect targets                                   |
| `EFFECT_FLAG_DAMAGE_STEP`   | Allows effect in the Damage Step                                   |
| `EFFECT_FLAG_CLIENT_HINT`   | Shows client hint                                                  |
| `EFFECT_FLAG_IGNORE_IMMUNE` | Ignores immunity                                                   |

Use these wisely with `SetProperty`.

---

## 🔁 Condition, Cost, Target, Operation

Correct order matters:

```lua
e:SetCondition(s.condition)
e:SetCost(s.cost)
e:SetTarget(s.target)
e:SetOperation(s.operation)
```

Each one should be modular.

---

## 🧲 Card Filters, Groups & Selection

Card filters:

```lua
function s.filter(c)
  return c:IsType(TYPE_MONSTER) and c:IsAbleToHand()
end
```

Common group operations:

```lua
Duel.IsExistingMatchingCard(s.filter, tp, LOCATION_DECK, 0, 1, nil)
Duel.SelectMatchingCard(tp, s.filter, tp, LOCATION_DECK, 0, 1, 1, nil)
```

For Necrovalley compatibility:

```lua
aux.NecroValleyFilter(s.filter)
```

---

## ⏲ Trigger Types: `O` vs `F`

* `TRIGGER_O` = Optional ("you can")
* `TRIGGER_F` = Forced ("when")

🧠 Use `EFFECT_FLAG_DELAY` with `TRIGGER_O` to allow timing flexibility ("If..." triggers).

Don't use `TRIGGER_F` unless it's **required** to force activation.

---

## ⌛ Timing and Activation Legality

Refer to:
[https://ygoproscripting.miraheze.org/wiki/Activation\_legality](https://ygoproscripting.miraheze.org/wiki/Activation_legality)

* Targets must be valid when the effect **resolves**, not just when it **activates**
* You can activate an effect that **will fail** (e.g. under Necrovalley)

✅ You **do not need** `aux.NecroValleyFilter` in `SetTarget`

❌ You **must use** it in the operation step

---

## ⚰️ Necrovalley Filter: When to Use It

Correct:

```lua
local g=Duel.SelectMatchingCard(tp, aux.NecroValleyFilter(s.filter), ...)
```

Incorrect:

```lua
-- Don’t use NecrovalleyFilter in SetTarget!
```

Only use the filter in resolution to prevent hard lockout of otherwise activatable effects.

---

## 📋 Common Patterns (Koishi-style Templates)

### Optional Trigger on Summon

```lua
local e1=Effect.CreateEffect(c)
e1:SetType(EFFECT_TYPE_SINGLE+EFFECT_TYPE_TRIGGER_O)
e1:SetCode(EVENT_SUMMON_SUCCESS)
e1:SetProperty(EFFECT_FLAG_DELAY)
e1:SetTarget(s.target)
e1:SetOperation(s.operation)
c:RegisterEffect(e1)
```

### Ignition Effect in Main Phase

```lua
local e2=Effect.CreateEffect(c)
e2:SetType(EFFECT_TYPE_IGNITION)
e2:SetRange(LOCATION_MZONE)
e2:SetCountLimit(1,id)
e2:SetTarget(s.target)
e2:SetOperation(s.operation)
c:RegisterEffect(e2)
```

---

## ✅ Do's and Don'ts

### ✅ DO:

* Use `aux.NecroValleyFilter` in operations from GY
* Use `EFFECT_FLAG_DELAY` on trigger effects
* Use `GetClassCount(Card.GetCode)` to count **unique codes**

### ❌ DON'T:

* Don’t use `NecrovalleyFilter` in `SetTarget`
* Don’t use global `function` definitions (`c12345678.initial_effect`)
* Don’t trust `GetCount() >= 3` for unique material checks

---

## 🧠 Advanced Notes

### Check for 3 Unique Gods

```lua
g:GetClassCount(Card.GetCode)==3
  and g:IsExists(Card.IsCode,1,nil,10000000)
  and g:IsExists(Card.IsCode,1,nil,10000010)
  and g:IsExists(Card.IsCode,1,nil,10000020)
```

### Check for 3 Zones

```lua
Duel.GetLocationCount(tp, LOCATION_MZONE) >= 3
```

Required if you're going to summon 3 monsters simultaneously.

---

## 🔗 Useful References

* [https://ygoproscripting.miraheze.org/wiki/Main\_Page](https://ygoproscripting.miraheze.org/wiki/Main_Page)
* [https://ygoproscripting.miraheze.org/wiki/Structure\_of\_a\_card\_script](https://ygoproscripting.miraheze.org/wiki/Structure_of_a_card_script)
* [https://ygoproscripting.miraheze.org/wiki/Functions\_for\_conditions,\_costs,\_activation\_procedures,\_and\_resolution\_of\_an\_effect](https://ygoproscripting.miraheze.org/wiki/Functions_for_conditions,_costs,_activation_procedures,_and_resolution_of_an_effect)
* [https://ygoproscripting.miraheze.org/wiki/List\_of\_functions\_that\_move\_cards\_across\_locations](https://ygoproscripting.miraheze.org/wiki/List_of_functions_that_move_cards_across_locations)
* [https://ygoproscripting.miraheze.org/wiki/Activated\_effects](https://ygoproscripting.miraheze.org/wiki/Activated_effects)

---


## Part 2 — Consolidated Koishi‑Style Guide (Auto‑Generated)

# 🧠 Koishi‑Style YGOPro/MDPro3 Scripting Wiki — Consolidated Guide

> A practical, truth‑checked reference for writing **Koishi‑style** Lua card scripts that work in YGOPro/MDPro3/MDPro3.  
> Compiled from the YGOPro Scripting Wiki (focus on “Koishi” sections) and validated against your local `constant.lua`, `procedure.lua`, `utility.lua`, and real scripts in `merged_cards.part*.json`. See inline citations.

---

## Contents
1. [Card Script Structure](#card-script-structure)  
2. [Effect Creation & Registration](#effect-creation--registration)  
3. [Effect Types, Triggers & Categories](#effect-types-triggers--categories)  
4. [Flags & Properties (When to Use What)](#flags--properties-when-to-use-what)  
5. [C‑C‑T‑O Order (Condition, Cost, Target, Operation)](#c-c-t-o-order-condition-cost-target-operation)  
6. [Filters, Groups & Selection](#filters-groups--selection)  
7. [Targeting vs. Non‑Targeting](#targeting-vs-non-targeting)  
8. [Activation Legality & Timing](#activation-legality--timing)  
9. [Continuous Effects (STATE & FIELD)](#continuous-effects-state--field)  
10. [Activated Effects (Ignition, Quick, Trigger)](#activated-effects-ignition-quick-trigger)  
11. [Methods that Affect Cards (Move/Destroy/Banish/etc.)](#methods-that-affect-cards-movedestroybanishetc)  
12. [Single‑Filter Selection & Targeting Patterns](#single-filter-selection--targeting-patterns)  
13. [Affecting All Cards in a Group](#affecting-all-cards-in-a-group)  
14. [Necrovalley Compatibility](#necrovalley-compatibility)  
15. [Common Koishi Patterns (with real examples)](#common-koishi-patterns-with-real-examples)  
16. [FX Procedure Helpers (Ritual/Synchro/Xyz/Link/Fusion)](#fx-procedure-helpers-ritualsynchroxyzlinkfusion)  
17. [Authoring Checklist](#authoring-checklist)  
18. [References](#references)

---

## Card Script Structure

Koishi‑style scripts follow this header:

```lua
--Card Name
local s,id=GetID()

function s.initial_effect(c)
  -- register effects here
end
```

`GetID()` provides the numeric code and a local table `s` for namespacing your helpers. Avoid old Edo global names like `function c12345678.initial_effect()`. fileciteturn3file0 citeturn1search0

---

## Effect Creation & Registration

Create an `Effect` on the handler card, configure it, and register it:

```lua
local e1=Effect.CreateEffect(c)
e1:SetType(EFFECT_TYPE_SINGLE)
e1:SetCode(EFFECT_UPDATE_ATTACK)
e1:SetValue(500)
c:RegisterEffect(e1)
```

This is the standard pattern the engine expects. fileciteturn3file0

---

## Effect Types, Triggers & Categories

**Typical types** you’ll use:
- `EFFECT_TYPE_SINGLE` — applies to the handler only
- `EFFECT_TYPE_IGNITION` — manual during Main Phase
- `EFFECT_TYPE_QUICK_O` — optional Quick Effect
- `EFFECT_TYPE_TRIGGER_O/F` — optional/forced triggers
- `EFFECT_TYPE_FIELD` — continuous aura/broad effects
- `EFFECT_TYPE_CONTINUOUS` — state watchers / hook‑style

Comprehensive descriptions and templates are on the wiki. citeturn1search1

**Common categories (inform the client/engine UI):** `CATEGORY_TOHAND`, `CATEGORY_SPECIAL_SUMMON`, `CATEGORY_TOGRAVE`, `CATEGORY_DESTROY`, `CATEGORY_REMOVE`, etc. citeturn1search1

Real scripts in your set constantly annotate categories before resolution. fileciteturn2file10

---

## Flags & Properties (When to Use What)

- `EFFECT_FLAG_CARD_TARGET` — the effect **targets** a card (you must also select targets during targeting). citeturn1search9
- `EFFECT_FLAG_DELAY` — optional triggers that should still fire when “If” timing applies; prevents missed timing. Use on `EVENT_TO_GRAVE` / `EVENT_SUMMON_SUCCESS`, etc. citeturn1search6
- `EFFECT_FLAG_DAMAGE_STEP` — allows activation in Damage Step (only certain operations). citeturn1search6
- `EFFECT_FLAG_CLIENT_HINT` — show a UI hint.  
- `EFFECT_FLAG_IGNORE_IMMUNE` — let the effect apply even to normally immune cards (use sparingly).  

You apply these via `SetProperty`. See examples below. fileciteturn2file7 fileciteturn2file3

---

## C‑C‑T‑O Order (Condition, Cost, Target, Operation)

Always wire handlers in this order:

```lua
e:SetCondition(s.condition)   -- optional
e:SetCost(s.cost)             -- pay costs first
e:SetTarget(s.target)         -- select targets, set opinfo
e:SetOperation(s.operation)   -- do the thing
```

Keeping them separate improves readability and legality checks. fileciteturn2file6

---

## Filters, Groups & Selection

A **filter** returns true/false on a `Card`. Groups are dynamic sets of cards.

```lua
function s.thfilter(c) return c:IsAbleToHand() and c:IsSetCard(0x1be) end
-- existence check
Duel.IsExistingMatchingCard(s.thfilter,tp,LOCATION_DECK,0,1,nil)
-- selection
Duel.SelectMatchingCard(tp,s.thfilter,tp,LOCATION_DECK,0,1,1,nil)
```

Helper makers in `utility.lua` let you build filters easily:
`aux.FilterBoolFunction`, `aux.TargetBoolFunction`, etc. fileciteturn3file12

When selecting from GY in the **operation**, wrap filters with `aux.NecroValleyFilter` (see below). fileciteturn2file8 citeturn1search3

---

## Targeting vs. Non‑Targeting

**Targeting** requires:
1) `e:SetProperty(EFFECT_FLAG_CARD_TARGET)`  
2) pick targets in `target()` (usually `Duel.SelectTarget`)  
3) use `Duel.GetFirstTarget()` or `Duel.GetTargetsRelateToChain()` in `operation()`.

Example (target topdeck/bounce): your dataset shows classic targeting with `EFFECT_FLAG_CARD_TARGET`, `Duel.SelectTarget`, then send to Deck/Hand in op. fileciteturn3file9

**Non‑targeting** effects only gather a group in operation (e.g., “destroy all face‑up monsters…”), sometimes selecting during operation and not marking as targets. fileciteturn2file14

The wiki’s “single‑filter selection/targeting” pages map directly onto these patterns. citeturn1search8turn1search9

---

## Activation Legality & Timing

- Targets must be **valid on resolution**, not only at activation.  
- Many effects are activatable even if they’ll **ultimately fail** (e.g., blocked by Necrovalley) — legality differs from success.  
- Use `EFFECT_FLAG_DELAY` for “If this card is sent…” style triggers to avoid missed timing.  

Authoritative timing rules: **Activation Legality**. citeturn1search2

Your scripts demonstrate correct timing with `EFFECT_FLAG_DELAY` and proper `SetHintTiming` usage on Quick effects. fileciteturn2file10

---

## Continuous Effects (STATE & FIELD)

Two common shapes:

1) **Field aura**: modifies ATK/DEF or rules for a range:
```lua
local e1=Effect.CreateEffect(c)
e1:SetType(EFFECT_TYPE_FIELD)
e1:SetCode(EFFECT_UPDATE_ATTACK)
e1:SetRange(LOCATION_MZONE)
e1:SetTargetRange(LOCATION_MZONE,0)
e1:SetValue(s.val)  -- often depends on game state
c:RegisterEffect(e1)
```
Examples in your set compute value from GY count or LP delta. fileciteturn2file3 fileciteturn2file7

2) **Continuous watchers**: `EFFECT_TYPE_FIELD+EFFECT_TYPE_CONTINUOUS` hooked to events like `EVENT_CHAINING`, `EVENT_SPSUMMON_SUCCESS`, etc., then run operations. fileciteturn2file9

The wiki’s “effects that apply continuously” and the tutorial cover these patterns. citeturn1search4turn1search5

---

## Activated Effects (Ignition, Quick, Trigger)

- **Ignition**: Main Phase actions (`EFFECT_TYPE_IGNITION`). Often use costs like “detach 1”. fileciteturn2file5  
- **Quick**: `EFFECT_TYPE_QUICK_O`, with `EVENT_FREE_CHAIN` (plus `SetHintTiming` appropriately). fileciteturn2file10  
- **Triggers**: `EFFECT_TYPE_SINGLE+EFFECT_TYPE_TRIGGER_O/F` on events (`EVENT_TO_GRAVE`, `EVENT_SUMMON_SUCCESS`, etc.), with `EFFECT_FLAG_DELAY` when needed. fileciteturn2file1

General guidance on the wiki’s Activated Effects page. citeturn1search6

---

## Methods that Affect Cards (Move/Destroy/Banish/etc.)

Common movers you’ll use (non‑exhaustive):  
`Duel.SendtoHand`, `Duel.SendtoGrave`, `Duel.SendtoDeck`, `Duel.Remove`, `Duel.Destroy`, `Duel.SpecialSummon`, `Duel.Overlay`, `Duel.Damage`, `Duel.Recover`. The wiki keeps a curated list and nuances (e.g., return‑to‑hand vs. add‑to‑hand). citeturn1search11

Your scripts show clean use of `Duel.SetOperationInfo` to announce what will happen, then perform the action in op. fileciteturn3file8

---

## Single‑Filter Selection & Targeting Patterns

**Selection (non‑target)**:
```lua
-- choose 1 from GY to overlay (non‑target)
local g=Duel.SelectMatchingCard(tp,aux.NecroValleyFilter(s.mtfilter),tp,LOCATION_GRAVE,0,1,1,nil,e)
if #g>0 then Duel.Overlay(c,g) end
```
Real example mirrors this for adding Xyz material from GY. fileciteturn2file8 citeturn1search8

**Targeting**:
```lua
e:SetProperty(EFFECT_FLAG_CARD_TARGET)

-- target()
Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_TODECK)
local g=Duel.SelectTarget(tp,s.tdfilter,tp,0,LOCATION_ONFIELD,1,1,nil)
Duel.SetOperationInfo(0,CATEGORY_TODECK,g,1,0,0)

-- operation()
local tc=Duel.GetFirstTarget()
if tc and tc:IsRelateToEffect(e) then
  Duel.SendtoDeck(tc,nil,SEQ_DECKTOP,REASON_EFFECT)
end
```
See your targeted topdeck/return patterns. fileciteturn3file9 citeturn1search9

---

## Affecting All Cards in a Group

Sometimes you compute a **group** and apply 1 action to all of them. Do not mark as targets unless they are selected as such.

```lua
local g=Duel.GetMatchingGroup(aux.TRUE,tp,0,LOCATION_ONFIELD,nil)
Duel.Destroy(g,REASON_EFFECT)
```
Example: “destroy all” using a group at op time. fileciteturn2file13 citeturn1search10

---

## Necrovalley Compatibility

- **Do not** use `aux.NecroValleyFilter` in `target()` legality checks.  
- **Do** wrap GY selections in **operation** with `aux.NecroValleyFilter`.  
- This ensures effects remain **activatable** even if they later fail under Necrovalley. citeturn1search2turn1search3

Your examples correctly wrap GY selects during resolution. fileciteturn2file8

---

## Common Koishi Patterns (with real examples)

### 1) Detach as Cost (Xyz)
```lua
function s.cost(e,tp,eg,ep,ev,re,r,rp,chk)
  if chk==0 then return e:GetHandler():CheckRemoveOverlayCard(tp,1,REASON_COST) end
  e:GetHandler():RemoveOverlayCard(tp,1,1,REASON_COST)
end
```
Used repeatedly across your scripts. fileciteturn2file5 fileciteturn2file1

### 2) Quick effect with hint timing
```lua
e:SetType(EFFECT_TYPE_QUICK_O)
e:SetCode(EVENT_FREE_CHAIN)
e:SetHintTiming(0,TIMINGS_CHECK_MONSTER) -- or +TIMING_END_PHASE, etc.
```
fileciteturn2file10

### 3) Optional trigger on “sent to GY” with DELAY
```lua
e:SetType(EFFECT_TYPE_SINGLE+EFFECT_TYPE_TRIGGER_O)
e:SetCode(EVENT_TO_GRAVE)
e:SetProperty(EFFECT_FLAG_DELAY)
```
fileciteturn2file1

### 4) Continuous aura ATK/DEF update by state
```lua
e1:SetType(EFFECT_TYPE_FIELD)
e1:SetCode(EFFECT_UPDATE_ATTACK)
e1:SetTargetRange(LOCATION_MZONE,0)
e1:SetValue(function(e,c) return Duel.GetFieldGroupCount(e:GetHandlerPlayer(),0,LOCATION_GRAVE)*100 end)
```
fileciteturn2file3

### 5) Multi‑mode choice (ATK or DEF +1000)
```lua
local opt=Duel.SelectOption(tp,aux.Stringid(id,2),aux.Stringid(id,3))
local e1=Effect.CreateEffect(c)
e1:SetType(EFFECT_TYPE_SINGLE)
e1:SetCode(opt==0 and EFFECT_UPDATE_ATTACK or EFFECT_UPDATE_DEFENSE)
e1:SetValue(1000)
c:RegisterEffect(e1)
```
fileciteturn2file19

### 6) “Destroy all” non‑target group op
See [Affecting All Cards in a Group](#affecting-all-cards-in-a-group). fileciteturn2file13

### 7) Overlay from GY (Necrovalley‑safe)
See [Selection (non‑target)](#single-filter-selection--targeting-patterns). fileciteturn2file8

### 8) Value based on LP difference or materials
Compute values dynamically with lambdas or helper functions; examples compute `abs(LP0-LP1)` or scale with overlay count. fileciteturn2file7 fileciteturn2file8

---

## FX Procedure Helpers (Ritual/Synchro/Xyz/Link/Fusion)

Use the **official helpers** from `procedure.lua` instead of hand‑coding summoning procedures:

- **Xyz**: `AddXyzProcedure(c, filter, rank, materials, ...)`  
- **Synchro**: `AddSynchroProcedure(...)`, `AddSynchroMixProcedure(...)`  
- **Link**: `AddLinkProcedure(c, f, min, max, gf)`  
- **Ritual**: `AddRitualProcEqual/Greater/...` family  
- **Fusion**: `AddFusionProc*` families, or build custom fusion conditions/goals

Your local `procedure.lua` exposes these with rich condition/target/operation helpers and label usage patterns. Prefer them over bespoke logic. fileciteturn2file12 fileciteturn3file17 fileciteturn3file13

---

## Authoring Checklist

- [ ] Start with `local s,id=GetID()` and keep helpers under `s.*`. fileciteturn3file0  
- [ ] Separate **condition / cost / target / operation** cleanly. fileciteturn2file6  
- [ ] Mark **targeting** effects with `EFFECT_FLAG_CARD_TARGET` and select targets in `target()`. citeturn1search9  
- [ ] Use `EFFECT_FLAG_DELAY` on optional triggers that can miss timing. citeturn1search6  
- [ ] Announce categories with `Duel.SetOperationInfo` where applicable. fileciteturn3file8  
- [ ] Wrap GY selections with `aux.NecroValleyFilter` **in operation**, not in target. citeturn1search2turn1search3  
- [ ] Prefer `procedure.lua` helpers for summoning procedures. fileciteturn2file12  
- [ ] For group‑wide effects, avoid marking as targets unless truly targeted. citeturn1search10  
- [ ] Always guard ops with `if not c:IsRelateToEffect(e) then return end`. (Common across your scripts.) fileciteturn2file18

---

## References

- **Main Page** — YGOPro Scripting Wiki. citeturn1search12  
- **Structure of a card script** (Koishi layout). citeturn1search0  
- **Effect type constants & templates**. citeturn1search1  
- **Functions for conditions, costs, activation, resolution**. citeturn1search14  
- **Activation Legality** (timing rules). citeturn1search2  
- **Filters & Groups** (handling Card/Group). citeturn1search3  
- **Continuous effects** + **tutorial**. citeturn1search4turn1search5  
- **Activated effects**. citeturn1search6  
- **Methods for affecting cards**. citeturn1search7  
- **Single‑filter selection / targeting**. citeturn1search8turn1search9  
- **Affecting all cards in a group**. citeturn1search10  
- **List of functions that move cards**. citeturn1search11

**Local sources cross‑checked:** `utility.lua`, `procedure.lua`, and dozens of real scripts in your `merged_cards.part*.json`. fileciteturn3file6 fileciteturn2file12 fileciteturn2file1 fileciteturn2file3 fileciteturn2file7 fileciteturn2file5
