# Duel.XyzSummon

## Signature

```lua
Duel.XyzSummon(int player, Card c, [Group|nil materials], [int minc], [int maxc]) -> void
```

## Description

Performs a rule Xyz Summon for player and c using an optional material group and min/max constraints.
Use this in effect operations after checking Card.IsXyzSummonable. The selected Xyz Monster's registered procedure still controls final material legality and overlaying.
The core rejects this during the Damage Step, yields while the summon is processed, and returns no Lua value.

## Parameters

- `player` `int` - Player performing the Xyz Summon.
- `c` `Card` - Xyz Monster to Summon.
- `materials` `Group|nil` optional - Optional material group supplied by the effect.
- `minc` `int` optional - Optional minimum material count override. Defaults to 0.
- `maxc` `int` optional - Optional maximum material count override. Defaults to 0.

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4868`
