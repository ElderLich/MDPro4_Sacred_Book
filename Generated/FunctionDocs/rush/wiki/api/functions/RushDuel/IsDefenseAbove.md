# RushDuel.IsDefenseAbove

Alias: `RD.IsDefenseAbove`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.IsDefenseAbove(any card, any def) -> any
```

## Description

Rush Duel helper declared in `RDCondition.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
条件: 守备力在 def 以上
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `def` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCondition.lua:95`

```lua
function RushDuel.IsDefenseAbove(card, def)
    return card:IsDefenseAbove(def) and not RushDuel.IsMaximumMode(card)
end
```
