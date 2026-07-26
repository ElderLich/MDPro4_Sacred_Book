# Card.CreateEffectRelation

## Signature

```lua
Card.CreateEffectRelation(Card c, Effect e) -> void
```

## Description

Creates a relation between c and effect e.
If e is the triggering effect of a current Chain Link, the relation is tied to that Chain Link; otherwise the core stores a direct effect relation.

## Parameters

- `c` `Card`
- `e` `Effect`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3562`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **54** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.CreateEffectRelation`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Tohushaddoll Grysta](/examples/cards/95072744) | `95072744` | [Scripts/c95072744.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c95072744.lua) | 64 |
| [Graydle Split](/examples/cards/75361204) | `75361204` | [Scripts/c75361204.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c75361204.lua) | 64 |
| [Particle Fusion](/examples/cards/39261576) | `39261576` | [Scripts/c39261576.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c39261576.lua) | 61 |
| Future Fusion | `77565204` | [Scripts/c77565204.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c77565204.lua) | 55 |
| Zebufera, Vaalmonican Hallow Heathen | `2815176` | [Scripts/c2815176.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c2815176.lua) | 52 |
| Thunder Dragon Thunderstormech | `12081875` | [Scripts/c12081875.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c12081875.lua) | 50 |
| Myutant Blast | `79072916` | [Scripts/c79072916.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c79072916.lua) | 49 |
| Noh-P.U.N.K. Deer Note | `6609736` | [Scripts/c6609736.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c6609736.lua) | 48 |
| Gunkan Suship Uni | `42377643` | [Scripts/c42377643.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c42377643.lua) | 47 |
| K9-66a Jokul | `28642461` | [Scripts/c28642461.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c28642461.lua) | 47 |
| Generaider Boss Bite | `720147` | [Scripts/c720147.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c720147.lua) | 47 |
| Gladiator Beast Gistel | `26582143` | [Scripts/c26582143.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c26582143.lua) | 46 |
| WAKE CUP! Macchia | `71410542` | [Scripts/c71410542.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71410542.lua) | 46 |
| Geistgrinder Golem | `26913989` | [Scripts/c26913989.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c26913989.lua) | 45 |
| Execution of the Contract | `55976207` | [Scripts/c55976207.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c55976207.lua) | 45 |
| Fishborg Harpooner | `57420265` | [Scripts/c57420265.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c57420265.lua) | 45 |
| Bait Doll | `7165085` | [Scripts/c7165085.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c7165085.lua) | 45 |
| Broomy | `57985393` | [Scripts/c57985393.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c57985393.lua) | 42 |
| Gouki Machine Suprex | `29099860` | [Scripts/c29099860.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c29099860.lua) | 42 |
| Ninjitsu Art of Shadow Sealing | `13629812` | [Scripts/c13629812.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c13629812.lua) | 42 |
| Parasomnia Pillow | `44092304` | [Scripts/c44092304.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44092304.lua) | 41 |
| Kewl Tune Playlist | `40847034` | [Scripts/c40847034.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c40847034.lua) | 41 |
| Arahime the Manifested Mikanko | `75771170` | [Scripts/c75771170.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c75771170.lua) | 40 |
| Galaxy Zero | `97617181` | [Scripts/c97617181.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c97617181.lua) | 40 |
| ...and 30 more |  |  |  |

## Script Examples

### Tohushaddoll Grysta (`95072744`)

Source: [Scripts/c95072744.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c95072744.lua)

```lua
	local tc=g:GetFirst()
	Duel.ClearTargetCard()
	tc:CreateEffectRelation(e)
	e:SetLabelObject(tc)
	local te=tc.shadoll_flip_effect
```

### Graydle Split (`75361204`)

Source: [Scripts/c75361204.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c75361204.lua)

```lua
		and Duel.IsExistingMatchingCard(c75361204.spfilter1,tp,LOCATION_DECK,0,1,nil,e,tp) end
	local ec=e:GetLabelObject()
	ec:CreateEffectRelation(e)
	Duel.SetOperationInfo(0,CATEGORY_DESTROY,ec,1,0,0)
	Duel.SetOperationInfo(0,CATEGORY_SPECIAL_SUMMON,nil,2,tp,LOCATION_DECK)
```

### Particle Fusion (`39261576`)

Source: [Scripts/c39261576.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c39261576.lua)

```lua
	Duel.Hint(HINT_SELECTMSG,tp,aux.Stringid(39261576,1))
	local g=mat:FilterSelect(tp,Card.IsSetCard,1,1,nil,0x1047)
	tc:CreateEffectRelation(e)
	Duel.SetTargetCard(g)
end
```
