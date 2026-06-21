# Duel.SendtoHand

## Signature

```lua
Duel.SendtoHand(Card|Group targets, [int|nil player], int reason, [int reason_player]) -> int
```

## Description

以reason原因把targets送去玩家player的手卡，返回值是实际被操作的数量
如果player是nil则返回卡的持有者的手卡
如果设置reason_player，则视为被玩家reason_player移动

## Parameters

- `targets` `Card|Group`
- `player` `int|nil` optional
- `reason` `int`
- `reason_player` `int` optional

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4861`
