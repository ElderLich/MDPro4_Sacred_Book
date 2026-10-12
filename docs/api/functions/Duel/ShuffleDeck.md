# Duel.ShuffleDeck

## Signature

```lua
Duel.ShuffleDeck(int player) -> void
```

## Description

Shuffles player's Deck and resets shuffle-check state.

## Parameters

- `player` `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4915`

## Guided Examples

Learn how to use this function in context:

- [Operation Results And Follow-Up Effects](/learn/operation-results-and-follow-up-effects)

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **246** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Duel.ShuffleDeck) with `Duel.ShuffleDeck`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Deftero Enneacraft - "alazoneIA"](/examples/cards/92171126) | `92171126` | [Scripts/c92171126.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c92171126.lua) | 1 |
| [GMX 55th Experiment Report](/examples/cards/38984832) | `38984832` | [Scripts/c38984832.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c38984832.lua) | 1 |
| Ojamassimilation | `2390019` | [Scripts/c2390019.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c2390019.lua) | 1 |
| Triamid Pulse | `96100333` | [Scripts/c96100333.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c96100333.lua) | 1 |
| GMX - VELOX | `82706696` | [Scripts/c82706696.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c82706696.lua) | 1 |
| Magellanica, the Deep Sea City | `26534688` | [Scripts/c26534688.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c26534688.lua) | 1 |
| Ojamatch | `38395123` | [Scripts/c38395123.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c38395123.lua) | 1 |
| Inzektor Picofalena | `97273514` | [Scripts/c97273514.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c97273514.lua) | 1 |
| Gunkan Sushipyard Seaside Supper Spot | `62200831` | [Scripts/c62200831.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c62200831.lua) | 1 |
| Indiora Doom Volt the Cubic Emperor | `3775068` | [Scripts/c3775068.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c3775068.lua) | 1 |
| Rank-Up-Magic Zexal Force | `36224040` | [Scripts/c36224040.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c36224040.lua) | 1 |
| Shuffle Reborn | `14816688` | [Scripts/c14816688.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c14816688.lua) | 1 |
| Ekto Enneacraft - "tromarIA" | `29570824` | [Scripts/c29570824.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c29570824.lua) | 1 |
| Enato Enneacraft - "oknirIA" | `55965529` | [Scripts/c55965529.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c55965529.lua) | 1 |
| Enneacraft Reverth | `80015408` | [Scripts/c80015408.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c80015408.lua) | 2 |
| Melffy Staring Contest | `76981308` | [Scripts/c76981308.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c76981308.lua) | 1 |
| Shinobaroness Peacock | `25415052` | [Scripts/c25415052.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c25415052.lua) | 2 |
| Triangle O | `11489642` | [Scripts/c11489642.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c11489642.lua) | 1 |
| Zoodiac Combo | `73881652` | [Scripts/c73881652.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c73881652.lua) | 1 |
| Trito Enneacraft - "exapatisIA" | `44716748` | [Scripts/c44716748.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c44716748.lua) | 1 |
| Proto Enneacraft - "orgIA" | `56187077` | [Scripts/c56187077.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c56187077.lua) | 1 |
| Knightmare Unicorn | `38342335` | [Scripts/c38342335.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c38342335.lua) | 1 |
| Duality | `39973386` | [Scripts/c39973386.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c39973386.lua) | 1 |
| Galaxy Cleric | `28770951` | [Scripts/c28770951.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c28770951.lua) | 1 |
| ...and 222 more |  |  |  |

## Script Examples

### Deftero Enneacraft - "alazoneIA" (`92171126`)

Source: [Scripts/c92171126.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c92171126.lua)

```lua
		Duel.Hint(HINT_SELECTMSG,1-tp,HINTMSG_ATOHAND)
		local tg=sg:RandomSelect(1-tp,1)
		Duel.ShuffleDeck(tp)
		tg:GetFirst():SetStatus(STATUS_TO_HAND_WITHOUT_CONFIRM,true)
		Duel.SendtoHand(tg,nil,REASON_EFFECT)
```

### GMX 55th Experiment Report (`38984832`)

Source: [Scripts/c38984832.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c38984832.lua)

```lua
		Duel.SendtoGrave(qc,REASON_RULE)
	end
	Duel.ShuffleDeck(tp)
end
```

### Ojamassimilation (`2390019`)

Source: [Scripts/c2390019.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c2390019.lua)

```lua
	Duel.SendtoDeck(tg,nil,SEQ_DECKSHUFFLE,REASON_EFFECT)
	local g=Duel.GetOperatedGroup()
	if g:IsExists(Card.IsLocation,1,nil,LOCATION_DECK) then Duel.ShuffleDeck(tp) end
	local ct=g:FilterCount(Card.IsLocation,nil,LOCATION_DECK+LOCATION_EXTRA)
	if ct>0 then
```
