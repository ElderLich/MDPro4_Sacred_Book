# Card.IsRelateToChain

## Signature

```lua
Card.IsRelateToChain(Card c, [int chainc]) -> bool
```

## Description

检查c是否和连锁chainc有联系
注：每次发动进入连锁的效果时，发动效果的卡，以及发动效果时指定的对象
（用Duel.SetTargetCard或者Duel.SelectTarget指定的，包括取对象和不取对象）
会自动与那个效果建立联系，一旦离场，联系会重置

## Parameters

- `c` `Card`
- `chainc` `int` optional - default: 0

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3563`
