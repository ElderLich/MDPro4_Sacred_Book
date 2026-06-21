# Card.GetCurrentScale

## Signature

```lua
Card.GetCurrentScale(Card c) -> int
```

## Description

Return the current Pendulum Scale of card c. If in the Left Pendulum Zone, return the left scale; if in the Right Pendulum Zone or not in a Pendulum Zone, return the right scale

## Parameters

- `c` `Card`

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3417`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **23** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.GetCurrentScale`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [DoSolfachord Coolia](/examples/cards/80776622) | `80776622` | [Scripts/c80776622.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c80776622.lua) | 61 |
| Odd-Eyes Pendulum Dragon of the Four Heavenly Dragons | `75787708` | [Scripts/c75787708.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c75787708.lua) | 51 |
| LaSolfachord Angelia | `27993919` | [Scripts/c27993919.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c27993919.lua) | 51 |
| TiSolfachord Beautia | `54387923` | [Scripts/c54387923.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c54387923.lua) | 50 |
| Solfachord Happiness | `93481594` | [Scripts/c93481594.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93481594.lua) | 49 |
| GranSolfachord Musecia | `37972500` | [Scripts/c37972500.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c37972500.lua) | 47 |
| Mayosenju Hitot | `21364070` | [Scripts/c21364070.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c21364070.lua) | 46 |
| ReSolfachord Dreamia | `92610868` | [Scripts/c92610868.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92610868.lua) | 45 |
| Solfachord Primoa | `11688916` | [Scripts/c11688916.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c11688916.lua) | 44 |
| GranSolfachord Coolia | `84521924` | [Scripts/c84521924.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c84521924.lua) | 44 |
| SolSolfachord Gracia | `91598270` | [Scripts/c91598270.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c91598270.lua) | 43 |
| Exceed the Pendulum | `92812851` | [Scripts/c92812851.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92812851.lua) | 40 |
| Pendulum Pendant | `65914127` | [Scripts/c65914127.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c65914127.lua) | 40 |
| Solfachord Elegance | `27870337` | [Scripts/c27870337.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c27870337.lua) | 39 |
| Solfachord Harmonia | `29650040` | [Scripts/c29650040.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c29650040.lua) | 39 |
| Solfachord Symphony | `56510115` | [Scripts/c56510115.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c56510115.lua) | 38 |
| Performapal Classikuriboh | `55554175` | [Scripts/c55554175.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c55554175.lua) | 37 |
| FaSolfachord Fancia | `54100561` | [Scripts/c54100561.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c54100561.lua) | 37 |
| Solfachord Musica | `56058749` | [Scripts/c56058749.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c56058749.lua) | 36 |
| MiSolfachord Eliteia | `28115467` | [Scripts/c28115467.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c28115467.lua) | 34 |
| DoSolfachord Cutia | `55226153` | [Scripts/c55226153.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c55226153.lua) | 33 |
| Pazuzule | `77384395` | [Scripts/c77384395.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c77384395.lua) | 27 |
| Tempura of Fortune - EBI | `86304179` | [Scripts/c86304179.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c86304179.lua) | 26 |

## Script Examples

### DoSolfachord Coolia (`80776622`)

Source: [Scripts/c80776622.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c80776622.lua)

```lua
end
function c80776622.pfilter(c)
	return c:GetCurrentScale()%2~=0
end
function c80776622.distg(e,tp,eg,ep,ev,re,r,rp,chk,chkc)
```

### Odd-Eyes Pendulum Dragon of the Four Heavenly Dragons (`75787708`)

Source: [Scripts/c75787708.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c75787708.lua)

```lua
	local l,r=Duel.GetFieldCard(e:GetHandlerPlayer(),LOCATION_PZONE,0),Duel.GetFieldCard(e:GetHandlerPlayer(),LOCATION_PZONE,1)
	if not (l and r) then return 0 end
	local ls,rs=l:GetCurrentScale(),r:GetCurrentScale()
	if ls==rs then return 0 end
	return math.abs(rs-ls)*300
```

### LaSolfachord Angelia (`27993919`)

Source: [Scripts/c27993919.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c27993919.lua)

```lua
	return (c:IsControler(tp) or c:IsFaceup()) and Duel.GetMZoneCount(tp,c)>0
		and c:IsSetCard(0x162) and c:IsType(TYPE_PENDULUM)
		and Duel.IsExistingMatchingCard(c27993919.spfilter,tp,LOCATION_DECK,0,1,nil,e,tp,c:GetCurrentScale())
end
function c27993919.spfilter(c,e,tp,sc)
```
