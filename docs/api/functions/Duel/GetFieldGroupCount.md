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

## Guided Examples

Learn how to use this function in context:

- [Draw, Hand, And Deck Effects](/learn/draw-hand-and-deck-effects)
- [Pendulum Procedure Guide](/learn/pendulum-procedure)

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **950** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Duel.GetFieldGroupCount) with `Duel.GetFieldGroupCount`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Levia-Dragoon - Daedalus](/examples/cards/78579058) | `78579058` | [Scripts/c78579058.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c78579058.lua) | 2 |
| [Spellbook of the Grand Circle](/examples/cards/11911336) | `11911336` | [Scripts/c11911336.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c11911336.lua) | 1 |
| [El Shaddoll Apkallone](/examples/cards/50907446) | `50907446` | [Scripts/c50907446.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c50907446.lua) | 1 |
| [GMX 55th Experiment Report](/examples/cards/38984832) | `38984832` | [Scripts/c38984832.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c38984832.lua) | 1 |
| [Nekroz Kaleidoscope](/examples/cards/51124303) | `51124303` | [Scripts/c51124303.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c51124303.lua) | 1 |
| [Junoldo the Shadespirit Power Patron](/examples/cards/10266279) | `10266279` | [Scripts/c10266279.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c10266279.lua) | 2 |
| [Odd-Eyes Arcray Dragon](/examples/cards/6218704) | `6218704` | [Scripts/c6218704.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c6218704.lua) | 1 |
| [Flower Cardian Peony with Butterfly](/examples/cards/57261568) | `57261568` | [Scripts/c57261568.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c57261568.lua) | 1 |
| Jupredo the Shademachine Power Patron | `43871165` | [Scripts/c43871165.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c43871165.lua) | 2 |
| Vernusylph and the Changing Season | `37313338` | [Scripts/c37313338.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c37313338.lua) | 1 |
| Ostinato | `9113513` | [Scripts/c9113513.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c9113513.lua) | 1 |
| Cyber Dragon, the Luminous Mech Dragon | `66664203` | [Scripts/c66664203.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c66664203.lua) | 1 |
| Nervedo the Shadebeast Power Patron | `17473466` | [Scripts/c17473466.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c17473466.lua) | 2 |
| GMX - VELOX | `82706696` | [Scripts/c82706696.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c82706696.lua) | 1 |
| Purrely | `25550531` | [Scripts/c25550531.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c25550531.lua) | 1 |
| Ghoti Fury | `65898344` | [Scripts/c65898344.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c65898344.lua) | 2 |
| Numeron Calling | `77402960` | [Scripts/c77402960.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c77402960.lua) | 1 |
| Kaiki the Unity Star | `60822251` | [Scripts/c60822251.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c60822251.lua) | 1 |
| Genex Ally Triarm | `17760003` | [Scripts/c17760003.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c17760003.lua) | 1 |
| Odd-Eyes Venom Dragon | `45014450` | [Scripts/c45014450.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c45014450.lua) | 2 |
| Gunkan Sushipyard Seaside Supper Spot | `62200831` | [Scripts/c62200831.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c62200831.lua) | 1 |
| PSY-Framegear Alpha | `75425043` | [Scripts/c75425043.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c75425043.lua) | 2 |
| Shimmering Shatterer of the Sacred Beasts | `3441553` | [Scripts/c3441553.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c3441553.lua) | 2 |
| Sylvan Dancepione | `21903613` | [Scripts/c21903613.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c21903613.lua) | 1 |
| ...and 926 more |  |  |  |

## Script Examples

### Levia-Dragoon - Daedalus (`78579058`)

Source: [Scripts/c78579058.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c78579058.lua)

```lua
function s.drtg(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then
		local h=Duel.GetFieldGroupCount(tp,0,LOCATION_HAND)
		return h>0 and Duel.IsPlayerCanDraw(1-tp,h)
	end
```

### Spellbook of the Grand Circle (`11911336`)

Source: [Scripts/c11911336.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c11911336.lua)

```lua
	if Duel.SendtoHand(sg,nil,REASON_EFFECT)>0 then
		Duel.ConfirmCards(1-tp,sg)
		if sg:IsExists(Card.IsLocation,1,nil,LOCATION_HAND) and Duel.GetFieldGroupCount(tp,LOCATION_HAND,0)>1 then
			Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_TODECK)
			local dg=Duel.SelectMatchingCard(tp,Card.IsAbleToDeck,tp,LOCATION_HAND,0,2,2,nil)
```

### El Shaddoll Apkallone (`50907446`)

Source: [Scripts/c50907446.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c50907446.lua)

```lua
	if g:GetCount()>0 and Duel.SendtoHand(g,nil,REASON_EFFECT)~=0 then
		Duel.ConfirmCards(1-tp,g)
		if g:GetFirst():IsLocation(LOCATION_HAND) and Duel.GetFieldGroupCount(tp,LOCATION_HAND,0)>0 then
			Duel.BreakEffect()
			Duel.ShuffleHand(tp)
```
