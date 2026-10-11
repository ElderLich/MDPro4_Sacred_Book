# Duel.SpecialSummonRule

## Signature

```lua
Duel.SpecialSummonRule(int player, Card c, [int sumtype]) -> void
```

## Description

Performs a rule Special Summon of c for player with optional summon type sumtype, unless the core is in effect damage step processing.
Most ordinary card scripts register an EFFECT_SPSUMMON_PROC instead of calling this directly. Prefer the established procedure helpers unless a local script pattern specifically needs this core entry point.

## Parameters

- `player` `int` - Player performing the rule Special Summon.
- `c` `Card` - Card to Special Summon by rule.
- `sumtype` `int` optional - Summon type value recorded for the rule Summon; default: 0.

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4866`

## Guided Examples

Learn how to use this function in context:

- [Special Summon-Only Monster Guide](/learn/special-summon-only-monsters)

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

No indexed local card script currently calls this function.

This can mean the function is unused in the current script set, is only called through an alias, or is available for future/manual scripts.
