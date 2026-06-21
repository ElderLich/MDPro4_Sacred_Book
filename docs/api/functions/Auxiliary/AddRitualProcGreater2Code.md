# Auxiliary.AddRitualProcGreater2Code

## Signature

```lua
Auxiliary.AddRitualProcGreater2Code(Card c, int code1, [int summon_location], [function|nil grave_filter], [function|nil mat_filter], [bool pause], [function|nil extra_operation], [function|nil extra_target]) -> Effect
```

## Description

Registers code1 as listed by c, then adds the Greater2 Ritual procedure restricted to Ritual Monsters with that code.

## Parameters

- `c` `Card`
- `code1` `int`
- `summon_location` `int` optional
- `grave_filter` `function|nil` optional
- `mat_filter` `function|nil` optional
- `pause` `bool` optional
- `extra_operation` `function|nil` optional
- `extra_target` `function|nil` optional

## Returns

- `Effect` - The created Ritual Summon effect.

## Source

- `Utilities/procedure.lua:1937`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

No indexed local card script currently calls this function.

This can mean the function is unused in the current script set, is only called through an alias, or is available for future/manual scripts.
