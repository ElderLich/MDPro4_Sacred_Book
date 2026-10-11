# RushDuel.MaximumMonster

Alias: `RD.MaximumMonster`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.MaximumMonster(any e, any c) -> any
```

## Description

Rush Duel helper declared in `RDMaximum.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

## Parameters

- `e` `any`: Type and behavior are not yet reviewed; see the source.
- `c` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDMaximum.lua:29`

```lua
function RushDuel.MaximumMonster(e, c)
    return c:IsHasEffect(EFFECT_MAXIMUM_MODE) and c:GetOverlayCount() > 0
end
```
