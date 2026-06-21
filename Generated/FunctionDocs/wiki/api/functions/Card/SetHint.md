# Card.SetHint

## Signature

```lua
Card.SetHint(Card c, int type, int value) -> void
```

## Description

为c设置类型为type的卡片提示信息
type只能为以下值，对应的value类型为
CHINT_TURN              回合数
CHINT_CARD              卡片id
CHINT_RACE              种族
CHINT_ATTRIBUTE         属性
CHINT_NUMBER            数字
CHINT_DESC              描述

## Parameters

- `c` `Card`
- `type` `int`
- `value` `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3655`
