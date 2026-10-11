# RushDuel.RitualCheckLocation

Alias: `RD.RitualCheckLocation`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.RitualCheckLocation(any e, any self_leave, any extra) -> any
```

## Description

Rush Duel helper declared in `RDRitual.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
判断条件: 怪兽区域判断
```

## Parameters

- `e` `any`: Type and behavior are not yet reviewed; see the source.
- `self_leave` `any`: Type and behavior are not yet reviewed; see the source.
- `extra` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDRitual.lua:320`

```lua
function RushDuel.RitualCheckLocation(e, self_leave, extra)
    return function(sg, tp, rc)
        local mg = nil
        if extra and not extra(tp, sg, rc) then
            return false
        elseif self_leave then
            mg = Group.FromCards(e:GetHandler())
            mg:Merge(sg)
        else
            mg = sg
        end
        if rc:IsLocation(LOCATION_EXTRA) then
            return Duel.GetLocationCountFromEx(tp, tp, mg, rc) > 0
        else
            return Duel.GetMZoneCount(tp, mg) > 0
        end
    end
end
```
