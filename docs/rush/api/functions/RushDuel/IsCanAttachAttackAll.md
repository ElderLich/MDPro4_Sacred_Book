# RushDuel.IsCanAttachAttackAll

Alias: `RD.IsCanAttachAttackAll`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.IsCanAttachAttackAll(any card, any value) -> any
```

## Description

Rush Duel helper declared in `RDCondition.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
条件: 可否赋予效果 - 全体攻击
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `value` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCondition.lua:273`

```lua
function RushDuel.IsCanAttachAttackAll(card, value)
    return RushDuel.IsCanAttack(card) and not RushDuel.IsHasAttachEffect(card, EFFECT_ATTACK_ALL)
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

No indexed local card script currently calls this function.

This can mean the function is unused in the current script set, is only called through an alias, or is available for future/manual scripts.
