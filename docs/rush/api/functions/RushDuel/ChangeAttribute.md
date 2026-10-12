# RushDuel.ChangeAttribute

Alias: `RD.ChangeAttribute`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.ChangeAttribute(any e, any card, any attribute, any reset, any forced) -> any
```

## Description

Rush Duel helper declared in `RDAttach.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
赋予: 改变属性
```

## Parameters

- `e` `any`: Type and behavior are not yet reviewed; see the source.
- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `attribute` `any`: Type and behavior are not yet reviewed; see the source.
- `reset` `any`: Type and behavior are not yet reviewed; see the source.
- `forced` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDAttach.lua:226`

```lua
function RushDuel.ChangeAttribute(e, card, attribute, reset, forced)
    return RushDuel.CreateSingleEffect(e, nil, card, EFFECT_CHANGE_ATTRIBUTE, attribute, reset, forced)
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **9** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.ChangeAttribute) with `RushDuel.ChangeAttribute`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Light of Bewitchment](/examples/rush-cards/120301074) | `120301074` | [Rush/Scripts/c120301074.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120301074.lua) | 1 |
| Familiar of the Earth Spiritualist | `120301013` | [Rush/Scripts/c120301013.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120301013.lua) | 1 |
| Familiar of the Water Spiritualist | `120301014` | [Rush/Scripts/c120301014.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120301014.lua) | 1 |
| Familiar of the Fire Spiritualist | `120301015` | [Rush/Scripts/c120301015.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120301015.lua) | 1 |
| Familiar of the Wind Spiritualist | `120301016` | [Rush/Scripts/c120301016.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120301016.lua) | 1 |
| Thunderbold, the Echoing Thunder | `120246002` | [Rush/Scripts/c120246002.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120246002.lua) | 1 |
| Burst Ray Blaster | `120222022` | [Rush/Scripts/c120222022.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120222022.lua) | 1 |
| Attribute Shift Bomb | `120130043` | [Rush/Scripts/c120130043.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120130043.lua) | 1 |
| Luminous Parrot | `120145036` | [Rush/Scripts/c120145036.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120145036.lua) | 1 |

## Script Examples

### Light of Bewitchment (`120301074`)

Source: [Rush/Scripts/c120301074.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120301074.lua)

```lua
	local filter=RD.Filter(cm.filter,attr)
	RD.SelectAndDoAction(aux.Stringid(m,1),filter,tp,0,LOCATION_MZONE,1,1,nil,function(g)
		RD.ChangeAttribute(e,g:GetFirst(),attr,RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END)
	end)
	local c=e:GetHandler()
```

### Familiar of the Earth Spiritualist (`120301013`)

Source: [Rush/Scripts/c120301013.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120301013.lua)

```lua
function cm.operation(e,tp,eg,ep,ev,re,r,rp)
	RD.SelectAndDoAction(aux.Stringid(m,3),cm.filter,tp,0,LOCATION_MZONE,1,1,nil,function(g)
		RD.ChangeAttribute(e,g:GetFirst(),ATTRIBUTE_EARTH,RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END)
		local filter=RD.Filter(cm.exfilter,e,tp)
		RD.CanSelectAndDoAction(aux.Stringid(m,4),HINTMSG_POSITION,filter,tp,LOCATION_MZONE,0,1,1,nil,function(sg)
```

### Familiar of the Water Spiritualist (`120301014`)

Source: [Rush/Scripts/c120301014.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120301014.lua)

```lua
function cm.operation(e,tp,eg,ep,ev,re,r,rp)
	RD.SelectAndDoAction(aux.Stringid(m,3),cm.filter,tp,0,LOCATION_MZONE,1,1,nil,function(g)
		RD.ChangeAttribute(e,g:GetFirst(),ATTRIBUTE_WATER,RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END)
		local filter=RD.Filter(cm.exfilter,e,tp)
		RD.CanSelectAndDoAction(aux.Stringid(m,4),HINTMSG_POSITION,filter,tp,LOCATION_MZONE,0,1,1,nil,function(sg)
```
