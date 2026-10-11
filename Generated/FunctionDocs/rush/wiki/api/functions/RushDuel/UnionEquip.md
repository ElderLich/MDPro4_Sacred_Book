# RushDuel.UnionEquip

Alias: `RD.UnionEquip`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.UnionEquip(any tp, any c, any ec) -> any
```

## Description

Rush Duel helper declared in `RDUnion.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
进行同盟装备
```

## Parameters

- `tp` `any`: Type and behavior are not yet reviewed; see the source.
- `c` `any`: Type and behavior are not yet reviewed; see the source.
- `ec` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDUnion.lua:84`

```lua
function RushDuel.UnionEquip(tp, c, ec)
    if c and ec and Duel.Equip(tp, ec, c) then
        local e1 = Effect.CreateEffect(ec)
        e1:SetType(EFFECT_TYPE_SINGLE)
        e1:SetCode(EFFECT_UNION_STATUS)
        e1:SetProperty(EFFECT_FLAG_CANNOT_DISABLE)
        e1:SetReset(RESET_EVENT+RESETS_STANDARD)
        ec:RegisterEffect(e1)
        return true
    end
    return false
end
```
