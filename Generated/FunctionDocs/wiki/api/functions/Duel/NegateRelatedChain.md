# Duel.NegateRelatedChain

## Signature

```lua
Duel.NegateRelatedChain(Card c, int reset_flag) -> void
```

## Description

For each current Chain Link whose triggering effect is handled by c and still related to c, registers a temporary EFFECT_DISABLE_CHAIN effect on c.
The generated disable effect resets with RESET_CHAIN, RESET_EVENT, and the supplied reset flags. The core does nothing if there is no earlier Chain Link to disable or if c is unaffected by the resolving effect.

## Parameters

- `c` `Card`
- `reset_flag` `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4931`
