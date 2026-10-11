# RushDuel.GetBaseAttackOnDestroy

Alias: `RD.GetBaseAttackOnDestroy`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.GetBaseAttackOnDestroy(any c) -> any
```

## Description

Rush Duel helper declared in `RDFunction.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
获取被破坏时的基础攻击力
```

## Parameters

- `c` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDFunction.lua:189`

```lua
function RushDuel.GetBaseAttackOnDestroy(c)
    local atk
    if RushDuel.IsPreviousMaximumMode(c) and c:IsReason(REASON_DESTROY) then
        atk = c.maximum_attack
    else
        atk = c:GetTextAttack()
    end
    return math.max(0, atk)
end
```
