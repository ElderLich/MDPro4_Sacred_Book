# Duel.SelectMatchingCard

## Signature

```lua
Duel.SelectMatchingCard(int sel_player, [function|nil f], int player, int s, int o, int min, int max, [Card|Group|nil ex], ... any) -> Group
```

## Description

Lets sel_player choose min to max cards from the specified locations that satisfy filter f and are not excluded by ex.
s is player's own location mask and o is the opponent's location mask from that player's viewpoint. Extra arguments after ex are passed to f.

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

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4973`
