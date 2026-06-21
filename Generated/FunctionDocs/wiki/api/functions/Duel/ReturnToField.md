# Duel.ReturnToField

## Signature

```lua
Duel.ReturnToField(Card c, [int pos], [int zone]) -> bool
```

## Description

把c以表示形式pos返回到场上[的区域 zone]，pos默认值是离场前的表示形式，返回值表示是否成功
c必须是以REASON_TEMPORARY原因离场，并且离场后没有离开过那个位置

## Parameters

- `c` `Card`
- `pos` `int` optional
- `zone` `int` optional - default: 0xff

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4883`
