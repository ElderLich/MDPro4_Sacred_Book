# Duel.SelectTribute

## Signature

```lua
Duel.SelectTribute(int player, Card c, int min, int max, [Group|nil mg], [int toplayer]) -> Group
```

## Description

Lets player select min to max Tribute candidates for Normal Summoning or Setting c and returns the selected Group.
mg can restrict the candidate pool. toplayer defaults to player; when toplayer differs, the core builds the extra release list for Tributing to that player's field.

## Parameters

- `player` `int`
- `c` `Card`
- `min` `int`
- `max` `int`
- `mg` `Group|nil` optional
- `toplayer` `int` optional - default: player

## Returns

- `Group`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4983`
