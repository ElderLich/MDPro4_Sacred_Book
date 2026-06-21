# Auxiliary.AddRitualProcGreater2Code2

## Signature

```lua
Auxiliary.AddRitualProcGreater2Code2(Card c, int code1, int code2, [int summon_location], [function|nil grave_filter], [function|nil mat_filter], [bool pause], [function|nil extra_operation], [function|nil extra_target]) -> Effect
```

## Description

Registers code1 and code2 as listed by c, then adds the Greater2 Ritual procedure restricted to Ritual Monsters with either code.

## Parameters

- `c` `Card`
- `code1` `int`
- `code2` `int`
- `summon_location` `int` optional
- `grave_filter` `function|nil` optional
- `mat_filter` `function|nil` optional
- `pause` `bool` optional
- `extra_operation` `function|nil` optional
- `extra_target` `function|nil` optional

## Returns

- `Effect` - The created Ritual Summon effect.

## Source

- `Utilities/procedure.lua:1941`
