# Card.GetCurrentScale

## Signature

```lua
Card.GetCurrentScale(Card c) -> int
```

## Description

Returns the Pendulum Scale c currently uses.
In a Pendulum Zone, this returns the left or right current scale according to c's zone sequence. Outside a Pendulum Zone, it returns c's printed left scale value.

## Parameters

- `c` `Card`

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3468`

## Guided Examples

Learn how to use this function in context:

- [Pendulum Procedure Guide](/learn/pendulum-procedure)

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **23** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Card.GetCurrentScale) with `Card.GetCurrentScale`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [DoSolfachord Coolia](/examples/cards/80776622) | `80776622` | [Scripts/c80776622.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c80776622.lua) | 2 |
| Odd-Eyes Pendulum Dragon, Four Heavenly Dragons | `75787708` | [Scripts/c75787708.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c75787708.lua) | 2 |
| LaSolfachord Angelia | `27993919` | [Scripts/c27993919.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c27993919.lua) | 4 |
| TiSolfachord Beautia | `54387923` | [Scripts/c54387923.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c54387923.lua) | 2 |
| Solfachord Happiness | `93481594` | [Scripts/c93481594.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93481594.lua) | 1 |
| GranSolfachord Musecia | `37972500` | [Scripts/c37972500.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c37972500.lua) | 5 |
| Mayosenju Hitot | `21364070` | [Scripts/c21364070.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c21364070.lua) | 1 |
| ReSolfachord Dreamia | `92610868` | [Scripts/c92610868.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92610868.lua) | 1 |
| Solfachord Primoa | `11688916` | [Scripts/c11688916.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c11688916.lua) | 1 |
| GranSolfachord Coolia | `84521924` | [Scripts/c84521924.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c84521924.lua) | 2 |
| SolSolfachord Gracia | `91598270` | [Scripts/c91598270.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c91598270.lua) | 1 |
| Exceed the Pendulum | `92812851` | [Scripts/c92812851.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92812851.lua) | 2 |
| Pendulum Pendant | `65914127` | [Scripts/c65914127.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c65914127.lua) | 1 |
| Solfachord Elegance | `27870337` | [Scripts/c27870337.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c27870337.lua) | 4 |
| Solfachord Harmonia | `29650040` | [Scripts/c29650040.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c29650040.lua) | 3 |
| Solfachord Symphony | `56510115` | [Scripts/c56510115.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c56510115.lua) | 2 |
| Performapal Classikuriboh | `55554175` | [Scripts/c55554175.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c55554175.lua) | 1 |
| FaSolfachord Fancia | `54100561` | [Scripts/c54100561.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c54100561.lua) | 1 |
| Solfachord Musica | `56058749` | [Scripts/c56058749.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c56058749.lua) | 2 |
| MiSolfachord Eliteia | `28115467` | [Scripts/c28115467.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c28115467.lua) | 1 |
| DoSolfachord Cutia | `55226153` | [Scripts/c55226153.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c55226153.lua) | 2 |
| Pazuzule | `77384395` | [Scripts/c77384395.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c77384395.lua) | 1 |
| Tempura of Fortune - EBI | `86304179` | [Scripts/c86304179.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c86304179.lua) | 1 |

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

### Odd-Eyes Pendulum Dragon, Four Heavenly Dragons (`75787708`)

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
