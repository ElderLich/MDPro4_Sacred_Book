# Duel.GetLinkedGroup

## Signature

```lua
Duel.GetLinkedGroup(int player, int s_range, int o_range) -> Group
```

## Description

Return the group of linked cards in s_range and o_range zones from player's perspective [as long as the last two parameters are not 0, they become LOCATION_MZONE]
NOTE: The original description includes a question mark (?), indicating potential uncertainty or incomplete information; translated as written

## Parameters

- `player` `int`
- `s_range` `int`
- `o_range` `int`

## Returns

- `Group`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4940`
