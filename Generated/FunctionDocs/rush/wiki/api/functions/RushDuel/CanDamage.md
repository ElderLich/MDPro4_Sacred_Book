# RushDuel.CanDamage

Alias: `RD.CanDamage`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CanDamage(any desc, any player, any damage, any break_effect) -> any
```

## Description

Rush Duel helper declared in `RDAction.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
可选操作: 伤害
```

## Parameters

- `desc` `any`: Type and behavior are not yet reviewed; see the source.
- `player` `any`: Type and behavior are not yet reviewed; see the source.
- `damage` `any`: Type and behavior are not yet reviewed; see the source.
- `break_effect` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDAction.lua:616`

```lua
function RushDuel.CanDamage(desc, player, damage, break_effect)
    if damage > 0 and Duel.SelectYesNo(player, desc) then
        if break_effect then
            Duel.BreakEffect()
        end
        return Duel.Damage(1 - player, damage, REASON_EFFECT)
    end
    return 0
end
```
