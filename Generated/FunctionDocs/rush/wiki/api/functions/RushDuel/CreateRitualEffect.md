# RushDuel.CreateRitualEffect

Alias: `RD.CreateRitualEffect`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CreateRitualEffect(Card card, int type, [function|nil matfilter], [function|nil spfilter], [function|nil exfilter], [int s_range], [int o_range], [function|nil mat_check], [function mat_move], [function|nil target_action], [function|nil operation_action], [function|nil limit_action], [bool including_self], [bool self_leave]) -> Effect
```

## Description

Creates an Effect with Rush Ritual target and operation callbacks. Configure the returned Effect's activation type, code, category and other requirements, then register it. The comparison mode is one of RITUAL_*; material locations default to zero and material movement defaults to RD.RitualToGrave.
Original/current selects which value of the Ritual monster sets the requirement. Material Level sums use Card.GetRitualLevel and ATK sums use Card.GetAttack in this snapshot; ORIGINAL does not universally mean reading every material's printed stat.
Use this factory for the pinned Ritual scripts. Resolution chooses an Extra Deck monster, then a material route and a legal material Group. Canceling material selection returns to monster selection. The operation callback receives the selected materials and Ritual monster, not a numeric summon result.

## Parameters

- `card` `Card`: Card receiving the unregistered summoning Effect.
- `type` `int`: RITUAL_* comparison mode; required.
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
- `including_self` `bool` (optional): Require the handler among selected materials; default false.
- `self_leave` `bool` (optional): Exclude the handler from materials and account for its departure when checking zones; default false.

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
