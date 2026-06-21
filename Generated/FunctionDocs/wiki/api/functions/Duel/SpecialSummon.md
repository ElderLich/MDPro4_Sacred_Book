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
