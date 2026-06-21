# Auxiliary.DarkFusionLimit

## Signature

```lua
Auxiliary.DarkFusionLimit(Effect e, Effect se, int sp, int st) -> bool
```

## Description

Special Summon restriction value for Evil HERO/Dark Fusion effects; allows Dark Fusion itself, the Dark Fusion summon value, or Fusion Summons while the player is affected by effect code 72043279.

## Parameters

- `e` `Effect`
- `se` `Effect`
- `sp` `int`
- `st` `int`

## Returns

- `bool` - true if the Summon matches Dark Fusion conditions.

## Source

- `Utilities/procedure.lua:2321`
