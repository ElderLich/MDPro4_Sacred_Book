# Card.IsSSetable

## Signature

```lua
Card.IsSSetable(Card c, [bool ignore_field]) -> bool
```

## Description

检查c是否可以set到魔法陷阱区，ignore_field=true则无视魔陷区格子是否能使用的限制

## Parameters

- `c` `Card`
- `ignore_field` `bool` optional - default: false

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3581`
