# Duel.SpecialSummon

## Signature

```lua
Duel.SpecialSummon(Card|Group targets, int sumtype, int sumplayer, int target_player, bool nocheck, bool nolimit, int pos, [int zone]) -> int
```

## Description

Special Summons targets to target_player's field in position pos and returns the number of cards successfully Summoned.
sumplayer is the player performing the Summon and sumtype records the Summon type. nocheck skips Summoning-condition checks; nolimit skips revive-limit checks.

## How To Use It

`targets` can be one Card or a Group. The return value is the number of cards actually Special Summoned, so check it if later steps depend on success.

`sumplayer` is the player performing the Summon. `target_player` is the player whose field receives the monster. For most simple effects, both are `tp`.

```lua
local g=Duel.SelectMatchingCard(tp,s.spfilter,tp,LOCATION_GRAVE,0,1,1,nil,e,tp)
if #g>0 then
    Duel.SpecialSummon(g,0,tp,tp,false,false,POS_FACEUP)
end
```

Use `nocheck=true` only when the effect intentionally ignores the monster's usual Summoning condition. Use `nolimit=true` only when the effect intentionally ignores the proper Summon/revive limit.

## Related Functions

- [Card.IsCanBeSpecialSummoned](/api/functions/Card/IsCanBeSpecialSummoned)
- [Duel.SpecialSummonStep](/api/functions/Duel/SpecialSummonStep)
- [Duel.SpecialSummonComplete](/api/functions/Duel/SpecialSummonComplete)
- [Duel.GetLocationCount](/api/functions/Duel/GetLocationCount)

## Parameters

- `targets` `Card|Group` - Card or Group to Special Summon.
- `sumtype` `int` - Summon type value recorded for the Summon.
- `sumplayer` `int` - Player treated as performing the Special Summon.
- `target_player` `int` - Player whose field receives the Summoned cards.
- `nocheck` `bool` - If true, skips Summoning-condition checks.
- `nolimit` `bool` - If true, skips revive-limit checks.
- `pos` `int` - POS_* position mask for the Summon.
- `zone` `int` optional - Allowed Monster Zone bitmask; default: 0xff.

## Returns

- `int` - Number of cards successfully Special Summoned.

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4873`
