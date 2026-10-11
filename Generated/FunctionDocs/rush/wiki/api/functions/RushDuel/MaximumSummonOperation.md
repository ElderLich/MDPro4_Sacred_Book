# RushDuel.MaximumSummonOperation

Alias: `RD.MaximumSummonOperation`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.MaximumSummonOperation(any left_code, any right_code) -> any
```

## Description

Rush Duel helper declared in `RDMaximum.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

## Parameters

- `left_code` `any`: Type and behavior are not yet reviewed; see the source.
- `right_code` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDMaximum.lua:100`

```lua
function RushDuel.MaximumSummonOperation(left_code, right_code)
    return function(e, tp, eg, ep, ev, re, r, rp, c, og, min, max)
        local fg = Duel.GetFieldGroup(tp, LOCATION_MZONE, 0)
        Duel.SendtoGrave(fg, REASON_RULE)
        local mg = e:GetLabelObject()
        local left = mg:GetFirst()
        local right = mg:GetNext()
        if left:IsCode(right_code) then
            left, right = right, left
        end
        Duel.MoveToField(left, tp, tp, LOCATION_MZONE, POS_FACEUP_ATTACK, false, 0x2)
        Duel.MoveToField(right, tp, tp, LOCATION_MZONE, POS_FACEUP_ATTACK, false, 0x8)
        c:SetMaterial(mg)
        Duel.Overlay(c, mg)
        mg:DeleteGroup()
        RushDuel.EnableMaximumMode(c, RESET_EVENT + 0xff0000)
    end
end
```
