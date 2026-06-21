# Auxiliary.GetMultiLinkedZone

## Signature

```lua
Auxiliary.GetMultiLinkedZone(int tp) -> int
```

## Description

Returns the zone mask of tp's Monster Zones that are linked by at least two face-up Link Monsters on either field.

## Parameters

- `tp` `int`

## Returns

- `int` - Zone mask for zones linked by at least two Link Monsters.

## Source

- `Utilities/utility.lua:1181`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **3** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Auxiliary.GetMultiLinkedZone`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Guardragon Pisty | `13143275` | [Scripts/c13143275.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c13143275.lua) | 33 |
| Guardragon Agarpain | `59537380` | [Scripts/c59537380.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59537380.lua) | 30 |
| Guardragon Elpy | `86148577` | [Scripts/c86148577.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c86148577.lua) | 30 |

## Script Examples

### Guardragon Pisty (`13143275`)

Source: [Scripts/c13143275.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c13143275.lua)

```lua
end
function c13143275.sptg(e,tp,eg,ep,ev,re,r,rp,chk,chkc)
	local zone=aux.GetMultiLinkedZone(tp)
	if chkc then return chkc:IsLocation(LOCATION_GRAVE+LOCATION_REMOVED) and chkc:IsControler(tp) and c13143275.spfilter(chkc,e,tp,zone) end
	if chk==0 then return zone~=0 and Duel.GetLocationCount(tp,LOCATION_MZONE)>0
```

### Guardragon Agarpain (`59537380`)

Source: [Scripts/c59537380.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59537380.lua)

```lua
end
function c59537380.sptg(e,tp,eg,ep,ev,re,r,rp,chk)
	local zone=aux.GetMultiLinkedZone(tp)
	if chk==0 then return zone~=0
		and Duel.IsExistingMatchingCard(c59537380.spfilter,tp,LOCATION_EXTRA,0,1,nil,e,tp,zone) end
```

### Guardragon Elpy (`86148577`)

Source: [Scripts/c86148577.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c86148577.lua)

```lua
end
function c86148577.sptg(e,tp,eg,ep,ev,re,r,rp,chk)
	local zone=aux.GetMultiLinkedZone(tp)
	if chk==0 then return Duel.IsExistingMatchingCard(c86148577.spfilter,tp,LOCATION_HAND+LOCATION_DECK,0,1,nil,e,tp,zone) end
	Duel.SetOperationInfo(0,CATEGORY_SPECIAL_SUMMON,nil,1,tp,LOCATION_HAND+LOCATION_DECK)
```
