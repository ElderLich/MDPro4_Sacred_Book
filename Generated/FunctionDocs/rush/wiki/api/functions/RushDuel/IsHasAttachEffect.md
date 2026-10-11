# RushDuel.IsHasAttachEffect

Alias: `RD.IsHasAttachEffect`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.IsHasAttachEffect(any card, any code) -> any
```

## Description

Rush Duel helper declared in `RDCondition.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
条件: 被赋予了效果
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `code` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCondition.lua:235`

```lua
function RushDuel.IsHasAttachEffect(card, code)
    return #RushDuel.GetAttachEffects(card, code) ~= 0
end
```
