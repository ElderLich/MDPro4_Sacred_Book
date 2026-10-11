# RushDuel.SwapAtkDef

Alias: `RD.SwapAtkDef`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.SwapAtkDef(any e, any card, any reset, any forced) -> any
```

## Description

Rush Duel helper declared in `RDAttach.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
赋予: 交换当前攻守
```

## Parameters

- `e` `any`: Type and behavior are not yet reviewed; see the source.
- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `reset` `any`: Type and behavior are not yet reviewed; see the source.
- `forced` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDAttach.lua:217`

```lua
function RushDuel.SwapAtkDef(e, card, reset, forced)
    if RushDuel.IsCanChangeDef(card) then
        local atk = card:GetAttack()
        local def = card:GetDefense()
        RushDuel.CreateSingleEffect(e, nil, card, EFFECT_SET_ATTACK_FINAL, def, reset, forced)
        RushDuel.CreateSingleEffect(e, nil, card, EFFECT_SET_DEFENSE_FINAL, atk, reset, forced)
    end
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

No indexed local card script currently calls this function.

This can mean the function is unused in the current script set, is only called through an alias, or is available for future/manual scripts.
