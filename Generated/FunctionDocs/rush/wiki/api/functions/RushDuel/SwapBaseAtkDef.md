# RushDuel.SwapBaseAtkDef

Alias: `RD.SwapBaseAtkDef`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.SwapBaseAtkDef(any e, any card, any reset, any forced) -> any
```

## Description

Rush Duel helper declared in `RDAttach.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
赋予: 交换原本攻守
```

## Parameters

- `e` `any`: Type and behavior are not yet reviewed; see the source.
- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `reset` `any`: Type and behavior are not yet reviewed; see the source.
- `forced` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDAttach.lua:211`

```lua
function RushDuel.SwapBaseAtkDef(e, card, reset, forced)
    if RushDuel.IsCanChangeDef(card) then
        RushDuel.CreateSingleEffect(e, nil, card, EFFECT_SWAP_BASE_AD, nil, reset, forced)
    end
end
```
