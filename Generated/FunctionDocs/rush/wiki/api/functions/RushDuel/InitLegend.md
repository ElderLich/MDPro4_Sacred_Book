# RushDuel.InitLegend

Alias: `RD.InitLegend`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.InitLegend() -> any
```

## Description

Rush Duel helper declared in `RDLegend.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
初始化传说卡
```

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDLegend.lua:11`

```lua
function RushDuel.InitLegend()
    -- local g = Duel.GetMatchingGroup(RushDuel.IsLegendCard, 0, 0xff, 0xff, nil, true)
    -- g:ForEach(RushDuel.InitLegendCard)
end
```
