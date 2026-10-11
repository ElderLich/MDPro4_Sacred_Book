# RushDuel.SetBaseAtkDef

Alias: `RD.SetBaseAtkDef`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.SetBaseAtkDef(any e, any card, any atk, any def, any reset, any forced) -> any
```

## Description

Rush Duel helper declared in `RDAttach.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
赋予: 变更原本攻守
```

## Parameters

- `e` `any`: Type and behavior are not yet reviewed; see the source.
- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `atk` `any`: Type and behavior are not yet reviewed; see the source.
- `def` `any`: Type and behavior are not yet reviewed; see the source.
- `reset` `any`: Type and behavior are not yet reviewed; see the source.
- `forced` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDAttach.lua:202`

```lua
function RushDuel.SetBaseAtkDef(e, card, atk, def, reset, forced)
    if atk ~= nil then
        RushDuel.CreateSingleEffect(e, nil, card, EFFECT_SET_BASE_ATTACK, atk, reset, forced)
    end
    if def ~= nil and RushDuel.IsCanChangeDef(card) then
        RushDuel.CreateSingleEffect(e, nil, card, EFFECT_SET_BASE_DEFENSE, def, reset, forced)
    end
end
```
