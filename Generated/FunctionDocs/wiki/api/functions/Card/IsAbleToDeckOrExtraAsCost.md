# Card.IsAbleToDeckOrExtraAsCost

## Signature

```lua
Card.IsAbleToDeckOrExtraAsCost(Card c) -> bool
```

## Description

检查c是否可以作为cost送去卡组或额外卡组（用于新宇侠、剑斗兽融合怪兽的召唤手续检测）等价于 (c:IsAbleToDeckAsCost() or c:IsAbleToExtraAsCost())

## Parameters

- `c` `Card`

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3592`
