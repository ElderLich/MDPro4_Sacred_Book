# Group.RandomSelect

## Signature

```lua
Group.RandomSelect(Group g, int player, int count) -> Group
```

## Description

Returns a new Group containing count randomly chosen cards from g.
count is clamped to g's size. The player argument is written to the random-selection message but does not influence the random choice.

## Parameters

- `g` `Group`
- `player` `int`
- `count` `int`

## Returns

- `Group`

## Source

- `D:\Programs\GitHub\ygopro-core\libgroup.cpp:917`
