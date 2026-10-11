# RushDuel.GetBaseAttackOnTribute

Alias: `RD.GetBaseAttackOnTribute`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.GetBaseAttackOnTribute(any c) -> any
```

## Description

Rush Duel helper declared in `RDFunction.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
获取被上级召唤解放时的基础攻击力
```

## Parameters

- `c` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDFunction.lua:178`

```lua
function RushDuel.GetBaseAttackOnTribute(c)
    local atk
    if RushDuel.IsMaximumMode(c) then
        atk = c.maximum_attack
    else
        atk = c:GetTextAttack()
    end
    return math.max(0, atk)
end
```
