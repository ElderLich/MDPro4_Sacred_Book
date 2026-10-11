# RushDuel.AttachLevel

Alias: `RD.AttachLevel`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.AttachLevel(any e, any card, any level, any reset, any forced) -> any
```

## Description

Rush Duel helper declared in `RDAttach.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
赋予: 等级升降
```

## Parameters

- `e` `any`: Type and behavior are not yet reviewed; see the source.
- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `level` `any`: Type and behavior are not yet reviewed; see the source.
- `reset` `any`: Type and behavior are not yet reviewed; see the source.
- `forced` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDAttach.lua:14`

```lua
function RushDuel.AttachLevel(e, card, level, reset, forced)
    return RushDuel.CreateSingleEffect(e, nil, card, EFFECT_UPDATE_LEVEL, level, reset, forced)
end
```
