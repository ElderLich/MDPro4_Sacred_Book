# RushDuel.MaximumMode

Alias: `RD.MaximumMode`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.MaximumMode(Effect e) -> bool|nil
```

## Description

Effect-condition callback: checks that the handler has EFFECT_MAXIMUM_MODE and at least one overlay component. Use RD.IsMaximumMode for a predicate receiving a Card.

## Parameters

- `e` `Effect`: Effect whose handler is checked.

## Returns

- `bool|nil`: Truthy when the Maximum marker and components are present.

## Source

`Rush/Utilities/RDMaximum.lua:133`

```lua
function RushDuel.MaximumMode(e)
    local c = e:GetHandler()
    return c:IsHasEffect(EFFECT_MAXIMUM_MODE) and c:GetOverlayCount() > 0
end
```
