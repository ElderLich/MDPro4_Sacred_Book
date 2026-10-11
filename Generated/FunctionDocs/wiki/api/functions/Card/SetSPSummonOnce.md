# Card.SetSPSummonOnce

## Signature

```lua
Card.SetSPSummonOnce(Card c, int spsummon_code) -> void
```

## Description

Marks c as sharing a once-per-turn Special Summon limit under spsummon_code.
Cards with the same nonzero spsummon_code share the limit for each player. The binding does nothing while c is copying another card's effect.

## Parameters

- `c` `Card`
- `spsummon_code` `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3716`
