# Auxiliary.AtkEqualsDef

## Signature

```lua
Auxiliary.AtkEqualsDef(Card c) -> void
```

## Description

Returns true for a non-Link Monster whose ATK equals DEF, using current values on the field or known printed values elsewhere.

## Parameters

- `c` `Card`

## Source

- `Utilities/utility.lua:1118`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **12** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Auxiliary.AtkEqualsDef) with `Auxiliary.AtkEqualsDef`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Helping Robo for Underwater Combat | `77856460` | [Scripts/c77856460.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c77856460.lua) | 1 |
| Despian Luluwalilith | `53971455` | [Scripts/c53971455.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c53971455.lua) | 1 |
| The Three Champions of Swordsoul | `74405783` | [Scripts/c74405783.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c74405783.lua) | 1 |
| Gizmek Inaba, the Hopping Hare of Hakuto | `50901852` | [Scripts/c50901852.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c50901852.lua) | 2 |
| Sacred Scrolls of the Gizmek Legend | `24793135` | [Scripts/c24793135.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c24793135.lua) | 2 |
| Checkker | `77435268` | [Scripts/c77435268.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c77435268.lua) | 1 |
| Gizmek Arakami, the Hailbringer Hog | `59789370` | [Scripts/c59789370.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c59789370.lua) | 3 |
| The Golden Swordsoul | `82489470` | [Scripts/c82489470.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c82489470.lua) | 1 |
| Gizmek Uka, the Festive Fox of Fecundity | `90361289` | [Scripts/c90361289.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c90361289.lua) | 1 |
| Gizmek Taniguku, the Immobile Intellect | `23384666` | [Scripts/c23384666.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c23384666.lua) | 2 |
| Gizmek Naganaki, the Sunrise Signaler | `96399967` | [Scripts/c96399967.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c96399967.lua) | 3 |
| Gizmek Makami, the Ferocious Fanged Fortress | `46809548` | [Scripts/c46809548.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c46809548.lua) | 1 |

## Script Examples

### Helping Robo for Underwater Combat (`77856460`)

Source: [Scripts/c77856460.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c77856460.lua)

```lua
end
function s.thfilter(c)
	return aux.AtkEqualsDef(c) and c:IsRace(RACE_MACHINE) and c:IsAbleToHand()
end
function s.thtg(e,tp,eg,ep,ev,re,r,rp,chk)
```

### Despian Luluwalilith (`53971455`)

Source: [Scripts/c53971455.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c53971455.lua)

```lua
end
function c53971455.spfilter(c,e,tp)
	return c:IsAttribute(ATTRIBUTE_LIGHT) and c:IsRace(RACE_SPELLCASTER) and aux.AtkEqualsDef(c) and c:IsCanBeSpecialSummoned(e,0,tp,false,false)
end
function c53971455.sptg(e,tp,eg,ep,ev,re,r,rp,chk)
```

### The Three Champions of Swordsoul (`74405783`)

Source: [Scripts/c74405783.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c74405783.lua)

```lua
end
function s.thfilter(c)
	return aux.AtkEqualsDef(c) and c:IsRace(RACE_SPELLCASTER)
		and c:IsLevel(4,8) and c:IsAbleToHand()
end
```
