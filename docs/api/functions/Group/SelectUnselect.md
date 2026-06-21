# Group.SelectUnselect

## Signature

```lua
Group.SelectUnselect(Group cg, [Group|nil sg], int player, bool btok, bool cancelable, int minc, int maxc) -> Card|nil
```

## Description

Have player select 1 card from cg to add to sg and return the selected card
btok indicates whether the confirm selection button is available, cancelable indicates whether selected cards can be canceled
minc and maxc are client-side text buffer prompts indicating the need to select minc-maxc cards, but this only affects visual display and does not enforce the selection count

## Parameters

- `cg` `Group`
- `sg` `Group|nil` optional - already selected cards that can be unselected
- `player` `int`
- `btok` `bool` - default: false
- `cancelable` `bool` - default: false
- `minc` `int`
- `maxc` `int`

## Returns

- `Card|nil`

## Source

- `D:\Programs\GitHub\ygopro-core\libgroup.cpp:916`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **167** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Group.SelectUnselect`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Artmage Non-Finito](/examples/cards/74631897) | `74631897` | [Scripts/c74631897.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74631897.lua) | 78 |
| [Odd-Eyes Arcray Dragon](/examples/cards/6218704) | `6218704` | [Scripts/c6218704.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c6218704.lua) | 62 |
| [Flower Cardian Peony with Butterfly](/examples/cards/57261568) | `57261568` | [Scripts/c57261568.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c57261568.lua) | 62 |
| [Ultimate Crystal Rainbow Dragon Overdrive](/examples/cards/84544192) | `84544192` | [Scripts/c84544192.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c84544192.lua) | 62 |
| [Flower Cardian Willow with Calligrapher](/examples/cards/89818984) | `89818984` | [Scripts/c89818984.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c89818984.lua) | 61 |
| [Cyber Pharos](/examples/cards/29719112) | `29719112` | [Scripts/c29719112.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c29719112.lua) | 61 |
| Vaylantz Genesis Grand Duke | `76075139` | [Scripts/c76075139.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c76075139.lua) | 60 |
| Gishki Nekromirror | `36982581` | [Scripts/c36982581.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c36982581.lua) | 59 |
| Malefic Paradigm Dragon | `16958382` | [Scripts/c16958382.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c16958382.lua) | 55 |
| Todoroki the Earthbolt Star | `30118701` | [Scripts/c30118701.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30118701.lua) | 55 |
| Thunder Dragonlord | `5206415` | [Scripts/c5206415.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c5206415.lua) | 54 |
| Dragunity Arma Leyvaten | `63487632` | [Scripts/c63487632.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63487632.lua) | 54 |
| Cyberdark End Dragon | `37542782` | [Scripts/c37542782.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c37542782.lua) | 53 |
| Rainbow Overdragon | `37440988` | [Scripts/c37440988.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c37440988.lua) | 52 |
| Egyptian God Slime | `42166000` | [Scripts/c42166000.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c42166000.lua) | 52 |
| Hieratic Dragon of Nebthet | `31516413` | [Scripts/c31516413.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c31516413.lua) | 50 |
| Grapha, Dragon Lord of Dark World | `34230233` | [Scripts/c34230233.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c34230233.lua) | 49 |
| Blue-Eyes Tyrant Dragon | `11443677` | [Scripts/c11443677.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c11443677.lua) | 49 |
| Hieratic Dragon of Su | `3300267` | [Scripts/c3300267.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c3300267.lua) | 49 |
| Dark Magician of Destruction | `59400890` | [Scripts/c59400890.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59400890.lua) | 48 |
| Infernoid Pirmais | `60551528` | [Scripts/c60551528.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c60551528.lua) | 48 |
| Infernoid Patrulea | `89423971` | [Scripts/c89423971.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c89423971.lua) | 48 |
| Infernoid Harmadik | `52038272` | [Scripts/c52038272.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c52038272.lua) | 48 |
| Gizmek Yata, the Gleaming Vanguard | `13224603` | [Scripts/c13224603.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c13224603.lua) | 47 |
| ...and 143 more |  |  |  |

## Script Examples

### Artmage Non-Finito (`74631897`)

Source: [Scripts/c74631897.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74631897.lua)

```lua
	local g2=Duel.GetMatchingGroup(s.cfilter,tp,LOCATION_HAND,0,nil)
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_DISCARD)
	local tc=g2:SelectUnselect(nil,tp,false,true,1,1)
	if tc then
		Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_RELEASE)
```

### Odd-Eyes Arcray Dragon (`6218704`)

Source: [Scripts/c6218704.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c6218704.lua)

```lua
	local g=Duel.GetReleaseGroup(tp,false,REASON_SPSUMMON):Filter(c6218704.hspfilter,nil,tp,c)
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_RELEASE)
	local tc=g:SelectUnselect(nil,tp,false,true,1,1)
	if tc then
		e:SetLabelObject(tc)
```

### Flower Cardian Peony with Butterfly (`57261568`)

Source: [Scripts/c57261568.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c57261568.lua)

```lua
	local g=Duel.GetReleaseGroup(tp,false,REASON_SPSUMMON):Filter(c57261568.hspfilter,nil,tp)
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_RELEASE)
	local tc=g:SelectUnselect(nil,tp,false,true,1,1)
	if tc then
		e:SetLabelObject(tc)
```
