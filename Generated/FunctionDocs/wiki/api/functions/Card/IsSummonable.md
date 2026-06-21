# Card.IsSummonable

## Signature

```lua
Card.IsSummonable(Card c, bool ignore_count, [Effect|nil e], [int min], [int zone]) -> bool
```

## Description

Check whether c is usually called (not including the normally called set), ignore_count = true does not check the number of calls limit
E ~ = nil check whether c can be the effect of e is usually called, min said at least the number of sacrifice (used to distinguish between compromise summons and superior call)

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
