# RushDuel.GroupBor

Alias: `RD.GroupBor`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.GroupBor(any g, any func, ... any) -> any
```

## Description

Rush Duel helper declared in `RDFunction.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
对卡片组里的全部卡片作位或运算
```

## Parameters

- `g` `any`: Type and behavior are not yet reviewed; see the source.
- `func` `any`: Type and behavior are not yet reviewed; see the source.
- `...` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDFunction.lua:79`

```lua
function RushDuel.GroupBor(g, func, ...)
    local result = 0
    local args = {...}
    g:ForEach(function(tc)
        result = result | func(tc, table.unpack(args))
    end)
    return result
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **1** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.GroupBor) with `RushDuel.GroupBor`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Imaginary Arc Turbulence](/examples/rush-cards/120196013) | `120196013` | [Rush/Scripts/c120196013.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120196013.lua) | 1 |

## Script Examples

### Imaginary Arc Turbulence (`120196013`)

Source: [Rush/Scripts/c120196013.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120196013.lua)

```lua
		if RD.ChangePosition(g,e,tp,REASON_EFFECT,POS_FACEUP_DEFENSE)~=0 then
			local sg=Duel.GetMatchingGroup(cm.exfilter,tp,LOCATION_GRAVE,0,nil)
			local race=RD.GroupBor(sg,Card.GetRace)
			if race~=0 then
				local desfilter=RD.Filter(cm.desfilter,race)
```
