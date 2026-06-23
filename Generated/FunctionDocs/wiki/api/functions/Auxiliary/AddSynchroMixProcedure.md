# Auxiliary.AddSynchroMixProcedure

## Signature

```lua
Auxiliary.AddSynchroMixProcedure(Card c, function|nil f1, function|nil f2, function|nil f3, function|nil f4, int minc, int maxc, [function gc]) -> void
```

## Description

Registers a mixed Synchro Summon procedure requiring up to three fixed material filters plus f4 repeated between minc and maxc times.
The helper creates an Extra Deck EFFECT_SPSUMMON_PROC with SUMMON_TYPE_SYNCHRO, checks the exact Synchro Level total, and handles mandatory material, hand Synchro, tuner-limit, and optional group-check rules.
The maximum count is capped by c's Level after subtracting any required fixed materials.

## Parameters

- `c` `Card`
- `f1` `function|nil`
- `f2` `function|nil`
- `f3` `function|nil`
- `f4` `function|nil`
- `minc` `int`
- `maxc` `int`
- `gc` `function` optional

## Source

- `Utilities/procedure.lua:135`
