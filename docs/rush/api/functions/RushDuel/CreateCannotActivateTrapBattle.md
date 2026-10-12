# RushDuel.CreateCannotActivateTrapBattle

Alias: `RD.CreateCannotActivateTrapBattle`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CreateCannotActivateTrapBattle(any e, any desc, any player, any s_range, any o_range) -> any
```

## Description

Rush Duel helper declared in `RDLimit.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
创建限制: 战斗阶段, 不能发动陷阱卡
```

## Parameters

- `e` `any`: Type and behavior are not yet reviewed; see the source.
- `desc` `any`: Type and behavior are not yet reviewed; see the source.
- `player` `any`: Type and behavior are not yet reviewed; see the source.
- `s_range` `any`: Type and behavior are not yet reviewed; see the source.
- `o_range` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDLimit.lua:329`

```lua
function RushDuel.CreateCannotActivateTrapBattle(e, desc, player, s_range, o_range)
    local e1 = RushDuel.CreateCannotActivateMix(e, desc, player, s_range, o_range, RESET_PHASE + PHASE_END,
        function(e, re, tp)
            local ph = Duel.GetCurrentPhase()
            return ph >= PHASE_BATTLE_START and ph <= PHASE_BATTLE and re:IsHasType(EFFECT_TYPE_ACTIVATE) and
                       re:IsActiveType(TYPE_TRAP)
        end)
    local e2 = Effect.CreateEffect(e:GetHandler())
    e2:SetType(EFFECT_TYPE_FIELD)
    e2:SetCode(EFFECT_PLAYER_CANNOT_ACTIVATE_TRAP_BATTLE)
    e2:SetProperty(EFFECT_FLAG_PLAYER_TARGET)
    e2:SetTargetRange(s_range, o_range)
    e2:SetReset(RESET_PHASE + PHASE_END)
    Duel.RegisterEffect(e2, player)
    return e1, e2
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **2** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.CreateCannotActivateTrapBattle) with `RushDuel.CreateCannotActivateTrapBattle`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Dark Matter Jelly | `120261022` | [Rush/Scripts/c120261022.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120261022.lua) | 1 |
| Headhunters' Lemurcunning | `120308006` | [Rush/Scripts/c120308006.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120308006.lua) | 1 |

## Script Examples

### Dark Matter Jelly (`120261022`)

Source: [Rush/Scripts/c120261022.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120261022.lua)

```lua
end
function cm.operation(e,tp,eg,ep,ev,re,r,rp)
	RD.CreateCannotActivateTrapBattle(e,aux.Stringid(m,1),tp,0,1)
	local c=e:GetHandler()
	if c:IsFaceup() and c:IsRelateToEffect(e) then
```

### Headhunters' Lemurcunning (`120308006`)

Source: [Rush/Scripts/c120308006.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120308006.lua)

```lua
		RD.SendToDeckAndExists(g,e,tp,REASON_EFFECT)
	end)
	RD.CreateCannotActivateTrapBattle(e,aux.Stringid(m,1),tp,0,1)
end
```
