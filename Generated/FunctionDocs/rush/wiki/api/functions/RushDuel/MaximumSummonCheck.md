# RushDuel.MaximumSummonCheck

Alias: `RD.MaximumSummonCheck`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.MaximumSummonCheck(any g) -> any
```

## Description

Rush Duel helper declared in `RDMaximum.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

## Parameters

- `g` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDMaximum.lua:72`

```lua
function RushDuel.MaximumSummonCheck(g)
    return g:GetClassCount(Card.GetCode) == #g
end
```
