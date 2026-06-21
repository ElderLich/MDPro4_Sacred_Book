# Auxiliary.EnableChangeCode

## Signature

```lua
Auxiliary.EnableChangeCode(Card c, int code, int location, function condition) -> void
```

## Description

Registers code as a listed code for c and gives c an EFFECT_CHANGE_CODE effect with that value.
If location is omitted, monsters use the Monster Zone and non-monsters use the Spell & Trap Zone. If condition is omitted, the code change is always active.

## Parameters

- `c` `Card`
- `code` `int`
- `location` `int`
- `condition` `function`

## Source

- `Utilities/utility.lua:433`
