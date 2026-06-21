# Card.GetColumnZone

## Signature

```lua
Card.GetColumnZone(Card c, int location, [int left], [int right], [int player]) -> int
```

## Description

返回[以 player 来看的] location 范围内与 c 同一纵列[包含左边 left 列和右边 right 列]的区域，
location 的值是 LOCATION_MZONE,LOCATION_SZONE,LOCATIOIN_ONFIELD

## Parameters

- `c` `Card`
- `location` `int`
- `left` `int` optional
- `right` `int` optional
- `player` `int` optional

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3429`
