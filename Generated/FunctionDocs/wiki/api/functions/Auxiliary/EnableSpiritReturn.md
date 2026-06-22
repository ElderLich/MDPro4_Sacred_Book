# Auxiliary.EnableSpiritReturn

## Signature

```lua
Auxiliary.EnableSpiritReturn(Card c, int event1, [... int]) -> void
```

## Description

Registers Spirit return setup for c.
When any listed event happens, it creates End Phase return-to-hand effects in the Monster Zone, respecting EFFECT_SPIRIT_DONOT_RETURN and EFFECT_SPIRIT_MAYNOT_RETURN.

## Parameters

- `c` `Card`
- `event1` `int`
- `...` `int` optional

## Source

- `Utilities/utility.lua:167`
