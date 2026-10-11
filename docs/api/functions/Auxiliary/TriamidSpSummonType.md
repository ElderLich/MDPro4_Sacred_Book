# Auxiliary.TriamidSpSummonType

## Signature

```lua
Auxiliary.TriamidSpSummonType(Card c) -> bool
```

## Description

Returns whether c is a Special Summon procedure monster, used by Triamid Special Summon helpers.

## Parameters

- `c` `Card`

## Returns

- `bool`

## Source

- `Utilities/utility.lua:1095`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **3** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Auxiliary.TriamidSpSummonType) with `Auxiliary.TriamidSpSummonType`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Triamid Pulse | `96100333` | [Scripts/c96100333.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c96100333.lua) | 3 |
| Triamid Loading | `64576557` | [Scripts/c64576557.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c64576557.lua) | 3 |
| Triamid Kingolem | `72772445` | [Scripts/c72772445.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c72772445.lua) | 3 |

## Script Examples

### Triamid Pulse (`96100333`)

Source: [Scripts/c96100333.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c96100333.lua)

```lua
end
function c96100333.spfilter(c,e,tp)
	return c:IsRace(RACE_ROCK) and c:IsCanBeSpecialSummoned(e,0,tp,false,aux.TriamidSpSummonType(c),POS_FACEUP_DEFENSE)
end
function c96100333.sptg(e,tp,eg,ep,ev,re,r,rp,chk,chkc)
```

### Triamid Loading (`64576557`)

Source: [Scripts/c64576557.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c64576557.lua)

```lua
end
function c64576557.spfilter(c,e,tp,eg)
	return c:IsSetCard(0xe2) and c:IsCanBeSpecialSummoned(e,0,tp,false,aux.TriamidSpSummonType(c)) and not eg:IsExists(Card.IsCode,1,nil,c:GetCode())
end
function c64576557.sptg(e,tp,eg,ep,ev,re,r,rp,chk)
```

### Triamid Kingolem (`72772445`)

Source: [Scripts/c72772445.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c72772445.lua)

```lua
end
function c72772445.spfilter(c,e,tp)
	return c:IsSetCard(0xe2) and c:IsCanBeSpecialSummoned(e,0,tp,false,aux.TriamidSpSummonType(c))
end
function c72772445.sptg(e,tp,eg,ep,ev,re,r,rp,chk)
```
