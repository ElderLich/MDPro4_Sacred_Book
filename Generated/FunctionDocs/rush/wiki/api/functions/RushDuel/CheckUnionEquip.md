# RushDuel.CheckUnionEquip

Alias: `RD.CheckUnionEquip`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CheckUnionEquip(any e, any c, any ec) -> any
```

## Description

Rush Duel helper declared in `RDUnion.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
检查是否可以同盟装备
```

## Parameters

- `e` `any`: Type and behavior are not yet reviewed; see the source.
- `c` `any`: Type and behavior are not yet reviewed; see the source.
- `ec` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDUnion.lua:72`

```lua
function RushDuel.CheckUnionEquip(e, c, ec)
    local effects = {ec:IsHasEffect(EFFECT_UNION_TARGET)}
    for i, effect in ipairs(effects) do
        local value = effect:GetValue()
        if value(c, effect, e) then
            return true
        end
    end
    return false
end
```
