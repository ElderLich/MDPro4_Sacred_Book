# RushDuel.AddTurnFlagCounter

Alias: `RD.AddTurnFlagCounter`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.AddTurnFlagCounter(any player, any code) -> any
```

## Description

Rush Duel helper declared in `RDFunction.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
添加以回合为基础的标记计数器
```

## Parameters

- `player` `any`: Type and behavior are not yet reviewed; see the source.
- `code` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDFunction.lua:241`

```lua
function RushDuel.AddTurnFlagCounter(player, code)
    local counter = Duel.GetFlagEffectLabel(player, code)
    if not counter then
        Duel.RegisterFlagEffect(player, code, RESET_PHASE + PHASE_END, 0, 1, 1)
    else
        Duel.SetFlagEffectLabel(player, code, counter + 1)
    end
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **1** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.AddTurnFlagCounter) with `RushDuel.AddTurnFlagCounter`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Red-Eyes Mars Dragon](/examples/rush-cards/120306034) | `120306034` | [Rush/Scripts/c120306034.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120306034.lua) | 1 |

## Script Examples

### Red-Eyes Mars Dragon (`120306034`)

Source: [Rush/Scripts/c120306034.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120306034.lua)

```lua
function cm.count(e,tp,eg,ep,ev,re,r,rp)
	if ep==tp and re:IsHasType(EFFECT_TYPE_ACTIVATE) and re:GetHandler():IsCode(list[2]) then
		RD.AddTurnFlagCounter(tp,m)
	end
end
```
