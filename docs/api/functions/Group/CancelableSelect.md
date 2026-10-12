# Group.CancelableSelect

## Signature

```lua
Group.CancelableSelect(Group g, int player, int min, int max, [Card|Group|nil ex]) -> Group|nil
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

- `Group|nil`

## Source

- `D:\Programs\GitHub\ygopro-core\libgroup.cpp:918`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **31** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Group.CancelableSelect) with `Group.CancelableSelect`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Destiny HERO - Destro-Dogma](/examples/cards/25158975) | `25158975` | [Scripts/c25158975.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c25158975.lua) | 1 |
| Meklord Astro Mekanikle | `63468625` | [Scripts/c63468625.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c63468625.lua) | 1 |
| Yummy☆Surprise | `29369059` | [Scripts/c29369059.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c29369059.lua) | 1 |
| Spirit Poacher | `85150300` | [Scripts/c85150300.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c85150300.lua) | 1 |
| Black Chaos | `98684220` | [Scripts/c98684220.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c98684220.lua) | 1 |
| SPYRAL Sleeper | `35699` | [Scripts/c35699.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c35699.lua) | 1 |
| Heavy Beetrooper Mighty Neptune | `14357527` | [Scripts/c14357527.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c14357527.lua) | 1 |
| Chaos Dragon Levianeer | `55878038` | [Scripts/c55878038.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c55878038.lua) | 1 |
| Chaotic Elements | `92221402` | [Scripts/c92221402.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c92221402.lua) | 1 |
| Ultimate Conductor Tyranno | `18940556` | [Scripts/c18940556.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c18940556.lua) | 1 |
| Regenesis Overlord | `47082621` | [Scripts/c47082621.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c47082621.lua) | 1 |
| Overtex Qoatlus | `41782653` | [Scripts/c41782653.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c41782653.lua) | 1 |
| Degrade Buster | `50426119` | [Scripts/c50426119.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c50426119.lua) | 1 |
| Dark Necrofear | `31829185` | [Scripts/c31829185.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c31829185.lua) | 1 |
| Batteryman Industrial Strength | `19441018` | [Scripts/c19441018.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c19441018.lua) | 1 |
| Block Dragon | `94689206` | [Scripts/c94689206.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c94689206.lua) | 1 |
| Enishi, Shien's Chancellor | `38280762` | [Scripts/c38280762.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c38280762.lua) | 1 |
| Akz, the Pumer | `38837163` | [Scripts/c38837163.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c38837163.lua) | 1 |
| Hieratic Dragon of Sutekh | `66789970` | [Scripts/c66789970.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c66789970.lua) | 1 |
| Knight of the Red Lotus | `46237548` | [Scripts/c46237548.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c46237548.lua) | 1 |
| Beargram, Shelled Emperor of the Forest Crown | `27134209` | [Scripts/c27134209.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c27134209.lua) | 1 |
| Gaia Plate the Earth Giant | `14258627` | [Scripts/c14258627.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c14258627.lua) | 1 |
| Gigastone Omega | `79080761` | [Scripts/c79080761.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c79080761.lua) | 1 |
| Montage Dragon | `23303072` | [Scripts/c23303072.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c23303072.lua) | 1 |
| ...and 7 more |  |  |  |

## Script Examples

### Destiny HERO - Destro-Dogma (`25158975`)

Source: [Scripts/c25158975.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c25158975.lua)

```lua
	local g=Duel.GetMatchingGroup(s.spfilter,tp,LOCATION_GRAVE,0,c)
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_REMOVE)
	local sg=g:CancelableSelect(tp,3,3,nil)
	if sg then
		sg:KeepAlive()
```

### Meklord Astro Mekanikle (`63468625`)

Source: [Scripts/c63468625.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c63468625.lua)

```lua
	local g=Duel.GetMatchingGroup(c63468625.spfilter,tp,LOCATION_HAND,0,c)
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_TOGRAVE)
	local sg=g:CancelableSelect(tp,3,3,nil)
	if sg then
		sg:KeepAlive()
```

### Yummy☆Surprise (`29369059`)

Source: [Scripts/c29369059.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c29369059.lua)

```lua
				if fg:GetCount()>0 and Duel.SelectYesNo(tp,aux.Stringid(id,4)) then
					Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_TOFIELD)
					local tfg=fg:CancelableSelect(tp,1,1,nil)
					if not tfg then goto cancel end
					tfc=tfg:GetFirst()
```
