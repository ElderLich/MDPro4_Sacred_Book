# Duel.GetFieldCard

## Signature

```lua
Duel.GetFieldCard(int player, int location, int seq) -> Card
```

## Description

返回玩家player的场上位于location序号为seq的卡，常用于获得场地区域·灵摆区域的卡
注：召唤·反转召唤·特殊召唤 之际 的卡无法获取

## Parameters

- `player` `int`
- `location` `int`
- `seq` `int`

## Returns

- `Card`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4943`
