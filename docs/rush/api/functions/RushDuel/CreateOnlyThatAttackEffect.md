# RushDuel.CreateOnlyThatAttackEffect

Alias: `RD.CreateOnlyThatAttackEffect`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CreateOnlyThatAttackEffect(any e, any card, any code, any player, any s_range, any o_range, any reset) -> any
```

## Description

Rush Duel helper declared in `RDLimit.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
创建限制: 只能用那只进行攻击
```

## Parameters

- `e` `any`: Type and behavior are not yet reviewed; see the source.
- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `code` `any`: Type and behavior are not yet reviewed; see the source.
- `player` `any`: Type and behavior are not yet reviewed; see the source.
- `s_range` `any`: Type and behavior are not yet reviewed; see the source.
- `o_range` `any`: Type and behavior are not yet reviewed; see the source.
- `reset` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDLimit.lua:252`

```lua
function RushDuel.CreateOnlyThatAttackEffect(e, card, code, player, s_range, o_range, reset)
    local flag = card:GetFieldID()
    local e1 = Effect.CreateEffect(e:GetHandler())
    e1:SetType(EFFECT_TYPE_FIELD)
    e1:SetCode(EFFECT_CANNOT_ATTACK_ANNOUNCE)
    e1:SetProperty(EFFECT_FLAG_IGNORE_IMMUNE)
    e1:SetLabelObject(card)
    e1:SetTargetRange(s_range, o_range)
    e1:SetTarget(function(e, c)
        return not (c == e:GetLabelObject() and c:GetFlagEffect(code) ~= 0 and c:GetFlagEffect(flag) ~= 0)
    end)
    e1:SetReset(reset)
    Duel.RegisterEffect(e1, player)
    card:RegisterFlagEffect(code, RESET_EVENT + RESETS_STANDARD - RESET_TURN_SET + reset, 0, 1)
    card:RegisterFlagEffect(flag, RESET_EVENT + RESETS_STANDARD - RESET_TURN_SET + reset, 0, 1)
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **1** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.CreateOnlyThatAttackEffect) with `RushDuel.CreateOnlyThatAttackEffect`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Void Dust Fusion | `120277052` | [Rush/Scripts/c120277052.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120277052.lua) | 1 |

## Script Examples

### Void Dust Fusion (`120277052`)

Source: [Rush/Scripts/c120277052.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120277052.lua)

```lua
function cm.operation(e,tp,eg,ep,ev,re,r,rp,mat,fc)
	RD.CreateHintEffect(e,aux.Stringid(m,1),tp,1,0,RESET_PHASE+PHASE_END)
	RD.CreateOnlyThatAttackEffect(e,fc,20277052,tp,LOCATION_MZONE,0,RESET_PHASE+PHASE_END)
end
```
