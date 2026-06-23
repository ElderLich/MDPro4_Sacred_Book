# Duel.IsCanAddCounter

## Signature

```lua
Duel.IsCanAddCounter(int player, [int countertype], [int count], [Card c]) -> bool
```

## Description

With only player, checks whether player is not forbidden from placing counters.
With countertype, count, and c, checks player-wide counter placement restrictions for that card target. It does not replace Card.IsCanAddCounter; use the Card check when you need to confirm the card's permit, face-up state, location, and counter limit.

## Parameters

- `player` `int` - Player attempting to place counters.
- `countertype` `int` optional - Counter type to test when the card-target overload is used.
- `count` `int` optional - Number of counters to test when the card-target overload is used.
- `c` `Card` optional - Card target passed to player-level counter-placement restriction effects.

## Returns

- `bool` - true when the player-level placement check passes; this does not by itself prove c can hold or receive the counters.

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4876`
