# Auxiliary.IsMaterialListType

## Signature

```lua
Auxiliary.IsMaterialListType(Card c, int type) -> bool
```

## Description

Returns true if c's stored material type mask contains type.

## Parameters

- `c` `Card`
- `type` `int`

## Returns

- `bool` - true if c's material type mask contains type.

## Source

- `Utilities/utility.lua:526`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **2** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Auxiliary.IsMaterialListType) with `Auxiliary.IsMaterialListType`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Miracle Synchro Fusion | `36484016` | [Scripts/c36484016.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c36484016.lua) | 1 |
| Scrap-Iron Signal | `50947142` | [Scripts/c50947142.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c50947142.lua) | 1 |

## Script Examples

### Miracle Synchro Fusion (`36484016`)

Source: [Scripts/c36484016.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c36484016.lua)

```lua
end
function c36484016.filter2(c,e,tp,m,f,chkf)
	if not (c:IsType(TYPE_FUSION) and aux.IsMaterialListType(c,TYPE_SYNCHRO) and (not f or f(c))
		and c:IsCanBeSpecialSummoned(e,SUMMON_TYPE_FUSION,tp,false,false)) then return false end
	aux.FCheckAdditional=c.synchro_fusion_check or c36484016.fcheck
```

### Scrap-Iron Signal (`50947142`)

Source: [Scripts/c50947142.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c50947142.lua)

```lua
end
function c50947142.filter(c)
	return c:IsType(TYPE_SYNCHRO) and aux.IsMaterialListType(c,TYPE_SYNCHRO) and c:IsFaceup()
end
function c50947142.condition(e,tp,eg,ep,ev,re,r,rp)
```
