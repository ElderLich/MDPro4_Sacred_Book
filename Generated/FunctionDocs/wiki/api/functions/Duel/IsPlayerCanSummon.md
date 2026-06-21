# Duel.IsPlayerCanSummon

## Signature

```lua
Duel.IsPlayerCanSummon(int player, [int sumtype], [Card c]) -> bool
```

## Description

Check player player can usually call [c, to sumtype]
If optional parameters are required, they must all be used
Returns false only if the player receives an effect such as "can not summon a superordinate"

## Parameters

- `player` `int`
- `sumtype` `int` optional
- `c` `Card` optional

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5047`
