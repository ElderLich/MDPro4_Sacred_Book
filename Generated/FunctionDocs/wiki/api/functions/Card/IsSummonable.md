# Card.IsSummonable

## Signature

```lua
Card.IsSummonable(Card c, bool ignore_count, [Effect|nil e], [int min], [int zone]) -> bool
```

## Description

检查c是否可以进行通常召唤（不包含通常召唤的set)，ignore_count=true则不检查召唤次数限制
e~=nil则检查c是否可以以效果e进行通常召唤，min表示至少需要的祭品数（用于区分妥协召唤与上级召唤）,zone 表示必须要召唤到的区域

## Parameters

- `c` `Card`
- `ignore_count` `bool`
- `e` `Effect|nil` optional
- `min` `int` optional - default: 0
- `zone` `int` optional - default: 0x1f

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3579`
