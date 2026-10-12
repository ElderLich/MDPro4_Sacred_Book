# RushDuel.ConditionSummonTurn

Alias: `RD.ConditionSummonTurn`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.ConditionSummonTurn(any e) -> any
```

## Description

Rush Duel helper declared in `RDCondition.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
通用条件: 这张卡召唤的回合
```

## Parameters

- `e` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCondition.lua:432`

```lua
function RushDuel.ConditionSummonTurn(e)
	return RushDuel.IsSummonTurn(e:GetHandler())
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **152** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.ConditionSummonTurn) with `RushDuel.ConditionSummonTurn`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Freshberry Collaboration](/examples/rush-cards/120301071) | `120301071` | [Rush/Scripts/c120301071.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120301071.lua) | 1 |
| [Lovely Wolf](/examples/rush-cards/120260046) | `120260046` | [Rush/Scripts/c120260046.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120260046.lua) | 1 |
| [Devil Foolish](/examples/rush-cards/120244026) | `120244026` | [Rush/Scripts/c120244026.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120244026.lua) | 1 |
| [Madrhea Amelo](/examples/rush-cards/120300028) | `120300028` | [Rush/Scripts/c120300028.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120300028.lua) | 1 |
| Plasmatic Model Smart Owl | `120285019` | [Rush/Scripts/c120285019.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120285019.lua) | 1 |
| Gilford the Legend | `120235029` | [Rush/Scripts/c120235029.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120235029.lua) | 1 |
| Hydrangea the Shadow Flower Tea Master | `120304029` | [Rush/Scripts/c120304029.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120304029.lua) | 1 |
| Rurigra the Eternal | `120285028` | [Rush/Scripts/c120285028.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120285028.lua) | 1 |
| Goe Goe the Rumored Ninja | `120306029` | [Rush/Scripts/c120306029.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120306029.lua) | 1 |
| Cornetlass the Music Princess | `120287066` | [Rush/Scripts/c120287066.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120287066.lua) | 1 |
| Jointech Leo | `120232002` | [Rush/Scripts/c120232002.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120232002.lua) | 1 |
| Udzue the Frost-Purifying Purebreed | `120296001` | [Rush/Scripts/c120296001.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120296001.lua) | 1 |
| Iris the Rare Shadow Flower | `120228018` | [Rush/Scripts/c120228018.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120228018.lua) | 1 |
| Jointech Raptor | `120109021` | [Rush/Scripts/c120109021.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120109021.lua) | 1 |
| Lovely Ange | `120272026` | [Rush/Scripts/c120272026.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120272026.lua) | 1 |
| Hebe the Star Vassal | `120244015` | [Rush/Scripts/c120244015.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120244015.lua) | 1 |
| Legendary Saber | `120238010` | [Rush/Scripts/c120238010.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120238010.lua) | 1 |
| Celeb Rose Wiz | `120253008` | [Rush/Scripts/c120253008.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120253008.lua) | 1 |
| Bandijo the Battle Ballad | `120228026` | [Rush/Scripts/c120228026.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120228026.lua) | 1 |
| Ice Age Catapult | `120170013` | [Rush/Scripts/c120170013.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120170013.lua) | 1 |
| Aise the Snowmaiden of Sacred Splendor | `120277036` | [Rush/Scripts/c120277036.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120277036.lua) | 1 |
| Marsphlox the Planetairy | `120293050` | [Rush/Scripts/c120293050.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120293050.lua) | 1 |
| Royal Rebel's Great Mixer | `120306004` | [Rush/Scripts/c120306004.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120306004.lua) | 1 |
| Healthie Shanlong | `120306020` | [Rush/Scripts/c120306020.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120306020.lua) | 1 |
| ...and 128 more |  |  |  |

## Script Examples

### Freshberry Collaboration (`120301071`)

Source: [Rush/Scripts/c120301071.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120301071.lua)

```lua
	e1:SetType(EFFECT_TYPE_IGNITION)
	e1:SetRange(LOCATION_MZONE)
	e1:SetCondition(RD.ConditionSummonTurn)
	e1:SetCost(cm.cost)
	e1:SetTarget(cm.target)
```

### Lovely Wolf (`120260046`)

Source: [Rush/Scripts/c120260046.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120260046.lua)

```lua
	e1:SetType(EFFECT_TYPE_IGNITION)
	e1:SetRange(LOCATION_MZONE)
	e1:SetCondition(RD.ConditionSummonTurn)
	e1:SetCost(cm.cost)
	e1:SetTarget(cm.target)
```

### Devil Foolish (`120244026`)

Source: [Rush/Scripts/c120244026.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120244026.lua)

```lua
	e1:SetType(EFFECT_TYPE_IGNITION)
	e1:SetRange(LOCATION_MZONE)
	e1:SetCondition(RD.ConditionSummonTurn)
	e1:SetCost(cm.cost)
	e1:SetTarget(cm.target)
```
