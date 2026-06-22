# Duel.GetDecktopGroup

## Signature

```lua
Duel.GetDecktopGroup(int player, int count) -> Group
```

## Description

Returns a Group containing up to count cards from the top of player's Deck.

## Parameters

- `player` `int`
- `count` `int`

## Returns

- `Group`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4967`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **185** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Duel.GetDecktopGroup`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [GMX 55th Experiment Report](/examples/cards/38984832) | `38984832` | [Scripts/c38984832.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c38984832.lua) | 64 |
| [Junoldo the Shadespirit Power Patron](/examples/cards/10266279) | `10266279` | [Scripts/c10266279.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c10266279.lua) | 62 |
| [Flower Cardian Peony with Butterfly](/examples/cards/57261568) | `57261568` | [Scripts/c57261568.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c57261568.lua) | 62 |
| [Jupredo the Shademachine Power Patron](/examples/cards/43871165) | `43871165` | [Scripts/c43871165.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c43871165.lua) | 60 |
| D/D Extra Surveyor | `74387963` | [Scripts/c74387963.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74387963.lua) | 60 |
| Nervedo the Shadebeast Power Patron | `17473466` | [Scripts/c17473466.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c17473466.lua) | 56 |
| Purrely | `25550531` | [Scripts/c25550531.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c25550531.lua) | 56 |
| Sylvan Dancepione | `21903613` | [Scripts/c21903613.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c21903613.lua) | 54 |
| Materiactor Meltthrough | `66059345` | [Scripts/c66059345.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c66059345.lua) | 53 |
| Time Thief Redoer | `55285840` | [Scripts/c55285840.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c55285840.lua) | 52 |
| Ma'at | `18631392` | [Scripts/c18631392.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c18631392.lua) | 51 |
| Loris, Lady of Lament | `50699850` | [Scripts/c50699850.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c50699850.lua) | 51 |
| Silk Bomb Moth | `18300894` | [Scripts/c18300894.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c18300894.lua) | 50 |
| Shadowreaver Knight 21 | `95506252` | [Scripts/c95506252.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c95506252.lua) | 50 |
| Bahalutiya, the Grand Radiance | `53318263` | [Scripts/c53318263.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c53318263.lua) | 49 |
| Materiactor Meltdown | `38669664` | [Scripts/c38669664.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c38669664.lua) | 49 |
| GMX Applied Experiment #55 | `18795635` | [Scripts/c18795635.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c18795635.lua) | 49 |
| Buerillabaisse de Nouvelles | `26223582` | [Scripts/c26223582.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c26223582.lua) | 48 |
| Magikey Mechmusket - Batosbuster | `19489718` | [Scripts/c19489718.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c19489718.lua) | 48 |
| Super Koi Koi | `66171432` | [Scripts/c66171432.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c66171432.lua) | 48 |
| Mariamne, the True Dracophoenix | `94160895` | [Scripts/c94160895.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c94160895.lua) | 48 |
| Chaos Ruler, the Chaotic Magical Dragon | `3040496` | [Scripts/c3040496.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c3040496.lua) | 48 |
| Adamancipator Risen - Leonite | `47674738` | [Scripts/c47674738.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c47674738.lua) | 48 |
| Runick Freezing Curses | `30430448` | [Scripts/c30430448.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30430448.lua) | 48 |
| ...and 161 more |  |  |  |

## Script Examples

### GMX 55th Experiment Report (`38984832`)

Source: [Scripts/c38984832.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c38984832.lua)

```lua
	local max_decktop=5
	if count>max_decktop then
		local g=Duel.GetDecktopGroup(tp,count)
		Duel.ConfirmCards(1-tp,g)
	else
```

### Junoldo the Shadespirit Power Patron (`10266279`)

Source: [Scripts/c10266279.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c10266279.lua)

```lua
end
function s.spcost(e,tp,eg,ep,ev,re,r,rp,chk)
	local g=Duel.GetDecktopGroup(tp,3)
	if chk==0 then return g:FilterCount(Card.IsAbleToRemoveAsCost,nil,POS_FACEDOWN)==3
		and Duel.GetFieldGroupCount(tp,LOCATION_DECK,0)>=3
```

### Flower Cardian Peony with Butterfly (`57261568`)

Source: [Scripts/c57261568.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c57261568.lua)

```lua
			if ct==0 then return end
			Duel.BreakEffect()
			local g=Duel.GetDecktopGroup(1-tp,ct)
			Duel.ConfirmCards(tp,g)
			local opt=Duel.SelectOption(tp,aux.Stringid(57261568,1),aux.Stringid(57261568,2))
```
