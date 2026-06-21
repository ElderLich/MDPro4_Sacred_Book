# Auxiliary.DrytronSpSummonLimit

## Signature

```lua
Auxiliary.DrytronSpSummonLimit(Effect e, Card c, int sump, int sumtype, int sumpos, int targetp, Effect se) -> void
```

## Description

Oath target for the shared Drytron cost; it prevents Special Summoning monsters that can be Normal Summoned/Set, excluding cards whose original type is Spell/Trap or Trap Monster.

## Parameters

- `e` `Effect`
- `c` `Card`
- `sump` `int`
- `sumtype` `int`
- `sumpos` `int`
- `targetp` `int`
- `se` `Effect`

## Source

- `Utilities/utility.lua:1054`
