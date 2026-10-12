# RushDuel.RegisterUnionEffect

Alias: `RD.RegisterUnionEffect`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.RegisterUnionEffect(any card, any target, any condition, any cost, any operation, any limit) -> any
```

## Description

Rush Duel helper declared in `RDUnion.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
注册效果: 同盟怪兽的同盟效果
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `target` `any`: Type and behavior are not yet reviewed; see the source.
- `condition` `any`: Type and behavior are not yet reviewed; see the source.
- `cost` `any`: Type and behavior are not yet reviewed; see the source.
- `operation` `any`: Type and behavior are not yet reviewed; see the source.
- `limit` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDUnion.lua:5`

```lua
function RushDuel.RegisterUnionEffect(card, target, condition, cost, operation, limit)
    local filter = function(c, e, re)
        return c:IsFaceup() and target(c, e, re)
    end
    -- Union
    local e1 = Effect.CreateEffect(card)
    e1:SetDescription(1060)
    e1:SetCategory(CATEGORY_EQUIP)
    e1:SetType(EFFECT_TYPE_IGNITION)
    e1:SetRange(LOCATION_MZONE)
    if condition then
        e1:SetCondition(condition)
    end
    if cost then
        e1:SetCost(cost)
    end
    e1:SetTarget(RushDuel.UnionTarget(filter))
    e1:SetOperation(RushDuel.UnionOperation(filter, operation, limit))
    card:RegisterEffect(e1)
    -- Equip Limit
    local e2 = Effect.CreateEffect(card)
    e2:SetType(EFFECT_TYPE_SINGLE)
    e2:SetCode(EFFECT_EQUIP_LIMIT)
    e2:SetProperty(EFFECT_FLAG_CANNOT_DISABLE)
    e2:SetValue(RushDuel.UnionFilter(filter))
    card:RegisterEffect(e2)
    local e3 = Effect.CreateEffect(card)
    e3:SetType(EFFECT_TYPE_SINGLE)
    e3:SetCode(EFFECT_UNION_TARGET)
    e3:SetProperty(EFFECT_FLAG_CANNOT_DISABLE)
    e3:SetValue(filter)
    card:RegisterEffect(e3)
    return e1
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **19** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.RegisterUnionEffect) with `RushDuel.RegisterUnionEffect`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Lostream Polka | `120309040` | [Rush/Scripts/c120309040.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120309040.lua) | 1 |
| Arthenée the Defender of Sacred Silence | `120306033` | [Rush/Scripts/c120306033.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120306033.lua) | 1 |
| Lostream Nepia | `120309038` | [Rush/Scripts/c120309038.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120309038.lua) | 1 |
| Lauan Mapper Ivy | `120306013` | [Rush/Scripts/c120306013.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120306013.lua) | 1 |
| Lostream Nemora | `120309037` | [Rush/Scripts/c120309037.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120309037.lua) | 1 |
| Lostream Nereides | `120109068` | [Rush/Scripts/c120109068.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120109068.lua) | 1 |
| Attrac Charm Sowaru | `120309055` | [Rush/Scripts/c120309055.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120309055.lua) | 1 |
| Lostream Myura | `120309041` | [Rush/Scripts/c120309041.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120309041.lua) | 1 |
| Powerful Machine Clockwork Walker | `120306030` | [Rush/Scripts/c120306030.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120306030.lua) | 1 |
| The Sacred Shield of Arthenée | `120306032` | [Rush/Scripts/c120306032.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120306032.lua) | 1 |
| SW - Asura Bat | `120305032` | [Rush/Scripts/c120305032.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120305032.lua) | 1 |
| Lauan Macho Dex | `120306014` | [Rush/Scripts/c120306014.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120306014.lua) | 1 |
| Z-Metal Tank | `120305058` | [Rush/Scripts/c120305058.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120305058.lua) | 1 |
| Y-Dragon Head | `120305057` | [Rush/Scripts/c120305057.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120305057.lua) | 1 |
| Koitsu | `120305043` | [Rush/Scripts/c120305043.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120305043.lua) | 1 |
| Doitsu | `120305044` | [Rush/Scripts/c120305044.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120305044.lua) | 1 |
| Attrac Charm Midi | `120309056` | [Rush/Scripts/c120309056.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120309056.lua) | 1 |
| The Sacred Spear of Arthenée | `120306031` | [Rush/Scripts/c120306031.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120306031.lua) | 1 |
| Leng Ling | `120308005` | [Rush/Scripts/c120308005.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120308005.lua) | 1 |

## Script Examples

### Lostream Polka (`120309040`)

Source: [Rush/Scripts/c120309040.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120309040.lua)

```lua
function cm.initial_effect(c)
	--Union
	local e1=RD.RegisterUnionEffect(c,cm.filter,nil,nil,cm.operation)
	e1:SetCategory(e1:GetCategory()|CATEGORY_TOHAND|CATEGORY_GRAVE_ACTION)
	--Cannot Be Battle Target
```

### Arthenée the Defender of Sacred Silence (`120306033`)

Source: [Rush/Scripts/c120306033.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120306033.lua)

```lua
	RD.AddHandConfirmSpecialSummonProcedure(c,aux.Stringid(m,0),cm.spconfilter)
	--Union
	RD.RegisterUnionEffect(c,aux.TRUE,nil,cm.cost)
	--Atk Up
	local e1=Effect.CreateEffect(c)
```

### Lostream Nepia (`120309038`)

Source: [Rush/Scripts/c120309038.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120309038.lua)

```lua
	Duel.AddCustomActivityCounter(m,ACTIVITY_SPSUMMON,cm.ctfilter)
	--Union
	local e1=RD.RegisterUnionEffect(c,cm.filter,cm.condition,nil,cm.operation)
	e1:SetCategory(e1:GetCategory()|CATEGORY_SPECIAL_SUMMON|CATEGORY_GRAVE_SPSUMMON)
	--Atk Down
```
