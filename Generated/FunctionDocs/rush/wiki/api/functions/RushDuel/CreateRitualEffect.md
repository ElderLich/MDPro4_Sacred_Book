# RushDuel.CreateRitualEffect

Alias: `RD.CreateRitualEffect`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CreateRitualEffect(any card, any type, any matfilter, any spfilter, any exfilter, any s_range, any o_range, any mat_check, any mat_move, any target_action, any operation_action, any limit_action, any including_self, any self_leave) -> Effect
```

## Description

Creates an Effect with Rush Ritual target and operation callbacks. Configure the returned Effect's activation type, code, category and other requirements, then register it. The comparison mode is one of RITUAL_*; material locations default to zero and material movement defaults to RD.RitualToGrave.
Original/current selects which value of the Ritual monster sets the requirement. Material Level sums use Card.GetRitualLevel and ATK sums use Card.GetAttack in this snapshot; ORIGINAL does not universally mean reading every material's printed stat.

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `type` `any`: Type and behavior are not yet reviewed; see the source.
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
- `including_self` `any`: Type and behavior are not yet reviewed; see the source.
- `self_leave` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `Effect`: Configured but unregistered effect.

## Source

`Rush/Utilities/RDRitual.lua:46`

```lua
function RushDuel.CreateRitualEffect(card, type, matfilter, spfilter, exfilter, s_range, o_range, mat_check, mat_move, target_action, operation_action, limit_action, including_self, self_leave)
    local self_range = s_range or 0
    local opponent_range = o_range or 0
    local move = mat_move or RushDuel.RitualToGrave
    local include = including_self or false
    local leave = self_leave or false
    local e = Effect.CreateEffect(card)
    e:SetTarget(RushDuel.RitualTarget(card, type, matfilter, spfilter, exfilter, self_range, opponent_range, mat_check, include, leave, target_action))
    e:SetOperation(RushDuel.RitualOperation(card, type, matfilter, spfilter, exfilter, self_range, opponent_range, mat_check, move, include, leave, operation_action, limit_action))
    return e
end
```
