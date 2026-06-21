# Group.FilterSelect

## Signature

```lua
Group.FilterSelect(Group g, int player, function f, int min, int max, [Card|Group|nil ex], ... any) -> Group
```

## Description

Filter function, allowing players to choose from the g player min-max sheets meet the screening conditions f and not equal to the ex card
Starting with the 7th argument is an additional parameter

## Parameters

- `g` `Group`
- `player` `int`
- `f` `function`
- `min` `int`
- `max` `int`
- `ex` `Card|Group|nil` optional
- `...` `any`

## Returns

- `Group`

## Source

- `D:\Programs\GitHub\ygopro-core\libgroup.cpp:914`
