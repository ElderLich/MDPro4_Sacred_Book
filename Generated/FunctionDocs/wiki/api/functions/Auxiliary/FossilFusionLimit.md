# Auxiliary.FossilFusionLimit

## Signature

```lua
Auxiliary.FossilFusionLimit(Effect e, Effect se, int sp, int st) -> bool
```

## Description

Special Summon restriction value for Fossil Fusion effects; allows Fossil Fusion's summon value, Fossil Fusion itself, or non-Extra Deck handlers.

## Parameters

- `e` `Effect`
- `se` `Effect`
- `sp` `int`
- `st` `int`

## Returns

- `bool` - true if the Summon matches Fossil Fusion conditions.

## Source

- `Utilities/procedure.lua:2327`
