# Card.IsCanBeSpecialSummoned

## Signature

```lua
Card.IsCanBeSpecialSummoned(Card c, Effect e, int sumtype, int sumplayer, bool nocheck, bool nolimit, [int sumpos], [int toplayer], [int zone]) -> bool
```

## Description

Check whether c can be sumplayer with the effect of the player e to sumtype form sumpos special summon to target_player field
If nocheck is true, the call condition of c is not checked, and if nolimit is true, then the limit of c is not checked

## Parameters

- `c` `Card`
- `e` `Effect`
- `sumtype` `int`
- `sumplayer` `int`
- `nocheck` `bool`
- `nolimit` `bool`
- `sumpos` `int` optional - default: POS_FACEUP
- `toplayer` `int` optional - default: sumplayer
- `zone` `int` optional - default: 0xff

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3582`
