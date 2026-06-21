# Card.IsAbleToHandAsCost

## Signature

```lua
Card.IsAbleToHandAsCost(Card c) -> bool
```

## Description

检查c是否可以作为cost送去手卡
注：此函数会在Card.IsAbleToHand的基础上追加检测c的实际目的地
当c送往手卡会被送去其它地方时（如缩退回路适用中，或者c是融合、同调 等额外怪兽的一种），此函数返回false
##以下几个函数类似

## Parameters

- `c` `Card`

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3589`
