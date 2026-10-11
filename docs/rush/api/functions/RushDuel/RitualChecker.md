# RushDuel.RitualChecker

Alias: `RD.RitualChecker`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.RitualChecker(any mg, any rc, any tp, any type, any gc) -> any
```

## Description

Rush Duel helper declared in `RDRitual.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
仪式召唤 - 仪式素材检测
```

## Parameters

- `mg` `any`: Type and behavior are not yet reviewed; see the source.
- `rc` `any`: Type and behavior are not yet reviewed; see the source.
- `tp` `any`: Type and behavior are not yet reviewed; see the source.
- `type` `any`: Type and behavior are not yet reviewed; see the source.
- `gc` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDRitual.lua:193`

```lua
function RushDuel.RitualChecker(mg, rc, tp, type, gc)
    if gc and not mg:IsContains(gc) then
        return false
    elseif rc.mat_group_check and not rc.mat_group_check(mg, tp) then
        return false
    elseif RushDuel.RitualExtraChecker and not RushDuel.RitualExtraChecker(mg, tp, rc) then
        return false
    elseif Auxiliary.RCheckAdditional and not Auxiliary.RCheckAdditional(tp, mg, rc) then
        return false
    else
        local value = RushDuel.GetRitualTypeValue(rc, type)
        if type == RITUAL_ORIGINAL_LEVEL_EQUAL or type == RITUAL_CURRENT_LEVEL_EQUAL then
            return mg:CheckWithSumEqual(Card.GetRitualLevel, value, #mg, #mg, rc)
        elseif type == RITUAL_ORIGINAL_LEVEL_GREATER or type == RITUAL_CURRENT_LEVEL_GREATER then
            Duel.SetSelectedCard(mg)
            return mg:CheckWithSumGreater(Card.GetRitualLevel, value, rc)
        elseif type == RITUAL_ORIGINAL_ATTACK_EQUAL or type == RITUAL_CURRENT_ATTACK_EQUAL then
            return mg:CheckWithSumEqual(Card.GetAttack, value, #mg, #mg, rc)
        elseif type == RITUAL_ORIGINAL_ATTACK_GREATER or type == RITUAL_CURRENT_ATTACK_GREATER then
            Duel.SetSelectedCard(mg)
            return mg:CheckWithSumGreater(Card.GetAttack, value, rc)
        end
    end
    return false
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

No indexed local card script currently calls this function.

This can mean the function is unused in the current script set, is only called through an alias, or is available for future/manual scripts.
