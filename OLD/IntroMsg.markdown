Always speak in English
# 🔧 Yu-Gi-Oh! YGOPro Scripting Project Brief

## 🎯 Purpose
Build a **definitive Lua scripting knowledge base** for creating custom Yu-Gi-Oh! cards in EDOPro, ensuring compatibility, modularity, and adherence to Koishi-style best practices. The central reference is `ScriptingWiki.md`, which guides all scripting tasks with standardized patterns and function usage.

---

## 📁 Provided Resources
### 🃏 Card Database (`merged_cards.part*.json`)
- **Fields**: `id`, `name`, `desc` (effect text, source of truth), `strings` (prompts), `script` (Lua code), `script_path`.
- **Usage**: Use `desc` for effect accuracy, cross-check with `script` for examples.

### ⚙️ Core Engine Files
- **`constant.lua`**: Defines locations (`LOCATION_MZONE`), types (`TYPE_FUSION`), timings (`TIMING_TOGRAVE`), etc.
- **`procedure.lua`**: Summon procedure helpers (e.g., `aux.AddFusionProcMix`, `aux.AddSynchroProcedure`).
- **`utility.lua`**: Helper functions (e.g., `GetID()`, `aux.NecroValleyFilter`, `aux.Stringid`).

### 📖 Documentation
- **`ScriptingWiki.md`**: Comprehensive Koishi-style guide with function reference, patterns, and best practices.

---

## 🧩 How to Use
When requesting:
- **“Script this card”**: I’ll use `desc` from `merged_cards`, apply Koishi-style patterns, and leverage `procedure.lua` helpers.
- **“Fix this effect”**: I’ll debug using `ScriptingWiki.md` and validate against EDOPro functions.
- **“Why doesn’t this trigger?”**: I’ll trace timing (`EVENT_*`, `TIMING_*`) and components (`condition`, `cost`, `target`, `operation`).

---

## 💡 Code Style Guide
- **Header**: `local s,id,o=GetID()` with `s.*` namespace.
- **Effect Structure**: Separate `condition`, `cost`, `target`, `operation` with clear comments.
> * Each effect must be separated into **sections** with:
>
>   ```lua
>   --====================
>   -- Effect X: [short description]
>   --====================
>   ```
- **Group helper functions under their own section with spacing between them.**
- **Best Practices**:
  - Use `Duel.SetOperationInfo` in `target`.
  - Guard with `if not c:IsRelateToEffect(e) then return end`.
  - Apply `aux.NecroValleyFilter` in `operation` for Graveyard effects.
  - Use `EFFECT_COUNT_CODE_OATH` for hard once-per-turn.
  - Prefer `procedure.lua` helpers for summoning.
* Make sure each condition, cost, target, and operation are separated clearly.

---

## 🧠 Features Supported
- **Complex Effects**: Contact Fusion, material uniqueness, Necrovalley legality, revival/float effects.
- **Timing**: `EFFECT_FLAG_DELAY` for optional triggers, `SetHintTiming` for Quick Effects.
- **Debugging**: Trace components, use `Debug.Message`, validate with `merged_cards` examples.

---

## 📌 Request Examples
- **Script a card**: Provide card ID or effect text.
- **Debug an issue**: Share the script and issue (e.g., “Effect doesn’t trigger in GY”).
- **Add functions**: Submit more documentation for translation or integration.
- **Custom format**: Request CSV output or specific markers (e.g., `Status: OK`).