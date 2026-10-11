# RushDuel.CreateFusionEffect

Alias: `RD.CreateFusionEffect`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CreateFusionEffect(any card, any matfilter, any spfilter, any exfilter, any s_range, any o_range, any mat_check, any mat_move, any target_action, any operation_action, any limit_action, any sum_pos, any including_self, any self_leave) -> Effect
```

## Description

Creates an Effect with Rush Fusion target and operation callbacks. It does not register an activation: set type, code, category, description and any costs on the returned Effect, then register it. Locations default to zero, material movement to RD.FusionToGrave, and summon position to POS_FACEUP.

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `matfilter` `any`: Type and behavior are not yet reviewed; see the source.
- `spfilter` `any`: Type and behavior are not yet reviewed; see the source.
- `exfilter` `any`: Type and behavior are not yet reviewed; see the source.
- `s_range` `any`: Type and behavior are not yet reviewed; see the source.
- `o_range` `any`: Type and behavior are not yet reviewed; see the source.
- `mat_check` `any`: Type and behavior are not yet reviewed; see the source.
- `mat_move` `any`: Type and behavior are not yet reviewed; see the source.
- `target_action` `any`: Type and behavior are not yet reviewed; see the source.
- `operation_action` `any`: Type and behavior are not yet reviewed; see the source.
- `limit_action` `any`: Type and behavior are not yet reviewed; see the source.
- `sum_pos` `any`: Type and behavior are not yet reviewed; see the source.
- `including_self` `any`: Type and behavior are not yet reviewed; see the source.
- `self_leave` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `Effect`: Configured but unregistered effect.

## Source

`Rush/Utilities/RDFusion.lua:365`

```lua
function RushDuel.CreateFusionEffect(card, matfilter, spfilter, exfilter, s_range, o_range, mat_check, mat_move, target_action, operation_action, limit_action, sum_pos, including_self, self_leave)
    local self_range = s_range or 0
    local opponent_range = o_range or 0
    local move = mat_move or RushDuel.FusionToGrave
    local include = including_self or false
    local leave = self_leave or false
    local pos = sum_pos or POS_FACEUP
    local e = Effect.CreateEffect(card)
    e:SetTarget(RushDuel.FusionTarget(card, matfilter, spfilter, exfilter, self_range, opponent_range, mat_check, include, leave, pos, target_action))
    e:SetOperation(RushDuel.FusionOperation(card, matfilter, spfilter, exfilter, self_range, opponent_range, mat_check, move, include, leave, pos, operation_action, limit_action))
    return e
end
```
