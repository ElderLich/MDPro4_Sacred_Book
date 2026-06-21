# Duel.ConfirmExtratop

## Signature

```lua
Duel.ConfirmExtratop(int player, int count) -> void
```

## Description

Confirm the top count face-down cards in player's Extra Deck

## Parameters

- `player` `int`
- `count` `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4891`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **1** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Duel.ConfirmExtratop`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Cynet Storm | `42461852` | [Scripts/c42461852.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c42461852.lua) | 31 |

## Script Examples

### Cynet Storm (`42461852`)

Source: [Scripts/c42461852.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c42461852.lua)

```lua
		or Duel.GetMatchingGroupCount(Card.IsFacedown,tp,LOCATION_EXTRA,0,nil)==0 then return end
	Duel.ShuffleExtra(tp)
	Duel.ConfirmExtratop(tp,1)
	local tc=Duel.GetExtraTopGroup(tp,1):GetFirst()
	if tc:IsType(TYPE_LINK) and tc:IsRace(RACE_CYBERSE) then
```
