# RushDuel.MaximumMonsterAtk

Alias: `RD.MaximumMonsterAtk`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.MaximumMonsterAtk(any e, any c) -> any
```

## Description

Rush Duel helper declared in `RDMaximum.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

## Parameters

- `e` `any`: Type and behavior are not yet reviewed; see the source.
- `c` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDMaximum.lua:32`

```lua
function RushDuel.MaximumMonsterAtk(e, c)
    return c:IsPosition(POS_FACEUP_ATTACK) and RushDuel.MaximumMonster(e, c)
end
```
