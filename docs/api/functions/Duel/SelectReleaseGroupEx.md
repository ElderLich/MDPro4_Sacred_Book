# Duel.SelectReleaseGroupEx

## Signature

```lua
Duel.SelectReleaseGroupEx(int player, [function|nil f], int min, int max, int reason, bool use_hand, [Card|Group|nil ex], ... any) -> Group
```

## Description

Lets player select min to max cards that can be Tributed/Released for effect purposes, optionally excluding ex and applying filter f.

## Parameters

- `player` `int`
- `f` `function|nil` optional
- `min` `int`
- `max` `int`
- `reason` `int`
- `use_hand` `bool`
- `ex` `Card|Group|nil` optional
- `...` `any`

## Returns

- `Group`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4979`
