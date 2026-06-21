# Auxiliary.dncheck

## Signature

```lua
Auxiliary.dncheck(Group g) -> void
```

## Description

Returns true if every card in g has a different card code.

## Parameters

- `g` `Group`

## Source

- `Utilities/utility.lua:1126`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **206** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Auxiliary.dncheck`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Ehther the Heavenly Monarch](/examples/cards/96570609) | `96570609` | [Scripts/c96570609.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c96570609.lua) | 65 |
| [Prank-Kids Weather Washer](/examples/cards/44509529) | `44509529` | [Scripts/c44509529.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44509529.lua) | 65 |
| [Shining Draw](/examples/cards/35906693) | `35906693` | [Scripts/c35906693.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c35906693.lua) | 63 |
| [Artmage Masterwork -Succession-](/examples/cards/37517035) | `37517035` | [Scripts/c37517035.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c37517035.lua) | 63 |
| [Chimera Fusion](/examples/cards/63136489) | `63136489` | [Scripts/c63136489.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63136489.lua) | 62 |
| [Prank-Kids Rocket Ride](/examples/cards/18514525) | `18514525` | [Scripts/c18514525.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c18514525.lua) | 61 |
| Regenesis Birth | `27781371` | [Scripts/c27781371.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c27781371.lua) | 60 |
| Vernusylph and the Changing Season | `37313338` | [Scripts/c37313338.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c37313338.lua) | 60 |
| Chaos Hats | `2372506` | [Scripts/c2372506.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c2372506.lua) | 59 |
| Isolde, Two Tales of the Noble Knights | `59934749` | [Scripts/c59934749.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59934749.lua) | 59 |
| Ojamassimilation | `2390019` | [Scripts/c2390019.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c2390019.lua) | 59 |
| Cyberse Reminder | `56337500` | [Scripts/c56337500.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c56337500.lua) | 58 |
| Vanquish Soul Trinity Burst | `53330789` | [Scripts/c53330789.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c53330789.lua) | 58 |
| Power Tool Braver Dragon | `63265554` | [Scripts/c63265554.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63265554.lua) | 58 |
| Alba System Dogmatikalamity | `93053159` | [Scripts/c93053159.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93053159.lua) | 58 |
| Prank-Kids Bow-Wow-Bark | `43886072` | [Scripts/c43886072.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c43886072.lua) | 58 |
| Divine Serpent Apophis | `97800311` | [Scripts/c97800311.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c97800311.lua) | 58 |
| Super Quantal Mech Ship Magnacarrier | `10424147` | [Scripts/c10424147.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c10424147.lua) | 57 |
| Erebus the Underworld Monarch | `23064604` | [Scripts/c23064604.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c23064604.lua) | 56 |
| World Legacy Monstrosity | `14604710` | [Scripts/c14604710.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c14604710.lua) | 56 |
| Numeron Calling | `77402960` | [Scripts/c77402960.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c77402960.lua) | 56 |
| Dual Avatar - Manifested A-Un | `28798938` | [Scripts/c28798938.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c28798938.lua) | 55 |
| Gem-Knight Master Diamond Dispersion | `25342956` | [Scripts/c25342956.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c25342956.lua) | 55 |
| ABC-Dragon Buster | `1561110` | [Scripts/c1561110.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c1561110.lua) | 55 |
| ...and 182 more |  |  |  |

## Script Examples

### Ehther the Heavenly Monarch (`96570609`)

Source: [Scripts/c96570609.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c96570609.lua)

```lua
	if g:GetClassCount(Card.GetCode)<2 then return end
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_TOGRAVE)
	local tg1=g:SelectSubGroup(tp,aux.dncheck,false,2,2)
	if Duel.SendtoGrave(tg1,REASON_EFFECT)~=0 and tg1:IsExists(Card.IsLocation,2,nil,LOCATION_GRAVE)
		and Duel.GetLocationCount(tp,LOCATION_MZONE)>0 then
```

### Prank-Kids Weather Washer (`44509529`)

Source: [Scripts/c44509529.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44509529.lua)

```lua
	local g=Duel.GetMatchingGroup(c44509529.spfilter,tp,LOCATION_GRAVE,0,nil,e,tp)
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_SPSUMMON)
	local g1=g:SelectSubGroup(tp,aux.dncheck,false,2,2)
	Duel.SetTargetCard(g1)
	Duel.SetOperationInfo(0,CATEGORY_SPECIAL_SUMMON,g1,2,0,0)
```

### Shining Draw (`35906693`)

Source: [Scripts/c35906693.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c35906693.lua)

```lua
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_EQUIP)
	local g=Duel.GetMatchingGroup(c35906693.eqfilter,tp,LOCATION_DECK+LOCATION_EXTRA,0,nil,tp)
	local sg=g:SelectSubGroup(tp,aux.dncheck,false,1,ft)
	if not sg then return end
	local ec=sg:GetFirst()
```
