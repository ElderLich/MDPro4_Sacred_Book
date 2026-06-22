# Duel.SelectReleaseGroup

## Signature

```lua
Duel.SelectReleaseGroup(int sel_player, [function|nil f], int min, int max, [Card|Group|nil ex], ... any) -> Group
```

## Description

Lets player select min to max releasable cards matching f, excluding ex, and returns the selected Group.
Extra arguments after ex are passed to f after the Card argument.

## Parameters

- `sel_player` `int`
- `f` `function|nil` optional
- `min` `int`
- `max` `int`
- `ex` `Card|Group|nil` optional
- `...` `any`

## Returns

- `Group`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4977`
