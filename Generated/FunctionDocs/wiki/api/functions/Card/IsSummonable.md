# Card.IsSummonable

## Signature

```lua
Card.IsSummonable(Card c, bool ignore_count, [Effect|nil e], [int min], [int zone]) -> bool
```

## Description

Checks whether c can be Normal Summoned, excluding Normal Summon/Set.
If e is not nil, checks whether c can be Normal Summoned by that effect. min is the minimum number of Tributes, and zone restricts the zone it must be Summoned to.

## Parameters

- `c` `Card`
- `ignore_count` `bool`
- `e` `Effect|nil` optional
- `min` `int` optional - default: 0
- `zone` `int` optional - default: 0x1f

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3634`
