# RushDuel.IsDefenseBelow

Alias: `RD.IsDefenseBelow`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.IsDefenseBelow(any card, any def) -> any
```

## Description

Rush Duel helper declared in `RDCondition.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
条件: 守备力在 def 以下
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `def` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCondition.lua:99`

```lua
function RushDuel.IsDefenseBelow(card, def)
    return card:IsDefenseBelow(def) and not RushDuel.IsMaximumMode(card)
end
```
