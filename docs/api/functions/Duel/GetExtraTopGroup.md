# Duel.GetExtraTopGroup

## Signature

```lua
Duel.GetExtraTopGroup(int player, int count) -> Group
```

## Description

Returns a Group containing up to count cards from the top of player's Extra Deck, after the face-up Pendulum section.

## Parameters

- `player` `int`
- `count` `int`

## Returns

- `Group`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4968`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **1** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Duel.GetExtraTopGroup) with `Duel.GetExtraTopGroup`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Cynet Storm | `42461852` | [Scripts/c42461852.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c42461852.lua) | 1 |

## Script Examples

### Cynet Storm (`42461852`)

Source: [Scripts/c42461852.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c42461852.lua)

```lua
	Duel.ShuffleExtra(tp)
	Duel.ConfirmExtratop(tp,1)
	local tc=Duel.GetExtraTopGroup(tp,1):GetFirst()
	if tc:IsType(TYPE_LINK) and tc:IsRace(RACE_CYBERSE) then
		Duel.SpecialSummon(tc,0,tp,tp,false,false,POS_FACEUP)
```
