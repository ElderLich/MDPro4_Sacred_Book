# RushDuel.SetLabelAndObject

Alias: `RD.SetLabelAndObject`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.SetLabelAndObject(any effect, any target, any set_label, any set_object) -> any
```

## Description

Rush Duel helper declared in `RDFunction.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
为效果设置标签
```

## Parameters

- `effect` `any`: Type and behavior are not yet reviewed; see the source.
- `target` `any`: Type and behavior are not yet reviewed; see the source.
- `set_label` `any`: Type and behavior are not yet reviewed; see the source.
- `set_object` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDFunction.lua:5`

```lua
function RushDuel.SetLabelAndObject(effect, target, set_label, set_object)
    if effect ~= nil and target ~= nil then
        if set_label ~= nil then
            effect:SetLabel(set_label(target))
        end
        if set_object ~= nil then
            effect:SetLabelObject(set_object(target))
        end
    end
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

No indexed local card script currently calls this function.

This can mean the function is unused in the current script set, is only called through an alias, or is available for future/manual scripts.
