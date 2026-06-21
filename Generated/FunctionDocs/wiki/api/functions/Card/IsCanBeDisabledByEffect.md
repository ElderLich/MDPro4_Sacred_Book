# Card.IsCanBeDisabledByEffect

## Signature

```lua
Card.IsCanBeDisabledByEffect(Card c, Effect e, [bool isMonsterEffect]) -> bool
```

## Description

检查c的效果是否能被e无效。
已经被无效的卡，或原本就没有效果的卡，或不受e影响的卡不能被无效。
第三个参数可选，指示其是否为怪兽效果。

## Parameters

- `c` `Card`
- `e` `Effect`
- `isMonsterEffect` `bool` optional

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3647`
