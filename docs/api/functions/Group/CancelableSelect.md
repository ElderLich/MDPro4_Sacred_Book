# Group.CancelableSelect

## Signature

```lua
Group.CancelableSelect(Group g, int player, int min, int max, [Card|Group|nil ex]) -> Group
```

## Description

Lets player select min to max cards from g, excluding ex; the selection can be canceled and return nil.

## Parameters

- `g` `Group`
- `player` `int`
- `min` `int`
- `max` `int`
- `ex` `Card|Group|nil` optional

## Returns

- `Group`

## Source

- `D:\Programs\GitHub\ygopro-core\libgroup.cpp:918`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **30** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Group.CancelableSelect`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Meklord Astro Mekanikle | `63468625` | [Scripts/c63468625.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63468625.lua) | 57 |
| Yummy☆Surprise | `29369059` | [Scripts/c29369059.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c29369059.lua) | 55 |
| Spirit Poacher | `85150300` | [Scripts/c85150300.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c85150300.lua) | 54 |
| Black Chaos the Ultimate Magical Swordsman | `98684220` | [Scripts/c98684220.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c98684220.lua) | 51 |
| SPYRAL Sleeper | `35699` | [Scripts/c35699.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c35699.lua) | 47 |
| Heavy Beetrooper Mighty Neptune | `14357527` | [Scripts/c14357527.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c14357527.lua) | 47 |
| Chaos Dragon Levianeer | `55878038` | [Scripts/c55878038.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c55878038.lua) | 46 |
| Chaotic Elements | `92221402` | [Scripts/c92221402.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92221402.lua) | 46 |
| Ultimate Conductor Tyranno | `18940556` | [Scripts/c18940556.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c18940556.lua) | 45 |
| Overtex Qoatlus | `41782653` | [Scripts/c41782653.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c41782653.lua) | 43 |
| Regenesis Overlord | `47082621` | [Scripts/c47082621.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c47082621.lua) | 43 |
| Degrade Buster | `50426119` | [Scripts/c50426119.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c50426119.lua) | 43 |
| Dark Necrofear | `31829185` | [Scripts/c31829185.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c31829185.lua) | 42 |
| Batteryman Industrial Strength | `19441018` | [Scripts/c19441018.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c19441018.lua) | 42 |
| Block Dragon | `94689206` | [Scripts/c94689206.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c94689206.lua) | 41 |
| Enishi, Shien's Chancellor | `38280762` | [Scripts/c38280762.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c38280762.lua) | 41 |
| Akz, the Pumer | `38837163` | [Scripts/c38837163.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c38837163.lua) | 38 |
| Hieratic Dragon of Sutekh | `66789970` | [Scripts/c66789970.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c66789970.lua) | 38 |
| Knight of the Red Lotus | `46237548` | [Scripts/c46237548.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c46237548.lua) | 37 |
| Beargram, Shelled Emperor of the Forest Crown | `27134209` | [Scripts/c27134209.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c27134209.lua) | 36 |
| Gaia Plate the Earth Giant | `14258627` | [Scripts/c14258627.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c14258627.lua) | 36 |
| Gigastone Omega | `79080761` | [Scripts/c79080761.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c79080761.lua) | 35 |
| Montage Dragon | `23303072` | [Scripts/c23303072.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c23303072.lua) | 31 |
| Fenrir | `218704` | [Scripts/c218704.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c218704.lua) | 30 |
| ...and 6 more |  |  |  |

## Script Examples

### Meklord Astro Mekanikle (`63468625`)

Source: [Scripts/c63468625.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63468625.lua)

```lua
	local g=Duel.GetMatchingGroup(c63468625.spfilter,tp,LOCATION_HAND,0,c)
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_TOGRAVE)
	local sg=g:CancelableSelect(tp,3,3,nil)
	if sg then
		sg:KeepAlive()
```

### Yummy☆Surprise (`29369059`)

Source: [Scripts/c29369059.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c29369059.lua)

```lua
				if fg:GetCount()>0 and Duel.SelectYesNo(tp,aux.Stringid(id,4)) then
					Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_TOFIELD)
					local tfg=fg:CancelableSelect(tp,1,1,nil)
					if not tfg then goto cancel end
					tfc=tfg:GetFirst()
```

### Spirit Poacher (`85150300`)

Source: [Scripts/c85150300.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c85150300.lua)

```lua
		if sg:GetCount()==0 or not Duel.SelectYesNo(1-tp,aux.Stringid(id,4)) then return false end
		Duel.Hint(HINT_SELECTMSG,1-tp,HINTMSG_SPSUMMON)
		local g=sg:CancelableSelect(1-tp,1,1,nil)
		if g==nil or g:GetCount()==0 then goto cancel end
		local tc=g:GetFirst()
```
