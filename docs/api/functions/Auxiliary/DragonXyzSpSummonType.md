# Auxiliary.DragonXyzSpSummonType

## Signature

```lua
Auxiliary.DragonXyzSpSummonType(Card c) -> bool
```

## Description

Returns true only for Soul Drain Dragon, used as a Special Summon procedure-type helper.

## Parameters

- `c` `Card`

## Returns

- `bool`

## Source

- `Utilities/utility.lua:1089`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **4** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Auxiliary.DragonXyzSpSummonType) with `Auxiliary.DragonXyzSpSummonType`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Number 46: Dragluon | `2978414` | [Scripts/c2978414.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c2978414.lua) | 3 |
| Queen Dragun Djinn | `90726340` | [Scripts/c90726340.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c90726340.lua) | 3 |
| Galaxy Stealth Dragon | `54358015` | [Scripts/c54358015.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c54358015.lua) | 3 |
| Hieratic Dragon King of Atum | `27337596` | [Scripts/c27337596.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c27337596.lua) | 3 |

## Script Examples

### Number 46: Dragluon (`2978414`)

Source: [Scripts/c2978414.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c2978414.lua)

```lua
end
function c2978414.spfilter(c,e,tp)
	return c:IsRace(RACE_DRAGON) and c:IsCanBeSpecialSummoned(e,0,tp,false,aux.DragonXyzSpSummonType(c))
end
function c2978414.sptg(e,tp,eg,ep,ev,re,r,rp,chk)
```

### Queen Dragun Djinn (`90726340`)

Source: [Scripts/c90726340.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c90726340.lua)

```lua
end
function c90726340.spfilter(c,e,tp)
	return c:IsLevelAbove(5) and c:IsRace(RACE_DRAGON) and c:IsCanBeSpecialSummoned(e,0,tp,false,aux.DragonXyzSpSummonType(c))
end
function c90726340.sptg(e,tp,eg,ep,ev,re,r,rp,chk,chkc)
```

### Galaxy Stealth Dragon (`54358015`)

Source: [Scripts/c54358015.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c54358015.lua)

```lua
end
function c54358015.spfilter(c,e,tp)
	return c:IsRace(RACE_DRAGON) and c:IsCanBeSpecialSummoned(e,0,tp,false,aux.DragonXyzSpSummonType(c))
end
function c54358015.sptg(e,tp,eg,ep,ev,re,r,rp,chk)
```
