# Duel.IsPlayerCanSummon

## Signature

```lua
Duel.IsPlayerCanSummon(int player, [int sumtype], [Card c]) -> bool
```

## Description

With only player, checks whether player is not forbidden from performing a Normal Summon by an untargeted EFFECT_CANNOT_SUMMON.
With sumtype and c, checks player EFFECT_CANNOT_SUMMON restrictions for Normal Summoning c with that sumtype. This binding does not check Summon count, costs, tribute availability, or zone availability.

## Parameters

- `player` `int`
- `sumtype` `int` optional
- `c` `Card` optional

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5047`
