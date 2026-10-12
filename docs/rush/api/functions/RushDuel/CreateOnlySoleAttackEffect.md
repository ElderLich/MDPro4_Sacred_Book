# RushDuel.CreateOnlySoleAttackEffect

Alias: `RD.CreateOnlySoleAttackEffect`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CreateOnlySoleAttackEffect(any e, any code, any player, any s_range, any o_range, any reset) -> any
```

## Description

Rush Duel helper declared in `RDLimit.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
创建限制: 只能用1只怪兽进行攻击
```

## Parameters

- `e` `any`: Type and behavior are not yet reviewed; see the source.
- `code` `any`: Type and behavior are not yet reviewed; see the source.
- `player` `any`: Type and behavior are not yet reviewed; see the source.
- `s_range` `any`: Type and behavior are not yet reviewed; see the source.
- `o_range` `any`: Type and behavior are not yet reviewed; see the source.
- `reset` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDLimit.lua:179`

```lua
function RushDuel.CreateOnlySoleAttackEffect(e, code, player, s_range, o_range, reset)
    local e1 = Effect.CreateEffect(e:GetHandler())
    e1:SetType(EFFECT_TYPE_FIELD + EFFECT_TYPE_CONTINUOUS)
    e1:SetCode(EVENT_ATTACK_ANNOUNCE)
    e1:SetProperty(EFFECT_FLAG_CANNOT_DISABLE)
    e1:SetOperation(function(e, tp, eg, ep, ev, re, r, rp)
        if Duel.GetFlagEffect(tp, code) == 0 then
            e:GetLabelObject():SetLabel(eg:GetFirst():GetFieldID())
            Duel.RegisterFlagEffect(tp, code, reset, 0, 1)
        end
    end)
    e1:SetReset(reset)
    Duel.RegisterEffect(e1, player)
    local e2 = Effect.CreateEffect(e:GetHandler())
    e2:SetType(EFFECT_TYPE_FIELD)
    e2:SetCode(EFFECT_CANNOT_ATTACK_ANNOUNCE)
    e2:SetProperty(EFFECT_FLAG_IGNORE_IMMUNE)
    e2:SetTargetRange(s_range, o_range)
    e2:SetCondition(function(e)
        return Duel.GetFlagEffect(e:GetHandlerPlayer(), code) ~= 0
    end)
    e2:SetTarget(function(e, c)
        return c:GetFieldID() ~= e:GetLabel()
    end)
    e2:SetReset(reset)
    Duel.RegisterEffect(e2, player)
    e1:SetLabelObject(e2)
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **6** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.CreateOnlySoleAttackEffect) with `RushDuel.CreateOnlySoleAttackEffect`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Voidalfr Star Mayfly](/examples/rush-cards/120300034) | `120300034` | [Rush/Scripts/c120300034.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120300034.lua) | 1 |
| [Analyze Phlogiston](/examples/rush-cards/120226001) | `120226001` | [Rush/Scripts/c120226001.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120226001.lua) | 1 |
| Sword Skill - Ruler's Slash | `120208046` | [Rush/Scripts/c120208046.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120208046.lua) | 1 |
| Gatling the Shadow Flower Shinobi | `120170032` | [Rush/Scripts/c120170032.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120170032.lua) | 1 |
| Destructor Soldier Haken | `120264012` | [Rush/Scripts/c120264012.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120264012.lua) | 1 |
| Level Blast | `120237010` | [Rush/Scripts/c120237010.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120237010.lua) | 1 |

## Script Examples

### Voidalfr Star Mayfly (`120300034`)

Source: [Rush/Scripts/c120300034.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120300034.lua)

```lua
	if Duel.GetFlagEffect(tp,m)~=0 then return end
	RD.CreateHintEffect(e,aux.Stringid(m,1),tp,1,0,RESET_PHASE+PHASE_END)
	RD.CreateOnlySoleAttackEffect(e,20300034,tp,LOCATION_MZONE,0,RESET_PHASE+PHASE_END)
	Duel.RegisterFlagEffect(tp,m,RESET_PHASE+PHASE_END,0,1)
end
```

### Analyze Phlogiston (`120226001`)

Source: [Rush/Scripts/c120226001.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120226001.lua)

```lua
	if Duel.GetFlagEffect(tp,m)~=0 then return end
	RD.CreateHintEffect(e,aux.Stringid(m,1),tp,1,0,RESET_PHASE+PHASE_END)
	RD.CreateOnlySoleAttackEffect(e,20226001,tp,LOCATION_MZONE,0,RESET_PHASE+PHASE_END)
	Duel.RegisterFlagEffect(tp,m,RESET_PHASE+PHASE_END,0,1)
end
```

### Sword Skill - Ruler's Slash (`120208046`)

Source: [Rush/Scripts/c120208046.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120208046.lua)

```lua
	if Duel.GetFlagEffect(tp,m)~=0 then return end
	RD.CreateHintEffect(e,aux.Stringid(m,2),tp,1,0,RESET_PHASE+PHASE_END)
	RD.CreateOnlySoleAttackEffect(e,20208046,tp,LOCATION_MZONE,0,RESET_PHASE+PHASE_END)
	Duel.RegisterFlagEffect(tp,m,RESET_PHASE+PHASE_END,0,1)
end
```
