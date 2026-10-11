# RushDuel.IsPreviousType

Alias: `RD.IsPreviousType`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.IsPreviousType(any card, any type) -> any
```

## Description

Rush Duel helper declared in `RDCondition.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
条件: 位置变化前的类型
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `type` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCondition.lua:198`

```lua
function RushDuel.IsPreviousType(card, type)
    return (card:GetPreviousTypeOnField() & type) ~= 0
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **11** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.IsPreviousType) with `RushDuel.IsPreviousType`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Revenge MAX](/examples/rush-cards/120228065) | `120228065` | [Rush/Scripts/c120228065.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120228065.lua) | 1 |
| [Star Protector Recapture](/examples/rush-cards/120306063) | `120306063` | [Rush/Scripts/c120306063.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120306063.lua) | 1 |
| Alchemicalize Salamandra | `120235032` | [Rush/Scripts/c120235032.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120235032.lua) | 1 |
| Resurrection of the Blaze Fiends | `120231017` | [Rush/Scripts/c120231017.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120231017.lua) | 1 |
| Archfiend's Revival | `120170062` | [Rush/Scripts/c120170062.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120170062.lua) | 1 |
| Counter Back | `120203031` | [Rush/Scripts/c120203031.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120203031.lua) | 1 |
| Faulty Fire | `120145060` | [Rush/Scripts/c120145060.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120145060.lua) | 1 |
| Driving Snow | `120130050` | [Rush/Scripts/c120130050.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120130050.lua) | 1 |
| Gust | `120120048` | [Rush/Scripts/c120120048.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120120048.lua) | 1 |
| Brutal Retribution | `120120049` | [Rush/Scripts/c120120049.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120120049.lua) | 1 |
| Hunting Strawberries | `120208064` | [Rush/Scripts/c120208064.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120208064.lua) | 1 |

## Script Examples

### Revenge MAX (`120228065`)

Source: [Rush/Scripts/c120228065.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120228065.lua)

```lua
	RD.SelectAndDoAction(HINTMSG_DESTROY,cm.filter,tp,LOCATION_ONFIELD,0,1,1,aux.ExceptThisCard(e),function(g)
		local tc=g:GetFirst()
		if Duel.Destroy(tc,REASON_EFFECT)~=0 and RD.IsPreviousType(tc,TYPE_EQUIP) then
			local sg=eg:Filter(cm.desfilter,nil)
			if sg:GetCount()>0 and Duel.SelectYesNo(tp,aux.Stringid(m,1)) then
```

### Star Protector Recapture (`120306063`)

Source: [Rush/Scripts/c120306063.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120306063.lua)

```lua
end
function cm.exfilter(c)
	return RD.IsPreviousType(c,TYPE_FUSION)
end
function cm.spfilter(c,e,tp)
```

### Alchemicalize Salamandra (`120235032`)

Source: [Rush/Scripts/c120235032.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120235032.lua)

```lua
end
function cm.exfilter(c)
	return RD.IsPreviousType(c,TYPE_SPELL)
end
function cm.condition(e,tp,eg,ep,ev,re,r,rp)
```
