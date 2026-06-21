# Duel.SpecialSummon

## Signature

```lua
Duel.SpecialSummon(Card|Group targets, int sumtype, int sumplayer, int target_player, bool nocheck, bool nolimit, int pos, [int zone]) -> int
```

## Description

让玩家 sumplayer 以sumtype方式，pos表示形式把targets特殊召唤到target_player场上[的区域 zone]
如果nocheck为true则无视卡的召唤条件，如果nolimit为true则无视卡的苏生限制
返回值是特殊召唤成功的卡的数量

## Parameters

- `targets` `Card|Group`
- `sumtype` `int`
- `sumplayer` `int`
- `target_player` `int`
- `nocheck` `bool`
- `nolimit` `bool`
- `pos` `int`
- `zone` `int` optional - default: 0xff

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4873`
