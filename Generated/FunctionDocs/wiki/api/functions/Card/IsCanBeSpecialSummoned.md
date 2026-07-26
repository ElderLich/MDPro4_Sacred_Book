# Card.IsCanBeSpecialSummoned

## Signature

```lua
Card.IsCanBeSpecialSummoned(Card c, Effect e, int sumtype, int sumplayer, bool nocheck, bool nolimit, [int sumpos], [int toplayer], [int zone]) -> bool
```

## Description

Checks whether c can be Special Summoned by effect e using sumtype, sumplayer, sumpos, target player, and optional zone.
Use the same nocheck, nolimit, position, target player, and zone values that the later Duel.SpecialSummon call will use.
If nocheck is true, c's Summoning condition is skipped. If nolimit is true, c's revive limit or proper-Summon limit is skipped. Leave both false unless the card text and local pattern justify bypassing those checks.

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

- `c` `Card` - Card being checked.
- `e` `Effect` - Effect that would perform the Special Summon.
- `sumtype` `int` - Summon type value recorded for the Special Summon.
- `sumplayer` `int` - Player treated as performing the Special Summon.
- `nocheck` `bool` - If true, skips c's Summoning-condition check, including EFFECT_SPSUMMON_CONDITION-style restrictions.
- `nolimit` `bool` - If true, skips c's revive-limit or proper-Summon completion check.
- `sumpos` `int` optional - Summon position mask checked by the core; default: POS_FACEUP.
- `toplayer` `int` optional - Player whose field c would be Summoned to; default: sumplayer.
- `zone` `int` optional - Allowed Monster Zone bitmask; default: 0xff.

## Returns

- `bool` - True if c can be Special Summoned with the supplied parameters.

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3585`
