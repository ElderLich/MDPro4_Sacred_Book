# RushDuel.CreateMultiChooseEffect3

Alias: `RD.CreateMultiChooseEffect3`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CreateMultiChooseEffect3(any card, any condition, any cost, any hint1, any target1, any operation1, any hint2, any target2, any operation2, any hint3, any target3, any operation3) -> any
```

## Description

Rush Duel helper declared in `RDBase.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
创建效果: 选择效果
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `condition` `any`: Type and behavior are not yet reviewed; see the source.
- `cost` `any`: Type and behavior are not yet reviewed; see the source.
- `hint1` `any`: Type and behavior are not yet reviewed; see the source.
- `target1` `any`: Type and behavior are not yet reviewed; see the source.
- `operation1` `any`: Type and behavior are not yet reviewed; see the source.
- `hint2` `any`: Type and behavior are not yet reviewed; see the source.
- `target2` `any`: Type and behavior are not yet reviewed; see the source.
- `operation2` `any`: Type and behavior are not yet reviewed; see the source.
- `hint3` `any`: Type and behavior are not yet reviewed; see the source.
- `target3` `any`: Type and behavior are not yet reviewed; see the source.
- `operation3` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDBase.lua:204`

```lua
function RushDuel.CreateMultiChooseEffect3(card, condition, cost, hint1, target1, operation1, hint2, target2, operation2, hint3, target3, operation3)
    local e1 = Effect.CreateEffect(card)
    e1:SetType(EFFECT_TYPE_IGNITION)
    e1:SetRange(LOCATION_MZONE)
    if condition ~= nil then
        e1:SetCondition(condition)
    end
    if cost ~= nil then
        e1:SetCost(cost)
    end
    local e2 = e1:Clone()
    local e3 = e1:Clone()
    e1:SetDescription(hint1)
    e2:SetDescription(hint2)
    e3:SetDescription(hint3)
    e1:SetTarget(RushDuel.MultiChooseEffectTarget(target1))
    e2:SetTarget(RushDuel.MultiChooseEffectTarget(target2))
    e3:SetTarget(RushDuel.MultiChooseEffectTarget(target3))
    e1:SetOperation(operation1)
    e2:SetOperation(operation2)
    e3:SetOperation(operation3)
    card:RegisterEffect(e1)
    card:RegisterEffect(e2)
    card:RegisterEffect(e3)
    return e1, e2, e3
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **1** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.CreateMultiChooseEffect3) with `RushDuel.CreateMultiChooseEffect3`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Digracheon the Skysavior Radiaknight | `120301036` | [Rush/Scripts/c120301036.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120301036.lua) | 1 |

## Script Examples

### Digracheon the Skysavior Radiaknight (`120301036`)

Source: [Rush/Scripts/c120301036.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120301036.lua)

```lua
	RD.AddFusionProcedure(c,cm.matfilter,list[1],list[2])
	--Multi-Choose Effect
	local e1,e2,e3=RD.CreateMultiChooseEffect3(c,nil,cm.cost,
		aux.Stringid(m,1),cm.target1,cm.operation1,
		aux.Stringid(m,2),nil,cm.operation2,
```
