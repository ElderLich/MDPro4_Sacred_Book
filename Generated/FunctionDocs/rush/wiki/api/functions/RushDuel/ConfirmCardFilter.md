# RushDuel.ConfirmCardFilter

Alias: `RD.ConfirmCardFilter`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.ConfirmCardFilter(any c) -> any
```

## Description

Rush Duel helper declared in `RDRitual.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
仪式召唤 - 确认素材过滤
```

## Parameters

- `c` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDRitual.lua:219`

```lua
function RushDuel.ConfirmCardFilter(c)
    return c:IsLocation(LOCATION_HAND) or (c:IsLocation(LOCATION_MZONE) and c:IsFacedown())
end
```
