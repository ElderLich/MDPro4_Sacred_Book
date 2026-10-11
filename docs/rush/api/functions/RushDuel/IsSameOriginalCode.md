# RushDuel.IsSameOriginalCode

Alias: `RD.IsSameOriginalCode`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.IsSameOriginalCode(any card1, any card2) -> any
```

## Description

Rush Duel helper declared in `RDLegend.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
条件: 是否为原本卡名相同的卡
```

## Parameters

- `card1` `any`: Type and behavior are not yet reviewed; see the source.
- `card2` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDLegend.lua:41`

```lua
function RushDuel.IsSameOriginalCode(card1, card2)
    return card1:IsOriginalCodeRule(card2:GetOriginalCodeRule())
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **4** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.IsSameOriginalCode) with `RushDuel.IsSameOriginalCode`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Hysteric Eyes | `120304063` | [Rush/Scripts/c120304063.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120304063.lua) | 2 |
| Eria the Water Spiritualist | `120301010` | [Rush/Scripts/c120301010.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120301010.lua) | 1 |
| Hybridrive Screwdriver | `120261006` | [Rush/Scripts/c120261006.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120261006.lua) | 1 |
| Lore Leimey | `120294037` | [Rush/Scripts/c120294037.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120294037.lua) | 1 |

## Script Examples

### Hysteric Eyes (`120304063`)

Source: [Rush/Scripts/c120304063.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120304063.lua)

```lua
				local tc1,tc2=sg:GetFirst(),sg:GetNext()
				local actlimit=function(e,re,tp)
					if tc1 and RD.IsSameOriginalCode(re:GetHandler(),tc1) then
						return true
					elseif tc2 and RD.IsSameOriginalCode(re:GetHandler(),tc2) then
```

### Eria the Water Spiritualist (`120301010`)

Source: [Rush/Scripts/c120301010.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120301010.lua)

```lua
		local tc=g:GetFirst()
		local sumlimit=function(e,c)
			return RD.IsSameOriginalCode(c,tc)
		end
		RD.CreateCannotSummonEffect(e,aux.Stringid(m,1),sumlimit,tp,0,1,RESET_PHASE+PHASE_END+RESET_OPPO_TURN)
```

### Hybridrive Screwdriver (`120261006`)

Source: [Rush/Scripts/c120261006.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120261006.lua)

```lua
			local tc=Duel.GetOperatedGroup():GetFirst()
			local sumlimit=function(e,c)
				return RD.IsSameOriginalCode(c,tc)
			end
			RD.CreateCannotSummonEffect(e,aux.Stringid(m,1),sumlimit,tp,1,1,RESET_PHASE+PHASE_END+RESET_OPPO_TURN)
```
