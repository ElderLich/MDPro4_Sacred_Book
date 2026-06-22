# Auxiliary.dogcon

## Signature

```lua
Auxiliary.dogcon(Effect e, int tp, Group eg, int ep, int ev, Effect re, int r, int rp) -> bool
```

## Description

EVENT_TO_GRAVE condition helper that checks whether the handler was previously controlled by tp and destroyed by the opponent.

## Parameters

- `e` `Effect`
- `tp` `int`
- `eg` `Group`
- `ep` `int`
- `ev` `int`
- `re` `Effect`
- `r` `int`
- `rp` `int`

## Returns

- `bool`

## Source

- `Utilities/utility.lua:791`
