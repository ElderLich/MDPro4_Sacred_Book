# Auxiliary.AddLinkProcedure

## Signature

```lua
Auxiliary.AddLinkProcedure(Card c, [function|nil f], int min, [int max], [function gf]) -> Effect
```

## Description

Registers the standard Link Summon procedure for c and returns the created Effect.
f filters materials, min/max constrain the material count, and gf optionally checks the selected material group.

## Parameters

- `c` `Card`
- `f` `function|nil` optional
- `min` `int`
- `max` `int` optional
- `gf` `function` optional

## Returns

- `Effect`

## Source

- `Utilities/procedure.lua:2128`
