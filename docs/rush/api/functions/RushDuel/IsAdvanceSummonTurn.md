# RushDuel.IsAdvanceSummonTurn

Alias: `RD.IsAdvanceSummonTurn`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.IsAdvanceSummonTurn(any card) -> any
```

## Description

Rush Duel helper declared in `RDCondition.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
条件: 这张卡攻击表示上级召唤的回合
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCondition.lua:34`

```lua
function RushDuel.IsAdvanceSummonTurn(card)
    return RushDuel.IsSummonTurn(card) and card:IsSummonType(SUMMON_TYPE_ADVANCE)
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **13** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.IsAdvanceSummonTurn) with `RushDuel.IsAdvanceSummonTurn`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Infernal Flame Emperor | `120109045` | [Rush/Scripts/c120109045.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120109045.lua) | 1 |
| Lindorm the Dragon Monarch | `120291003` | [Rush/Scripts/c120291003.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120291003.lua) | 1 |
| Caius the Shadow Monarch | `120291001` | [Rush/Scripts/c120291001.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120291001.lua) | 1 |
| Lindorm the Mega Monarch | `120291002` | [Rush/Scripts/c120291002.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120291002.lua) | 1 |
| Star Monarch Estrome | `120244017` | [Rush/Scripts/c120244017.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120244017.lua) | 1 |
| Thestalos the Firestorm Monarch | `120248001` | [Rush/Scripts/c120248001.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120248001.lua) | 1 |
| Wilhel the Wisdom Monarch | `120244016` | [Rush/Scripts/c120244016.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120244016.lua) | 1 |
| Mega Star Monarch Estrome | `120244019` | [Rush/Scripts/c120244019.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120244019.lua) | 1 |
| Wilhel the Mega Monarch | `120244018` | [Rush/Scripts/c120244018.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120244018.lua) | 1 |
| Raiza the Storm Monarch | `120247064` | [Rush/Scripts/c120247064.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120247064.lua) | 1 |
| Mobius the Frost Monarch | `120271003` | [Rush/Scripts/c120271003.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120271003.lua) | 1 |
| Granmarg the Rock Monarch | `120261033` | [Rush/Scripts/c120261033.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120261033.lua) | 1 |
| Zaborg the Thunder Monarch | `120244020` | [Rush/Scripts/c120244020.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120244020.lua) | 1 |

## Script Examples

### Infernal Flame Emperor (`120109045`)

Source: [Rush/Scripts/c120109045.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120109045.lua)

```lua
end
function cm.condition(e,tp,eg,ep,ev,re,r,rp)
	return RD.IsAdvanceSummonTurn(e:GetHandler())
end
cm.cost=RD.CostSendGraveToDeckBottom(cm.costfilter,1,cm.max,nil,nil,Group.GetCount)
```

### Lindorm the Dragon Monarch (`120291003`)

Source: [Rush/Scripts/c120291003.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120291003.lua)

```lua
end
function cm.condition(e,tp,eg,ep,ev,re,r,rp)
	return RD.IsAdvanceSummonTurn(e:GetHandler()) and Duel.GetFieldGroupCount(tp,LOCATION_EXTRA,0)==0
end
function cm.target(e,tp,eg,ep,ev,re,r,rp,chk)
```

### Caius the Shadow Monarch (`120291001`)

Source: [Rush/Scripts/c120291001.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120291001.lua)

```lua
--To Deck
function cm.condition(e,tp,eg,ep,ev,re,r,rp)
	return RD.IsAdvanceSummonTurn(e:GetHandler())
end
function cm.target(e,tp,eg,ep,ev,re,r,rp,chk)
```
