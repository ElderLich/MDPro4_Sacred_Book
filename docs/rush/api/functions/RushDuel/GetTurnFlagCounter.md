# RushDuel.GetTurnFlagCounter

Alias: `RD.GetTurnFlagCounter`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.GetTurnFlagCounter(any player, any code) -> any
```

## Description

Rush Duel helper declared in `RDFunction.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
获取以回合为基础的标记计数器
```

## Parameters

- `player` `any`: Type and behavior are not yet reviewed; see the source.
- `code` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDFunction.lua:251`

```lua
function RushDuel.GetTurnFlagCounter(player, code)
    local counter = Duel.GetFlagEffectLabel(player, code)
    if not counter then
        return 0
    else
        return counter
    end
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **1** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.GetTurnFlagCounter) with `RushDuel.GetTurnFlagCounter`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Red-Eyes Mars Dragon](/examples/rush-cards/120306034) | `120306034` | [Rush/Scripts/c120306034.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120306034.lua) | 1 |

## Script Examples

### Red-Eyes Mars Dragon (`120306034`)

Source: [Rush/Scripts/c120306034.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120306034.lua)

```lua
end
function cm.aclimit(e,re,tp)
	if RD.GetTurnFlagCounter(tp,m)<2 then return false end
	local tc=re:GetHandler()
	return re:IsHasType(EFFECT_TYPE_ACTIVATE) and tc:IsCode(list[2])
```
