# Auxiliary.AddRitualProcEqual2

## Signature

```lua
Auxiliary.AddRitualProcEqual2(Card c, function filter, int summon_location, [function|nil grave_filter], [function|nil mat_filter], [bool pause], [function|nil extra_operation], [function|nil extra_target]) -> Effect
```

## Description

Registers an exact-Level Ritual Summon procedure using Card.GetLevel and returns the created Effect.

## Parameters

- `c` `Card`
- `filter` `function`
- `summon_location` `int`
- `grave_filter` `function|nil` optional
- `mat_filter` `function|nil` optional
- `pause` `bool` optional
- `extra_operation` `function|nil` optional
- `extra_target` `function|nil` optional

## Returns

- `Effect`

## Source

- `Utilities/procedure.lua:1922`
