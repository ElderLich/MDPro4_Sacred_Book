# Duel.Destroy

## Signature

```lua
Duel.Destroy(Card|Group targets, int reason, [int dest], [int reason_player]) -> int
```

## Description

Destroy targets dest by reason reason, the return value is actually destroyed by the number
If the reason contains REASON_RULE, the break event will not check whether the card is immune,
Does not trigger the generation of breaking effect and ignore the "can not destroy"

## Parameters

- `targets` `Card|Group`
- `reason` `int`
- `dest` `int` optional
- `reason_player` `int` optional

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4858`
