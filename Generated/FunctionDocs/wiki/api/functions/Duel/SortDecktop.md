# Duel.SortDecktop

## Signature

```lua
Duel.SortDecktop(int sort_player, int target_player, int count) -> void
```

## Description

让玩家sort_player对玩家target_player的卡组最上方count张卡进行排序，最先选的卡在最上面，然后下面是第二张选择的卡，以此类推
最多只能排序16张卡

## Parameters

- `sort_player` `int`
- `target_player` `int`
- `count` `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4893`
