# Duel.Recover

## Signature

```lua
Duel.Recover(int player, int value, int reason, [bool is_step]) -> int
```

## Description

To reason reason players to player value LP, return to the actual response value
The return value is 0 if it is affected by an effect such as a return to harm.
Is_step to true is the damage / recovery LP process decomposition, need to call Duel.RDComplete() trigger point

## Parameters

- `player` `int`
- `value` `int`
- `reason` `int`
- `is_step` `bool` optional - default: false

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4902`
