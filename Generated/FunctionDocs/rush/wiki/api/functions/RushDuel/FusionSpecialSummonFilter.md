# RushDuel.FusionSpecialSummonFilter

Alias: `RD.FusionSpecialSummonFilter`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.FusionSpecialSummonFilter(any c, any e, any tp, any pos, any m, any f, any gc, any chkf, any filter) -> any
```

## Description

Rush Duel helper declared in `RDFusion.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
融合召唤 - 融合召唤的怪兽过滤
```

## Parameters

- `c` `any`: Type and behavior are not yet reviewed; see the source.
- `e` `any`: Type and behavior are not yet reviewed; see the source.
- `tp` `any`: Type and behavior are not yet reviewed; see the source.
- `pos` `any`: Type and behavior are not yet reviewed; see the source.
- `m` `any`: Type and behavior are not yet reviewed; see the source.
- `f` `any`: Type and behavior are not yet reviewed; see the source.
- `gc` `any`: Type and behavior are not yet reviewed; see the source.
- `chkf` `any`: Type and behavior are not yet reviewed; see the source.
- `filter` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDFusion.lua:400`

```lua
function RushDuel.FusionSpecialSummonFilter(c, e, tp, pos, m, f, gc, chkf, filter)
    RushDuel.SetFusionEffectParameter(e)
    local res = c:IsType(TYPE_FUSION) and (not filter or filter(c, e, tp, m, f, chkf)) and (not f or f(c)) and c:IsCanBeSpecialSummoned(e, SUMMON_TYPE_FUSION, tp, false, false, pos) and
                    c:CheckFusionMaterial(m, gc, chkf)
    RushDuel.SetFusionEffectParameter()
    return res
end
```
