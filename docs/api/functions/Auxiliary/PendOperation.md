# Auxiliary.PendOperation

## Signature

```lua
Auxiliary.PendOperation(Effect e, int tp, Group eg, int ep, int ev, Effect re, int r, int rp, Card c, Group sg, Group|nil og) -> void
```

## Description

Operation function for the shared Pendulum Summon procedure. It chooses the regular or extra Pendulum Summon effect, selects monsters within hand/Extra Deck zone limits, updates the checklist, and merges the selection into sg.

## Parameters

- `e` `Effect`
- `tp` `int`
- `eg` `Group`
- `ep` `int`
- `ev` `int`
- `re` `Effect`
- `r` `int`
- `rp` `int`
- `c` `Card`
- `sg` `Group`
- `og` `Group|nil`

## Source

- `Utilities/procedure.lua:2033`
