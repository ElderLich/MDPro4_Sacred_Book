# RushDuel.AttachCannotTribute

Alias: `RD.AttachCannotTribute`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.AttachCannotTribute(any e, any card, any value, any desc, any reset, any forced) -> any
```

## Description

Rush Duel helper declared in `RDAttach.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
赋予: 不能用于上级召唤而解放
```

## Parameters

- `e` `any`: Type and behavior are not yet reviewed; see the source.
- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `value` `any`: Type and behavior are not yet reviewed; see the source.
- `desc` `any`: Type and behavior are not yet reviewed; see the source.
- `reset` `any`: Type and behavior are not yet reviewed; see the source.
- `forced` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDAttach.lua:182`

```lua
function RushDuel.AttachCannotTribute(e, card, value, desc, reset, forced)
    return RushDuel.CreateSingleEffect(e, desc, card, EFFECT_UNRELEASABLE_SUM, value, reset, forced)
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **6** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.AttachCannotTribute) with `RushDuel.AttachCannotTribute`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Necromaid Trickment](/examples/rush-cards/120294063) | `120294063` | [Rush/Scripts/c120294063.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120294063.lua) | 1 |
| Gaigust the Defiant Soul | `120264031` | [Rush/Scripts/c120264031.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120264031.lua) | 1 |
| King's Authority | `120254088` | [Rush/Scripts/c120254088.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120254088.lua) | 1 |
| Stumbling Rock | `120264060` | [Rush/Scripts/c120264060.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120264060.lua) | 1 |
| Mind Control | `120280029` | [Rush/Scripts/c120280029.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120280029.lua) | 1 |
| Mystery Handcuffs | `120186032` | [Rush/Scripts/c120186032.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120186032.lua) | 1 |

## Script Examples

### Necromaid Trickment (`120294063`)

Source: [Rush/Scripts/c120294063.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120294063.lua)

```lua
		RD.ChangePosition(g,e,tp,REASON_EFFECT,POS_FACEUP_DEFENSE)
		g:ForEach(function(tc)
			local e1=RD.AttachCannotTribute(e,tc,cm.sumlimit,aux.Stringid(m,1),RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END)
			e1:SetLabel(tp)
			local e2=RD.AttachCannotBeRitualMaterial(e,tc,cm.ritlimit,aux.Stringid(m,2),RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END)
```

### Gaigust the Defiant Soul (`120264031`)

Source: [Rush/Scripts/c120264031.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120264031.lua)

```lua
	local c=e:GetHandler()
	if c:IsFaceup() and c:IsRelateToEffect(e) then
		local e1=RD.AttachCannotTribute(e,c,cm.sumlimit,aux.Stringid(m,1),RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END)
		e1:SetLabel(tp)
	end
```

### King's Authority (`120254088`)

Source: [Rush/Scripts/c120254088.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120254088.lua)

```lua
				return e:GetHandlerPlayer()~=tp
			end
			RD.AttachCannotTribute(e,tc,sumlimit,aux.Stringid(m,3),RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END)
		end)
	end)
```
