# Group.GetMaxGroup

## Signature

```lua
Group.GetMaxGroup(Group g, function f, ... any) -> Group,int
```

## Description

F is the function that returns an interger value, and the card with the largest value of f is selected from g
The second return value is the maximum value, starting with the third parameter as an additional parameter
To use the second return value Note Check g is not empty

## Parameters

- `g` `Group`
- `f` `function`
- `...` `any`

## Returns

- `Group`
- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libgroup.cpp:925`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **53** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Group.GetMaxGroup`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [DoSolfachord Coolia](/examples/cards/80776622) | `80776622` | [Scripts/c80776622.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c80776622.lua) | 61 |
| Theia, the Primal Being | `85687952` | [Scripts/c85687952.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c85687952.lua) | 56 |
| Gouki The Master Ogre | `30286474` | [Scripts/c30286474.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30286474.lua) | 51 |
| Keel, Shipwright Fur Hire | `66736884` | [Scripts/c66736884.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c66736884.lua) | 50 |
| Tri-Brigade Nervall | `14816857` | [Scripts/c14816857.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c14816857.lua) | 49 |
| GMX Applied Experiment #55 | `18795635` | [Scripts/c18795635.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c18795635.lua) | 49 |
| Tri-Brigade Fraktall | `87209160` | [Scripts/c87209160.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c87209160.lua) | 48 |
| Naturia Mole Cricket | `93454062` | [Scripts/c93454062.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93454062.lua) | 48 |
| Tri-Brigade Kitt | `56196385` | [Scripts/c56196385.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c56196385.lua) | 48 |
| Tri-Brigade Kerass | `50810455` | [Scripts/c50810455.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c50810455.lua) | 48 |
| Tri-Brigade Hammer | `92269002` | [Scripts/c92269002.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92269002.lua) | 47 |
| Armed Neos | `31817415` | [Scripts/c31817415.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c31817415.lua) | 47 |
| Winged Kuriboh Sabatiel LV10 | `40237839` | [Scripts/c40237839.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c40237839.lua) | 46 |
| Centur-Ion Legatia | `15982593` | [Scripts/c15982593.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c15982593.lua) | 45 |
| Dreamland | `26920296` | [Scripts/c26920296.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c26920296.lua) | 44 |
| Drill Armed Dragon | `46221535` | [Scripts/c46221535.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c46221535.lua) | 44 |
| Tri-Brigade Revolt | `40975243` | [Scripts/c40975243.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c40975243.lua) | 44 |
| Ancient Warriors - Rebellious Lu Feng | `82791472` | [Scripts/c82791472.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c82791472.lua) | 43 |
| Divine Serpent Geh | `82103466` | [Scripts/c82103466.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c82103466.lua) | 43 |
| Rock of the Vanquisher | `28168628` | [Scripts/c28168628.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c28168628.lua) | 43 |
| Timaeus the Knight of Destiny | `53315891` | [Scripts/c53315891.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c53315891.lua) | 42 |
| Ace★Spades Speculation | `10796448` | [Scripts/c10796448.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c10796448.lua) | 42 |
| Pandemic Dragon | `68299524` | [Scripts/c68299524.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c68299524.lua) | 42 |
| Red Reign | `5376159` | [Scripts/c5376159.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c5376159.lua) | 41 |
| ...and 29 more |  |  |  |

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
