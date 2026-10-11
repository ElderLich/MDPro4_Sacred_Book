# Card.IsMSetable

## Signature

```lua
Card.IsMSetable(Card c, bool ignore_count, [Effect|nil e], [int min], [int zone]) -> bool
```

## Description

Checks whether c can be Normal Set in a Monster Zone for the current reason player.
ignore_count skips the Normal Summon/Set count check. e checks Set legality for that effect, min is the minimum number of releases required, and zone restricts usable Monster Zones.

## Parameters

- `c` `Card`
- `ignore_count` `bool`
- `e` `Effect|nil` optional
- `min` `int` optional - default: 0
- `zone` `int` optional - default: 0x1f

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3635`
