# Auxiliary.SelectTargetFromFieldFirst

## Signature

```lua
Auxiliary.SelectTargetFromFieldFirst(int tp, function f, int player, int s, int o, int min, int max, any ex, ... any) -> Group
```

## Description

Target-selection helper that first offers matching on-field effect targets with HINTMSG_FIELD_FIRST. If accepted, it sets those cards as targets; otherwise it restores the previous hint and falls back to Duel.SelectTarget.

## Parameters

- `tp` `int`
- `f` `function`
- `player` `int`
- `s` `int`
- `o` `int`
- `min` `int`
- `max` `int`
- `ex` `any`
- `...` `any`

## Returns

- `Group` - The selected target cards.

## Source

- `Utilities/utility.lua:1395`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **32** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Auxiliary.SelectTargetFromFieldFirst`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Exciting Melffy Time](/examples/cards/58036097) | `58036097` | [Scripts/c58036097.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c58036097.lua) | 69 |
| S:P Little Knight | `29301450` | [Scripts/c29301450.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c29301450.lua) | 58 |
| Zoroa, the Magistus Verethragna | `37260677` | [Scripts/c37260677.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c37260677.lua) | 57 |
| Snake-Eyes Vengeance Dragon | `79415624` | [Scripts/c79415624.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c79415624.lua) | 52 |
| Snake-Eyes Flamberge Dragon | `48452496` | [Scripts/c48452496.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c48452496.lua) | 50 |
| Metalfoes Vanisher | `56518311` | [Scripts/c56518311.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c56518311.lua) | 49 |
| Primite Roar | `92501449` | [Scripts/c92501449.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92501449.lua) | 49 |
| Primite Howl | `41488249` | [Scripts/c41488249.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c41488249.lua) | 49 |
| Startling Stare of the Snake-Eyes | `74906081` | [Scripts/c74906081.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74906081.lua) | 48 |
| Filia Regis | `70538272` | [Scripts/c70538272.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c70538272.lua) | 47 |
| The Undying Legion | `43355214` | [Scripts/c43355214.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c43355214.lua) | 46 |
| Exosister Returnia | `197042` | [Scripts/c197042.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c197042.lua) | 46 |
| Strength in Unity | `96239878` | [Scripts/c96239878.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c96239878.lua) | 46 |
| Dragonmaid Tidying | `57416183` | [Scripts/c57416183.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c57416183.lua) | 46 |
| Vernusylph in Full Bloom | `7206349` | [Scripts/c7206349.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c7206349.lua) | 43 |
| Blitzclique - Return Stroke | `23526128` | [Scripts/c23526128.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c23526128.lua) | 43 |
| Exosister Mikailis | `42741437` | [Scripts/c42741437.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c42741437.lua) | 43 |
| Regenesis Overlord | `47082621` | [Scripts/c47082621.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c47082621.lua) | 43 |
| S-Force Sorted World | `11642993` | [Scripts/c11642993.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c11642993.lua) | 40 |
| Expurrely Noir | `83827392` | [Scripts/c83827392.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c83827392.lua) | 40 |
| Virgil, Rock Star of the Burning Abyss | `601193` | [Scripts/c601193.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c601193.lua) | 40 |
| Swordsoul Auspice Chunjun | `29884951` | [Scripts/c29884951.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c29884951.lua) | 39 |
| Skeletal Dragon Felgrand | `65187687` | [Scripts/c65187687.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c65187687.lua) | 39 |
| Dark Contract with the Different Dimension | `54936778` | [Scripts/c54936778.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c54936778.lua) | 39 |
| ...and 8 more |  |  |  |

## Script Examples

### Exciting Melffy Time (`58036097`)

Source: [Scripts/c58036097.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c58036097.lua)

```lua
	if chk==0 then return Duel.IsExistingTarget(s.thfilter,tp,LOCATION_MZONE+LOCATION_GRAVE,0,1,nil) end
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_RTOHAND)
	local g=aux.SelectTargetFromFieldFirst(tp,s.thfilter,tp,LOCATION_MZONE+LOCATION_GRAVE,0,1,1,nil)
	Duel.SetOperationInfo(0,CATEGORY_TOHAND,g,1,0,0)
end
```

### S:P Little Knight (`29301450`)

Source: [Scripts/c29301450.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c29301450.lua)

```lua
	if chk==0 then return Duel.IsExistingTarget(Card.IsAbleToRemove,tp,LOCATION_GRAVE+LOCATION_ONFIELD,LOCATION_GRAVE+LOCATION_ONFIELD,1,nil) end
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_REMOVE)
	local g=aux.SelectTargetFromFieldFirst(tp,Card.IsAbleToRemove,tp,LOCATION_GRAVE+LOCATION_ONFIELD,LOCATION_GRAVE+LOCATION_ONFIELD,1,1,nil)
	Duel.SetOperationInfo(0,CATEGORY_REMOVE,g,1,0,0)
end
```

### Zoroa, the Magistus Verethragna (`37260677`)

Source: [Scripts/c37260677.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c37260677.lua)

```lua
		and Duel.IsExistingTarget(s.eqfilter,tp,LOCATION_GRAVE,LOCATION_ONFIELD,1,nil,tp) end
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_EQUIP)
	local g=aux.SelectTargetFromFieldFirst(tp,s.eqfilter,tp,LOCATION_GRAVE,LOCATION_ONFIELD,1,1,nil,tp)
	if g:FilterCount(Card.IsLocation,nil,LOCATION_GRAVE)>0 then
		Duel.SetOperationInfo(0,CATEGORY_LEAVE_GRAVE,g,1,0,0)
```
