# Auxiliary.FShaddollExFilter

## Signature

```lua
Auxiliary.FShaddollExFilter(Card c, Card fc, int attr, Effect fe) -> bool
```

## Description

Opponent-field Shaddoll Fusion Material filter used with effect code 81788994; c must be face-up, affected by the field effect, and pass the standard Shaddoll material filter.

## Parameters

- `c` `Card`
- `fc` `Card`
- `attr` `int`
- `fe` `Effect`

## Returns

- `bool` - true if c is a valid opponent-field Shaddoll Fusion Material.

## Source

- `Utilities/procedure.lua:1354`
