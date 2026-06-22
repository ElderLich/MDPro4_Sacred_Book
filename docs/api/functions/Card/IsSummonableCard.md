# Card.IsSummonableCard

## Signature

```lua
Card.IsSummonableCard(Card c) -> bool
```

## Description

Checks whether c's card data represents a monster that is allowed to be Normal Summoned or Set by card kind.
This rejects non-monsters, Extra Deck monsters, Ritual Monsters, Special Summon-only monsters, and Tokens. It does not check current costs, Summon count, locations, or player restrictions.

## Parameters

- `c` `Card`

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3572`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **27** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.IsSummonableCard`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Union Activation | `38527680` | [Scripts/c38527680.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c38527680.lua) | 57 |
| Vernusylph of the Awakening Forests | `36745317` | [Scripts/c36745317.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c36745317.lua) | 53 |
| Max Metalmorph | `89812483` | [Scripts/c89812483.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c89812483.lua) | 53 |
| The Chaotic Sacred Beasts | `7894706` | [Scripts/c7894706.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c7894706.lua) | 49 |
| Elemental HERO Flame Wingman - Infernal Rage | `93347961` | [Scripts/c93347961.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93347961.lua) | 47 |
| Flame Coating Metalmorph | `91152455` | [Scripts/c91152455.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c91152455.lua) | 47 |
| Storm-Bane Dragon Destorbim | `94641726` | [Scripts/c94641726.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c94641726.lua) | 45 |
| Golden-Eyes Idol | `78642798` | [Scripts/c78642798.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c78642798.lua) | 44 |
| Chaos Space | `99266988` | [Scripts/c99266988.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c99266988.lua) | 43 |
| Crimson Blade Dragon | `3294539` | [Scripts/c3294539.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c3294539.lua) | 41 |
| Cyber Emergency | `60600126` | [Scripts/c60600126.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c60600126.lua) | 40 |
| Principug | `11496832` | [Scripts/c11496832.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c11496832.lua) | 39 |
| Zoodiac Broadbull | `85115440` | [Scripts/c85115440.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c85115440.lua) | 38 |
| Drytron Nova | `94187078` | [Scripts/c94187078.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c94187078.lua) | 37 |
| Unleashing the Sacred Beasts | `38776201` | [Scripts/c38776201.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c38776201.lua) | 36 |
| G Golem Stubborn Menhir | `97053215` | [Scripts/c97053215.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c97053215.lua) | 36 |
| A Wild Monster Appears! | `23587624` | [Scripts/c23587624.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c23587624.lua) | 35 |
| Mausoleum of the Emperor | `80921533` | [Scripts/c80921533.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c80921533.lua) | 35 |
| Monster Gate | `43040603` | [Scripts/c43040603.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c43040603.lua) | 34 |
| Reasoning | `58577036` | [Scripts/c58577036.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c58577036.lua) | 30 |
| Tribute Doll | `2903036` | [Scripts/c2903036.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c2903036.lua) | 28 |
| Hypernova Burst | `90384300` | [Scripts/c90384300.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c90384300.lua) | 27 |
| Time Dimension Hole | `90615639` | [Scripts/c90615639.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c90615639.lua) | 23 |
| Brain Control | `87910978` | [Scripts/c87910978.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c87910978.lua) | 23 |
| ...and 3 more |  |  |  |

## Script Examples

### Union Activation (`38527680`)

Source: [Scripts/c38527680.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c38527680.lua)

```lua
function s.thfilter2(c,e,tp)
	local minc,maxc=c:GetTributeRequirement()
	return c:IsAttackAbove(3000) and c:IsSummonable(true,nil) and c:IsSummonableCard() and c:IsAbleToHand() and s.sunthfilter(c,e,tp,minc,maxc) and Duel.IsPlayerCanSummon(tp,SUMMON_TYPE_ADVANCE,c)
end
function s.sunthfilter(c,e,tp,minc,maxc)
```

### Vernusylph of the Awakening Forests (`36745317`)

Source: [Scripts/c36745317.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c36745317.lua)

```lua
end
function c36745317.tgfilter(c)
	return c:IsAttribute(ATTRIBUTE_EARTH) and c:IsSummonableCard() and c:IsAbleToGrave()
end
function c36745317.tgtg(e,tp,eg,ep,ev,re,r,rp,chk)
```

### Max Metalmorph (`89812483`)

Source: [Scripts/c89812483.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c89812483.lua)

```lua
end
function s.filter2(c,e,tp,ft,lv,race,att)
	if not (not c:IsSummonableCard() and aux.IsCodeListed(c,89812483) and c:IsType(TYPE_MONSTER)) then return false end
	local proc=e:GetHandler():IsCode(id) and c.Metallization_material and c.Metallization_material(ft,lv,race,att)
	return c:IsCanBeSpecialSummoned(e,0,tp,proc,proc,POS_FACEUP)
```
