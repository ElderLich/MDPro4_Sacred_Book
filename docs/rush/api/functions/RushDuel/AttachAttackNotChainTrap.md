# RushDuel.AttachAttackNotChainTrap

Alias: `RD.AttachAttackNotChainTrap`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.AttachAttackNotChainTrap(any e, any code, any card, any desc, any reset, any forced) -> any
```

## Description

Rush Duel helper declared in `RDAttach.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
赋予: 攻击宣言时, 对方不能把陷阱卡发动
```

## Parameters

- `e` `any`: Type and behavior are not yet reviewed; see the source.
- `code` `any`: Type and behavior are not yet reviewed; see the source.
- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `desc` `any`: Type and behavior are not yet reviewed; see the source.
- `reset` `any`: Type and behavior are not yet reviewed; see the source.
- `forced` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDAttach.lua:124`

```lua
function RushDuel.AttachAttackNotChainTrap(e, code, card, desc, reset, forced)
    local e1 = Effect.CreateEffect(e:GetHandler())
    e1:SetType(EFFECT_TYPE_SINGLE + EFFECT_TYPE_CONTINUOUS)
    e1:SetCode(EVENT_ATTACK_ANNOUNCE)
    if desc ~= nil then
        e1:SetDescription(desc)
        e1:SetProperty(EFFECT_FLAG_CLIENT_HINT)
    end
    e1:SetLabel(code)
    e1:SetOperation(RushDuel.AttackNotChainTrapOperation)
    e1:SetReset(reset)
    card:RegisterEffect(e1, forced)
    local e2 = RushDuel.CreateSingleEffect(e, desc, card, EFFECT_ATTACK_NOT_CHAIN_TRAP, nil, reset, forced)
    return e1, e2
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **6** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.AttachAttackNotChainTrap) with `RushDuel.AttachAttackNotChainTrap`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Dragonic Force | `120246034` | [Rush/Scripts/c120246034.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120246034.lua) | 1 |
| Yurushima Warrior | `120140004` | [Rush/Scripts/c120140004.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120140004.lua) | 1 |
| CAN - Sp:D | `120217029` | [Rush/Scripts/c120217029.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120217029.lua) | 1 |
| Neutron Blast | `120283038` | [Rush/Scripts/c120283038.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120283038.lua) | 1 |
| Jointech Tosceratops | `120224001` | [Rush/Scripts/c120224001.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120224001.lua) | 1 |
| Harpie Lady 2 | `120247005` | [Rush/Scripts/c120247005.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120247005.lua) | 1 |

## Script Examples

### Dragonic Force (`120246034`)

Source: [Rush/Scripts/c120246034.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120246034.lua)

```lua
		local tc=g:GetFirst()
		RD.AttachAtkDef(e,tc,900,0,RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END)
		RD.AttachAttackNotChainTrap(e,m,tc,aux.Stringid(m,2),RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END)
		RD.CanSelectAndSpecialSummon(aux.Stringid(m,1),aux.NecroValleyFilter(cm.spfilter),tp,LOCATION_GRAVE,0,1,1,nil,e,POS_FACEUP_DEFENSE)
	end)
```

### Yurushima Warrior (`120140004`)

Source: [Rush/Scripts/c120140004.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120140004.lua)

```lua
function cm.operation(e,tp,eg,ep,ev,re,r,rp)
	RD.SelectAndDoAction(aux.Stringid(m,1),cm.filter,tp,LOCATION_MZONE,0,1,1,nil,function(g)
		RD.AttachAttackNotChainTrap(e,m,g:GetFirst(),aux.Stringid(m,2),RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END)
	end)
end
```

### CAN - Sp:D (`120217029`)

Source: [Rush/Scripts/c120217029.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120217029.lua)

```lua
		local tc=g:GetFirst()
		RD.AttachAtkDef(e,tc,200,0,RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END)
		RD.AttachAttackNotChainTrap(e,m,tc,aux.Stringid(m,2),RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END)
	end)
end
```
