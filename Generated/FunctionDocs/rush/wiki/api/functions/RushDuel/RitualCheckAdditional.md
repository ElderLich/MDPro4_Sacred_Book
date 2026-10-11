# RushDuel.RitualCheckAdditional

Alias: `RD.RitualCheckAdditional`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.RitualCheckAdditional(any rc, any type) -> any
```

## Description

Rush Duel helper declared in `RDRitual.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
仪式召唤 - 素材不能超过必要的数量
```

## Parameters

- `rc` `any`: Type and behavior are not yet reviewed; see the source.
- `type` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDRitual.lua:175`

```lua
function RushDuel.RitualCheckAdditional(rc, type)
    local value = RushDuel.GetRitualTypeValue(rc, type)
    local getter = RushDuel.GetRitualMaterialGetter(type)
    if type == RITUAL_ORIGINAL_LEVEL_EQUAL or type == RITUAL_CURRENT_LEVEL_EQUAL or type == RITUAL_ORIGINAL_ATTACK_EQUAL or type == RITUAL_CURRENT_ATTACK_EQUAL then
        return function(g)
            return (not Auxiliary.RGCheckAdditional or Auxiliary.RGCheckAdditional(g)) and g:GetSum(getter, rc) <= value
        end
    elseif type == RITUAL_ORIGINAL_LEVEL_GREATER or type == RITUAL_CURRENT_LEVEL_GREATER or type == RITUAL_ORIGINAL_ATTACK_GREATER or type == RITUAL_CURRENT_ATTACK_GREATER then
        return function(g, ec)
            if ec then
                return (not Auxiliary.RGCheckAdditional or Auxiliary.RGCheckAdditional(g, ec)) and g:GetSum(getter, rc) - getter(ec, rc) <= value
            else
                return not Auxiliary.RGCheckAdditional or Auxiliary.RGCheckAdditional(g)
            end
        end
    end
end
```
