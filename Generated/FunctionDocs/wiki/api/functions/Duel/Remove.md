# Duel.Remove

## Signature

```lua
Duel.Remove(Card|Group targets, int pos, int reason, [int reason_player]) -> int
```

## Description

以reason原因，pos表示形式除外targets，返回值是实际被操作的数量
如果reason包含REASON_TEMPORARY，那么视为是暂时除外，可以通过Duel.ReturnToField返回到场上
如果设置reason_player，则视为被玩家reason_player移动

## Parameters

- `targets` `Card|Group`
- `pos` `int`
- `reason` `int`
- `reason_player` `int` optional

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4859`
