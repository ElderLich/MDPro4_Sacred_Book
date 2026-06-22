# Duel.SwapSequence

## Signature

```lua
Duel.SwapSequence(Card c1, Card c2) -> void
```

## Description

Swaps the Monster Zone sequences of c1 and c2 when both are controlled by the same player, both are affected by the current reason effect, and both are in the Monster Zone.
The core raises move events for the swapped cards when the swap occurs.

## Parameters

- `c1` `Card`
- `c2` `Card`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4885`
