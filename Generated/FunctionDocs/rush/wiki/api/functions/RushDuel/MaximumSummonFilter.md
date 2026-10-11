# RushDuel.MaximumSummonFilter

Alias: `RD.MaximumSummonFilter`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.MaximumSummonFilter(any c, any e, any tp, any left_code, any right_code) -> any
```

## Description

Rush Duel helper declared in `RDMaximum.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

## Parameters

- `c` `any`: Type and behavior are not yet reviewed; see the source.
- `e` `any`: Type and behavior are not yet reviewed; see the source.
- `tp` `any`: Type and behavior are not yet reviewed; see the source.
- `left_code` `any`: Type and behavior are not yet reviewed; see the source.
- `right_code` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDMaximum.lua:69`

```lua
function RushDuel.MaximumSummonFilter(c, e, tp, left_code, right_code)
    return c:IsCode(left_code, right_code)
end
```
