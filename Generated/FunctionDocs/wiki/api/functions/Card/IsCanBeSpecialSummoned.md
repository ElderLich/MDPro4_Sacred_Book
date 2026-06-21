# Card.IsCanBeSpecialSummoned

## Signature

```lua
Card.IsCanBeSpecialSummoned(Card c, Effect e, int sumtype, int sumplayer, bool nocheck, bool nolimit, [int sumpos], [int toplayer], [int zone]) -> bool
```

## Description

Checks whether c can be Special Summoned by effect e using sumtype, sumplayer, sumpos, target player, and optional zone.
If nocheck is true, c's Summoning condition is skipped. If nolimit is true, c's revive limit or proper-Summon limit is skipped.

## How To Use It

Use this in activation checks before selecting a monster to Special Summon.

The parameters should match the later `Duel.SpecialSummon` call as closely as possible: same effect, Summon type, Summon player, target player, position, and zone restrictions.

```lua
function s.spfilter(c,e,tp)
    return c:IsCanBeSpecialSummoned(e,0,tp,false,false,POS_FACEUP,tp)
end
```

This is only a legality check. It does not reserve a zone or Summon the card.

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
