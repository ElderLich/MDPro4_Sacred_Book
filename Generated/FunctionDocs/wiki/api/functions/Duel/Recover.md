# Duel.Recover

## Signature

```lua
Duel.Recover(int player, int value, int reason, [bool is_step]) -> int
```

## Description

Gives player LP for reason and returns the amount processed.
Effects can reverse recovery into damage. With is_step=true, finish the damage/recovery batch with Duel.RDComplete.

## Parameters

- `player` `int`
- `value` `int`
- `reason` `int`
- `is_step` `bool` optional - default: false

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4902`
