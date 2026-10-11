# RushDuel.IsCanAttachEffectIndes

Alias: `RD.IsCanAttachEffectIndes`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.IsCanAttachEffectIndes(any card, any player, any value) -> any
```

## Description

Rush Duel helper declared in `RDCondition.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
条件: 可否赋予效果 - 效果破坏抗性
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `player` `any`: Type and behavior are not yet reviewed; see the source.
- `value` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCondition.lua:316`

```lua
function RushDuel.IsCanAttachEffectIndes(card, player, value)
    local effects = RushDuel.GetAttachEffects(card, EFFECT_INDESTRUCTABLE_EFFECT)
    return RushDuel.CheckValueEffectIndesType(player, effects, value)
end
```
