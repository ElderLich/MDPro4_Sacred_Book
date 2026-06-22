# Duel.DiscardHand

## Signature

```lua
Duel.DiscardHand(int player, [function|nil f], int min, int max, int reason, [Card|Group|nil ex], ... any) -> int
```

## Description

Lets player choose and discard min to max matching cards from their hand for reason, then returns the number discarded.
Cards in ex are excluded. Extra arguments after ex are passed to filter f.

## Parameters

- `player` `int`
- `f` `function|nil` optional
- `min` `int`
- `max` `int`
- `reason` `int`
- `ex` `Card|Group|nil` optional
- `...` `any`

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4911`
