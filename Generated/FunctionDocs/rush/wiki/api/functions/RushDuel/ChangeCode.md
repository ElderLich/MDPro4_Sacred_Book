# RushDuel.ChangeCode

Alias: `RD.ChangeCode`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.ChangeCode(any e, any card, any code, any reset, any forced) -> any
```

## Description

Rush Duel helper declared in `RDAttach.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
赋予: 改变卡名
```

## Parameters

- `e` `any`: Type and behavior are not yet reviewed; see the source.
- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `code` `any`: Type and behavior are not yet reviewed; see the source.
- `reset` `any`: Type and behavior are not yet reviewed; see the source.
- `forced` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDAttach.lua:234`

```lua
function RushDuel.ChangeCode(e, card, code, reset, forced)
    return RushDuel.CreateSingleEffect(e, nil, card, EFFECT_CHANGE_CODE, code, reset, forced)
end
```
