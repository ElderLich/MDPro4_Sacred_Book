# Group.CheckWithSumGreater

## Signature

```lua
Group.CheckWithSumGreater(Group g, function f, int acc, [... any]) -> bool
```

## Description

Checks whether g can satisfy an f-sum of at least acc.
Cards previously set with Duel.SetSelectedCard are forced into the sum and the must-select list is cleared before returning.

## Parameters

- `g` `Group`
- `f` `function`
- `acc` `int`
- `...` `any` optional

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libgroup.cpp:922`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **15** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Group.CheckWithSumGreater) with `Group.CheckWithSumGreater`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Meteoroa Drytron](/examples/cards/24166324) | `24166324` | [Scripts/c24166324.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24166324.lua) | 1 |
| [Pere-Zenet Em Heru](/examples/cards/46273941) | `46273941` | [Scripts/c46273941.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c46273941.lua) | 1 |
| [Am Duazenet](/examples/cards/45151304) | `45151304` | [Scripts/c45151304.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c45151304.lua) | 1 |
| Meteonis Drytron | `22398665` | [Scripts/c22398665.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c22398665.lua) | 1 |
| Theia, the Primal Being | `85687952` | [Scripts/c85687952.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c85687952.lua) | 1 |
| Machina Ruinforce | `46033517` | [Scripts/c46033517.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c46033517.lua) | 2 |
| Subterror Nemesis Warrior | `16719140` | [Scripts/c16719140.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c16719140.lua) | 1 |
| Toon Black Luster Soldier | `28711704` | [Scripts/c28711704.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c28711704.lua) | 1 |
| Machina Fortress | `5556499` | [Scripts/c5556499.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c5556499.lua) | 2 |
| Kozmo Dark Planet | `85991529` | [Scripts/c85991529.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c85991529.lua) | 2 |
| King Beast Barbaros | `63972571` | [Scripts/c63972571.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63972571.lua) | 1 |
| Armor Dragon Ritual | `58827995` | [Scripts/c58827995.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c58827995.lua) | 1 |
| Ten Thousand Dragon | `10000` | [Scripts/c10000.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c10000.lua) | 1 |
| Duck Fighter | `54813225` | [Scripts/c54813225.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c54813225.lua) | 1 |
| Emperor Tanuki's Critter Count | `20560620` | [Scripts/c20560620.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c20560620.lua) | 1 |

## Script Examples

### Meteoroa Drytron (`24166324`)

Source: [Scripts/c24166324.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24166324.lua)

```lua
	if atk==0 then return false end
	Duel.SetSelectedCard(g)
	return g:CheckWithSumGreater(aux.GetCappedAttack,atk)
end
function s.RitualCheckEqual(g,c,atk)
```

### Pere-Zenet Em Heru (`46273941`)

Source: [Scripts/c46273941.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c46273941.lua)

```lua
	if Duel.GetMZoneCount(tp,g)<=0 then return false end
	Duel.SetSelectedCard(g)
	return g:CheckWithSumGreater(s.getrlv,lv,c)
end
function s.spfilter(c,e,tp,m)
```

### Am Duazenet (`45151304`)

Source: [Scripts/c45151304.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c45151304.lua)

```lua
	if Duel.GetMZoneCount(tp,g)<=0 then return false end
	Duel.SetSelectedCard(g)
	return g:CheckWithSumGreater(s.getrlv,lv,c)
end
function s.spfilter(c,e,tp,m)
```
