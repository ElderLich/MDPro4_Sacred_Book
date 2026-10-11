# RushDuel.EnableUnionFusion

Alias: `RD.EnableUnionFusion`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.EnableUnionFusion(any card, any desc) -> any
```

## Description

Rush Duel helper declared in `RDFusion.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
可以进行同盟融合术
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `desc` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDFusion.lua:309`

```lua
function RushDuel.EnableUnionFusion(card, desc)
    local e = Effect.CreateEffect(card)
    e:SetDescription(desc)
    e:SetType(EFFECT_TYPE_FIELD)
    e:SetCode(EFFECT_SPSUMMON_PROC)
    e:SetProperty(EFFECT_FLAG_CANNOT_DISABLE + EFFECT_FLAG_UNCOPYABLE)
    e:SetRange(LOCATION_EXTRA)
    e:SetCondition(RushDuel.UnionFusionCondition)
    e:SetTarget(RushDuel.UnionFusionTarget)
    e:SetOperation(RushDuel.UnionFusionOperation)
    e:SetValue(SUMMON_TYPE_FUSION)
    card:RegisterEffect(e)
    return e
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **6** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.EnableUnionFusion) with `RushDuel.EnableUnionFusion`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [YXZ-Cannon Dragon](/examples/rush-cards/120305004) | `120305004` | [Rush/Scripts/c120305004.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120305004.lua) | 1 |
| XYZ-Dragon Cannon | `120305003` | [Rush/Scripts/c120305003.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120305003.lua) | 1 |
| XZ-Tank Cannon | `120305006` | [Rush/Scripts/c120305006.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120305006.lua) | 1 |
| YZ-Tank Dragon | `120305007` | [Rush/Scripts/c120305007.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120305007.lua) | 1 |
| XY-Dragon Cannon | `120305005` | [Rush/Scripts/c120305005.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120305005.lua) | 1 |
| Soitsu and Doitsu | `120306040` | [Rush/Scripts/c120306040.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120306040.lua) | 1 |

## Script Examples

### YXZ-Cannon Dragon (`120305004`)

Source: [Rush/Scripts/c120305004.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120305004.lua)

```lua
	RD.SetFusionMaterial(c,{list[1],list[2],list[3]},3,3)
	--Union Fusion
	RD.EnableUnionFusion(c,aux.Stringid(m,0))
	--Change Code
	RD.EnableChangeCode(c,list[4],LOCATION_EXTRA)
```

### XYZ-Dragon Cannon (`120305003`)

Source: [Rush/Scripts/c120305003.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120305003.lua)

```lua
	RD.SetFusionMaterial(c,{list[1],list[2],list[3]},3,3)
	--Union Fusion
	RD.EnableUnionFusion(c,aux.Stringid(m,0))
	--Destroy
	local e1=Effect.CreateEffect(c)
```

### XZ-Tank Cannon (`120305006`)

Source: [Rush/Scripts/c120305006.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120305006.lua)

```lua
	RD.AddFusionProcedure(c,list[1],list[2])
	--Union Fusion
	RD.EnableUnionFusion(c,aux.Stringid(m,0))
	--Extra Material
	local e1=Effect.CreateEffect(c)
```
