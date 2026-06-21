# Card.IsNonAttribute

## Signature

```lua
Card.IsNonAttribute(Card c, int attribute) -> bool
```

## Description

检查c是否有attribute以外的属性
（如暗黑神鸟同时具有暗和风属性，not IsAttribute(暗)是false，但IsNonAttribute(暗)是true）

## Parameters

- `c` `Card`
- `attribute` `int`

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3497`
