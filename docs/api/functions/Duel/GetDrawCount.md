# Duel.GetDrawCount

## Signature

```lua
Duel.GetDrawCount(int player) -> int
```

## Description

Returns the player's number of rules drawn per turn

## Parameters

- `player` `int`

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4851`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **3** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Duel.GetDrawCount`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Gravekeeper's Trap | `98715423` | [Scripts/c98715423.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c98715423.lua) | 49 |
| Zexal Field | `95856586` | [Scripts/c95856586.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c95856586.lua) | 42 |
| Skull Flame | `99899504` | [Scripts/c99899504.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c99899504.lua) | 42 |

## Script Examples

### Gravekeeper's Trap (`98715423`)

Source: [Scripts/c98715423.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c98715423.lua)

```lua
function c98715423.cfcon(e,tp,eg,ep,ev,re,r,rp)
	return Duel.GetTurnPlayer()==1-tp and Duel.GetFieldGroupCount(1-tp,LOCATION_DECK,0)>0
		and Duel.GetDrawCount(1-tp)>0 and e:GetHandler():IsStatus(STATUS_EFFECT_ENABLED)
end
function c98715423.cftg(e,tp,eg,ep,ev,re,r,rp,chk)
```

### Zexal Field (`95856586`)

Source: [Scripts/c95856586.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c95856586.lua)

```lua
function c95856586.tdcon(e,tp,eg,ep,ev,re,r,rp)
	return tp==Duel.GetTurnPlayer() and Duel.GetFieldGroupCount(tp,LOCATION_DECK,0)>0
		and Duel.GetDrawCount(tp)>0
end
function c95856586.tdfilter(c)
```

### Skull Flame (`99899504`)

Source: [Scripts/c99899504.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c99899504.lua)

```lua
	if chkc then return chkc:IsControler(tp) and chkc:IsLocation(LOCATION_GRAVE) and c99899504.thfilter(chkc) end
	if chk==0 then return Duel.IsExistingTarget(c99899504.thfilter,tp,LOCATION_GRAVE,0,1,nil) end
	local dt=Duel.GetDrawCount(tp)
	if dt~=0 then
		e:SetLabel(1)
```
