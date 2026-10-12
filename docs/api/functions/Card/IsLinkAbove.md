# Card.IsLinkAbove

## Signature

```lua
Card.IsLinkAbove(Card c, int link) -> bool
```

## Description

Checks whether c has a nonzero Link Rating greater than or equal to link.

## Parameters

- `c` `Card`
- `link` `int`

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3672`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **28** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Card.IsLinkAbove) with `Card.IsLinkAbove`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Yummy★Snatchy](/examples/cards/30581601) | `30581601` | [Scripts/c30581601.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c30581601.lua) | 1 |
| Unchained Soul Rage Abominator | `21419436` | [Scripts/c21419436.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c21419436.lua) | 1 |
| Marincess Cascade | `27012990` | [Scripts/c27012990.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c27012990.lua) | 2 |
| Code of Soul | `74652966` | [Scripts/c74652966.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c74652966.lua) | 1 |
| Scareclaw Twinsaw | `95245571` | [Scripts/c95245571.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c95245571.lua) | 1 |
| Sunavalon Dryatrentiay | `92770064` | [Scripts/c92770064.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c92770064.lua) | 1 |
| Rustin Mammoth | `3434362` | [Scripts/c3434362.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c3434362.lua) | 2 |
| Fiendsmith's Desirae | `82135803` | [Scripts/c82135803.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c82135803.lua) | 1 |
| Sunvine Thrasher | `91557476` | [Scripts/c91557476.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c91557476.lua) | 1 |
| Marincess Circulation | `83723605` | [Scripts/c83723605.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c83723605.lua) | 1 |
| Armored Bitron | `29374928` | [Scripts/c29374928.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c29374928.lua) | 1 |
| Marincess Bubble Ring | `19712214` | [Scripts/c19712214.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c19712214.lua) | 1 |
| Sunvine Healer | `65563871` | [Scripts/c65563871.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c65563871.lua) | 1 |
| Gouki The Tyrant Ogre | `7782069` | [Scripts/c7782069.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c7782069.lua) | 1 |
| Salamangreat Fennec | `49094491` | [Scripts/c49094491.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c49094491.lua) | 1 |
| Protectcode Talker | `58036229` | [Scripts/c58036229.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c58036229.lua) | 1 |
| Cyberse Desavewurm | `92422871` | [Scripts/c92422871.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c92422871.lua) | 1 |
| Furtive Techniques Fur Hire, Fur All Your Ultimate Moves | `59374259` | [Scripts/c59374259.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c59374259.lua) | 2 |
| Marincess Wave | `52945066` | [Scripts/c52945066.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c52945066.lua) | 2 |
| A.I.'s Show | `54374642` | [Scripts/c54374642.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c54374642.lua) | 1 |
| Gouki Gameface | `95448372` | [Scripts/c95448372.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c95448372.lua) | 1 |
| S-Force Edge Razor | `91864689` | [Scripts/c91864689.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c91864689.lua) | 1 |
| Link Devotee | `48068378` | [Scripts/c48068378.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c48068378.lua) | 1 |
| Sunavalon Bloom | `54340229` | [Scripts/c54340229.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c54340229.lua) | 1 |
| ...and 4 more |  |  |  |

## Script Examples

### Yummy★Snatchy (`30581601`)

Source: [Scripts/c30581601.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c30581601.lua)

```lua
end
function s.splimit(e,c,tp,sumtp,sumpos)
	return c:IsLinkAbove(3) and bit.band(sumtp,SUMMON_TYPE_LINK)==SUMMON_TYPE_LINK
end
function s.sccon(e,tp,eg,ep,ev,re,r,rp)
```

### Unchained Soul Rage Abominator (`21419436`)

Source: [Scripts/c21419436.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c21419436.lua)

```lua
end
function s.cfilter(c)
	return c:IsFaceup() and c:IsLinkAbove(4) and c:IsSetCard(0x130)
end
function s.descon(e,tp,eg,ep,ev,re,r,rp)
```

### Marincess Cascade (`27012990`)

Source: [Scripts/c27012990.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c27012990.lua)

```lua
end
function c27012990.costfilter(c)
	return c:IsFaceup() and c:IsSetCard(0x12b) and c:IsType(TYPE_LINK) and c:IsLinkAbove(1) and c:IsAbleToRemoveAsCost()
end
function c27012990.fselect(g,tp)
```
