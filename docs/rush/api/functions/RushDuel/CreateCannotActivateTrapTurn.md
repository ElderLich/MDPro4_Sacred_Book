# RushDuel.CreateCannotActivateTrapTurn

Alias: `RD.CreateCannotActivateTrapTurn`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CreateCannotActivateTrapTurn(any e, any desc, any player, any s_range, any o_range) -> any
```

## Description

Rush Duel helper declared in `RDLimit.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
创建限制: 整个回合, 不能发动陷阱卡
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

`Rush/Utilities/RDLimit.lua:314`

```lua
function RushDuel.CreateCannotActivateTrapTurn(e, desc, player, s_range, o_range)
    local e1 = RushDuel.CreateCannotActivateMix(e, desc, player, s_range, o_range, RESET_PHASE + PHASE_END,
        function(e, re, tp)
            return re:IsHasType(EFFECT_TYPE_ACTIVATE) and re:IsActiveType(TYPE_TRAP)
        end)
    local e2 = Effect.CreateEffect(e:GetHandler())
    e2:SetType(EFFECT_TYPE_FIELD)
    e2:SetCode(EFFECT_PLAYER_CANNOT_ACTIVATE_TRAP)
    e2:SetProperty(EFFECT_FLAG_PLAYER_TARGET)
    e2:SetTargetRange(s_range, o_range)
    e2:SetReset(RESET_PHASE + PHASE_END)
    Duel.RegisterEffect(e2, player)
    return e1, e2
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **1** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.CreateCannotActivateTrapTurn) with `RushDuel.CreateCannotActivateTrapTurn`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Triangle Ecstasy Spark | `120247013` | [Rush/Scripts/c120247013.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120247013.lua) | 1 |

## Script Examples

### Triangle Ecstasy Spark (`120247013`)

Source: [Rush/Scripts/c120247013.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120247013.lua)

```lua
		end)
		--Cannot Activate Trap
		RD.CreateCannotActivateTrapTurn(e,aux.Stringid(m,2),tp,0,1)
	end)
end
```
