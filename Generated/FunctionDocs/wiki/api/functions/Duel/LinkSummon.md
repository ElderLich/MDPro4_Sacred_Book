# Duel.LinkSummon

## Signature

```lua
Duel.LinkSummon(int player, Card c, Group|nil materials, [Card|nil lcard], [int minc], [int maxc]) -> void
```

## Description

Performs a rule Link Summon for player and c using an optional material group, fixed material, and min/max constraints.
Use this in effect operations after checking Card.IsLinkSummonable. The selected Link Monster's registered procedure still controls final material selection and sends materials to the GY.
The core rejects this during the Damage Step, yields while the Summon is processed, and returns no Lua value.

## Parameters

- `player` `int` - Player performing the Link Summon.
- `c` `Card` - Link Monster to Link Summon.
- `materials` `Group|nil` - Optional temporary material pool. nil uses the Link Monster's normal procedure pool.
- `lcard` `Card|nil` optional - Optional fixed material that must be included in the selected group.
- `minc` `int` optional - Runtime minimum material-card count. default: 0
- `maxc` `int` optional - Runtime maximum material-card count. default: 0

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4869`
