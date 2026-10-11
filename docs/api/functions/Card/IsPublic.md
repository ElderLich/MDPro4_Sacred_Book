# Card.IsPublic

## Signature

```lua
Card.IsPublic(Card c) -> bool
```

## Description

Checks whether c is currently public to both players, represented by face-up position in this core.

## Parameters

- `c` `Card`

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3679`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **239** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Card.IsPublic) with `Card.IsPublic`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Deftero Enneacraft - "alazoneIA"](/examples/cards/92171126) | `92171126` | [Scripts/c92171126.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92171126.lua) | 2 |
| [Meteoroa Drytron](/examples/cards/24166324) | `24166324` | [Scripts/c24166324.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24166324.lua) | 1 |
| [Enneacraft - Asta.PIXEA](/examples/cards/28454232) | `28454232` | [Scripts/c28454232.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c28454232.lua) | 2 |
| [Enneacraft - Archa.TAIL](/examples/cards/81237046) | `81237046` | [Scripts/c81237046.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c81237046.lua) | 2 |
| [Enneacraft - Atil.SPIA](/examples/cards/71801447) | `71801447` | [Scripts/c71801447.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71801447.lua) | 2 |
| [Enneacraft - Aiza.LEON](/examples/cards/82359538) | `82359538` | [Scripts/c82359538.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c82359538.lua) | 2 |
| [Dracotail Shaulas](/examples/cards/42125140) | `42125140` | [Scripts/c42125140.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c42125140.lua) | 3 |
| [Transonic Bird](/examples/cards/34072799) | `34072799` | [Scripts/c34072799.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c34072799.lua) | 1 |
| Jupredo the Shademachine Power Patron | `43871165` | [Scripts/c43871165.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c43871165.lua) | 2 |
| Enneacraft - Atori.MAR | `54842941` | [Scripts/c54842941.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c54842941.lua) | 2 |
| Koa'ki Meiru Rooklord | `10060427` | [Scripts/c10060427.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c10060427.lua) | 1 |
| Purrely | `25550531` | [Scripts/c25550531.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c25550531.lua) | 1 |
| Dracotail Arthalion | `33760966` | [Scripts/c33760966.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c33760966.lua) | 3 |
| R.B. Lambda Cannon | `81794107` | [Scripts/c81794107.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c81794107.lua) | 1 |
| Astrazma Urania | `18738846` | [Scripts/c18738846.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c18738846.lua) | 1 |
| Vanquish Soul Caesar Valius | `91073013` | [Scripts/c91073013.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c91073013.lua) | 2 |
| Shimmering Shatterer of the Sacred Beasts | `3441553` | [Scripts/c3441553.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c3441553.lua) | 1 |
| The Continuing Epic of Charles | `11802691` | [Scripts/c11802691.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c11802691.lua) | 1 |
| Dracotail Gulamel | `79755671` | [Scripts/c79755671.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c79755671.lua) | 3 |
| Phara the Primordial Goddess | `82344137` | [Scripts/c82344137.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c82344137.lua) | 2 |
| Ekto Enneacraft - "tromarIA" | `29570824` | [Scripts/c29570824.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c29570824.lua) | 2 |
| Enato Enneacraft - "oknirIA" | `55965529` | [Scripts/c55965529.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c55965529.lua) | 2 |
| Gunkan Suship Shari Red | `63748694` | [Scripts/c63748694.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63748694.lua) | 1 |
| Melffy Staring Contest | `76981308` | [Scripts/c76981308.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c76981308.lua) | 2 |
| ...and 215 more |  |  |  |

## Script Examples

### Deftero Enneacraft - "alazoneIA" (`92171126`)

Source: [Scripts/c92171126.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92171126.lua)

```lua
end
function s.spcost(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return not e:GetHandler():IsPublic()
		and Duel.GetCustomActivityCount(id,tp,ACTIVITY_SPSUMMON)==0 end
	local e1=Effect.CreateEffect(e:GetHandler())
```

### Meteoroa Drytron (`24166324`)

Source: [Scripts/c24166324.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24166324.lua)

```lua
end
function s.costfilter(c)
	return c:IsCode(22398665) and not c:IsPublic()
end
function s.spcost(e,tp,eg,ep,ev,re,r,rp,chk)
```

### Enneacraft - Asta.PIXEA (`28454232`)

Source: [Scripts/c28454232.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c28454232.lua)

```lua
end
function s.spcost(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return not e:GetHandler():IsPublic()
		and Duel.GetCustomActivityCount(id,tp,ACTIVITY_SPSUMMON)==0 end
	local e1=Effect.CreateEffect(e:GetHandler())
```
