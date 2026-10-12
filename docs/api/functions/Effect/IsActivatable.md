# Effect.IsActivatable

## Signature

```lua
Effect.IsActivatable(Effect e, int player, [bool neglect_loc], [bool neglect_target]) -> bool
```

## Description

Checks whether e can currently be activated by player, with optional booleans to ignore location and target checks.

## Parameters

- `e` `Effect`
- `player` `int`
- `neglect_loc` `bool` optional
- `neglect_target` `bool` optional

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libeffect.cpp:654`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **3** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Effect.IsActivatable) with `Effect.IsActivatable`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Favorite Hero | `11881272` | [Scripts/c11881272.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c11881272.lua) | 2 |
| Bait Doll | `7165085` | [Scripts/c7165085.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c7165085.lua) | 1 |
| Metaverse | `89208725` | [Scripts/c89208725.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c89208725.lua) | 2 |

## Script Examples

### Favorite Hero (`11881272`)

Source: [Scripts/c11881272.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c11881272.lua)

```lua
end
function c11881272.actfilter(c,tp)
	return c:IsType(TYPE_FIELD) and c:GetActivateEffect():IsActivatable(tp,true,true)
end
function c11881272.acttg(e,tp,eg,ep,ev,re,r,rp,chk)
```

### Bait Doll (`7165085`)

Source: [Scripts/c7165085.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c7165085.lua)

```lua
			local target=te:GetTarget()
			local operation=te:GetOperation()
			if te:GetCode()==EVENT_FREE_CHAIN and te:IsActivatable(tep)
				and (not condition or condition(te,tep,eg,ep,ev,re,r,rp))
				and (not cost or cost(te,tep,eg,ep,ev,re,r,rp,0))
```

### Metaverse (`89208725`)

Source: [Scripts/c89208725.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c89208725.lua)

```lua
end
function c89208725.filter(c,tp)
	return c:IsType(TYPE_FIELD) and (c:IsAbleToHand() or c:GetActivateEffect():IsActivatable(tp,true,true))
end
function c89208725.target(e,tp,eg,ep,ev,re,r,rp,chk)
```
