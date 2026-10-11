# RushDuel.CreateCannotDirectAttackEffect

Alias: `RD.CreateCannotDirectAttackEffect`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CreateCannotDirectAttackEffect(any e, any target, any player, any s_range, any o_range, any reset) -> any
```

## Description

Rush Duel helper declared in `RDLimit.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
创建限制: 不能直接攻击
```

## Parameters

- `e` `any`: Type and behavior are not yet reviewed; see the source.
- `target` `any`: Type and behavior are not yet reviewed; see the source.
- `player` `any`: Type and behavior are not yet reviewed; see the source.
- `s_range` `any`: Type and behavior are not yet reviewed; see the source.
- `o_range` `any`: Type and behavior are not yet reviewed; see the source.
- `reset` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDLimit.lua:75`

```lua
function RushDuel.CreateCannotDirectAttackEffect(e, target, player, s_range, o_range, reset)
    local e1 = Effect.CreateEffect(e:GetHandler())
    e1:SetType(EFFECT_TYPE_FIELD)
    e1:SetCode(EFFECT_CANNOT_DIRECT_ATTACK)
    e1:SetProperty(EFFECT_FLAG_IGNORE_IMMUNE)
    e1:SetTargetRange(s_range, o_range)
    if target ~= nil then
        e1:SetTarget(target)
    end
    e1:SetReset(reset)
    Duel.RegisterEffect(e1, player)
    return e1
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **4** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.CreateCannotDirectAttackEffect) with `RushDuel.CreateCannotDirectAttackEffect`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Joining Chairs | `120151028` | [Rush/Scripts/c120151028.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120151028.lua) | 1 |
| King's Reward | `120140024` | [Rush/Scripts/c120140024.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120140024.lua) | 1 |
| Astrobio Drake | `120235026` | [Rush/Scripts/c120235026.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120235026.lua) | 1 |
| Royal Rebel's Rocker | `120140017` | [Rush/Scripts/c120140017.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120140017.lua) | 1 |

## Script Examples

### Joining Chairs (`120151028`)

Source: [Rush/Scripts/c120151028.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120151028.lua)

```lua
		if RD.ChangePosition(g,e,tp,REASON_EFFECT,POS_FACEUP_DEFENSE)~=0 and Duel.GetFlagEffect(tp,m)==0 then
			RD.CreateHintEffect(e,aux.Stringid(m,1),tp,0,1,RESET_PHASE+PHASE_END)
			RD.CreateCannotDirectAttackEffect(e,nil,tp,0,LOCATION_MZONE,RESET_PHASE+PHASE_END)
			RD.CreateCannotSelectBattleTargetEffect(e,cm.atkcon,nil,cm.atklimit,tp,0,LOCATION_MZONE,RESET_PHASE+PHASE_END)
			Duel.RegisterFlagEffect(tp,m,RESET_PHASE+PHASE_END,0,1)
```

### King's Reward (`120140024`)

Source: [Rush/Scripts/c120140024.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120140024.lua)

```lua
	if Duel.GetFlagEffect(tp,m)~=0 then return end
	RD.CreateHintEffect(e,aux.Stringid(m,1),tp,1,0,RESET_PHASE+PHASE_END)
	RD.CreateCannotDirectAttackEffect(e,nil,tp,LOCATION_MZONE,0,RESET_PHASE+PHASE_END)
	Duel.RegisterFlagEffect(tp,m,RESET_PHASE+PHASE_END,0,1)
end
```

### Astrobio Drake (`120235026`)

Source: [Rush/Scripts/c120235026.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120235026.lua)

```lua
	if Duel.GetFlagEffect(tp,m)~=0 then return end
	RD.CreateHintEffect(e,aux.Stringid(m,1),tp,1,0,RESET_PHASE+PHASE_END)
	RD.CreateCannotDirectAttackEffect(e,cm.atktg,tp,LOCATION_MZONE,0,RESET_PHASE+PHASE_END)
	Duel.RegisterFlagEffect(tp,m,RESET_PHASE+PHASE_END,0,1)
end
```
