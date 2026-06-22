# Duel.Readjust

## Signature

```lua
Duel.Readjust() -> void
```

## Description

Requests a field readjust for the current reason effect's handler.
If the same handler requests readjustment more than three times in the current tracking map, the core sends it to the Graveyard by rule instead.

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4962`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **10** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Duel.Readjust`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Ocean Dragon Lord - Kairyu-Shin | `23931679` | [Scripts/c23931679.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c23931679.lua) | 43 |
| Double Fusion | `10218411` | [Scripts/c10218411.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c10218411.lua) | 41 |
| There Can Be Only One | `24207889` | [Scripts/c24207889.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24207889.lua) | 32 |
| Pole Position | `73578229` | [Scripts/c73578229.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c73578229.lua) | 30 |
| Kotodama | `19406822` | [Scripts/c19406822.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c19406822.lua) | 29 |
| Gozen Match | `53334471` | [Scripts/c53334471.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c53334471.lua) | 29 |
| Rivalry of Warlords | `90846359` | [Scripts/c90846359.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c90846359.lua) | 29 |
| Spatial Collapse | `20644748` | [Scripts/c20644748.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c20644748.lua) | 24 |
| True Exodia | `37984331` | [Scripts/c37984331.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c37984331.lua) | 19 |
| Call of Darkness | `78637313` | [Scripts/c78637313.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c78637313.lua) | 19 |

## Script Examples

### Ocean Dragon Lord - Kairyu-Shin (`23931679`)

Source: [Scripts/c23931679.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c23931679.lua)

```lua
	if g1:GetCount()>0 then
		Duel.SendtoGrave(g1,REASON_RULE)
		Duel.Readjust()
	end
end
```

### Double Fusion (`10218411`)

Source: [Scripts/c10218411.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c10218411.lua)

```lua
function s.activate(e,tp,eg,ep,ev,re,r,rp)
	if s.fop(e,tp,eg,ep,ev,re,r,rp)>0 then
		Duel.Readjust()
		if s.fcon(e,tp) and Duel.SelectYesNo(tp,aux.Stringid(id,1)) then
			Duel.BreakEffect()
```

### There Can Be Only One (`24207889`)

Source: [Scripts/c24207889.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24207889.lua)

```lua
	if sg:GetCount()>0 then
		Duel.SendtoGrave(sg,REASON_RULE)
		Duel.Readjust()
	end
	for p=0,1 do
```
