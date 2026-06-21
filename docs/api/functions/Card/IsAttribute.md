# Card.IsAttribute

## Signature

```lua
Card.IsAttribute(Card c, int attribute) -> bool
```

## Description

Check whether c belongs to attribute attribute

## Parameters

- `c` `Card`
- `attribute` `int`

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3494`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **1441** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.IsAttribute`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Salamandra with Chain](/examples/cards/62091148) | `62091148` | [Scripts/c62091148.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c62091148.lua) | 81 |
| [Fiendsmith's Sequence](/examples/cards/49867899) | `49867899` | [Scripts/c49867899.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c49867899.lua) | 68 |
| [Future Fusion Nova](/examples/cards/92058902) | `92058902` | [Scripts/c92058902.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92058902.lua) | 63 |
| [Odd-Eyes Arcray Dragon](/examples/cards/6218704) | `6218704` | [Scripts/c6218704.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c6218704.lua) | 62 |
| [Tellusion the Magna Warrior](/examples/cards/24431911) | `24431911` | [Scripts/c24431911.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24431911.lua) | 62 |
| [Ashened to Endlessness](/examples/cards/34813443) | `34813443` | [Scripts/c34813443.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c34813443.lua) | 62 |
| [Starving Venemy Dragon](/examples/cards/93729065) | `93729065` | [Scripts/c93729065.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93729065.lua) | 61 |
| [A Bao A Qu, the Lightless Shadow](/examples/cards/4731783) | `4731783` | [Scripts/c4731783.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c4731783.lua) | 61 |
| [Earthbound Servant Geo Gremlin](/examples/cards/8690387) | `8690387` | [Scripts/c8690387.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c8690387.lua) | 61 |
| [Fiendsmith Kyrie](/examples/cards/26434972) | `26434972` | [Scripts/c26434972.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c26434972.lua) | 61 |
| Gravity Balance | `37930737` | [Scripts/c37930737.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c37930737.lua) | 60 |
| Supreme King Dragon Lightwurm | `41908872` | [Scripts/c41908872.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c41908872.lua) | 59 |
| Hojo the Vaylantz Warrior | `88919365` | [Scripts/c88919365.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c88919365.lua) | 59 |
| Angelica, Princess of Noble Arms | `36320744` | [Scripts/c36320744.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c36320744.lua) | 59 |
| Starving Venom Fusion Dragon of the Four Heavenly Dragons | `27118421` | [Scripts/c27118421.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c27118421.lua) | 59 |
| Super Duper Polymerization | `44886582` | [Scripts/c44886582.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44886582.lua) | 59 |
| Magikey Dragon - Andrabime | `71159974` | [Scripts/c71159974.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71159974.lua) | 59 |
| Hunting Horn | `55421040` | [Scripts/c55421040.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c55421040.lua) | 59 |
| Ojamassimilation | `2390019` | [Scripts/c2390019.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c2390019.lua) | 59 |
| Echelon of the Fire Kings | `38798785` | [Scripts/c38798785.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c38798785.lua) | 59 |
| Fusion Destiny | `52947044` | [Scripts/c52947044.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c52947044.lua) | 59 |
| Chaos Emperor, the Dragon of Armageddon | `4538826` | [Scripts/c4538826.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c4538826.lua) | 58 |
| Rank-Up-Magic Astral Force | `45950291` | [Scripts/c45950291.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c45950291.lua) | 58 |
| Overload Future Fusion | `33099732` | [Scripts/c33099732.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c33099732.lua) | 58 |
| ...and 1417 more |  |  |  |

## Script Examples

### Salamandra with Chain (`62091148`)

Source: [Scripts/c62091148.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c62091148.lua)

```lua
end
function s.filter(c)
	return c:IsFaceup() and c:IsAttribute(ATTRIBUTE_FIRE)
end
function s.target(e,tp,eg,ep,ev,re,r,rp,chk,chkc)
```

### Fiendsmith's Sequence (`49867899`)

Source: [Scripts/c49867899.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c49867899.lua)

```lua
end
function s.eqfilter(c)
	return c:IsFaceup() and c:IsRace(RACE_FIEND) and c:IsAttribute(ATTRIBUTE_LIGHT) and not c:IsType(TYPE_LINK)
end
function s.eqtg(e,tp,eg,ep,ev,re,r,rp,chk,chkc)
```

### Future Fusion Nova (`92058902`)

Source: [Scripts/c92058902.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92058902.lua)

```lua
end
function s.filter2(c,e,tp,m,f,chkf)
	if not (c:IsType(TYPE_FUSION) and c:IsRace(RACE_MACHINE) and c:IsAttribute(ATTRIBUTE_LIGHT) and (not f or f(c))
		and c:IsCanBeSpecialSummoned(e,SUMMON_TYPE_FUSION,tp,false,false)) then return false end
	aux.FCheckAdditional=s.fcheck
```
