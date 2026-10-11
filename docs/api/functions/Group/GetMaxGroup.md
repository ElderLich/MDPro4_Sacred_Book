# Group.GetMaxGroup

## Signature

```lua
Group.GetMaxGroup(Group g, function f, [... any]) -> Group|nil,int|nil
```

## Description

Calls f for each card in g, forwards any extra arguments, and returns a Group containing every card tied for the maximum value.
The second return is the maximum integer value. If g is empty, this binding returns no Lua values.
Keep all ties when the card text affects every highest-scoring card; call Group.Select when a player must choose one tied card.

## How To Use It

Use this to find every card tied for the highest score in an existing Group.

```lua
local highg,atk=g:GetMaxGroup(Card.GetAttack)
if #highg>0 then
    Duel.HintSelection(highg)
end
```

The score function receives each candidate card first, then any extra arguments. Ties stay in the returned Group so the script can let a player choose or affect all tied cards.

## Related Functions

- [Group.GetMinGroup](/api/functions/Group/GetMinGroup)
- [Group.Select](/api/functions/Group/Select)
- [Duel.SelectMatchingCard](/api/functions/Duel/SelectMatchingCard)

## Parameters

- `g` `Group`
- `f` `function`
- `...` `any` optional

## Returns

- `Group|nil` - Cards tied for maximum value.
- `int|nil` - Maximum value.

## Source

- `D:\Programs\GitHub\ygopro-core\libgroup.cpp:925`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **54** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Group.GetMaxGroup) with `Group.GetMaxGroup`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [DoSolfachord Coolia](/examples/cards/80776622) | `80776622` | [Scripts/c80776622.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c80776622.lua) | 1 |
| Theia, the Primal Being | `85687952` | [Scripts/c85687952.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c85687952.lua) | 1 |
| Gouki The Master Ogre | `30286474` | [Scripts/c30286474.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30286474.lua) | 1 |
| Keel, Shipwright Fur Hire | `66736884` | [Scripts/c66736884.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c66736884.lua) | 1 |
| Tri-Brigade Nervall | `14816857` | [Scripts/c14816857.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c14816857.lua) | 1 |
| GMX Applied Experiment #55 | `18795635` | [Scripts/c18795635.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c18795635.lua) | 4 |
| Tri-Brigade Fraktall | `87209160` | [Scripts/c87209160.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c87209160.lua) | 1 |
| Naturia Mole Cricket | `93454062` | [Scripts/c93454062.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93454062.lua) | 1 |
| Tri-Brigade Kitt | `56196385` | [Scripts/c56196385.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c56196385.lua) | 1 |
| Tri-Brigade Kerass | `50810455` | [Scripts/c50810455.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c50810455.lua) | 1 |
| Tri-Brigade Hammer | `92269002` | [Scripts/c92269002.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92269002.lua) | 1 |
| Armed Neos | `31817415` | [Scripts/c31817415.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c31817415.lua) | 1 |
| Winged Kuriboh Sabatiel LV10 | `40237839` | [Scripts/c40237839.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c40237839.lua) | 1 |
| Centur-Ion Legatia | `15982593` | [Scripts/c15982593.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c15982593.lua) | 1 |
| Dreamland | `26920296` | [Scripts/c26920296.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c26920296.lua) | 2 |
| Drill Armed Dragon | `46221535` | [Scripts/c46221535.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c46221535.lua) | 1 |
| Tri-Brigade Revolt | `40975243` | [Scripts/c40975243.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c40975243.lua) | 2 |
| Ancient Warriors - Rebellious Lu Feng | `82791472` | [Scripts/c82791472.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c82791472.lua) | 4 |
| Divine Serpent Geh | `82103466` | [Scripts/c82103466.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c82103466.lua) | 2 |
| Mind Mirror Force | `66247039` | [Scripts/c66247039.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c66247039.lua) | 1 |
| Rock of the Vanquisher | `28168628` | [Scripts/c28168628.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c28168628.lua) | 1 |
| Timaeus the Knight of Destiny | `53315891` | [Scripts/c53315891.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c53315891.lua) | 2 |
| Ace★Spades Speculation | `10796448` | [Scripts/c10796448.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c10796448.lua) | 1 |
| Pandemic Dragon | `68299524` | [Scripts/c68299524.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c68299524.lua) | 1 |
| ...and 30 more |  |  |  |

## Script Examples

### DoSolfachord Coolia (`80776622`)

Source: [Scripts/c80776622.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c80776622.lua)

```lua
	local g=Duel.GetFieldGroup(tp,LOCATION_PZONE,0)
	if g:GetCount()==0 then return false end
	local _,max=g:GetMaxGroup(Card.GetCurrentScale)
	return rc:IsAttackBelow(max*300)
end
```

### Theia, the Primal Being (`85687952`)

Source: [Scripts/c85687952.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c85687952.lua)

```lua
		local g=Duel.GetMatchingGroup(Card.IsFaceup,tp,LOCATION_MZONE,LOCATION_MZONE,nil)
		if g:GetCount()>0 then
			local tg=g:GetMaxGroup(Card.GetAttack)
			if tg:GetCount()>1 then
				Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_DESTROY)
```

### Gouki The Master Ogre (`30286474`)

Source: [Scripts/c30286474.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30286474.lua)

```lua
function c30286474.atlimit(e,c)
	local g=Duel.GetMatchingGroup(Card.IsFaceup,e:GetHandlerPlayer(),0,LOCATION_MZONE,nil)
	local tg=g:GetMaxGroup(Card.GetAttack)
	return not tg:IsContains(c) or c:IsFacedown()
end
```
