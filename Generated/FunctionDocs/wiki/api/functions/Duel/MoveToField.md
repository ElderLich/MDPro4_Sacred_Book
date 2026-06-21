# Duel.MoveToField

## Signature

```lua
Duel.MoveToField(Card c, int move_player, int target_player, int dest, int pos, bool enable, [int zone]) -> bool
```

## Description

让玩家move_player把c移动的target_player的场上，返回值表示是否成功
dest只能是LOCATION_MZONE或者LOCATION_SZONE，pos表示可选表示形式， enable 表示是否立刻适用c的效果

## Parameters

- `c` `Card`
- `move_player` `int`
- `target_player` `int`
- `dest` `int`
- `pos` `int`
- `enable` `bool`
- `zone` `int` optional

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4882`
