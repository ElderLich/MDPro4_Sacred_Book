# RushDuel.RitualToGrave

Alias: `RD.RitualToGrave`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.RitualToGrave(any tp, any mat) -> any
```

## Description

Rush Duel helper declared in `RDRitual.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
素材去向: 墓地
```

## Parameters

- `tp` `any`: Type and behavior are not yet reviewed; see the source.
- `mat` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDRitual.lua:441`

```lua
function RushDuel.RitualToGrave(tp, mat)
    Duel.SendtoGrave(mat, REASON_EFFECT + REASON_MATERIAL + REASON_RITUAL)
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **18** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.RitualToGrave) with `RushDuel.RitualToGrave`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Jeweled Tusk Ritual | `120290056` | [Rush/Scripts/c120290056.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120290056.lua) | 1 |
| Skullrise Squall | `120298011` | [Rush/Scripts/c120298011.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120298011.lua) | 1 |
| Dimension Pair Link L | `120309030` | [Rush/Scripts/c120309030.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120309030.lua) | 1 |
| Dimension Pair Link R | `120309031` | [Rush/Scripts/c120309031.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120309031.lua) | 1 |
| Healthy's High! | `120306051` | [Rush/Scripts/c120306051.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120306051.lua) | 1 |
| I'm Having Trouble with My Fields Being Destroyed! | `120298028` | [Rush/Scripts/c120298028.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120298028.lua) | 1 |
| I Need Holy Water to Ward Off Evil Spirits! | `120298029` | [Rush/Scripts/c120298029.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120298029.lua) | 1 |
| Ninjitsu Art of Ultimate Transformation | `120306056` | [Rush/Scripts/c120306056.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120306056.lua) | 1 |
| Plasmatic Model Another Play | `120301070` | [Rush/Scripts/c120301070.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120301070.lua) | 1 |
| Skullrise Violent | `120298012` | [Rush/Scripts/c120298012.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120298012.lua) | 1 |
| Plasmatic Model Another Docking | `120290051` | [Rush/Scripts/c120290051.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120290051.lua) | 1 |
| Beastly Mirror Calling | `120304057` | [Rush/Scripts/c120304057.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120304057.lua) | 1 |
| Altar of the Twin Blaze Fiends | `120287036` | [Rush/Scripts/c120287036.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120287036.lua) | 1 |
| Plasmatic Model Play | `120285058` | [Rush/Scripts/c120285058.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120285058.lua) | 1 |
| Necromaid Resize | `120294050` | [Rush/Scripts/c120294050.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120294050.lua) | 1 |
| Plasmatic Model Docking | `120285057` | [Rush/Scripts/c120285057.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120285057.lua) | 1 |
| War-Lion Assault | `120294058` | [Rush/Scripts/c120294058.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120294058.lua) | 1 |
| Root of Despair | `120301033` | [Rush/Scripts/c120301033.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120301033.lua) | 1 |

## Script Examples

### Jeweled Tusk Ritual (`120290056`)

Source: [Rush/Scripts/c120290056.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120290056.lua)

```lua
	Duel.AddCustomActivityCounter(m,ACTIVITY_SPSUMMON,cm.ctfilter)
	--Activate
	local e1=RD.CreateRitualEffect(c,RITUAL_ORIGINAL_LEVEL_GREATER,cm.matfilter,cm.spfilter,nil,0,0,nil,RD.RitualToGrave,nil,cm.operation)
	e1:SetCategory(CATEGORY_SPECIAL_SUMMON)
	e1:SetType(EFFECT_TYPE_ACTIVATE)
```

### Skullrise Squall (`120298011`)

Source: [Rush/Scripts/c120298011.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120298011.lua)

```lua
	RD.AddCodeList(c,list)
	--Activate
	local e1=RD.CreateRitualEffect(c,RITUAL_ORIGINAL_LEVEL_GREATER,cm.matfilter,cm.spfilter,nil,0,0,nil,RD.RitualToGrave,nil,cm.operation)
	e1:SetCategory(CATEGORY_SPECIAL_SUMMON+CATEGORY_DESTROY)
	e1:SetType(EFFECT_TYPE_ACTIVATE)
```

### Dimension Pair Link L (`120309030`)

Source: [Rush/Scripts/c120309030.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120309030.lua)

```lua
	RD.AddCodeList(c,list)
	--Activate
	local e1=RD.CreateRitualEffect(c,RITUAL_ORIGINAL_LEVEL_GREATER,cm.matfilter,cm.spfilter,nil,0,0,nil,RD.RitualToGrave,nil,cm.operation)
	e1:SetCategory(CATEGORY_SPECIAL_SUMMON+CATEGORY_TOGRAVE+CATEGORY_GRAVE_SPSUMMON)
	e1:SetType(EFFECT_TYPE_ACTIVATE)
```
