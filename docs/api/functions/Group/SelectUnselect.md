# Group.SelectUnselect

## Signature

```lua
Group.SelectUnselect(Group cg, [Group|nil sg], int player, [bool finishable], [bool cancelable], [int min], [int max]) -> Card|nil
```

## Description

Lets player choose one card from cg to add to the current selection or one card from sg to remove from it, then returns the card that was chosen.
sg may be nil. finishable controls whether the selection can finish at its current size, cancelable allows cancellation, and cancellation returns nil. min and max default to 1.
This is a building block for step-by-step material or procedure selections. For ordinary one-shot choices, Group.Select, Group.FilterSelect, or Duel.SelectMatchingCard is usually clearer.

## How To Use It

Use this for custom selection loops that need to add and remove candidates while tracking whether the current choice can finish.

It is lower-level than `Group.Select` and is mostly useful inside helper procedures. For ordinary card choices, prefer `Group.Select`, `Group.FilterSelect`, or `Duel.SelectMatchingCard`.

## Related Functions

- [Group.SelectSubGroup](/api/functions/Group/SelectSubGroup)
- [Group.Select](/api/functions/Group/Select)
- [Group.CheckSubGroup](/api/functions/Group/CheckSubGroup)

## Parameters

- `cg` `Group`
- `sg` `Group|nil` optional
- `player` `int`
- `finishable` `bool` optional - default: false
- `cancelable` `bool` optional - default: false
- `min` `int` optional - default: 1
- `max` `int` optional - default: 1

## Returns

- `Card|nil` - Chosen card, or nil if the selection is canceled.

## Source

- `D:\Programs\GitHub\ygopro-core\libgroup.cpp:916`

## Guided Examples

Learn how to use this function in context:

- [Selection And Group Handling](/learn/selection-and-group-handling)

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **175** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Group.SelectUnselect) with `Group.SelectUnselect`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Artmage Non-Finito](/examples/cards/74631897) | `74631897` | [Scripts/c74631897.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74631897.lua) | 2 |
| [Ashtraja Susanoo](/examples/cards/17020474) | `17020474` | [Scripts/c17020474.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c17020474.lua) | 1 |
| [Odd-Eyes Arcray Dragon](/examples/cards/6218704) | `6218704` | [Scripts/c6218704.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c6218704.lua) | 1 |
| [Flower Cardian Peony with Butterfly](/examples/cards/57261568) | `57261568` | [Scripts/c57261568.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c57261568.lua) | 1 |
| [Ultimate Crystal Rainbow Dragon Overdrive](/examples/cards/84544192) | `84544192` | [Scripts/c84544192.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c84544192.lua) | 1 |
| Flower Cardian Willow with Calligrapher | `89818984` | [Scripts/c89818984.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c89818984.lua) | 1 |
| Cyber Pharos | `29719112` | [Scripts/c29719112.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c29719112.lua) | 1 |
| Vaylantz Genesis Grand Duke | `76075139` | [Scripts/c76075139.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c76075139.lua) | 1 |
| Gishki Nekromirror | `36982581` | [Scripts/c36982581.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c36982581.lua) | 1 |
| Malefic Paradigm Dragon | `16958382` | [Scripts/c16958382.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c16958382.lua) | 1 |
| Todoroki the Earthbolt Star | `30118701` | [Scripts/c30118701.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30118701.lua) | 1 |
| Thunder Dragonlord | `5206415` | [Scripts/c5206415.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c5206415.lua) | 1 |
| Dragunity Arma Leyvaten | `63487632` | [Scripts/c63487632.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63487632.lua) | 1 |
| Cyberdark End Dragon | `37542782` | [Scripts/c37542782.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c37542782.lua) | 1 |
| Red-Eyes Black Dragon Exceed | `17242022` | [Scripts/c17242022.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c17242022.lua) | 1 |
| Rainbow Overdragon | `37440988` | [Scripts/c37440988.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c37440988.lua) | 1 |
| Egyptian God Slime | `42166000` | [Scripts/c42166000.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c42166000.lua) | 1 |
| Destiny HERO - Dreadnought Master | `54641720` | [Scripts/c54641720.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c54641720.lua) | 1 |
| Hieratic Dragon of Nebthet | `31516413` | [Scripts/c31516413.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c31516413.lua) | 1 |
| Grapha, Dragon Lord of Dark World | `34230233` | [Scripts/c34230233.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c34230233.lua) | 1 |
| Blue-Eyes Tyrant Dragon | `11443677` | [Scripts/c11443677.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c11443677.lua) | 1 |
| Hieratic Dragon of Su | `3300267` | [Scripts/c3300267.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c3300267.lua) | 1 |
| Dark Magician of Destruction | `59400890` | [Scripts/c59400890.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59400890.lua) | 1 |
| Infernoid Pirmais | `60551528` | [Scripts/c60551528.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c60551528.lua) | 1 |
| ...and 151 more |  |  |  |

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

### Ashtraja Susanoo (`17020474`)

Source: [Scripts/c17020474.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c17020474.lua)

```lua
				local tmg=tg:Clone()
				tmg:Sub(selg)
				local tc=tmg:SelectUnselect(selg,tp,finish,false,1,tg:GetCount())
				if not tc then
					setg:Merge(selg)
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
