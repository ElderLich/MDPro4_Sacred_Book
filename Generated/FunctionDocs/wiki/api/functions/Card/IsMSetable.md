# Card.IsMSetable

## Signature

```lua
Card.IsMSetable(Card c, bool ignore_count, [Effect|nil e], [int min], [int zone]) -> bool
```

## Description

Check whether c can be normally called set, ignore_count = true does not check the number of calls limit
E ~ = nil then check whether c can be the effect of e is usually called set, min that at least the number of sacrifices needed (used to distinguish between compromise summoned set and superior summoned set)

## Parameters

- `c` `Card`
- `ignore_count` `bool`
- `e` `Effect|nil` optional
- `min` `int` optional - default: 0
- `zone` `int` optional - default: 0x1f

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3580`
