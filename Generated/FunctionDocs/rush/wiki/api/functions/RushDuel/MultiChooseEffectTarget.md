# RushDuel.MultiChooseEffectTarget

Alias: `RD.MultiChooseEffectTarget`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.MultiChooseEffectTarget(any target) -> any
```

## Description

Rush Duel helper declared in `RDBase.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

## Parameters

- `target` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDBase.lua:230`

```lua
function RushDuel.MultiChooseEffectTarget(target)
    if target ~= nil then
        return target
    else
        return function(e, tp, eg, ep, ev, re, r, rp, chk)
            if chk == 0 then
                return true
            end
            Duel.Hint(HINT_OPSELECTED, 1 - tp, e:GetDescription())
        end
    end
end
```
