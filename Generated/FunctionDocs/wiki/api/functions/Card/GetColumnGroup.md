# Card.GetColumnGroup

## Signature

```lua
Card.GetColumnGroup(Card c, [int left], [int right]) -> Group
```

## Description

返回与c同一纵列的c以外的卡片组，后2个参数会计算卡片c左边 left 列 和右边 right 列的所有卡，
比如c在中间的格子，那么 c:GetColumnGroup(2,2) 就相当于获取了除场地魔法以外的 场上的所有卡

## Parameters

- `c` `Card`
- `left` `int` optional - default: 0
- `right` `int` optional - default: 0

## Returns

- `Group`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3427`
