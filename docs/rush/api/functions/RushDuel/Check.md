# RushDuel.Check

Alias: `RD.Check`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.Check(function check, ... any) -> function
```

## Description

Returns a group predicate that invokes check(g, ...) with captured extra arguments. Use for subgroup constraints.

## Parameters

- `check` `function`: Predicate receiving the selected Group and captured arguments.
- `...` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `function`: Group predicate.

## Source

`Rush/Utilities/RDFunction.lua:24`

```lua
function RushDuel.Check(check, ...)
    local args = {...}
    return function(g)
        return check(g, table.unpack(args))
    end
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **9** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.Check) with `RushDuel.Check`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Analyze Phlogiston](/examples/rush-cards/120226001) | `120226001` | [Rush/Scripts/c120226001.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120226001.lua) | 1 |
| [Animagica Majesty](/examples/rush-cards/120277063) | `120277063` | [Rush/Scripts/c120277063.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120277063.lua) | 1 |
| Finalize Phoenix | `120231046` | [Rush/Scripts/c120231046.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120231046.lua) | 1 |
| Cyber Tactical Dragon | `120244044` | [Rush/Scripts/c120244044.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120244044.lua) | 1 |
| Fusion Cancel | `120253066` | [Rush/Scripts/c120253066.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120253066.lua) | 1 |
| Explosive Destructor Wyrm Dangerous Bakhamut | `120247038` | [Rush/Scripts/c120247038.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120247038.lua) | 1 |
| Tail Swipe | `120277059` | [Rush/Scripts/c120277059.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120277059.lua) | 1 |
| Destructurtle Meteor | `120205054` | [Rush/Scripts/c120205054.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120205054.lua) | 1 |
| Blades of Divine Wind | `120130042` | [Rush/Scripts/c120130042.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120130042.lua) | 1 |

## Script Examples

### Analyze Phlogiston (`120226001`)

Source: [Rush/Scripts/c120226001.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120226001.lua)

```lua
	local g=Duel.GetMatchingGroup(cm.desfilter,tp,0,LOCATION_MZONE,nil)
	local lv=g:GetSum(Card.GetLevel,nil)
	local check=RD.Check(cm.check,lv)
	RD.SelectGroupAndDoAction(HINTMSG_TODECK,aux.NecroValleyFilter(cm.filter),check,tp,LOCATION_GRAVE,0,3,3,nil,function(sg)
		if RD.SendToDeckAndExists(sg,e,tp,REASON_EFFECT) then
```

### Animagica Majesty (`120277063`)

Source: [Rush/Scripts/c120277063.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120277063.lua)

```lua
function cm.activate(e,tp,eg,ep,ev,re,r,rp)
	local filter=RD.Filter(cm.filter,e,tp)
	local check=RD.Check(cm.check,tp)
	RD.SelectGroupAndDoAction(aux.Stringid(m,1),filter,check,tp,LOCATION_MZONE,LOCATION_MZONE,2,3,nil,function(g)
		local sg=g:Filter(Card.IsControler,nil,1-tp)
```

### Finalize Phoenix (`120231046`)

Source: [Rush/Scripts/c120231046.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120231046.lua)

```lua
	local g=Duel.GetMatchingGroup(Card.IsFaceup,tp,0,LOCATION_MZONE,nil)
	local lv=g:GetSum(Card.GetLevel,nil)
	local check=RD.Check(cm.check,lv,tp)
	RD.SelectGroupAndSpecialSummon(aux.NecroValleyFilter(cm.spfilter),check,tp,LOCATION_GRAVE,0,1,2,nil,e,POS_FACEUP)
end
```
