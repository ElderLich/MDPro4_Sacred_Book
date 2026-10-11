# RushDuel.AttachEffectIndes

Alias: `RD.AttachEffectIndes`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.AttachEffectIndes(any e, any card, any value, any desc, any reset, any forced) -> any
```

## Description

Rush Duel helper declared in `RDAttach.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
赋予: 效果破坏抗性
```

## Parameters

- `e` `any`: Type and behavior are not yet reviewed; see the source.
- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `value` `any`: Type and behavior are not yet reviewed; see the source.
- `desc` `any`: Type and behavior are not yet reviewed; see the source.
- `reset` `any`: Type and behavior are not yet reviewed; see the source.
- `forced` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDAttach.lua:79`

```lua
function RushDuel.AttachEffectIndes(e, card, value, desc, reset, forced)
    local attach = RushDuel.CreateSingleEffect(e, desc, card, EFFECT_INDESTRUCTABLE_EFFECT, value, reset, forced)
    attach:SetOwnerPlayer(e:GetHandlerPlayer())
    return attach
end
```
