# RushDuel.AdvanceMaterialCheck

Alias: `RD.AdvanceMaterialCheck`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.AdvanceMaterialCheck(any card, any effect, any getter) -> any
```

## Description

Rush Duel helper declared in `RDSummon.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
计算上级召唤时解放怪兽的合计值
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `effect` `any`: Type and behavior are not yet reviewed; see the source.
- `getter` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDSummon.lua:247`

```lua
function RushDuel.AdvanceMaterialCheck(card, effect, getter)
    local e = Effect.CreateEffect(card)
    e:SetType(EFFECT_TYPE_SINGLE)
    e:SetCode(EFFECT_MATERIAL_CHECK)
    e:SetLabelObject(effect)
    e:SetValue(RushDuel.AdvanceMaterialCheckValue(getter))
    card:RegisterEffect(e)
    return e
end
```
