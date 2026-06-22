# Duel.SpecialSummonStep

## Signature

```lua
Duel.SpecialSummonStep(Card c, int sumtype, int sumplayer, int target_player, bool nocheck, bool nolimit, int pos, [int zone]) -> bool
```

## Description

Special Summons one card as part of a multi-step Summon procedure and returns true if that step succeeds.
Every successful step batch must finish with Duel.SpecialSummonComplete.

## How To Use It

Use this only for procedures that need to Special Summon cards one at a time before raising the final Summon events.

Every batch must end with `Duel.SpecialSummonComplete`. For ordinary effects that just Special Summon one Card or Group, use `Duel.SpecialSummon` instead.

## Related Functions

- [Duel.SpecialSummonComplete](/api/functions/Duel/SpecialSummonComplete)
- [Card.IsCanBeSpecialSummoned](/api/functions/Card/IsCanBeSpecialSummoned)

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
