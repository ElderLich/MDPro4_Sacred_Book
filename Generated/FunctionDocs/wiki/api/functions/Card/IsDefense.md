# Card.IsDefense

## Signature

```lua
Card.IsDefense(Card c, int def, [int atk2], [... int]) -> bool
```

## Description

检查c的守备力是否是 def1[, 或者为 def2...]，如果c不是怪兽卡，或者不在 LOCATION_MZONE 则都返回false

## Parameters

- `c` `Card`
- `def` `int`
- `atk2` `int` optional
- `...` `int` optional

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3491`
