# RushDuel.IsSummonOrSpecialSummonMainPhase

Alias: `RD.IsSummonOrSpecialSummonMainPhase`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.IsSummonOrSpecialSummonMainPhase(any card) -> any
```

## Description

Rush Duel helper declared in `RDCondition.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
条件: 这张卡召唤·特殊召唤的自己主要阶段
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCondition.lua:47`

```lua
function RushDuel.IsSummonOrSpecialSummonMainPhase(card)
    return card:IsReason(REASON_SUMMON + REASON_SPSUMMON) and card:IsStatus(STATUS_SUMMON_TURN + STATUS_SPSUMMON_TURN)
        and card:GetFlagEffect(FLAG_SUMMON_MAIN_PHASE) ~= 0
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **9** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.IsSummonOrSpecialSummonMainPhase) with `RushDuel.IsSummonOrSpecialSummonMainPhase`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Eria the Water Spiritualist | `120301010` | [Rush/Scripts/c120301010.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120301010.lua) | 1 |
| UMP Sky Forbia | `120306017` | [Rush/Scripts/c120306017.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120306017.lua) | 1 |
| Etraynze the Sprinting Shadow Flower Ninja | `120285012` | [Rush/Scripts/c120285012.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120285012.lua) | 1 |
| Aussa the Earth Spiritualist | `120301009` | [Rush/Scripts/c120301009.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120301009.lua) | 1 |
| Wynn the Wind Spiritualist | `120301012` | [Rush/Scripts/c120301012.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120301012.lua) | 1 |
| Voidvelg Transi | `120109018` | [Rush/Scripts/c120109018.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120109018.lua) | 1 |
| Galactica Oblivion Ark | `120277008` | [Rush/Scripts/c120277008.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120277008.lua) | 1 |
| Hiita the Fire Spiritualist | `120301011` | [Rush/Scripts/c120301011.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120301011.lua) | 1 |
| Mean Mutt Duke Doberguardian | `120222031` | [Rush/Scripts/c120222031.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120222031.lua) | 1 |

## Script Examples

### Eria the Water Spiritualist (`120301010`)

Source: [Rush/Scripts/c120301010.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120301010.lua)

```lua
end
function cm.condition(e,tp,eg,ep,ev,re,r,rp)
	return RD.IsSummonOrSpecialSummonMainPhase(e:GetHandler())
end
cm.cost=RD.CostSendHandOrFieldToGrave(cm.costfilter,1,1,false)
```

### UMP Sky Forbia (`120306017`)

Source: [Rush/Scripts/c120306017.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120306017.lua)

```lua
	return Duel.IsAbleToEnterBP()
		and RD.IsCanAttachDirectAttack(c)
		and RD.IsSummonOrSpecialSummonMainPhase(c)
end
cm.cost=RD.CostSendDeckTopToGrave(1)
```

### Etraynze the Sprinting Shadow Flower Ninja (`120285012`)

Source: [Rush/Scripts/c120285012.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120285012.lua)

```lua
	if c:IsFaceup() and c:IsRelateToEffect(e) then
		RD.ChangeCode(e,c,list[1],RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END)
		if RD.IsSummonOrSpecialSummonMainPhase(c) then
			RD.CanSelectAndDoAction(aux.Stringid(m,1),HINTMSG_ATOHAND,aux.NecroValleyFilter(cm.thfilter),tp,LOCATION_GRAVE,0,1,2,nil,function(g)
				RD.SendToHandAndExists(g,e,tp,REASON_EFFECT)
```
