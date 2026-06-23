# Auxiliary.PendOperation

## Signature

```lua
Auxiliary.PendOperation(Effect e, int tp, Group eg, int ep, int ev, Effect re, int r, int rp, Card c, Group sg, Group|nil og) -> void
```

## Description

Operation function for the shared Pendulum Summon procedure.
It chooses the regular or extra Pendulum Summon option, computes hand, Extra Deck, and total Monster Zone limits, selects a legal subgroup, updates the shared checklist or consumes the extra effect's count limit, and merges the selected cards into sg for the core group Summon path.

## Parameters

- `e` `Effect`
- `tp` `int`
- `eg` `Group`
- `ep` `int`
- `ev` `int`
- `re` `Effect`
- `r` `int`
- `rp` `int`
- `c` `Card` - Left Pendulum Zone card whose procedure is being used.
- `sg` `Group` - Core-provided group that receives the selected Pendulum Summon monsters.
- `og` `Group|nil` - Optional candidate group; nil rebuilds candidates from the player's hand and face-up Extra Deck.

## Source

- `Utilities/procedure.lua:2033`
