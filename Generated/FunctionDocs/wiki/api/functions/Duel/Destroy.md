# Duel.Destroy

## Signature

```lua
Duel.Destroy(Card|Group targets, int reason, [int dest], [int reason_player]) -> int
```

## Description

以reason原因破坏targets去dest，返回值是实际被破坏的数量
如果reason包含REASON_RULE，则破坏事件将不会检查卡片是否免疫效果，
不会触发代破效果并且无视“不能破坏”
如果设置reason_player，则视为被玩家reason_player移动

## Parameters

- `targets` `Card|Group`
- `reason` `int`
- `dest` `int` optional
- `reason_player` `int` optional

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4858`
