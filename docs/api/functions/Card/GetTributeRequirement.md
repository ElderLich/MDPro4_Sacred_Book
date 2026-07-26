# Card.GetTributeRequirement

## Signature

```lua
Card.GetTributeRequirement(Card c) -> int,int
```

## Description

Returns the minimum and maximum Tribute counts for Normal Summoning c.

## Parameters

- `c` `Card`

## Returns

- `int` - Minimum Tribute count.
- `int` - Maximum Tribute count.

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3655`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **8** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.GetTributeRequirement`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Union Activation | `38527680` | [Scripts/c38527680.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c38527680.lua) | 2 |
| Condemned Darklord | `35306215` | [Scripts/c35306215.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c35306215.lua) | 1 |
| Leo Wizard the Dark Fiend | `55423549` | [Scripts/c55423549.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c55423549.lua) | 1 |
| Floowandereeze and the Unexplored Winds | `55521751` | [Scripts/c55521751.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c55521751.lua) | 1 |
| Mausoleum of the Emperor | `80921533` | [Scripts/c80921533.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c80921533.lua) | 3 |
| Tribute Burial | `80230510` | [Scripts/c80230510.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c80230510.lua) | 1 |
| Ancient Gear Castle | `92001300` | [Scripts/c92001300.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92001300.lua) | 1 |
| Kaiser Colosseum | `35059553` | [Scripts/c35059553.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c35059553.lua) | 1 |

## Script Examples

### Union Activation (`38527680`)

Source: [Scripts/c38527680.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c38527680.lua)

```lua
end
function s.thfilter2(c,e,tp)
	local minc,maxc=c:GetTributeRequirement()
	return c:IsAttackAbove(3000) and c:IsSummonable(true,nil) and c:IsSummonableCard() and c:IsAbleToHand() and s.sunthfilter(c,e,tp,minc,maxc) and Duel.IsPlayerCanSummon(tp,SUMMON_TYPE_ADVANCE,c)
end
```

### Condemned Darklord (`35306215`)

Source: [Scripts/c35306215.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c35306215.lua)

```lua
end
function c35306215.ottg(e,c)
	local mi,ma=c:GetTributeRequirement()
	return mi<=2 and ma>=2 and c:IsRace(RACE_FAIRY)
end
```

### Leo Wizard the Dark Fiend (`55423549`)

Source: [Scripts/c55423549.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c55423549.lua)

```lua
function s.ttcon(e,c,minc)
	if c==nil then return true end
	local min,max=c:GetTributeRequirement()
	return min<=1 and Duel.CheckTribute(c,1)
end
```
