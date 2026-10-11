# RushDuel.CreateLimitAttackCountEffect

Alias: `RD.CreateLimitAttackCountEffect`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CreateLimitAttackCountEffect(any e, any desc, any count, any player, any s_range, any o_range, any reset) -> any
```

## Description

Rush Duel helper declared in `RDLimit.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
创建限制: 只能攻击宣言X次
```

## Parameters

- `e` `any`: Type and behavior are not yet reviewed; see the source.
- `desc` `any`: Type and behavior are not yet reviewed; see the source.
- `count` `any`: Type and behavior are not yet reviewed; see the source.
- `player` `any`: Type and behavior are not yet reviewed; see the source.
- `s_range` `any`: Type and behavior are not yet reviewed; see the source.
- `o_range` `any`: Type and behavior are not yet reviewed; see the source.
- `reset` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDLimit.lua:269`

```lua
function RushDuel.CreateLimitAttackCountEffect(e, desc, count, player, s_range, o_range, reset)
    local e1 = Effect.CreateEffect(e:GetHandler())
    e1:SetDescription(desc)
    e1:SetType(EFFECT_TYPE_FIELD)
    e1:SetCode(EFFECT_CANNOT_ATTACK_ANNOUNCE)
    e1:SetProperty(EFFECT_FLAG_PLAYER_TARGET + EFFECT_FLAG_CLIENT_HINT)
    e1:SetTargetRange(s_range, o_range)
    e1:SetLabel(0, count)
    e1:SetCondition(function(e)
        local ct1, ct2 = e:GetLabel()
        return ct1 >= ct2
    end)
    e1:SetReset(reset)
    Duel.RegisterEffect(e1, player)
    local e2 = Effect.CreateEffect(e:GetHandler())
    e2:SetType(EFFECT_TYPE_FIELD + EFFECT_TYPE_CONTINUOUS)
    e2:SetCode(EVENT_ATTACK_ANNOUNCE)
    e2:SetLabelObject(e1)
    e2:SetOperation(function(e)
        local te = e:GetLabelObject()
        local ct1, ct2 = te:GetLabel()
        te:SetLabel(ct1 + 1, ct2)
    end)
    e2:SetReset(reset)
    Duel.RegisterEffect(e2, player)
    return e1, e2
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **4** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.CreateLimitAttackCountEffect) with `RushDuel.CreateLimitAttackCountEffect`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Qadi of the Monumenthes | `120300009` | [Rush/Scripts/c120300009.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120300009.lua) | 1 |
| OuTerverSe Direct Driver | `120109056` | [Rush/Scripts/c120109056.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120109056.lua) | 1 |
| Harpie Lady 3 &amp; 1 | `120285044` | [Rush/Scripts/c120285044.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120285044.lua) | 1 |
| SW - Asura Bat | `120305032` | [Rush/Scripts/c120305032.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120305032.lua) | 1 |

## Script Examples

### Qadi of the Monumenthes (`120300009`)

Source: [Rush/Scripts/c120300009.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120300009.lua)

```lua
end
function cm.operation(e,tp,eg,ep,ev,re,r,rp)
	local e1,e2=RD.CreateLimitAttackCountEffect(e,aux.Stringid(m,2),2,tp,0,1,RESET_PHASE+PHASE_END+RESET_OPPO_TURN)
	e2:SetCondition(cm.atkcon)
	Duel.RegisterFlagEffect(1-tp,FLAG_MAX_ATTACK_TWICE_NEXT_TURN,RESET_PHASE+PHASE_END+RESET_OPPO_TURN,0,1)
```

### OuTerverSe Direct Driver (`120109056`)

Source: [Rush/Scripts/c120109056.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120109056.lua)

```lua
					RD.AttachDirectAttack(e,tc,aux.Stringid(m,3),RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END)
				end)
				RD.CreateLimitAttackCountEffect(e,aux.Stringid(m,4),2,tp,1,0,RESET_PHASE+PHASE_END)
			end)
		end
```

### Harpie Lady 3 & 1 (`120285044`)

Source: [Rush/Scripts/c120285044.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120285044.lua)

```lua
	end
	if Duel.GetFlagEffect(1-tp,FLAG_MAX_ATTACK_TWICE_NEXT_TURN)~=0 then return end
	local e1,e2=RD.CreateLimitAttackCountEffect(e,aux.Stringid(m,2),2,tp,0,1,RESET_PHASE+PHASE_END+RESET_OPPO_TURN)
	e2:SetCondition(cm.atkcon)
	Duel.RegisterFlagEffect(1-tp,FLAG_MAX_ATTACK_TWICE_NEXT_TURN,RESET_PHASE+PHASE_END+RESET_OPPO_TURN,0,1)
```
