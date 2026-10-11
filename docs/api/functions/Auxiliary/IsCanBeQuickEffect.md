# Auxiliary.IsCanBeQuickEffect

## Signature

```lua
Auxiliary.IsCanBeQuickEffect(Card c, int tp, int code) -> bool
```

## Description

Checks whether player tp is affected by code, code has a registered quick-effect filter, and that filter accepts c.

## Parameters

- `c` `Card`
- `tp` `int`
- `code` `int`

## Returns

- `bool`

## Source

- `Utilities/utility.lua:1993`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **16** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Auxiliary.IsCanBeQuickEffect) with `Auxiliary.IsCanBeQuickEffect`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Enlilgirsu, the Orcust Mekk-Knight | `74820316` | [Scripts/c74820316.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74820316.lua) | 4 |
| Chaos Allure Queen | `29925614` | [Scripts/c29925614.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c29925614.lua) | 2 |
| Allure Queen LV5 | `23756165` | [Scripts/c23756165.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c23756165.lua) | 2 |
| Ars Magna of Purification and Corruption | `62368221` | [Scripts/c62368221.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c62368221.lua) | 2 |
| Ars Magna of Infinity and Finity | `36270527` | [Scripts/c36270527.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c36270527.lua) | 2 |
| Allure Queen LV3 | `87257460` | [Scripts/c87257460.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c87257460.lua) | 2 |
| Ars Magna of Unification and Separation | `99753860` | [Scripts/c99753860.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c99753860.lua) | 2 |
| Galatea-I, the Orcust Automaton | `48835607` | [Scripts/c48835607.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c48835607.lua) | 2 |
| Longirsu, the Orcust Orchestrator | `76145142` | [Scripts/c76145142.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c76145142.lua) | 2 |
| Galatea, the Orcust Automaton | `30741503` | [Scripts/c30741503.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30741503.lua) | 2 |
| Orcustrion | `3134857` | [Scripts/c3134857.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c3134857.lua) | 2 |
| Orcust Knightmare | `4055337` | [Scripts/c4055337.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c4055337.lua) | 2 |
| Allure Queen LV7 | `50140163` | [Scripts/c50140163.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c50140163.lua) | 2 |
| Orcust Cymbal Skeleton | `21441617` | [Scripts/c21441617.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c21441617.lua) | 2 |
| Orcust Brass Bombard | `94046012` | [Scripts/c94046012.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c94046012.lua) | 2 |
| Orcust Harp Horror | `57835716` | [Scripts/c57835716.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c57835716.lua) | 2 |

## Script Examples

### Enlilgirsu, the Orcust Mekk-Knight (`74820316`)

Source: [Scripts/c74820316.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74820316.lua)

```lua
end
function s.thcon1(e,tp,eg,ep,ev,re,r,rp)
	return not aux.IsCanBeQuickEffect(e:GetHandler(),tp,90351981)
end
function s.thcon2(e,tp,eg,ep,ev,re,r,rp)
```

### Chaos Allure Queen (`29925614`)

Source: [Scripts/c29925614.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c29925614.lua)

```lua
end
function s.eqcon1(e,tp,eg,ep,ev,re,r,rp)
	return not aux.IsCanBeQuickEffect(e:GetHandler(),tp,95937545)
end
function s.eqcon2(e,tp,eg,ep,ev,re,r,rp)
```

### Allure Queen LV5 (`23756165`)

Source: [Scripts/c23756165.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c23756165.lua)

```lua
function c23756165.eqcon1(e,tp,eg,ep,ev,re,r,rp)
	local c=e:GetHandler()
	return c:GetFlagEffect(id+1)>0 and not aux.IsSelfEquip(c,FLAG_ID_ALLURE_QUEEN) and not aux.IsCanBeQuickEffect(c,tp,95937545)
end
function c23756165.eqcon2(e,tp,eg,ep,ev,re,r,rp)
```
