# RushDuel.AttachIndesCount

Alias: `RD.AttachIndesCount`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.AttachIndesCount(any e, any card, any count, any value, any desc, any reset, any forced) -> any
```

## Description

Rush Duel helper declared in `RDAttach.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
赋予: 战斗, 效果破坏抗性 (有次数限制)
```

## Parameters

- `e` `any`: Type and behavior are not yet reviewed; see the source.
- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `count` `any`: Type and behavior are not yet reviewed; see the source.
- `value` `any`: Type and behavior are not yet reviewed; see the source.
- `desc` `any`: Type and behavior are not yet reviewed; see the source.
- `reset` `any`: Type and behavior are not yet reviewed; see the source.
- `forced` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDAttach.lua:85`

```lua
function RushDuel.AttachIndesCount(e, card, count, value, desc, reset, forced)
    local e1 = RushDuel.CreateSingleEffect(e, desc, card, EFFECT_INDESTRUCTABLE_COUNT, value, reset, forced)
    e1:SetCountLimit(count)
    return e1
end
```
