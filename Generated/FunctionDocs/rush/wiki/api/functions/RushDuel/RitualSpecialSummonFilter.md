# RushDuel.RitualSpecialSummonFilter

Alias: `RD.RitualSpecialSummonFilter`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.RitualSpecialSummonFilter(any c, any e, any tp, any type, any mat, any f, any gc, any chkf, any filter) -> any
```

## Description

Rush Duel helper declared in `RDRitual.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
仪式召唤 - 仪式召唤的怪兽过滤
```

## Parameters

- `c` `any`: Type and behavior are not yet reviewed; see the source.
- `e` `any`: Type and behavior are not yet reviewed; see the source.
- `tp` `any`: Type and behavior are not yet reviewed; see the source.
- `type` `any`: Type and behavior are not yet reviewed; see the source.
- `mat` `any`: Type and behavior are not yet reviewed; see the source.
- `f` `any`: Type and behavior are not yet reviewed; see the source.
- `gc` `any`: Type and behavior are not yet reviewed; see the source.
- `chkf` `any`: Type and behavior are not yet reviewed; see the source.
- `filter` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDRitual.lua:132`

```lua
function RushDuel.RitualSpecialSummonFilter(c, e, tp, type, mat, f, gc, chkf, filter)
    RushDuel.CurrentRitualEffect = e
    local mg = mat
    if RushDuel.RitualExtraMaterialFilter then
        mg = mg:Filter(RushDuel.RitualExtraMaterialFilter, nil, e, tp, c, mg)
    end
    local res = c:GetType() & 0x81 == 0x81 and (not filter or filter(c, e, tp, mg, f, chkf)) and (not f or f(c))
        and RushDuel.GetRitualTypeValue(c, type) > 0
        and c:IsCanBeSpecialSummoned(e, SUMMON_TYPE_RITUAL, tp, false, false)
        and RushDuel.CheckRitualMaterial(tp, c, type, mg, gc)
    RushDuel.CurrentRitualEffect = nil
    return res
end
```
