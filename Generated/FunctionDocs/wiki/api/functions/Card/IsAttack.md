# Card.IsAttack

## Signature

```lua
Card.IsAttack(Card c, int atk1, [int atk2], [... int]) -> bool
```

## Description

检查c的攻击力是否是 atk1[, 或者为 atk2...]，如果c不是怪兽卡，或者不在 LOCATION_MZONE 则都返回false

## Parameters

- `c` `Card`
- `atk1` `int`
- `atk2` `int` optional
- `...` `int` optional

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3490`
