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

## Guided Examples

Learn how to use this function in context:

- [Rush Fusion And Ritual: Let The Player Choose](/learn/rush-fusion-ritual-choices)

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **56** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.CreateFusionEffect) with `RushDuel.CreateFusionEffect`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Void Dust Fusion | `120277052` | [Rush/Scripts/c120277052.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120277052.lua) | 1 |
| Flash Memory Fusion | `120285062` | [Rush/Scripts/c120285062.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120285062.lua) | 1 |
| Tama Bond | `120285053` | [Rush/Scripts/c120285053.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120285053.lua) | 1 |
| Rising Equip | `120304062` | [Rush/Scripts/c120304062.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120304062.lua) | 1 |
| Dragon Tribe Fusion | `120238024` | [Rush/Scripts/c120238024.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120238024.lua) | 1 |
| Speed Sniper | `120301060` | [Rush/Scripts/c120301060.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120301060.lua) | 2 |
| Galaxy Chaos Fusion | `120277051` | [Rush/Scripts/c120277051.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120277051.lua) | 1 |
| Road Apostle Slinger | `120285032` | [Rush/Scripts/c120285032.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120285032.lua) | 1 |
| Imaginary Arc Surge | `120271040` | [Rush/Scripts/c120271040.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120271040.lua) | 1 |
| Delirium Rebirth | `120274067` | [Rush/Scripts/c120274067.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120274067.lua) | 1 |
| Princess Cosmos Stirs | `120293054` | [Rush/Scripts/c120293054.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120293054.lua) | 1 |
| Cyber Rush Fusion | `120278029` | [Rush/Scripts/c120278029.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120278029.lua) | 1 |
| Power Bond | `120231070` | [Rush/Scripts/c120231070.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120231070.lua) | 1 |
| Delirium Embrace | `120274065` | [Rush/Scripts/c120274065.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120274065.lua) | 1 |
| Deep Warning Fusion | `120260020` | [Rush/Scripts/c120260020.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120260020.lua) | 1 |
| Super Polymerization | `120307014` | [Rush/Scripts/c120307014.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120307014.lua) | 1 |
| Elemental HERO Voltic Wingman | `120277065` | [Rush/Scripts/c120277065.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120277065.lua) | 1 |
| The United Front with Timaeus | `120309016` | [Rush/Scripts/c120309016.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120309016.lua) | 1 |
| Dragons Boost Fusion | `120244049` | [Rush/Scripts/c120244049.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120244049.lua) | 1 |
| Cyber Surveillance Dragon | `120285043` | [Rush/Scripts/c120285043.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120285043.lua) | 1 |
| The Versus Fusion | `120283051` | [Rush/Scripts/c120283051.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120283051.lua) | 1 |
| Metarion Fusion | `120271036` | [Rush/Scripts/c120271036.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120271036.lua) | 1 |
| Miracle Secret Arts | `120290054` | [Rush/Scripts/c120290054.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120290054.lua) | 1 |
| Psyquip Fusion | `120253051` | [Rush/Scripts/c120253051.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120253051.lua) | 1 |
| ...and 32 more |  |  |  |

## Script Examples

### Void Dust Fusion (`120277052`)

Source: [Rush/Scripts/c120277052.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120277052.lua)

```lua
function cm.initial_effect(c)
	--Activate
	local e1=RD.CreateFusionEffect(c,aux.FALSE,cm.spfilter,cm.matfilter,LOCATION_GRAVE,0,cm.matcheck,RD.FusionToDeck,nil,cm.operation)
	e1:SetCategory(CATEGORY_SPECIAL_SUMMON+CATEGORY_FUSION_SUMMON+CATEGORY_DESTROY)
	e1:SetType(EFFECT_TYPE_ACTIVATE)
```

### Flash Memory Fusion (`120285062`)

Source: [Rush/Scripts/c120285062.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120285062.lua)

```lua
	RD.AddCodeList(c,list)
	--Activate
	local e1=RD.CreateFusionEffect(c,aux.FALSE,cm.spfilter,cm.matfilter,LOCATION_GRAVE,0,nil,RD.FusionToDeck,nil,cm.operation)
	e1:SetCategory(CATEGORY_SPECIAL_SUMMON+CATEGORY_FUSION_SUMMON+CATEGORY_GRAVE_SPSUMMON)
	e1:SetType(EFFECT_TYPE_ACTIVATE)
```

### Tama Bond (`120285053`)

Source: [Rush/Scripts/c120285053.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120285053.lua)

```lua
	RD.AddCodeList(c,list)
	--Activate
	local e1=RD.CreateFusionEffect(c,cm.matfilter,cm.spfilter,nil,0,0,nil,RD.FusionToGrave,nil,cm.operation)
	e1:SetCategory(CATEGORY_SPECIAL_SUMMON+CATEGORY_FUSION_SUMMON+CATEGORY_ATKCHANGE)
	e1:SetType(EFFECT_TYPE_ACTIVATE)
```
