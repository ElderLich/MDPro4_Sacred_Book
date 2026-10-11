# Auxiliary.GetXyzNumber

## Signature

```lua
Auxiliary.GetXyzNumber(any v) -> int|nil
```

## Description

Returns the stored Xyz Number value for v, where v can be a Card or a numeric card code. Returns nil when no value is registered.

## Parameters

- `v` `any`

## Returns

- `int|nil` - Registered Xyz Number value, if any.

## Source

- `Utilities/utility.lua:60`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **18** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Auxiliary.GetXyzNumber) with `Auxiliary.GetXyzNumber`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Number 99: Utopia Dragonar | `95134948` | [Scripts/c95134948.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c95134948.lua) | 1 |
| Number 78: Number Archive | `29085954` | [Scripts/c29085954.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c29085954.lua) | 1 |
| CXyz N.As.Ch. Knight | `61374414` | [Scripts/c61374414.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c61374414.lua) | 1 |
| Don Thousand's Throne | `93238626` | [Scripts/c93238626.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93238626.lua) | 3 |
| Seventh Eternity | `60158866` | [Scripts/c60158866.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c60158866.lua) | 1 |
| Galaxy Satellite Dragon | `92362073` | [Scripts/c92362073.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92362073.lua) | 2 |
| Rebirth of the Seventh Emperors | `83888009` | [Scripts/c83888009.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c83888009.lua) | 1 |
| Barian Untopia | `30761649` | [Scripts/c30761649.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30761649.lua) | 1 |
| Seventh Force | `83293635` | [Scripts/c83293635.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c83293635.lua) | 1 |
| Barian's Seal | `38001022` | [Scripts/c38001022.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c38001022.lua) | 1 |
| CXyz Barian Hope | `67926903` | [Scripts/c67926903.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c67926903.lua) | 1 |
| Rank-Up-Magic - The Seventh One | `57734012` | [Scripts/c57734012.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c57734012.lua) | 3 |
| Seventh Tachyon | `7477101` | [Scripts/c7477101.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c7477101.lua) | 1 |
| N.As.H. Knight | `34876719` | [Scripts/c34876719.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c34876719.lua) | 1 |
| Numbers Eveil | `20994205` | [Scripts/c20994205.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c20994205.lua) | 7 |
| Reincarnation of the Seventh Emperors | `57499304` | [Scripts/c57499304.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c57499304.lua) | 1 |
| Rank-Up-Magic Quick Chaos | `33252803` | [Scripts/c33252803.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c33252803.lua) | 3 |
| CXyz Chaos Barian Hope Dragon | `79791695` | [Scripts/c79791695.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c79791695.lua) | 1 |

## Script Examples

### Number 99: Utopia Dragonar (`95134948`)

Source: [Scripts/c95134948.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c95134948.lua)

```lua
end
function c95134948.spfilter(c,e,tp)
	local no=aux.GetXyzNumber(c)
	return no and no>=1 and no<=100 and c:IsSetCard(0x48)
		and c:IsCanBeSpecialSummoned(e,SUMMON_TYPE_XYZ,tp,false,false) and Duel.GetLocationCountFromEx(tp,tp,nil,c)>0
```

### Number 78: Number Archive (`29085954`)

Source: [Scripts/c29085954.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c29085954.lua)

```lua
end
function c29085954.filter(c,e,tp,mc)
	local no=aux.GetXyzNumber(c)
	return no and no>=1 and no<=99 and c:IsSetCard(0x48)
		and mc:IsCanBeXyzMaterial(c)
```

### CXyz N.As.Ch. Knight (`61374414`)

Source: [Scripts/c61374414.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c61374414.lua)

```lua
end
function c61374414.spfilter(c,e,tp,mc)
	local no=aux.GetXyzNumber(c)
	return no and no>=101 and no<=107 and c:IsSetCard(0x48) and c:IsType(TYPE_XYZ) and mc:IsCanBeXyzMaterial(c)
		and c:IsCanBeSpecialSummoned(e,SUMMON_TYPE_XYZ,tp,false,false) and Duel.GetLocationCountFromEx(tp,tp,mc,c)>0
```
