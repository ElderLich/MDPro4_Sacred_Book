# Duel.SetOperationInfo

## Signature

```lua
Duel.SetOperationInfo(int chainc, int category, [Card|Group|nil|0 targets], int count, int target_player, int target_param) -> void
```

## Description

Records operation information for category on chainc.
Use concrete targets and count when the affected cards are known. For unresolved non-targeting movement effects, pass nil targets with the expected count, target player, and target location.
This information is used by response checks such as Stardust Dragon-style effects.

## Parameters

- `chainc` `int`
- `category` `int`
- `targets` `Card|Group|nil|0` optional
- `count` `int`
- `target_player` `int`
- `target_param` `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5008`
