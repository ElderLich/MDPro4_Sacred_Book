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

- `Utilities/utility.lua:1129`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **213** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Auxiliary.dncheck) with `Auxiliary.dncheck`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Ehther the Heavenly Monarch](/examples/cards/96570609) | `96570609` | [Scripts/c96570609.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c96570609.lua) | 1 |
| [Pere-Zenet Em Heru](/examples/cards/46273941) | `46273941` | [Scripts/c46273941.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c46273941.lua) | 1 |
| [Am Duazenet](/examples/cards/45151304) | `45151304` | [Scripts/c45151304.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c45151304.lua) | 1 |
| [Prank-Kids Weather Washer](/examples/cards/44509529) | `44509529` | [Scripts/c44509529.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c44509529.lua) | 1 |
| [Shining Draw](/examples/cards/35906693) | `35906693` | [Scripts/c35906693.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c35906693.lua) | 1 |
| [Artmage Masterwork -Succession-](/examples/cards/37517035) | `37517035` | [Scripts/c37517035.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c37517035.lua) | 2 |
| [Chimera Fusion](/examples/cards/63136489) | `63136489` | [Scripts/c63136489.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c63136489.lua) | 1 |
| Prank-Kids Rocket Ride | `18514525` | [Scripts/c18514525.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c18514525.lua) | 1 |
| Regenesis Birth | `27781371` | [Scripts/c27781371.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c27781371.lua) | 1 |
| Vernusylph and the Changing Season | `37313338` | [Scripts/c37313338.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c37313338.lua) | 1 |
| Chaos Magical Hats | `2372506` | [Scripts/c2372506.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c2372506.lua) | 2 |
| Isolde, Two Tales of the Noble Knights | `59934749` | [Scripts/c59934749.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c59934749.lua) | 1 |
| Ojamassimilation | `2390019` | [Scripts/c2390019.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c2390019.lua) | 2 |
| Cyberse Reminder | `56337500` | [Scripts/c56337500.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c56337500.lua) | 1 |
| Vanquish Soul Trinity Burst | `53330789` | [Scripts/c53330789.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c53330789.lua) | 1 |
| Power Tool Braver Dragon | `63265554` | [Scripts/c63265554.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c63265554.lua) | 1 |
| Alba System Dogmatikalamity | `93053159` | [Scripts/c93053159.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c93053159.lua) | 2 |
| Prank-Kids Bow-Wow-Bark | `43886072` | [Scripts/c43886072.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c43886072.lua) | 1 |
| Super Quantal Mech Ship Magnacarrier | `10424147` | [Scripts/c10424147.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c10424147.lua) | 1 |
| Divine Serpent Apophis | `97800311` | [Scripts/c97800311.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c97800311.lua) | 1 |
| Erebus the Underworld Monarch | `23064604` | [Scripts/c23064604.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c23064604.lua) | 1 |
| World Legacy Monstrosity | `14604710` | [Scripts/c14604710.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c14604710.lua) | 1 |
| Numeron Calling | `77402960` | [Scripts/c77402960.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c77402960.lua) | 1 |
| Dual Avatar - Manifested A-Un | `28798938` | [Scripts/c28798938.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c28798938.lua) | 2 |
| ...and 189 more |  |  |  |

## Script Examples

### Ehther the Heavenly Monarch (`96570609`)

Source: [Scripts/c96570609.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c96570609.lua)

```lua
	if g:GetClassCount(Card.GetCode)<2 then return end
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_TOGRAVE)
	local tg1=g:SelectSubGroup(tp,aux.dncheck,false,2,2)
	if Duel.SendtoGrave(tg1,REASON_EFFECT)~=0 and tg1:IsExists(Card.IsLocation,2,nil,LOCATION_GRAVE)
		and Duel.GetLocationCount(tp,LOCATION_MZONE)>0 then
```

### Pere-Zenet Em Heru (`46273941`)

Source: [Scripts/c46273941.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c46273941.lua)

```lua
function s.gcheckf(tc,lv)
	return function(sg,ec)
		if not aux.dncheck(sg) then return false end
		if ec then
			return sg:GetSum(s.getrlv,tc)-s.getrlv(ec,tc)<=lv
```

### Am Duazenet (`45151304`)

Source: [Scripts/c45151304.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c45151304.lua)

```lua
function s.gcheckf(tc,lv)
	return function(sg,ec)
		if not aux.dncheck(sg) then return false end
		if ec then
			return sg:GetSum(s.getrlv,tc)-s.getrlv(ec,tc)<=lv
```
