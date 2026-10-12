# RushDuel.CreateCannotSetMonsterEffect

Alias: `RD.CreateCannotSetMonsterEffect`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CreateCannotSetMonsterEffect(any e, any desc, any target, any player, any s_range, any o_range, any reset) -> any
```

## Description

Rush Duel helper declared in `RDLimit.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
创建限制: 不能盖放怪兽
```

## Parameters

- `e` `any`: Type and behavior are not yet reviewed; see the source.
- `desc` `any`: Type and behavior are not yet reviewed; see the source.
- `target` `any`: Type and behavior are not yet reviewed; see the source.
- `player` `any`: Type and behavior are not yet reviewed; see the source.
- `s_range` `any`: Type and behavior are not yet reviewed; see the source.
- `o_range` `any`: Type and behavior are not yet reviewed; see the source.
- `reset` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDLimit.lua:124`

```lua
function RushDuel.CreateCannotSetMonsterEffect(e, desc, target, player, s_range, o_range, reset)
    local e1 = Effect.CreateEffect(e:GetHandler())
    e1:SetDescription(desc)
    e1:SetType(EFFECT_TYPE_FIELD)
    e1:SetCode(EFFECT_CANNOT_MSET)
    e1:SetProperty(EFFECT_FLAG_PLAYER_TARGET + EFFECT_FLAG_CLIENT_HINT)
    e1:SetTargetRange(s_range, o_range)
    if target ~= nil then
        e1:SetTarget(target)
    end
    e1:SetReset(reset)
    Duel.RegisterEffect(e1, player)
    local e2 = Effect.CreateEffect(e:GetHandler())
    e2:SetType(EFFECT_TYPE_FIELD)
    e2:SetCode(EFFECT_LIMIT_SPECIAL_SUMMON_POSITION)
    e2:SetProperty(EFFECT_FLAG_PLAYER_TARGET)
    e2:SetTargetRange(s_range, o_range)
    e2:SetTarget(function(e, c, sump, sumtype, sumpos, targetp)
        return sumpos & POS_FACEDOWN > 0 and (not target or target(e, c))
    end)
    e2:SetReset(reset)
    Duel.RegisterEffect(e2, player)
    return e1, e2
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **3** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.CreateCannotSetMonsterEffect) with `RushDuel.CreateCannotSetMonsterEffect`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Devil Foolish](/examples/rush-cards/120244026) | `120244026` | [Rush/Scripts/c120244026.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120244026.lua) | 1 |
| Super Electromagnetic Maximum | `120239024` | [Rush/Scripts/c120239024.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120239024.lua) | 1 |
| Tiger Roll the Sushi Fairy | `120151041` | [Rush/Scripts/c120151041.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120151041.lua) | 1 |

## Script Examples

### Devil Foolish (`120244026`)

Source: [Rush/Scripts/c120244026.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120244026.lua)

```lua
	if Duel.GetFlagEffect(tp,m)~=0 then return end
	RD.CreateCannotSummonEffect(e,aux.Stringid(m,1),cm.sumlimit,tp,1,0,RESET_PHASE+PHASE_END)
	RD.CreateCannotSetMonsterEffect(e,aux.Stringid(m,2),cm.setlimit,tp,1,0,RESET_PHASE+PHASE_END)
	Duel.RegisterFlagEffect(tp,m,RESET_PHASE+PHASE_END,0,1)
end
```

### Super Electromagnetic Maximum (`120239024`)

Source: [Rush/Scripts/c120239024.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120239024.lua)

```lua
		if RD.SendToHandAndExists(g,e,tp,REASON_EFFECT) and Duel.GetFlagEffect(tp,m)==0 then
			RD.CreateCannotSummonEffect(e,aux.Stringid(m,1),cm.sumlimit,tp,1,0,RESET_PHASE+PHASE_END)
			RD.CreateCannotSetMonsterEffect(e,aux.Stringid(m,2),cm.sumlimit,tp,1,0,RESET_PHASE+PHASE_END)
			Duel.RegisterFlagEffect(tp,m,RESET_PHASE+PHASE_END,0,1)
		end
```

### Tiger Roll the Sushi Fairy (`120151041`)

Source: [Rush/Scripts/c120151041.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120151041.lua)

```lua
		if RD.SendToHandAndExists(g,e,tp,REASON_EFFECT) and Duel.GetFlagEffect(tp,m)==0 then
			RD.CreateCannotSummonEffect(e,aux.Stringid(m,1),cm.sumlimit,tp,1,0,RESET_PHASE+PHASE_END)
			RD.CreateCannotSetMonsterEffect(e,aux.Stringid(m,2),cm.sumlimit,tp,1,0,RESET_PHASE+PHASE_END)
			RD.CreateCannotSpecialSummonEffect(e,aux.Stringid(m,3),cm.sumlimit,tp,1,0,RESET_PHASE+PHASE_END)
			Duel.RegisterFlagEffect(tp,m,RESET_PHASE+PHASE_END,0,1)
```
