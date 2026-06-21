# Duel.SynchroSummon

## Signature

```lua
Duel.SynchroSummon(int player, Card c, [Card|nil tuner], [Group|nil mg], [int minc], [int maxc]) -> void
```

## Description

让玩家player以tuner作为调整,场上的卡[或mg]为素材，对c进行同调召唤手续

## Parameters

- `player` `int`
- `c` `Card`
- `tuner` `Card|nil` optional
- `mg` `Group|nil` optional
- `minc` `int` optional - default: 0
- `maxc` `int` optional - default: 0

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4867`
