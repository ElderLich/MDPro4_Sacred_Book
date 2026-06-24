# Auxiliary.MulcharmyGlobalCheck

## Signature

```lua
Auxiliary.MulcharmyGlobalCheck(Effect e, int tp, Group eg, int ep, int ev, Effect re, int r, int rp) -> void
```

## Description

Internal EVENT_CHAINING operation installed by Auxiliary.EnableMulcharmyGlobalCheck.
When the triggering effect is a monster effect whose handler is in set 0x1b2, it registers player flag 84192580 on the activating player until the End Phase.
Card scripts should call Auxiliary.EnableMulcharmyGlobalCheck instead of registering this operation directly.

## Parameters

- `e` `Effect` - The global continuous effect that received EVENT_CHAINING.
- `tp` `int` - Controller of the global effect. This helper uses rp for the activating player.
- `eg` `Group` - Event group supplied by EVENT_CHAINING.
- `ep` `int` - Event player supplied by EVENT_CHAINING.
- `ev` `int` - Event value supplied by EVENT_CHAINING.
- `re` `Effect` - The effect being activated in the Chain.
- `r` `int` - Reason flags supplied by EVENT_CHAINING.
- `rp` `int` - Player who activated re; this player receives flag 84192580 when the Mulcharmy check matches.

## Source

- `Utilities/utility.lua:2050`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

No indexed local card script currently calls this function.

This can mean the function is unused in the current script set, is only called through an alias, or is available for future/manual scripts.
