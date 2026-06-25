# Group.GetMinGroup

## Signature

```lua
Group.GetMinGroup(Group g, function f, [... any]) -> Group|nil,int|nil
```

## Description

Calls f for each card in g, forwards any extra arguments, and returns a Group containing every card tied for the minimum value.
The second return is the minimum integer value. If g is empty, this binding returns no Lua values.
Keep all ties when the card text affects every lowest-scoring card; call Group.Select when a player must choose one tied card.

## How To Use It

Use this to find every card tied for the lowest score in an existing Group.

```lua
local lowg,atk=g:GetMinGroup(Card.GetAttack)
if #lowg>0 then
    local sg=lowg:Select(tp,1,1,nil)
end
```

The return values are the tied Group and the minimum score. If the source Group is empty, this binding returns no values.

## Related Functions

- [Group.GetMaxGroup](/api/functions/Group/GetMaxGroup)
- [Group.Select](/api/functions/Group/Select)
- [Duel.SelectMatchingCard](/api/functions/Duel/SelectMatchingCard)

## Parameters

- `g` `Group`
- `f` `function`
- `...` `any` optional

## Returns

- `Group|nil` - Cards tied for the minimum value.
- `int|nil` - Minimum value.

## Source

- `D:\Programs\GitHub\ygopro-core\libgroup.cpp:924`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **23** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Group.GetMinGroup`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| TiSolfachord Beautia | `54387923` | [Scripts/c54387923.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c54387923.lua) | 50 |
| Vanquish Soul Hollie Sue | `93156774` | [Scripts/c93156774.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93156774.lua) | 48 |
| Vanquish Soul Dr. Mad Love | `29280200` | [Scripts/c29280200.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c29280200.lua) | 46 |
| Uradora of Fate | `27753563` | [Scripts/c27753563.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c27753563.lua) | 46 |
| Mayakashi Mayhem | `41867019` | [Scripts/c41867019.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c41867019.lua) | 41 |
| Wrecker Panda | `28139785` | [Scripts/c28139785.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c28139785.lua) | 41 |
| Chain Summon | `90812044` | [Scripts/c90812044.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c90812044.lua) | 41 |
| Mad Hacker | `86993168` | [Scripts/c86993168.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c86993168.lua) | 39 |
| Clashing Souls | `57496978` | [Scripts/c57496978.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c57496978.lua) | 38 |
| Ninjitsu Art of Super-Transformation | `90200789` | [Scripts/c90200789.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c90200789.lua) | 38 |
| Unibird | `21296383` | [Scripts/c21296383.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c21296383.lua) | 37 |
| Card of Sacrifice | `88513608` | [Scripts/c88513608.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c88513608.lua) | 32 |
| Queen Angel of Roses | `96470883` | [Scripts/c96470883.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c96470883.lua) | 32 |
| Chthonian Blast | `18271561` | [Scripts/c18271561.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c18271561.lua) | 27 |
| Unbreakable Spirit | `88494120` | [Scripts/c88494120.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c88494120.lua) | 27 |
| The Great Noodle Inversion | `67906797` | [Scripts/c67906797.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c67906797.lua) | 27 |
| Fire Prison | `269510` | [Scripts/c269510.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c269510.lua) | 25 |
| Burst Breath | `80163754` | [Scripts/c80163754.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c80163754.lua) | 25 |
| Super Junior Confrontation | `29590905` | [Scripts/c29590905.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c29590905.lua) | 23 |
| Zubaba Buster | `57036718` | [Scripts/c57036718.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c57036718.lua) | 23 |
| Utopia Buster | `30341772` | [Scripts/c30341772.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30341772.lua) | 22 |
| Goblin Circus | `18658572` | [Scripts/c18658572.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c18658572.lua) | 22 |
| Fissure | `66788016` | [Scripts/c66788016.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c66788016.lua) | 18 |

## Script Examples

### TiSolfachord Beautia (`54387923`)

Source: [Scripts/c54387923.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c54387923.lua)

```lua
	local g=Duel.GetFieldGroup(tp,LOCATION_PZONE,0)
	if g:GetCount()==0 then return false end
	local _,min=g:GetMinGroup(Card.GetCurrentScale)
	return bc:IsAttackAbove(min*300)
end
```

### Vanquish Soul Hollie Sue (`93156774`)

Source: [Scripts/c93156774.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93156774.lua)

```lua
		local g=Duel.GetMatchingGroup(s.ctfilter,tp,0,LOCATION_MZONE,nil)
		if #g<=0 then return false end
		local tg=g:GetMinGroup(Card.GetAttack):Filter(Card.IsControlerCanBeChanged,nil)
		return tg:GetCount()>0 and Duel.GetMZoneCount(tp,c,tp,LOCATION_REASON_CONTROL)>0 and Duel.GetFlagEffect(tp,id)==0
	end
```

### Vanquish Soul Dr. Mad Love (`29280200`)

Source: [Scripts/c29280200.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c29280200.lua)

```lua
function c29280200.rthtg(e,tp,eg,ep,ev,re,r,rp,chk)
	local g=Duel.GetMatchingGroup(c29280200.rthtgfilter,tp,LOCATION_MZONE,LOCATION_MZONE,nil)
	local tg=g:GetMinGroup(Card.GetDefense)
	if chk==0 then return tg:IsExists(Card.IsAbleToHand,1,nil)
		and Duel.GetFlagEffect(tp,29280200)==0 end
```
