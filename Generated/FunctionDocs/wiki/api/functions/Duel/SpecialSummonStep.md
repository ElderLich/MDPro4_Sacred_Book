# Duel.SpecialSummonStep

## Signature

```lua
Duel.SpecialSummonStep(Card c, int sumtype, int sumplayer, int target_player, bool nocheck, bool nolimit, int pos, [int zone]) -> bool
```

## Description

此函数是Duel.SpecialSummon的分解过程，只特殊召唤一张卡c ，其他参数用法和 Duel.SpecialSummon 一样
此函数用于一个效果同时特殊召唤多张参数不同的卡
此函数必须和Duel.SpecialSummonComplete一起使用
返回值表示是否特殊召唤成功

## Parameters

- `c` `Card`
- `sumtype` `int`
- `sumplayer` `int`
- `target_player` `int`
- `nocheck` `bool`
- `nolimit` `bool`
- `pos` `int`
- `zone` `int` optional - default: 0xff

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4874`
