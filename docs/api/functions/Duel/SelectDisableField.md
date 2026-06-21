# Duel.SelectDisableField

## Signature

```lua
Duel.SelectDisableField(int player, int count, int s, int o, int filter) -> int
```

## Description

Let the player player select the specified position to meet the marker condition filter count of the available space, and return to select the location of the marker
Commonly used to select areas can not use or move the monster grid
0: 16) + (l [i] == LOCATION_MZONE? 0: 8)) ## flag|= 1 << (seq [i] + (p [i] == player?

## Parameters

- `player` `int`
- `count` `int`
- `s` `int`
- `o` `int`
- `filter` `int`

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5028`
