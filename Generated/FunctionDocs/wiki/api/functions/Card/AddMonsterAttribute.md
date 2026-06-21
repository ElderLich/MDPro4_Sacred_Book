# Card.AddMonsterAttribute

## Signature

```lua
Card.AddMonsterAttribute(Card c, int type, [int attribute], [int race], [int level], [int atk], [int def]) -> void
```

## Description

为魔陷卡c添加怪兽数值,type 为怪兽类型，不能是没有等级的怪兽
注：在数据库中有记录的数值视为原本数值

## Parameters

- `c` `Card`
- `type` `int`
- `attribute` `int` optional
- `race` `int` optional
- `level` `int` optional
- `atk` `int` optional
- `def` `int` optional

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3650`
