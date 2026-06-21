# Duel.SendtoExtraP

## Signature

```lua
Duel.SendtoExtraP(Card|Group targets, [int|nil player], int reason) -> int
```

## Description

以reason原因把灵摆卡targets表侧表示送去玩家player的额外卡组，返回值是实际被操作的数量
如果player是nil则返回卡的持有者的额外卡组

## Parameters

- `targets` `Card|Group`
- `player` `int|nil` optional
- `reason` `int`

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4863`
