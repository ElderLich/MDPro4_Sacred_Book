# Effect.IsHasCategory

## Signature

```lua
Effect.IsHasCategory(Effect e, int cate) -> bool
```

## Description

Checks whether e's category bitmask contains cate.

## Parameters

- `e` `Effect`
- `cate` `int`

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libeffect.cpp:651`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **38** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Effect.IsHasCategory`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Deftero Enneacraft - "alazoneIA"](/examples/cards/92171126) | `92171126` | [Scripts/c92171126.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92171126.lua) | 68 |
| [Enneacraft - Archa.TAIL](/examples/cards/81237046) | `81237046` | [Scripts/c81237046.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c81237046.lua) | 63 |
| Artmage Pact -Awakening- | `23599634` | [Scripts/c23599634.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c23599634.lua) | 60 |
| Ekto Enneacraft - "tromarIA" | `29570824` | [Scripts/c29570824.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c29570824.lua) | 52 |
| Trito Enneacraft - "exapatisIA" | `44716748` | [Scripts/c44716748.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44716748.lua) | 51 |
| Branded Retribution | `17751597` | [Scripts/c17751597.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c17751597.lua) | 48 |
| Dragonroid | `9069157` | [Scripts/c9069157.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c9069157.lua) | 47 |
| Meklord Emperor Wisel - Synchro Absorption | `30221870` | [Scripts/c30221870.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30221870.lua) | 46 |
| Underworld Goddess of the Closed World | `98127546` | [Scripts/c98127546.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c98127546.lua) | 46 |
| Shooting Star Dragon | `24696097` | [Scripts/c24696097.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24696097.lua) | 45 |
| Evil★Twin GG EZ | `34365442` | [Scripts/c34365442.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c34365442.lua) | 45 |
| Stardust Dragon | `44508094` | [Scripts/c44508094.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44508094.lua) | 45 |
| D/D/D Wave High King Caesar | `79559912` | [Scripts/c79559912.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c79559912.lua) | 43 |
| Cyber Angel Vrash | `78316184` | [Scripts/c78316184.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c78316184.lua) | 42 |
| Tearlaments Rulkallos | `84330567` | [Scripts/c84330567.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c84330567.lua) | 41 |
| Derk, Longing for the Blue Skies | `46708514` | [Scripts/c46708514.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c46708514.lua) | 40 |
| Armament Reincarnation | `53770666` | [Scripts/c53770666.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c53770666.lua) | 40 |
| Branded Lost | `18973184` | [Scripts/c18973184.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c18973184.lua) | 40 |
| Vendread Chimera | `13482075` | [Scripts/c13482075.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c13482075.lua) | 39 |
| Shipping Error | `58761791` | [Scripts/c58761791.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c58761791.lua) | 36 |
| Magical Meltdown | `47679935` | [Scripts/c47679935.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c47679935.lua) | 35 |
| Retaliating "C" | `46502744` | [Scripts/c46502744.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c46502744.lua) | 34 |
| Rebound | `983995` | [Scripts/c983995.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c983995.lua) | 32 |
| Learning Elf | `32126000` | [Scripts/c32126000.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c32126000.lua) | 31 |
| ...and 14 more |  |  |  |

## Script Examples

### Deftero Enneacraft - "alazoneIA" (`92171126`)

Source: [Scripts/c92171126.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92171126.lua)

```lua
end
function s.thcon2(e,tp,eg,ep,ev,re,r,rp)
	local ex4=re:IsHasCategory(CATEGORY_DRAW)
	local ex5=re:IsHasCategory(CATEGORY_SEARCH)
	return ep==1-tp and (ex4 or ex5) and e:GetHandler():IsFacedown()
```

### Enneacraft - Archa.TAIL (`81237046`)

Source: [Scripts/c81237046.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c81237046.lua)

```lua
function s.indcon(e,tp,eg,ep,ev,re,r,rp)
	if e:GetHandler():IsStatus(STATUS_BATTLE_DESTROYED) or not Duel.IsChainNegatable(ev) then return false end
	if re:IsHasCategory(CATEGORY_NEGATE)
		and Duel.GetChainInfo(ev-1,CHAININFO_TRIGGERING_EFFECT):IsHasType(EFFECT_TYPE_ACTIVATE) then return false end
	local ex,tg,tc=Duel.GetOperationInfo(ev,CATEGORY_DESTROY)
```

### Artmage Pact -Awakening- (`23599634`)

Source: [Scripts/c23599634.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c23599634.lua)

```lua
	local p=e:GetHandlerPlayer()
	local te,tp=Duel.GetChainInfo(ct,CHAININFO_TRIGGERING_EFFECT,CHAININFO_TRIGGERING_PLAYER)
	return p==tp and te:IsHasCategory(CATEGORY_FUSION_SUMMON)
end
function s.limfilter(c,tp)
```
