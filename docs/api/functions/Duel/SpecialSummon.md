# Duel.SpecialSummon

## Signature

```lua
Duel.SpecialSummon(Card|Group targets, int sumtype, int sumplayer, int target_player, bool nocheck, bool nolimit, int pos, [int zone]) -> int
```

## Description

Let player player to sumtype way, pos that special targets to target_player target field
If nocheck is true, the card's calling condition is disregarded. If nolimit is true,
The return value is the number of cards that were successfully summoned

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
