# Duel.SendtoDeck

## Signature

```lua
Duel.SendtoDeck(Card|Group targets, [int|nil player], int seq, int reason, [int reason_player], [bool send_activating]) -> int
```

## Description

以reason原因把targets送去玩家player的卡组，返回值是实际被操作的数量
如果player是nil则返回卡的持有者的卡组
如果seq=0，则是返回卡组最顶端；seq=1则是返回卡组最底端；
其余情况则是返回最顶端并且标记需要洗卡组
如果设置reason_player，则视为被玩家reason_player移动
如果设置send_activating，则可以移动发动中的魔法陷阱卡

## Parameters

- `targets` `Card|Group`
- `player` `int|nil` optional
- `seq` `int`
- `reason` `int`
- `reason_player` `int` optional
- `send_activating` `bool` optional

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4862`
