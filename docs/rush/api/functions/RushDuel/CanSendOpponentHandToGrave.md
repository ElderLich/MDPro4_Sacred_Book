# RushDuel.CanSendOpponentHandToGrave

Alias: `RD.CanSendOpponentHandToGrave`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CanSendOpponentHandToGrave(any desc, any tp, any hint, any min, any max, any break_effect) -> any
```

## Description

Rush Duel helper declared in `RDAction.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
可选操作: 随机选对方的手卡送去墓地
```

## Parameters

- `desc` `any`: Type and behavior are not yet reviewed; see the source.
- `tp` `any`: Type and behavior are not yet reviewed; see the source.
- `hint` `any`: Type and behavior are not yet reviewed; see the source.
- `min` `any`: Type and behavior are not yet reviewed; see the source.
- `max` `any`: Type and behavior are not yet reviewed; see the source.
- `break_effect` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDAction.lua:341`

```lua
function RushDuel.CanSendOpponentHandToGrave(desc, tp, hint, min, max, break_effect)
    local g = Duel.GetFieldGroup(tp, 0, LOCATION_HAND)
    local ct = #g
    if ct > 0 and Duel.SelectYesNo(tp, desc) then
        if break_effect then
            Duel.BreakEffect()
        end
        return RushDuel.SendOpponentHandToGrave(tp, hint, min, max)
    end
    return 0
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **4** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.CanSendOpponentHandToGrave) with `RushDuel.CanSendOpponentHandToGrave`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Confronting the Black Dragon | `120274030` | [Rush/Scripts/c120274030.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120274030.lua) | 1 |
| Mazera, Devil of the Den | `120290036` | [Rush/Scripts/c120290036.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120290036.lua) | 1 |
| Hack for the Intel | `120290059` | [Rush/Scripts/c120290059.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120290059.lua) | 1 |
| Auspicious Arrival of Divine Doubt | `120261065` | [Rush/Scripts/c120261065.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120261065.lua) | 1 |

## Script Examples

### Confronting the Black Dragon (`120274030`)

Source: [Rush/Scripts/c120274030.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120274030.lua)

```lua
	end
	if Duel.GetFieldGroupCount(tp,0,LOCATION_HAND)>2 then
		RD.CanSendOpponentHandToGrave(aux.Stringid(m,1),tp,aux.Stringid(m,2),1,1,true)
	end
end
```

### Mazera, Devil of the Den (`120290036`)

Source: [Rush/Scripts/c120290036.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120290036.lua)

```lua
	if c:IsFaceup() and c:IsRelateToEffect(e) then
		RD.AttachAtkDef(e,c,500,0,RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END)
		RD.CanSendOpponentHandToGrave(aux.Stringid(m,1),tp,aux.Stringid(m,2),1,3,true)
	end
end
```

### Hack for the Intel (`120290059`)

Source: [Rush/Scripts/c120290059.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120290059.lua)

```lua
	if RD.SelectAndToHandOrSpecialSummon(aux.Stringid(m,1),aux.NecroValleyFilter(cm.filter),tp,LOCATION_GRAVE,0,nil,e,POS_FACEUP)
		and Duel.IsExistingMatchingCard(cm.exfilter,tp,LOCATION_MZONE,0,1,nil) then
		RD.CanSendOpponentHandToGrave(aux.Stringid(m,1),tp,aux.Stringid(m,2),1,1,true)
	end
end
```
