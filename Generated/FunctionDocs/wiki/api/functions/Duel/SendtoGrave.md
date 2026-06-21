# Duel.SendtoGrave

## Signature

```lua
Duel.SendtoGrave(Card|Group targets, int reason, [int reason_player]) -> int
```

## Description

以reason原因把targets送去墓地，返回值是实际被操作的数量
如果设置reason_player，则视为被玩家reason_player移动

## Parameters

- `targets` `Card|Group`
- `reason` `int`
- `reason_player` `int` optional

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4860`
