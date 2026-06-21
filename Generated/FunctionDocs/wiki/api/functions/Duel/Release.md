# Duel.Release

## Signature

```lua
Duel.Release(Card|Group targets, int reason, [int reason_player]) -> int
```

## Description

以reason原因解放targets ，返回值是实际解放的数量
如果reason含有REASON_COST，则不会检查卡片是否不受效果影响
如果设置reason_player，则视为被玩家reason_player移动

## Parameters

- `targets` `Card|Group`
- `reason` `int`
- `reason_player` `int` optional

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4881`
