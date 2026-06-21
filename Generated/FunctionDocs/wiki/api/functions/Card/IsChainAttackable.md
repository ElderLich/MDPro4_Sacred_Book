# Card.IsChainAttackable

## Signature

```lua
Card.IsChainAttackable(Card c, [int ac], [bool monsteronly]) -> bool
```

## Description

检查c是否可以连续攻击，c的攻击宣言次数>=ac则返回false
monsteronly = true 则表示只能对怪兽攻击
注：当c因为闪光之双剑等效果进行过多次攻击之后此函数返回false

## Parameters

- `c` `Card`
- `ac` `int` optional
- `monsteronly` `bool` optional

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3599`
