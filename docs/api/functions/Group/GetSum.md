# Group.GetSum

## Signature

```lua
Group.GetSum(Group g, function f, ... any) -> int
```

## Description

Calls f for each card in g, forwards any extra arguments, and returns the sum of the integer values produced.

## Parameters

- `g` `Group`
- `f` `function`
- `...` `any`

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libgroup.cpp:926`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **147** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Group.GetSum) with `Group.GetSum`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Meteoroa Drytron](/examples/cards/24166324) | `24166324` | [Scripts/c24166324.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24166324.lua) | 2 |
| [Pere-Zenet Em Heru](/examples/cards/46273941) | `46273941` | [Scripts/c46273941.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c46273941.lua) | 1 |
| [Am Duazenet](/examples/cards/45151304) | `45151304` | [Scripts/c45151304.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c45151304.lua) | 1 |
| [Converging Wishes](/examples/cards/20007374) | `20007374` | [Scripts/c20007374.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c20007374.lua) | 1 |
| [D/D Count Surveyor](/examples/cards/5997110) | `5997110` | [Scripts/c5997110.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c5997110.lua) | 2 |
| [Nekroz Kaleidoscope](/examples/cards/51124303) | `51124303` | [Scripts/c51124303.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c51124303.lua) | 2 |
| [D/D/D/D Super-Dimensional Sovereign Emperor Zero Paradox](/examples/cards/97417863) | `97417863` | [Scripts/c97417863.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c97417863.lua) | 2 |
| Frightfur Meister | `77522571` | [Scripts/c77522571.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c77522571.lua) | 2 |
| Sonic Tracker | `17888577` | [Scripts/c17888577.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c17888577.lua) | 1 |
| Meteonis Drytron | `22398665` | [Scripts/c22398665.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c22398665.lua) | 2 |
| Awakening of the Sacred Beasts | `53701259` | [Scripts/c53701259.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c53701259.lua) | 2 |
| Black Garden | `71645242` | [Scripts/c71645242.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71645242.lua) | 1 |
| Blessing of the Voiceless Voice | `39114494` | [Scripts/c39114494.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c39114494.lua) | 1 |
| Horn of Olifant | `55749927` | [Scripts/c55749927.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c55749927.lua) | 1 |
| Gunkan Sushipyard Seaside Supper Spot | `62200831` | [Scripts/c62200831.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c62200831.lua) | 1 |
| Crealtar, the Impcantation Originator | `96915510` | [Scripts/c96915510.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c96915510.lua) | 1 |
| Synchro Panic | `83962752` | [Scripts/c83962752.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c83962752.lua) | 1 |
| Drytron Meteonis DA Draconids | `56863746` | [Scripts/c56863746.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c56863746.lua) | 1 |
| Madolche Dessert | `51650038` | [Scripts/c51650038.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c51650038.lua) | 1 |
| Eternal Bond | `45283341` | [Scripts/c45283341.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c45283341.lua) | 1 |
| Marincess Cascade | `27012990` | [Scripts/c27012990.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c27012990.lua) | 1 |
| Melffy Staring Contest | `76981308` | [Scripts/c76981308.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c76981308.lua) | 1 |
| Raidraptor - Rising Rebellion Falcon | `71222868` | [Scripts/c71222868.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71222868.lua) | 2 |
| Armed Dragon LV10 White | `84425220` | [Scripts/c84425220.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c84425220.lua) | 2 |
| ...and 123 more |  |  |  |

## Script Examples

### Meteoroa Drytron (`24166324`)

Source: [Scripts/c24166324.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24166324.lua)

```lua
	if greater_or_equal=="Equal" then
		return  function(g)
					return (not aux.RGCheckAdditional or aux.RGCheckAdditional(g)) and g:GetSum(aux.GetCappedAttack)<=atk
				end
	else
```

### Pere-Zenet Em Heru (`46273941`)

Source: [Scripts/c46273941.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c46273941.lua)

```lua
		if not aux.dncheck(sg) then return false end
		if ec then
			return sg:GetSum(s.getrlv,tc)-s.getrlv(ec,tc)<=lv
		else
			return true
```

### Am Duazenet (`45151304`)

Source: [Scripts/c45151304.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c45151304.lua)

```lua
		if not aux.dncheck(sg) then return false end
		if ec then
			return sg:GetSum(s.getrlv,tc)-s.getrlv(ec,tc)<=lv
		else
			return true
```
