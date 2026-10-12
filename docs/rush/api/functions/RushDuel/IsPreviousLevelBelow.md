# RushDuel.IsPreviousLevelBelow

Alias: `RD.IsPreviousLevelBelow`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.IsPreviousLevelBelow(any card, any level) -> any
```

## Description

Rush Duel helper declared in `RDCondition.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
条件: 位置变化前的等级小于
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `level` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCondition.lua:218`

```lua
function RushDuel.IsPreviousLevelBelow(card, level)
    return card:GetPreviousLevelOnField() > 0 and card:GetPreviousLevelOnField() <= level
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **1** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.IsPreviousLevelBelow) with `RushDuel.IsPreviousLevelBelow`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Stardom Light | `120184003` | [Rush/Scripts/c120184003.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120184003.lua) | 1 |

## Script Examples

### Stardom Light (`120184003`)

Source: [Rush/Scripts/c120184003.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120184003.lua)

```lua
cm.cost=RD.CostSendMZoneToGrave(cm.costfilter,1,1,false,nil,nil,function(g)
	local tc=g:GetFirst()
	if RD.IsPreviousLevelBelow(tc,2) then
		return 20184003
	else
```
