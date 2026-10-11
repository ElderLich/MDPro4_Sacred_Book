# RushDuel.CreateFusionSummonFlag

Alias: `RD.CreateFusionSummonFlag`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CreateFusionSummonFlag(any card, any flag) -> any
```

## Description

Rush Duel helper declared in `RDSummon.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
记录融合术召唤的状态
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `flag` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDSummon.lua:308`

```lua
function RushDuel.CreateFusionSummonFlag(card, flag)
    local e1 = Effect.CreateEffect(card)
    e1:SetType(EFFECT_TYPE_SINGLE + EFFECT_TYPE_CONTINUOUS)
    e1:SetCode(EVENT_SPSUMMON_SUCCESS)
    e1:SetProperty(EFFECT_FLAG_CANNOT_DISABLE)
    e1:SetLabel(flag)
    e1:SetCondition(RushDuel.FusionSummonFlagCondition)
    e1:SetOperation(RushDuel.FusionSummonFlagOperation)
    card:RegisterEffect(e1)
    return e1
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **5** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.CreateFusionSummonFlag) with `RushDuel.CreateFusionSummonFlag`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Princess Cosmos the Cosmic Trickster | `120293043` | [Rush/Scripts/c120293043.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120293043.lua) | 1 |
| Ancient Gear Megaton Golem | `120283030` | [Rush/Scripts/c120283030.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120283030.lua) | 1 |
| Dark Matter Enigmata | `120261048` | [Rush/Scripts/c120261048.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120261048.lua) | 1 |
| Chimeratech Crush Dragon | `120283031` | [Rush/Scripts/c120283031.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120283031.lua) | 1 |
| Chimeratech Overdragon | `120278001` | [Rush/Scripts/c120278001.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120278001.lua) | 1 |

## Script Examples

### Princess Cosmos the Cosmic Trickster (`120293043`)

Source: [Rush/Scripts/c120293043.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120293043.lua)

```lua
	RD.AddFusionProcedureRep(c,true,true,cm.matfilter,2,63,list[1])
	-- Fusion Flag
	RD.CreateFusionSummonFlag(c,20293043)
	--Destroy
	local e1=Effect.CreateEffect(c)
```

### Ancient Gear Megaton Golem (`120283030`)

Source: [Rush/Scripts/c120283030.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120283030.lua)

```lua
	RD.AddFusionProcedure(c,cm.matfilter,cm.matfilter,cm.matfilter)
	-- Fusion Flag
	RD.CreateFusionSummonFlag(c,20283030)
	-- Cannot Activate
	local e1=RD.ContinuousAttackNotChainTrap(c)
```

### Dark Matter Enigmata (`120261048`)

Source: [Rush/Scripts/c120261048.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120261048.lua)

```lua
	RD.AddFusionProcedure(c,list[1],list[1])
	-- Fusion Flag
	RD.CreateFusionSummonFlag(c,20261048)
	--Atk Up
	local e1=Effect.CreateEffect(c)
```
