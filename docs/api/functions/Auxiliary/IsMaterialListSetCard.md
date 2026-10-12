# Auxiliary.IsMaterialListSetCard

## Signature

```lua
Auxiliary.IsMaterialListSetCard(Card c, int setcode) -> bool
```

## Description

Checks whether c lists setcode in its material_setcode metadata, including packed sub-set matching.

## Parameters

- `c` `Card`
- `setcode` `int`

## Returns

- `bool`

## Source

- `Utilities/utility.lua:515`

## Guided Examples

Learn how to use this function in context:

- [Archetypes and Set Codes](/learn/archetypes-and-setcodes)

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **9** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Auxiliary.IsMaterialListSetCard) with `Auxiliary.IsMaterialListSetCard`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Fusion Destiny | `52947044` | [Scripts/c52947044.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c52947044.lua) | 1 |
| Cyberload Fusion | `55704856` | [Scripts/c55704856.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c55704856.lua) | 1 |
| Red-Eyes Fusion | `6172122` | [Scripts/c6172122.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c6172122.lua) | 1 |
| Junk Anchor | `25148255` | [Scripts/c25148255.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c25148255.lua) | 1 |
| Favorite Contact | `75047173` | [Scripts/c75047173.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c75047173.lua) | 1 |
| Cybernetic Revolution | `18597560` | [Scripts/c18597560.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c18597560.lua) | 1 |
| Scrap Synchron | `16449363` | [Scripts/c16449363.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c16449363.lua) | 1 |
| Legacy of a HERO | `25614410` | [Scripts/c25614410.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c25614410.lua) | 1 |
| Quickdraw Synchron | `20932152` | [Scripts/c20932152.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c20932152.lua) | 1 |

## Script Examples

### Fusion Destiny (`52947044`)

Source: [Scripts/c52947044.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c52947044.lua)

```lua
end
function s.filter2(c,e,tp,m,f,chkf)
	return c:IsType(TYPE_FUSION) and aux.IsMaterialListSetCard(c,0xc008) and (not f or f(c))
		and c:IsCanBeSpecialSummoned(e,SUMMON_TYPE_FUSION,tp,false,false) and c:CheckFusionMaterial(m,nil,chkf)
end
```

### Cyberload Fusion (`55704856`)

Source: [Scripts/c55704856.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c55704856.lua)

```lua
end
function c55704856.filter2(c,e,tp,m,f,chkf)
	if not (c:IsType(TYPE_FUSION) and aux.IsMaterialListSetCard(c,0x1093) and (not f or f(c))
		and c:IsCanBeSpecialSummoned(e,SUMMON_TYPE_FUSION,tp,false,false)) then return false end
	aux.FCheckAdditional=c.cyber_fusion_check or c55704856.fcheck
```

### Red-Eyes Fusion (`6172122`)

Source: [Scripts/c6172122.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c6172122.lua)

```lua
end
function c6172122.filter2(c,e,tp,m,f,chkf)
	if not (c:IsType(TYPE_FUSION) and aux.IsMaterialListSetCard(c,0x3b) and (not f or f(c))
		and c:IsCanBeSpecialSummoned(e,SUMMON_TYPE_FUSION,tp,false,false)) then return false end
	aux.FCheckAdditional=c.red_eyes_fusion_check or c6172122.fcheck
```
