# RushDuel.HandConfirmSpecialSummonOperation

Alias: `RD.HandConfirmSpecialSummonOperation`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.HandConfirmSpecialSummonOperation(any e, any tp, any eg, any ep, any ev, any re, any r, any rp, any c) -> any
```

## Description

Rush Duel helper declared in `RDSummon.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

## Parameters

- `e` `any`: Type and behavior are not yet reviewed; see the source.
- `tp` `any`: Type and behavior are not yet reviewed; see the source.
- `eg` `any`: Type and behavior are not yet reviewed; see the source.
- `ep` `any`: Type and behavior are not yet reviewed; see the source.
- `ev` `any`: Type and behavior are not yet reviewed; see the source.
- `re` `any`: Type and behavior are not yet reviewed; see the source.
- `r` `any`: Type and behavior are not yet reviewed; see the source.
- `rp` `any`: Type and behavior are not yet reviewed; see the source.
- `c` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDSummon.lua:441`

```lua
function RushDuel.HandConfirmSpecialSummonOperation(e, tp, eg, ep, ev, re, r, rp, c)
    local tc = e:GetLabelObject()
    Duel.ConfirmCards(1 - tp, tc)
    Duel.ShuffleHand(tp)
end
```
