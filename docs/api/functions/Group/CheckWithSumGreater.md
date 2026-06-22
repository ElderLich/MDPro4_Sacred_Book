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

- Detected in **13** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Group.CheckWithSumGreater`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Meteoroa Drytron](/examples/cards/24166324) | `24166324` | [Scripts/c24166324.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24166324.lua) | 67 |
| Meteonis Drytron | `22398665` | [Scripts/c22398665.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c22398665.lua) | 58 |
| Theia, the Primal Being | `85687952` | [Scripts/c85687952.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c85687952.lua) | 56 |
| Subterror Nemesis Warrior | `16719140` | [Scripts/c16719140.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c16719140.lua) | 51 |
| Machina Ruinforce | `46033517` | [Scripts/c46033517.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c46033517.lua) | 50 |
| Toon Black Luster Soldier | `28711704` | [Scripts/c28711704.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c28711704.lua) | 50 |
| Machina Fortress | `5556499` | [Scripts/c5556499.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c5556499.lua) | 50 |
| Kozmo Dark Planet | `85991529` | [Scripts/c85991529.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c85991529.lua) | 47 |
| King Beast Barbaros | `63972571` | [Scripts/c63972571.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63972571.lua) | 43 |
| Armor Dragon Ritual | `58827995` | [Scripts/c58827995.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c58827995.lua) | 37 |
| Ten Thousand Dragon | `10000` | [Scripts/c10000.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c10000.lua) | 32 |
| Duck Fighter | `54813225` | [Scripts/c54813225.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c54813225.lua) | 26 |
| Emperor Tanuki's Critter Count | `20560620` | [Scripts/c20560620.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c20560620.lua) | 24 |

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

### Meteonis Drytron (`22398665`)

Source: [Scripts/c22398665.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c22398665.lua)

```lua
	if atk==0 then return false end
	Duel.SetSelectedCard(g)
	return g:CheckWithSumGreater(aux.GetCappedAttack,atk)
end
function c22398665.RitualCheckEqual(g,c,atk)
```

### Theia, the Primal Being (`85687952`)

Source: [Scripts/c85687952.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c85687952.lua)

```lua
function s.relgoal(sg,tp)
	Duel.SetSelectedCard(sg)
	return sg:CheckWithSumGreater(Card.GetLevel,11) and aux.mzctcheckrel(sg,tp)
end
function s.spcon(e,tp,eg,ep,ev,re,r,rp)
```
