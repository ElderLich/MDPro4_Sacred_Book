# Duel.SelectTarget

## Signature

```lua
Duel.SelectTarget(int sel_player, [function|nil f], int player, int s, int o, int min, int max, [Card|Group|nil ex], ... any) -> Group
```

## Description

Filter function, so that player sel_player select the specified location to meet the filter condition f and not equal ex
And can be the min-max card of the object that is currently processing the effect
The ninth parameter starts as an extra parameter
This function sets the currently locked object to the selected card at the same time

## Parameters

- `sel_player` `int`
- `f` `function|nil` optional
- `player` `int`
- `s` `int`
- `o` `int`
- `min` `int`
- `max` `int`
- `ex` `Card|Group|nil` optional
- `...` `any`

## Returns

- `Group`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4986`
