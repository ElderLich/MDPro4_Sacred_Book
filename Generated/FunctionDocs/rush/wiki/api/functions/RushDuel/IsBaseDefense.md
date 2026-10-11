# RushDuel.IsBaseDefense

Alias: `RD.IsBaseDefense`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.IsBaseDefense(any card, any def) -> any
```

## Description

Rush Duel helper declared in `RDCondition.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
条件: 原本守备力为 def
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `def` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCondition.lua:103`

```lua
function RushDuel.IsBaseDefense(card, def)
    return card:GetBaseDefense() == def and not RushDuel.IsMaximumMode(card)
end
```
