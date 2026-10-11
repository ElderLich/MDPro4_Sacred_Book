# RushDuel.GetRitualMaterialGetter

Alias: `RD.GetRitualMaterialGetter`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.GetRitualMaterialGetter(any type) -> any
```

## Description

Rush Duel helper declared in `RDRitual.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
仪式召唤 - 素材数值参考
```

## Parameters

- `type` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDRitual.lua:82`

```lua
function RushDuel.GetRitualMaterialGetter(type)
    if type == RITUAL_ORIGINAL_LEVEL_EQUAL or type == RITUAL_ORIGINAL_LEVEL_GREATER or type == RITUAL_CURRENT_LEVEL_EQUAL or type == RITUAL_CURRENT_LEVEL_GREATER then
        return RushDuel.RitualCheckAdditionalLevel
    elseif type == RITUAL_ORIGINAL_ATTACK_EQUAL or type == RITUAL_ORIGINAL_ATTACK_GREATER or type == RITUAL_CURRENT_ATTACK_EQUAL or type == RITUAL_CURRENT_ATTACK_GREATER then
        return RushDuel.RitualCheckAdditionalAttack
    end
end
```
