# RushDuel.CreateFusionEffect

Alias: `RD.CreateFusionEffect`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CreateFusionEffect(Card card, [function|nil matfilter], [function|nil spfilter], [function|nil exfilter], [int s_range], [int o_range], [function|nil mat_check], [function mat_move], [function|nil target_action], [function|nil operation_action], [function|nil limit_action], [int sum_pos], [bool including_self], [bool self_leave]) -> Effect
```

## Description

Creates an Effect with Rush Fusion target and operation callbacks. It does not register an activation: set type, code, category, description and any costs on the returned Effect, then register it. Locations default to zero, material movement to RD.FusionToGrave, and summon position to POS_FACEUP.
Legality checks do not choose the monster or materials. Resolution rebuilds both pools, chooses the monster and any alternative material route, then selects materials. The operation callback receives materials then the chosen monster; the internal executor does not forward the core summon count.

## Parameters

- `card` `Card`: Card receiving the unregistered summoning Effect.
- `matfilter` `function|nil` (optional): Filter for the ordinary material pool, called with a Card.
- `spfilter` `function|nil` (optional): Summon-candidate filter receiving card, effect, player, material Group, optional route filter and check flags.
- `exfilter` `function|nil` (optional): Filter for extra material locations; separate from matfilter.
- `s_range` `int` (optional): Extra material locations on the player side; default 0. These add to the ordinary pool.
- `o_range` `int` (optional): Extra material locations on the opponent side; default 0.
- `mat_check` `function|nil` (optional): Whole-material-Group restriction evaluated with player, selected Group and summon candidate (plus Fusion check flags for Fusion).
- `mat_move` `function` (optional): Material-movement callback (player, selected Group, effect); defaults to the matching FusionToGrave or RitualToGrave helper.
- `target_action` `function|nil` (optional): Additional target-stage action; not called for chk==0.
- `operation_action` `function|nil` (optional): Additional resolution callback (e,tp,eg,ep,ev,re,r,rp,materials,summon_card) after the executor returns; not proof of a positive summon count.
- `limit_action` `function|nil` (optional): Runs after resolution cleanup even when no candidate remains.
- `sum_pos` `int` (optional): Allowed summon positions; defaults to POS_FACEUP.
- `including_self` `bool` (optional): Require the handler among selected materials; default false.
- `self_leave` `bool` (optional): Exclude the handler from materials and account for its departure when checking zones; default false.

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
