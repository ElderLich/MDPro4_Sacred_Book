# RushDuel.SetBaseAtkDef

Alias: `RD.SetBaseAtkDef`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.SetBaseAtkDef(any e, any card, any atk, any def, any reset, any forced) -> any
```

## Description

Rush Duel helper declared in `RDAttach.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
赋予: 变更原本攻守
```

## Parameters

- `e` `any`: Type and behavior are not yet reviewed; see the source.
- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `atk` `any`: Type and behavior are not yet reviewed; see the source.
- `def` `any`: Type and behavior are not yet reviewed; see the source.
- `reset` `any`: Type and behavior are not yet reviewed; see the source.
- `forced` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDAttach.lua:202`

```lua
function RushDuel.SetBaseAtkDef(e, card, atk, def, reset, forced)
    if atk ~= nil then
        RushDuel.CreateSingleEffect(e, nil, card, EFFECT_SET_BASE_ATTACK, atk, reset, forced)
    end
    if def ~= nil and RushDuel.IsCanChangeDef(card) then
        RushDuel.CreateSingleEffect(e, nil, card, EFFECT_SET_BASE_DEFENSE, def, reset, forced)
    end
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **7** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.SetBaseAtkDef) with `RushDuel.SetBaseAtkDef`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Sevens Road Wiz | `120183014` | [Rush/Scripts/c120183014.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120183014.lua) | 1 |
| Drilling Mandrill | `120155031` | [Rush/Scripts/c120155031.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120155031.lua) | 1 |
| Nullstrike Dragon Zerogias | `120180001` | [Rush/Scripts/c120180001.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120180001.lua) | 1 |
| Void Strike Dragon Zerogaigias | `120211001` | [Rush/Scripts/c120211001.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120211001.lua) | 1 |
| Gajumaru the Shadow Flower Lion | `120170030` | [Rush/Scripts/c120170030.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120170030.lua) | 1 |
| Mask of Volos | `120120034` | [Rush/Scripts/c120120034.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120120034.lua) | 1 |
| Triple Threat Thunder | `120145047` | [Rush/Scripts/c120145047.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120145047.lua) | 1 |

## Script Examples

### Sevens Road Wiz (`120183014`)

Source: [Rush/Scripts/c120183014.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120183014.lua)

```lua
	local filter=RD.Filter(cm.filter,c:GetAttack())
	RD.SelectAndDoAction(aux.Stringid(m,1),filter,tp,0,LOCATION_MZONE,1,1,nil,function(g)
		RD.SetBaseAtkDef(e,g:GetFirst(),0,nil,RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END)
		if Duel.IsExistingMatchingCard(cm.exfilter,tp,LOCATION_GRAVE,0,1,nil) then
			RD.CanDraw(aux.Stringid(m,2),tp,1)
```

### Drilling Mandrill (`120155031`)

Source: [Rush/Scripts/c120155031.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120155031.lua)

```lua
			local og=Duel.GetOperatedGroup()
			og:ForEach(function(tc)
				RD.SetBaseAtkDef(e,tc,0,nil,RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END)
			end)
		end
```

### Nullstrike Dragon Zerogias (`120180001`)

Source: [Rush/Scripts/c120180001.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120180001.lua)

```lua
function cm.operation(e,tp,eg,ep,ev,re,r,rp)
	RD.SelectAndDoAction(aux.Stringid(m,1),cm.filter,tp,0,LOCATION_MZONE,1,1,nil,function(g)
		RD.SetBaseAtkDef(e,g:GetFirst(),0,nil,RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END)
		local c=e:GetHandler()
		if c:IsFaceup() and c:IsRelateToEffect(e) then
```
