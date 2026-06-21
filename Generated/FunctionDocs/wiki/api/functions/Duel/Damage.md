# Duel.Damage

## Signature

```lua
Duel.Damage(int player, int value, int reason, [bool is_step]) -> int
```

## Description

To the reason reason to give players the player caused value damage, the actual value of the damage received
The return value is 0 if the damage becomes an effect such as a reply.
Is_step to true is the damage / recovery LP process decomposition, need to call Duel.RDComplete() trigger point

## Parameters

- `player` `int`
- `value` `int`
- `reason` `int`
- `is_step` `bool` optional - default: false

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4901`
