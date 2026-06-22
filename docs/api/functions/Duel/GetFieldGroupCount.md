# Duel.GetFieldGroupCount

## Signature

```lua
Duel.GetFieldGroupCount(int player, int s, int o) -> int
```

## Description

Returns the number of cards in the specified locations from player's viewpoint.

## Parameters

- `player` `int`
- `s` `int`
- `o` `int`

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4966`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **938** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Duel.GetFieldGroupCount`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Spellbook of the Grand Circle](/examples/cards/11911336) | `11911336` | [Scripts/c11911336.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c11911336.lua) | 71 |
| [El Shaddoll Apkallone](/examples/cards/50907446) | `50907446` | [Scripts/c50907446.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c50907446.lua) | 68 |
| [GMX 55th Experiment Report](/examples/cards/38984832) | `38984832` | [Scripts/c38984832.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c38984832.lua) | 64 |
| [Nekroz Kaleidoscope](/examples/cards/51124303) | `51124303` | [Scripts/c51124303.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c51124303.lua) | 63 |
| [Junoldo the Shadespirit Power Patron](/examples/cards/10266279) | `10266279` | [Scripts/c10266279.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c10266279.lua) | 62 |
| [Odd-Eyes Arcray Dragon](/examples/cards/6218704) | `6218704` | [Scripts/c6218704.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c6218704.lua) | 62 |
| [Flower Cardian Peony with Butterfly](/examples/cards/57261568) | `57261568` | [Scripts/c57261568.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c57261568.lua) | 62 |
| [Jupredo the Shademachine Power Patron](/examples/cards/43871165) | `43871165` | [Scripts/c43871165.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c43871165.lua) | 60 |
| Vernusylph and the Changing Season | `37313338` | [Scripts/c37313338.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c37313338.lua) | 60 |
| Ostinato | `9113513` | [Scripts/c9113513.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c9113513.lua) | 60 |
| Revolution Cyber Dragon | `66664203` | [Scripts/c66664203.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c66664203.lua) | 58 |
| Nervedo the Shadebeast Power Patron | `17473466` | [Scripts/c17473466.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c17473466.lua) | 56 |
| GMX - VELOX | `82706696` | [Scripts/c82706696.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c82706696.lua) | 56 |
| Purrely | `25550531` | [Scripts/c25550531.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c25550531.lua) | 56 |
| Ghoti Fury | `65898344` | [Scripts/c65898344.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c65898344.lua) | 56 |
| Numeron Calling | `77402960` | [Scripts/c77402960.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c77402960.lua) | 56 |
| Kaiki the Unity Star | `60822251` | [Scripts/c60822251.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c60822251.lua) | 55 |
| Genex Ally Triarm | `17760003` | [Scripts/c17760003.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c17760003.lua) | 55 |
| Odd-Eyes Venom Dragon | `45014450` | [Scripts/c45014450.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c45014450.lua) | 54 |
| Gunkan Sushipyard Seaside Supper Spot | `62200831` | [Scripts/c62200831.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c62200831.lua) | 54 |
| PSY-Framegear Alpha | `75425043` | [Scripts/c75425043.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c75425043.lua) | 54 |
| Sylvan Dancepione | `21903613` | [Scripts/c21903613.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c21903613.lua) | 54 |
| Crealtar, the Impcantation Originator | `96915510` | [Scripts/c96915510.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c96915510.lua) | 54 |
| Supreme King Gate Infinity | `22211622` | [Scripts/c22211622.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c22211622.lua) | 53 |
| ...and 914 more |  |  |  |

## Script Examples

### Spellbook of the Grand Circle (`11911336`)

Source: [Scripts/c11911336.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c11911336.lua)

```lua
	if Duel.SendtoHand(sg,nil,REASON_EFFECT)>0 then
		Duel.ConfirmCards(1-tp,sg)
		if sg:IsExists(Card.IsLocation,1,nil,LOCATION_HAND) and Duel.GetFieldGroupCount(tp,LOCATION_HAND,0)>1 then
			Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_TODECK)
			local dg=Duel.SelectMatchingCard(tp,Card.IsAbleToDeck,tp,LOCATION_HAND,0,2,2,nil)
```

### El Shaddoll Apkallone (`50907446`)

Source: [Scripts/c50907446.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c50907446.lua)

```lua
	if g:GetCount()>0 and Duel.SendtoHand(g,nil,REASON_EFFECT)~=0 then
		Duel.ConfirmCards(1-tp,g)
		if g:GetFirst():IsLocation(LOCATION_HAND) and Duel.GetFieldGroupCount(tp,LOCATION_HAND,0)>0 then
			Duel.BreakEffect()
			Duel.ShuffleHand(tp)
```

### GMX 55th Experiment Report (`38984832`)

Source: [Scripts/c38984832.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c38984832.lua)

```lua
end
function s.digop(e,tp,eg,ep,ev,re,r,rp)
	local dcount=Duel.GetFieldGroupCount(tp,LOCATION_DECK,0)
	if dcount==0 then return end
	local mg=Duel.GetMatchingGroup(s.deckgmx,tp,LOCATION_DECK,0,nil)
```
