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

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **41** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.CreateRitualEffect) with `RushDuel.CreateRitualEffect`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Ceremonial Gate](/examples/rush-cards/120280031) | `120280031` | [Rush/Scripts/c120280031.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120280031.lua) | 1 |
| [Black Magic Ritual](/examples/rush-cards/120280030) | `120280030` | [Rush/Scripts/c120280030.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120280030.lua) | 1 |
| Jeweled Tusk Ritual | `120290056` | [Rush/Scripts/c120290056.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120290056.lua) | 1 |
| Skullrise Squall | `120298011` | [Rush/Scripts/c120298011.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120298011.lua) | 1 |
| Dimension Pair Link L | `120309030` | [Rush/Scripts/c120309030.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120309030.lua) | 1 |
| Dimension Pair Link R | `120309031` | [Rush/Scripts/c120309031.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120309031.lua) | 1 |
| Healthy's High! | `120306051` | [Rush/Scripts/c120306051.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120306051.lua) | 1 |
| I'm Having Trouble with My Fields Being Destroyed! | `120298028` | [Rush/Scripts/c120298028.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120298028.lua) | 1 |
| I Need Holy Water to Ward Off Evil Spirits! | `120298029` | [Rush/Scripts/c120298029.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120298029.lua) | 1 |
| Endless Partner | `120300050` | [Rush/Scripts/c120300050.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120300050.lua) | 1 |
| Monumenthes Festival -The Isyria Seance- | `120300046` | [Rush/Scripts/c120300046.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120300046.lua) | 1 |
| Ninjitsu Art of Ultimate Transformation | `120306056` | [Rush/Scripts/c120306056.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120306056.lua) | 1 |
| Plasmatic Model Another Play | `120301070` | [Rush/Scripts/c120301070.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120301070.lua) | 1 |
| Skullrise Violent | `120298012` | [Rush/Scripts/c120298012.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120298012.lua) | 1 |
| Plasmatic Model Another Docking | `120290051` | [Rush/Scripts/c120290051.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120290051.lua) | 1 |
| Beastly Mirror Calling | `120304057` | [Rush/Scripts/c120304057.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120304057.lua) | 1 |
| Altar of the Twin Blaze Fiends | `120287036` | [Rush/Scripts/c120287036.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120287036.lua) | 1 |
| Plasmatic Model Play | `120285058` | [Rush/Scripts/c120285058.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120285058.lua) | 1 |
| Necromaid Resize | `120294050` | [Rush/Scripts/c120294050.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120294050.lua) | 1 |
| Plasmatic Model Docking | `120285057` | [Rush/Scripts/c120285057.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120285057.lua) | 1 |
| Healthy Mind Speedy Buzzer Battle! | `120306052` | [Rush/Scripts/c120306052.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120306052.lua) | 1 |
| Bluefin Oath | `120287085` | [Rush/Scripts/c120287085.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120287085.lua) | 1 |
| Legend Possessed | `120293068` | [Rush/Scripts/c120293068.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120293068.lua) | 1 |
| War-Lion Assault | `120294058` | [Rush/Scripts/c120294058.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120294058.lua) | 1 |
| ...and 17 more |  |  |  |

## Script Examples

### Ceremonial Gate (`120280031`)

Source: [Rush/Scripts/c120280031.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120280031.lua)

```lua
	RD.AddCodeList(c,list)
	--Activate
	local e1=RD.CreateRitualEffect(c,RITUAL_ORIGINAL_LEVEL_GREATER,cm.matfilter,cm.spfilter)
	e1:SetCategory(CATEGORY_SPECIAL_SUMMON)
	e1:SetType(EFFECT_TYPE_ACTIVATE)
```

### Black Magic Ritual (`120280030`)

Source: [Rush/Scripts/c120280030.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120280030.lua)

```lua
	RD.AddCodeList(c,list)
	--Activate
	local e1=RD.CreateRitualEffect(c,RITUAL_ORIGINAL_LEVEL_GREATER,nil,cm.spfilter)
	e1:SetCategory(CATEGORY_SPECIAL_SUMMON)
	e1:SetType(EFFECT_TYPE_ACTIVATE)
```

### Jeweled Tusk Ritual (`120290056`)

Source: [Rush/Scripts/c120290056.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120290056.lua)

```lua
	Duel.AddCustomActivityCounter(m,ACTIVITY_SPSUMMON,cm.ctfilter)
	--Activate
	local e1=RD.CreateRitualEffect(c,RITUAL_ORIGINAL_LEVEL_GREATER,cm.matfilter,cm.spfilter,nil,0,0,nil,RD.RitualToGrave,nil,cm.operation)
	e1:SetCategory(CATEGORY_SPECIAL_SUMMON)
	e1:SetType(EFFECT_TYPE_ACTIVATE)
```
