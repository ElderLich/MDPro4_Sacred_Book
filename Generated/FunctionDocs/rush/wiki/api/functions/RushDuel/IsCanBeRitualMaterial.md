# RushDuel.IsCanBeRitualMaterial

Alias: `RD.IsCanBeRitualMaterial`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.IsCanBeRitualMaterial(any c, any rc) -> any
```

## Description

Rush Duel helper declared in `RDRitual.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
仪式召唤 - 可以作为仪式素材
```

## Parameters

- `c` `any`: Type and behavior are not yet reviewed; see the source.
- `rc` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDRitual.lua:111`

```lua
function RushDuel.IsCanBeRitualMaterial(c, rc)
    if c:IsLocation(LOCATION_HAND + LOCATION_DECK + LOCATION_ONFIELD) and not c:IsCanBeRitualMaterial(rc) then
        return false
    end
    local effects = {c:IsHasEffect(EFFECT_CANNOT_BE_RITUAL_MATERIAL)}
    for i, e in ipairs(effects) do
        local value = e:GetValue()
        if value == 1 then
            return false
        elseif type(value) == "function" and value(e, c, SUMMON_TYPE_RITUAL) then
            return false
        end
    end
    return true
end
```
