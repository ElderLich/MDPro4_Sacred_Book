# Duel.GetTargetCount

## Signature

```lua
Duel.GetTargetCount(function|nil filter, int player, int location1, int location2, Card|Group|nil exception, [... any]) -> int
```

## Description

Counts cards matching filter in the given field locations that can be used as effect targets, excluding exception when supplied.

## Parameters

- `filter` `function|nil`
- `player` `int`
- `location1` `int`
- `location2` `int`
- `exception` `Card|Group|nil`
- `...` `any` optional

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4984`
