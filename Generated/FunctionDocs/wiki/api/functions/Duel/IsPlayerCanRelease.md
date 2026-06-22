# Duel.IsPlayerCanRelease

## Signature

```lua
Duel.IsPlayerCanRelease(int player, [Card c], [int reason]) -> bool
```

## Description

Checks whether player can release cards at all, or whether player can release c for reason.
When c is supplied and reason is omitted, the core uses REASON_COST.

## Parameters

- `player` `int`
- `c` `Card` optional
- `reason` `int` optional - default: REASON_COST

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5054`
