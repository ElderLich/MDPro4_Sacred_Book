# RushDuel.AttackNotChainTrapOperation

Alias: `RD.AttackNotChainTrapOperation`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.AttackNotChainTrapOperation(any e, any tp, any eg, any ep, any ev, any re, any r, any rp) -> any
```

## Description

Rush Duel helper declared in `RDContinuous.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

## Parameters

- `e` `any`: Type and behavior are not yet reviewed; see the source.
- `tp` `any`: Type and behavior are not yet reviewed; see the source.
- `eg` `any`: Type and behavior are not yet reviewed; see the source.
- `ep` `any`: Type and behavior are not yet reviewed; see the source.
- `ev` `any`: Type and behavior are not yet reviewed; see the source.
- `re` `any`: Type and behavior are not yet reviewed; see the source.
- `r` `any`: Type and behavior are not yet reviewed; see the source.
- `rp` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDContinuous.lua:76`

```lua
function RushDuel.AttackNotChainTrapOperation(e, tp, eg, ep, ev, re, r, rp)
    Duel.Hint(HINT_CARD, 0, e:GetLabel())
    Duel.SetChainLimitTillChainEnd(RushDuel.AttachAttackNotChainTrapLimit)
end
```
