# Card.GetLink

## Signature

```lua
Card.GetLink(Card c) -> int
```

## Description

Returns c's Link Rating, or 0 if c is not a Link Monster.

## Parameters

- `c` `Card`

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3410`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **54** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.GetLink`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Marincess Cascade | `27012990` | [Scripts/c27012990.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c27012990.lua) | 1 |
| Gergonne's End | `59490397` | [Scripts/c59490397.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59490397.lua) | 1 |
| Accesscode Talker | `86066372` | [Scripts/c86066372.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c86066372.lua) | 1 |
| Clown Crew Finale | `84031736` | [Scripts/c84031736.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c84031736.lua) | 2 |
| Tri-Brigade Nervall | `14816857` | [Scripts/c14816857.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c14816857.lua) | 1 |
| Sharv Sarga | `75728539` | [Scripts/c75728539.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c75728539.lua) | 1 |
| Marincess Coral Triangle | `84546257` | [Scripts/c84546257.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c84546257.lua) | 2 |
| Cyberse Clock Dragon | `42717221` | [Scripts/c42717221.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c42717221.lua) | 1 |
| Tri-Brigade Fraktall | `87209160` | [Scripts/c87209160.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c87209160.lua) | 1 |
| Tri-Brigade Kitt | `56196385` | [Scripts/c56196385.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c56196385.lua) | 1 |
| Tri-Brigade Kerass | `50810455` | [Scripts/c50810455.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c50810455.lua) | 1 |
| Benghalancer the Resurgent | `73345237` | [Scripts/c73345237.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c73345237.lua) | 2 |
| Quadborrel Dragon | `29296344` | [Scripts/c29296344.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c29296344.lua) | 1 |
| V-LAN Hydra | `13536606` | [Scripts/c13536606.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c13536606.lua) | 2 |
| Rustin Mammoth | `3434362` | [Scripts/c3434362.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c3434362.lua) | 2 |
| Salamangreat Rage | `14934922` | [Scripts/c14934922.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c14934922.lua) | 1 |
| Tri-Brigade Hammer | `92269002` | [Scripts/c92269002.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92269002.lua) | 1 |
| Akashic Magician | `28776350` | [Scripts/c28776350.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c28776350.lua) | 2 |
| Fiendsmith's Desirae | `82135803` | [Scripts/c82135803.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c82135803.lua) | 2 |
| Sunvine Thrasher | `91557476` | [Scripts/c91557476.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c91557476.lua) | 2 |
| Marincess Circulation | `83723605` | [Scripts/c83723605.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c83723605.lua) | 1 |
| Marincess Bubble Ring | `19712214` | [Scripts/c19712214.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c19712214.lua) | 1 |
| Marincess Snow | `80627281` | [Scripts/c80627281.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c80627281.lua) | 3 |
| Gouki The Powerload Ogre | `11516241` | [Scripts/c11516241.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c11516241.lua) | 2 |
| ...and 30 more |  |  |  |

## Script Examples

### Marincess Cascade (`27012990`)

Source: [Scripts/c27012990.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c27012990.lua)

```lua
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_REMOVE)
	local rg=g:SelectSubGroup(tp,c27012990.fselect,false,1,g:GetCount(),tp)
	local ct=rg:GetSum(Card.GetLink)
	e:SetLabel(ct)
	local tct=1
```

### Gergonne's End (`59490397`)

Source: [Scripts/c59490397.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59490397.lua)

```lua
function c59490397.descon(e,tp,eg,ep,ev,re,r,rp)
	local tc=e:GetHandler():GetEquipTarget()
	return tc and tc:GetLinkedGroupCount()==tc:GetLink()
end
function c59490397.destg(e,tp,eg,ep,ev,re,r,rp,chk)
```

### Accesscode Talker (`86066372`)

Source: [Scripts/c86066372.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c86066372.lua)

```lua
		e1:SetType(EFFECT_TYPE_SINGLE)
		e1:SetCode(EFFECT_UPDATE_ATTACK)
		e1:SetValue(tc:GetLink()*1000)
		e1:SetReset(RESET_EVENT+RESETS_STANDARD+RESET_DISABLE)
		c:RegisterEffect(e1)
```
