# RushDuel.SwapBaseAtkDef

Alias: `RD.SwapBaseAtkDef`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.SwapBaseAtkDef(any e, any card, any reset, any forced) -> any
```

## Description

Rush Duel helper declared in `RDAttach.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
赋予: 交换原本攻守
```

## Parameters

- `e` `any`: Type and behavior are not yet reviewed; see the source.
- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `reset` `any`: Type and behavior are not yet reviewed; see the source.
- `forced` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDAttach.lua:211`

```lua
function RushDuel.SwapBaseAtkDef(e, card, reset, forced)
    if RushDuel.IsCanChangeDef(card) then
        RushDuel.CreateSingleEffect(e, nil, card, EFFECT_SWAP_BASE_AD, nil, reset, forced)
    end
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **3** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.SwapBaseAtkDef) with `RushDuel.SwapBaseAtkDef`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Sword &amp; Shield | `120155052` | [Rush/Scripts/c120155052.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120155052.lua) | 2 |
| It's Right Behind You! | `120217084` | [Rush/Scripts/c120217084.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120217084.lua) | 1 |
| Shield &amp; Sword | `120140009` | [Rush/Scripts/c120140009.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120140009.lua) | 1 |

## Script Examples

### Sword & Shield (`120155052`)

Source: [Rush/Scripts/c120155052.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120155052.lua)

```lua
	if tc:IsRelateToBattle() and tc:IsFaceup() and RD.IsCanChangeDef(tc)
		and bc:IsRelateToBattle() and bc:IsFaceup() and RD.IsCanChangeDef(bc) then
		RD.SwapBaseAtkDef(e,tc,RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END)
		RD.SwapBaseAtkDef(e,bc,RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END)
		RD.CanSelectAndDoAction(aux.Stringid(m,1),HINTMSG_ATOHAND,aux.NecroValleyFilter(cm.thfilter),tp,LOCATION_GRAVE,0,1,1,nil,function(g)
```

### It's Right Behind You! (`120217084`)

Source: [Rush/Scripts/c120217084.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120217084.lua)

```lua
	if RD.SelectAndSpecialSummon(aux.NecroValleyFilter(cm.spfilter),tp,LOCATION_HAND+LOCATION_GRAVE,0,1,1,nil,e,POS_FACEUP)~=0 then
		local tc=Duel.GetOperatedGroup():GetFirst()
		RD.SwapBaseAtkDef(e,tc,RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END)
	end
end
```

### Shield & Sword (`120140009`)

Source: [Rush/Scripts/c120140009.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120140009.lua)

```lua
	local g=Duel.GetMatchingGroup(cm.filter,tp,LOCATION_MZONE,LOCATION_MZONE,nil)
	g:ForEach(function(tc)
		RD.SwapBaseAtkDef(e,tc,RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END)
	end)
end
```
