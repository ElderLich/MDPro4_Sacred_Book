# Auxiliary.AddSynchroProcedure

## Signature

```lua
Auxiliary.AddSynchroProcedure(Card c, [function|nil f1], [function|nil f2], int minc, [int maxc]) -> void
```

## Description

Registers the standard Synchro Summon procedure for c.
f1 filters the Tuner material, f2 filters non-Tuner materials, and minc/maxc set the number of non-Tuner materials required.
The created procedure lives in the Extra Deck, checks materials through the core Synchro helpers, stores the selected group for the operation, and sends materials to the GY with REASON_MATERIAL+REASON_SYNCHRO.

## Parameters

- `c` `Card` - Synchro Monster that receives the procedure.
- `f1` `function|nil` optional - Optional Tuner filter. nil accepts any legal Tuner.
- `f2` `function|nil` optional - Optional non-Tuner filter, commonly built with Auxiliary.NonTuner.
- `minc` `int` - Minimum number of non-Tuner materials.
- `maxc` `int` optional - Maximum number of non-Tuner materials. If omitted, the helper caps it by c's Level minus 1.

## Source

- `Utilities/procedure.lua:60`
