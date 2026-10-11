# Auxiliary.tgoval

## Signature

```lua
Auxiliary.tgoval(Effect e, Effect re, int rp) -> void
```

## Description

Shared value function for EFFECT_CANNOT_BE_EFFECT_TARGET effects that protect against the opponent's effects.
It returns true when the reason player rp is the opponent of e's handler player.

## Parameters

- `e` `Effect`
- `re` `Effect`
- `rp` `int`

## Source

- `Utilities/utility.lua:839`
