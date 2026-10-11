# RushDuel.CostChoose

Alias: `RD.CostChoose`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CostChoose(any hit1, any cost1, any hit2, any cost2, any set_label) -> any
```

## Description

Rush Duel helper declared in `RDCost.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
代价: 从2个代价中选择1个(分开选)
```

## Parameters

- `hit1` `any`: Type and behavior are not yet reviewed; see the source.
- `cost1` `any`: Type and behavior are not yet reviewed; see the source.
- `hit2` `any`: Type and behavior are not yet reviewed; see the source.
- `cost2` `any`: Type and behavior are not yet reviewed; see the source.
- `set_label` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCost.lua:541`

```lua
function RushDuel.CostChoose(hit1, cost1, hit2, cost2, set_label)
    return function(e, tp, eg, ep, ev, re, r, rp, chk)
        local s1 = cost1(e, tp, eg, ep, ev, re, r, rp, 0)
        local s2 = cost2(e, tp, eg, ep, ev, re, r, rp, 0)
        if chk == 0 then
            return s1 or s2
        end
        local res = 0
        if s1 and s2 then
            RushDuel.CostCancelable = true
            ::cancel::
            res = RushDuel.SelectOption(tp, {s1, hit1}, {s2, hit2})
            if res == 1 then
                if not cost1(e, tp, eg, ep, ev, re, r, rp, 1) then
                    goto cancel
                end
            elseif res == 2 then
                if not cost2(e, tp, eg, ep, ev, re, r, rp, 1) then
                    goto cancel
                end
            end
            RushDuel.CostCancelable = false
        elseif s1 then
            cost1(e, tp, eg, ep, ev, re, r, rp, 1)
            res = 1
        elseif s2 then
            cost2(e, tp, eg, ep, ev, re, r, rp, 1)
            res = 2
        end
        if res ~= 0 and set_label then
            e:SetLabel(res)
        end
    end
end
```
