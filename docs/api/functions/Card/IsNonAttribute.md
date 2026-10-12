# Card.IsNonAttribute

## Signature

```lua
Card.IsNonAttribute(Card c, int attribute) -> bool
```

## Description

Checks whether c has any Attribute other than attribute.
For example, if a monster is both DARK and WIND, IsAttribute(DARK) is true, but IsNonAttribute(DARK) is also true.

## Parameters

- `c` `Card`
- `attribute` `int`

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3552`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **27** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Card.IsNonAttribute) with `Card.IsNonAttribute`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Mixeroid | `71340250` | [Scripts/c71340250.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c71340250.lua) | 1 |
| ZS - Ouroboros Sage | `32281491` | [Scripts/c32281491.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c32281491.lua) | 1 |
| Mariamne, the True Dracophoenix | `94160895` | [Scripts/c94160895.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c94160895.lua) | 1 |
| Dragonroid | `9069157` | [Scripts/c9069157.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c9069157.lua) | 1 |
| True King Lithosagym, the Disaster | `30539496` | [Scripts/c30539496.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c30539496.lua) | 1 |
| Sea Stealth II | `58203736` | [Scripts/c58203736.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c58203736.lua) | 1 |
| True King Agnimazud, the Vanisher | `96746083` | [Scripts/c96746083.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c96746083.lua) | 1 |
| Ocean Dragon Lord - Kairyu-Shin | `23931679` | [Scripts/c23931679.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c23931679.lua) | 2 |
| True King Bahrastos, the Fathomer | `82321037` | [Scripts/c82321037.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c82321037.lua) | 1 |
| Super Quantum White Layer | `73422829` | [Scripts/c73422829.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c73422829.lua) | 1 |
| Salamangreat Miragestallio | `87327776` | [Scripts/c87327776.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c87327776.lua) | 1 |
| Thunderspeed Summon | `55557574` | [Scripts/c55557574.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c55557574.lua) | 1 |
| Sirenorca | `50074392` | [Scripts/c50074392.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c50074392.lua) | 1 |
| Yosenju Misak | `39853199` | [Scripts/c39853199.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c39853199.lua) | 1 |
| Snowdust Giant | `73659078` | [Scripts/c73659078.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c73659078.lua) | 1 |
| Photon Delta Wing | `47051709` | [Scripts/c47051709.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c47051709.lua) | 1 |
| Fires of Doomsday | `46173679` | [Scripts/c46173679.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c46173679.lua) | 1 |
| Windwitch - Snow Bell | `70117860` | [Scripts/c70117860.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c70117860.lua) | 1 |
| Fairy King Albverdich | `28290705` | [Scripts/c28290705.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c28290705.lua) | 1 |
| Amphibious Bugroth MK-11 | `4754691` | [Scripts/c4754691.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c4754691.lua) | 1 |
| Eisbahn | `54059040` | [Scripts/c54059040.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c54059040.lua) | 1 |
| Evilswarm Golem | `31456110` | [Scripts/c31456110.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c31456110.lua) | 1 |
| Ally of Justice Catastor | `26593852` | [Scripts/c26593852.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c26593852.lua) | 1 |
| Ally of Justice Thousand Arms | `85876417` | [Scripts/c85876417.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c85876417.lua) | 1 |
| ...and 3 more |  |  |  |

## Script Examples

### Mixeroid (`71340250`)

Source: [Scripts/c71340250.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c71340250.lua)

```lua
end
function c71340250.filter(c,e,tp)
	return c:IsSetCard(0x16) and c:IsNonAttribute(ATTRIBUTE_WIND) and c:IsCanBeSpecialSummoned(e,0,tp,false,false)
end
function c71340250.target(e,tp,eg,ep,ev,re,r,rp,chk)
```

### ZS - Ouroboros Sage (`32281491`)

Source: [Scripts/c32281491.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c32281491.lua)

```lua
end
function c32281491.spfilter(c,e,tp)
	return c:IsNonAttribute(ATTRIBUTE_LIGHT) and c:IsSetCard(0x48) and c:IsCanBeSpecialSummoned(e,0,tp,false,false)
end
function c32281491.eqfilter(c)
```

### Mariamne, the True Dracophoenix (`94160895`)

Source: [Scripts/c94160895.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c94160895.lua)

```lua
end
function c94160895.thfilter(c)
	return c:IsNonAttribute(ATTRIBUTE_WIND) and c:IsRace(RACE_WYRM) and c:IsAbleToHand()
end
function c94160895.thtg(e,tp,eg,ep,ev,re,r,rp,chk)
```
