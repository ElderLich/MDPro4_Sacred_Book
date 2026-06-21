# Duel.SpecialSummonStep

## Signature

```lua
Duel.SpecialSummonStep(Card c, int sumtype, int sumplayer, int target_player, bool nocheck, bool nolimit, int pos, [int zone]) -> bool
```

## Description

This function is Duel.SpecialSummon decomposition process, only a special summon a card c
This function is used for an effect while simultaneously calling multiple cards with different parameters
This function must be used with Duel.SpecialSummonComplete
The return value indicates whether or not the special call succeeded

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
