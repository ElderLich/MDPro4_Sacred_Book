# RushDuel.ChangeAttribute

Alias: `RD.ChangeAttribute`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.ChangeAttribute(any e, any card, any attribute, any reset, any forced) -> any
```

## Description

Rush Duel helper declared in `RDAttach.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
赋予: 改变属性
```

## Parameters

- `e` `any`: Type and behavior are not yet reviewed; see the source.
- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `attribute` `any`: Type and behavior are not yet reviewed; see the source.
- `reset` `any`: Type and behavior are not yet reviewed; see the source.
- `forced` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDAttach.lua:226`

```lua
function RushDuel.ChangeAttribute(e, card, attribute, reset, forced)
    return RushDuel.CreateSingleEffect(e, nil, card, EFFECT_CHANGE_ATTRIBUTE, attribute, reset, forced)
end
```
