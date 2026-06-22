# Auxiliary.AddFusionProcMix

## Signature

```lua
Auxiliary.AddFusionProcMix(Card fcard, bool sub, bool insf, ... int|function|table) -> void
```

## Description

Registers a fixed-count mixed Fusion Material procedure on fcard.
Each extra argument is a required material slot and may be a card code, filter function, or table of alternatives. Numeric material slots update listed-material metadata.

## Parameters

- `fcard` `Card`
- `sub` `bool`
- `insf` `bool`
- `...` `int|function|table`

## Source

- `Utilities/procedure.lua:862`
