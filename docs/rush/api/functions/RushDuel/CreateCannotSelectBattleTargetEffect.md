# RushDuel.CreateCannotSelectBattleTargetEffect

Alias: `RD.CreateCannotSelectBattleTargetEffect`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CreateCannotSelectBattleTargetEffect(any e, any condition, any target, any value, any player, any s_range, any o_range, any reset) -> any
```

## Description

Rush Duel helper declared in `RDLimit.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
创建限制: 不能选择攻击目标
```

## Parameters

- `e` `any`: Type and behavior are not yet reviewed; see the source.
- `condition` `any`: Type and behavior are not yet reviewed; see the source.
- `target` `any`: Type and behavior are not yet reviewed; see the source.
- `value` `any`: Type and behavior are not yet reviewed; see the source.
- `player` `any`: Type and behavior are not yet reviewed; see the source.
- `s_range` `any`: Type and behavior are not yet reviewed; see the source.
- `o_range` `any`: Type and behavior are not yet reviewed; see the source.
- `reset` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDLimit.lua:89`

```lua
function RushDuel.CreateCannotSelectBattleTargetEffect(e, condition, target, value, player, s_range, o_range, reset)
    local e1 = Effect.CreateEffect(e:GetHandler())
    e1:SetType(EFFECT_TYPE_FIELD)
    e1:SetCode(EFFECT_CANNOT_SELECT_BATTLE_TARGET)
    e1:SetProperty(EFFECT_FLAG_IGNORE_IMMUNE)
    e1:SetTargetRange(s_range, o_range)
    e1:SetCondition(function(e)
        return not RushDuel.IsAttacking(e) and (not condition or condition(e))
    end)
    if target ~= nil then
        e1:SetTarget(target)
    end
    if value ~= nil then
        e1:SetValue(value)
    end
    e1:SetReset(reset)
    Duel.RegisterEffect(e1, player)
    return e1
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **3** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.CreateCannotSelectBattleTargetEffect) with `RushDuel.CreateCannotSelectBattleTargetEffect`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Joining Chairs | `120151028` | [Rush/Scripts/c120151028.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120151028.lua) | 1 |
| Terrorphone Number | `120217087` | [Rush/Scripts/c120217087.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120217087.lua) | 1 |
| Elegant Egotist | `120247014` | [Rush/Scripts/c120247014.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120247014.lua) | 1 |

## Script Examples

### Joining Chairs (`120151028`)

Source: [Rush/Scripts/c120151028.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120151028.lua)

```lua
			RD.CreateHintEffect(e,aux.Stringid(m,1),tp,0,1,RESET_PHASE+PHASE_END)
			RD.CreateCannotDirectAttackEffect(e,nil,tp,0,LOCATION_MZONE,RESET_PHASE+PHASE_END)
			RD.CreateCannotSelectBattleTargetEffect(e,cm.atkcon,nil,cm.atklimit,tp,0,LOCATION_MZONE,RESET_PHASE+PHASE_END)
			Duel.RegisterFlagEffect(tp,m,RESET_PHASE+PHASE_END,0,1)
		end
```

### Terrorphone Number (`120217087`)

Source: [Rush/Scripts/c120217087.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120217087.lua)

```lua
	if Duel.GetFlagEffect(tp,m)~=0 then return end
	RD.CreateHintEffect(e,aux.Stringid(m,1),tp,0,1,RESET_PHASE+PHASE_END)
	RD.CreateCannotSelectBattleTargetEffect(e,cm.atkcon,nil,cm.atklimit,tp,0,LOCATION_MZONE,RESET_PHASE+PHASE_END)
	Duel.RegisterFlagEffect(tp,m,RESET_PHASE+PHASE_END,0,1)
end
```

### Elegant Egotist (`120247014`)

Source: [Rush/Scripts/c120247014.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120247014.lua)

```lua
	if Duel.GetFlagEffect(tp,m)~=0 then return end
	RD.CreateHintEffect(e,aux.Stringid(m,1),tp,1,0,RESET_PHASE+PHASE_END)
	RD.CreateCannotSelectBattleTargetEffect(e,nil,nil,cm.atklimit,tp,LOCATION_MZONE,0,RESET_PHASE+PHASE_END)
	Duel.RegisterFlagEffect(tp,m,RESET_PHASE+PHASE_END,0,1)
end
```
