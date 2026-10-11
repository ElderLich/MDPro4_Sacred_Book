# RushDuel.CreateMultiChooseEffect

Alias: `RD.CreateMultiChooseEffect`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CreateMultiChooseEffect(any card, any condition, any cost, any hint1, any target1, any operation1, any hint2, any target2, any operation2) -> any
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

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDBase.lua:182`

```lua
function RushDuel.CreateMultiChooseEffect(card, condition, cost, hint1, target1, operation1, hint2, target2, operation2)
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
    e1:SetDescription(hint1)
    e2:SetDescription(hint2)
    e1:SetTarget(RushDuel.MultiChooseEffectTarget(target1))
    e2:SetTarget(RushDuel.MultiChooseEffectTarget(target2))
    e1:SetOperation(operation1)
    e2:SetOperation(operation2)
    card:RegisterEffect(e1)
    card:RegisterEffect(e2)
    return e1, e2
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **41** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.CreateMultiChooseEffect) with `RushDuel.CreateMultiChooseEffect`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Yamiterasu the Divine Ruler | `120199036` | [Rush/Scripts/c120199036.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120199036.lua) | 1 |
| The Trinity Dragiastar | `120109031` | [Rush/Scripts/c120109031.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120109031.lua) | 1 |
| The Dragiastar | `120235035` | [Rush/Scripts/c120235035.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120235035.lua) | 1 |
| Metarion King Cobrastar | `120205039` | [Rush/Scripts/c120205039.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120205039.lua) | 1 |
| Roadstar Gladimagia | `120272042` | [Rush/Scripts/c120272042.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120272042.lua) | 1 |
| CAN:D LIVE | `120199035` | [Rush/Scripts/c120199035.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120199035.lua) | 1 |
| Chartres the Skysavior Shining Light | `120301037` | [Rush/Scripts/c120301037.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120301037.lua) | 1 |
| Gulflare, the Skysavior | `120253049` | [Rush/Scripts/c120253049.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120253049.lua) | 1 |
| Sevens Paladin | `120196015` | [Rush/Scripts/c120196015.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120196015.lua) | 1 |
| Void Strike Dragon Zerogaigias | `120211001` | [Rush/Scripts/c120211001.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120211001.lua) | 1 |
| Fullmetarion Ashurastar | `120271016` | [Rush/Scripts/c120271016.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120271016.lua) | 1 |
| Princess Omega the Shining Megastar | `120217025` | [Rush/Scripts/c120217025.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120217025.lua) | 1 |
| Gaia, Conqueror of Champions | `120249046` | [Rush/Scripts/c120249046.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120249046.lua) | 1 |
| Metarion Vritrastar | `120196002` | [Rush/Scripts/c120196002.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120196002.lua) | 1 |
| Metarion Armarostar | `120272046` | [Rush/Scripts/c120272046.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120272046.lua) | 1 |
| Sevensgias the Magical Dragon Knight | `120208037` | [Rush/Scripts/c120208037.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120208037.lua) | 1 |
| Solciere, the Radiant Skysavior | `120235038` | [Rush/Scripts/c120235038.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120235038.lua) | 1 |
| Semeterasu the Divine Ruler | `120205036` | [Rush/Scripts/c120205036.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120205036.lua) | 1 |
| Raidacross Ash, Hero of Chaos | `120199034` | [Rush/Scripts/c120199034.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120199034.lua) | 1 |
| Endless Romance Blitz | `120205034` | [Rush/Scripts/c120205034.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120205034.lua) | 1 |
| Solid Strike Dragon Metagiastar F | `120217004` | [Rush/Scripts/c120217004.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120217004.lua) | 1 |
| Omega Guitarna the Shining Megastar | `120217024` | [Rush/Scripts/c120217024.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120217024.lua) | 1 |
| Hyperstrike Dragon Dragiastar IF | `120294040` | [Rush/Scripts/c120294040.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120294040.lua) | 1 |
| Metarion Medustar | `120271018` | [Rush/Scripts/c120271018.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120271018.lua) | 1 |
| ...and 17 more |  |  |  |

## Script Examples

### Yamiterasu the Divine Ruler (`120199036`)

Source: [Rush/Scripts/c120199036.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120199036.lua)

```lua
	RD.AddFusionProcedure(c,list[1],list[2])
	--Multi-Choose Effect
	local e1,e2=RD.CreateMultiChooseEffect(c,nil,cm.cost,aux.Stringid(m,1),nil,cm.operation1,aux.Stringid(m,2),cm.target2,cm.operation2)
	e1:SetCategory(CATEGORY_ATKCHANGE)
	e2:SetCategory(CATEGORY_POSITION)
```

### The Trinity Dragiastar (`120109031`)

Source: [Rush/Scripts/c120109031.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120109031.lua)

```lua
	RD.AddFusionProcedure(c,list[1],list[1],list[1])
	--Multi-Choose Effect
	local e1,e2=RD.CreateMultiChooseEffect(c,cm.condition,cm.cost,aux.Stringid(m,1),cm.target1,cm.operation1,aux.Stringid(m,2),cm.target2,cm.operation2)
	e2:SetCategory(CATEGORY_TOGRAVE+CATEGORY_GRAVE_ACTION+CATEGORY_DESTROY)
end
```

### The Dragiastar (`120235035`)

Source: [Rush/Scripts/c120235035.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120235035.lua)

```lua
	RD.AddFusionProcedure(c,list[1],list[1])
	--Multi-Choose Effect
	local e1,e2=RD.CreateMultiChooseEffect(c,cm.condition,cm.cost,aux.Stringid(m,1),cm.target1,cm.operation1,aux.Stringid(m,2),cm.target2,cm.operation2)
	e2:SetCategory(CATEGORY_SPECIAL_SUMMON+CATEGORY_GRAVE_SPSUMMON)
end
```
