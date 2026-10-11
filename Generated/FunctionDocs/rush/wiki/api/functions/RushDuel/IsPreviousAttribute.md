# RushDuel.IsPreviousAttribute

Alias: `RD.IsPreviousAttribute`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.IsPreviousAttribute(any card, any attr) -> any
```

## Description

Rush Duel helper declared in `RDCondition.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
条件: 位置变化前的属性
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `attr` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCondition.lua:202`

```lua
function RushDuel.IsPreviousAttribute(card, attr)
    return (card:GetPreviousAttributeOnField() & attr) ~= 0
end
```
