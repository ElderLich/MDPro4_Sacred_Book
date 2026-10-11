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

- `Utilities/utility.lua:1398`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **35** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Auxiliary.SelectTargetFromFieldFirst) with `Auxiliary.SelectTargetFromFieldFirst`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Melffy Playtime Surprise](/examples/cards/58036097) | `58036097` | [Scripts/c58036097.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c58036097.lua) | 1 |
| S:P Little Knight | `29301450` | [Scripts/c29301450.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c29301450.lua) | 1 |
| Zoroa, the Magistus Verethragna | `37260677` | [Scripts/c37260677.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c37260677.lua) | 1 |
| Snake-Eyes Vengeance Dragon | `79415624` | [Scripts/c79415624.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c79415624.lua) | 1 |
| Snake-Eyes Flamberge Dragon | `48452496` | [Scripts/c48452496.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c48452496.lua) | 1 |
| Metalfoes Vanisher | `56518311` | [Scripts/c56518311.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c56518311.lua) | 1 |
| Primite Roar | `92501449` | [Scripts/c92501449.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92501449.lua) | 1 |
| Primite Howl | `41488249` | [Scripts/c41488249.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c41488249.lua) | 1 |
| Ars Magna - "Philosophirum" | `90728287` | [Scripts/c90728287.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c90728287.lua) | 1 |
| Startling Stare of the Snake-Eyes | `74906081` | [Scripts/c74906081.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74906081.lua) | 1 |
| Filia Regis | `70538272` | [Scripts/c70538272.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c70538272.lua) | 1 |
| The Undying Legion | `43355214` | [Scripts/c43355214.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c43355214.lua) | 1 |
| Adamancipator Crystal - Tiamite | `51420096` | [Scripts/c51420096.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c51420096.lua) | 1 |
| Exosister Returnia | `197042` | [Scripts/c197042.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c197042.lua) | 1 |
| Strength in Unity | `96239878` | [Scripts/c96239878.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c96239878.lua) | 1 |
| Dragonmaid Tidying | `57416183` | [Scripts/c57416183.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c57416183.lua) | 1 |
| Adamancipator Luminous | `41458361` | [Scripts/c41458361.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c41458361.lua) | 1 |
| Regenesis Overlord | `47082621` | [Scripts/c47082621.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c47082621.lua) | 1 |
| Vernusylph in Full Bloom | `7206349` | [Scripts/c7206349.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c7206349.lua) | 1 |
| Blitzclique Return Stroke | `23526128` | [Scripts/c23526128.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c23526128.lua) | 1 |
| Exosister Mikailis | `42741437` | [Scripts/c42741437.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c42741437.lua) | 1 |
| S-Force World Sorting | `11642993` | [Scripts/c11642993.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c11642993.lua) | 1 |
| Expurrely Noir | `83827392` | [Scripts/c83827392.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c83827392.lua) | 1 |
| Virgil, Rock Star of the Burning Abyss | `601193` | [Scripts/c601193.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c601193.lua) | 1 |
| ...and 11 more |  |  |  |

## Script Examples

### Melffy Playtime Surprise (`58036097`)

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
