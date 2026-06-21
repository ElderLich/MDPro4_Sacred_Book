# Card.IsDiscardable

## Signature

```lua
Card.IsDiscardable(Card c, [int reason]) -> bool
```

## Description

检查c是否可以以reason原因丢弃
注：此函数仅用于检测，
以REASON_DISCARD作为原因把一张手卡送墓并不会导致那张卡不能丢弃

## Parameters

- `c` `Card`
- `reason` `int` optional - default: REASON_COST

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3597`
