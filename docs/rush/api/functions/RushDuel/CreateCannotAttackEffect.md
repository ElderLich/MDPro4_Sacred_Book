# RushDuel.CreateCannotAttackEffect

Alias: `RD.CreateCannotAttackEffect`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CreateCannotAttackEffect(any e, any desc, any player, any s_range, any o_range, any reset) -> any
```

## Description

Rush Duel helper declared in `RDLimit.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
创建限制: 不能攻击
```

## Parameters

- `e` `any`: Type and behavior are not yet reviewed; see the source.
- `desc` `any`: Type and behavior are not yet reviewed; see the source.
- `player` `any`: Type and behavior are not yet reviewed; see the source.
- `s_range` `any`: Type and behavior are not yet reviewed; see the source.
- `o_range` `any`: Type and behavior are not yet reviewed; see the source.
- `reset` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDLimit.lua:19`

```lua
function RushDuel.CreateCannotAttackEffect(e, desc, player, s_range, o_range, reset)
    local s_target, o_traget = 0, 0
    if s_range == 1 then
        s_target = LOCATION_MZONE
    end
    if o_range == 1 then
        o_traget = LOCATION_MZONE
    end
    local e1 = Effect.CreateEffect(e:GetHandler())
    e1:SetType(EFFECT_TYPE_FIELD)
    e1:SetCode(EFFECT_CANNOT_ATTACK)
    e1:SetProperty(EFFECT_FLAG_IGNORE_IMMUNE)
    e1:SetTargetRange(s_target, o_traget)
    e1:SetReset(reset)
    Duel.RegisterEffect(e1, player)
    local e2 = Effect.CreateEffect(e:GetHandler())
    e2:SetDescription(desc)
    e2:SetType(EFFECT_TYPE_FIELD)
    e2:SetCode(EFFECT_PLAYER_CANNOT_ATTACK)
    e2:SetProperty(EFFECT_FLAG_PLAYER_TARGET + EFFECT_FLAG_CLIENT_HINT)
    e2:SetTargetRange(s_range, o_range)
    e2:SetReset(reset)
    Duel.RegisterEffect(e2, player)
    return e1, e2
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **3** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.CreateCannotAttackEffect) with `RushDuel.CreateCannotAttackEffect`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Makiu, the Magical Mist | `120205058` | [Rush/Scripts/c120205058.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120205058.lua) | 1 |
| Thunderbeetle Gift | `120150033` | [Rush/Scripts/c120150033.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120150033.lua) | 1 |
| Nightmare Knock | `120217079` | [Rush/Scripts/c120217079.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120217079.lua) | 1 |

## Script Examples

### Makiu, the Magical Mist (`120205058`)

Source: [Rush/Scripts/c120205058.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120205058.lua)

```lua
	end)
	if Duel.GetFlagEffect(tp,m)~=0 then return end
	RD.CreateCannotAttackEffect(e,aux.Stringid(m,2),tp,1,0,RESET_PHASE+PHASE_END)
	Duel.RegisterFlagEffect(tp,m,RESET_PHASE+PHASE_END,0,1)
end
```

### Thunderbeetle Gift (`120150033`)

Source: [Rush/Scripts/c120150033.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120150033.lua)

```lua
	RD.Damage(nil,Duel.GetMatchingGroupCount(cm.filter,tp,LOCATION_MZONE,0,nil)*500)
	if Duel.GetFlagEffect(tp,m)~=0 then return end
	RD.CreateCannotAttackEffect(e,aux.Stringid(m,1),tp,1,0,RESET_PHASE+PHASE_END)
	Duel.RegisterFlagEffect(tp,m,RESET_PHASE+PHASE_END,0,1)
end
```

### Nightmare Knock (`120217079`)

Source: [Rush/Scripts/c120217079.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120217079.lua)

```lua
	end)
	if Duel.GetFlagEffect(tp,m)~=0 then return end
	RD.CreateCannotAttackEffect(e,aux.Stringid(m,2),tp,1,0,RESET_PHASE+PHASE_END)
	Duel.RegisterFlagEffect(tp,m,RESET_PHASE+PHASE_END,0,1)
end
```
