# Card.IsLinkSummonable

## Signature

```lua
Card.IsLinkSummonable(Card c, [Group|nil mg], [int min], [int max]) -> bool
```

## Description

检查是否可以在场上的卡[或mg][中选出 min-max 个连接素材]对c进行连接召唤手续
如果mg为nil，此函数与 c:IsSpecialSummonable(SUMMON_TYPE_LINK)作用相同

## Parameters

- `c` `Card`
- `mg` `Group|nil` optional
- `min` `int` optional - default: 0
- `max` `int` optional - default: 0

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3578`
