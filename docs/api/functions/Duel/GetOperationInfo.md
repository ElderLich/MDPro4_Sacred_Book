# Duel.GetOperationInfo

## Signature

```lua
Duel.GetOperationInfo(int chainc, int category) -> bool,Group,int,int,int
```

## Description

Returns operation information recorded for category on chainc.
The first return value is false when that category is not recorded. Otherwise, the remaining values correspond to Duel.SetOperationInfo: targets, count, target_player, and target_param.

## Parameters

- `chainc` `int`
- `category` `int`

## Returns

- `bool`
- `Group` - may be nil
- `int` - may be nil
- `int` - may be nil
- `int` - may be nil

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5009`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **71** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Duel.GetOperationInfo`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Enneacraft - Archa.TAIL](/examples/cards/81237046) | `81237046` | [Scripts/c81237046.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c81237046.lua) | 63 |
| Ruddy Rose Dragon | `40139997` | [Scripts/c40139997.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c40139997.lua) | 50 |
| Raiza the Mega Monarch | `69327790` | [Scripts/c69327790.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c69327790.lua) | 48 |
| Keaf, Murk of the Ghoti | `99529628` | [Scripts/c99529628.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c99529628.lua) | 47 |
| Meklord Emperor Wisel - Synchro Absorption | `30221870` | [Scripts/c30221870.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30221870.lua) | 46 |
| Underworld Goddess of the Closed World | `98127546` | [Scripts/c98127546.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c98127546.lua) | 46 |
| Shield Handler | `93655221` | [Scripts/c93655221.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93655221.lua) | 46 |
| Shooting Star Dragon | `24696097` | [Scripts/c24696097.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24696097.lua) | 45 |
| Evil★Twin GG EZ | `34365442` | [Scripts/c34365442.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c34365442.lua) | 45 |
| Stardust Dragon | `44508094` | [Scripts/c44508094.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44508094.lua) | 45 |
| Baxia, Brightness of the Yang Zing | `83755611` | [Scripts/c83755611.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c83755611.lua) | 44 |
| Salamangreat Charge | `83533296` | [Scripts/c83533296.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c83533296.lua) | 43 |
| Cyber Angel Vrash | `78316184` | [Scripts/c78316184.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c78316184.lua) | 42 |
| Van'Dalgyon the Dark Dragon Lord | `24857466` | [Scripts/c24857466.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24857466.lua) | 42 |
| Meklord Astro Dragon Asterisk | `38522377` | [Scripts/c38522377.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c38522377.lua) | 42 |
| Atomic Scrap Dragon | `92361635` | [Scripts/c92361635.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92361635.lua) | 41 |
| Scrap Twin Dragon | `50278554` | [Scripts/c50278554.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c50278554.lua) | 40 |
| Tip of the Tinying Tongue | `85640370` | [Scripts/c85640370.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c85640370.lua) | 40 |
| Vendread Chimera | `13482075` | [Scripts/c13482075.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c13482075.lua) | 39 |
| Reptilianne Recoil | `17000165` | [Scripts/c17000165.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c17000165.lua) | 38 |
| Engraver of the Mark | `50078320` | [Scripts/c50078320.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c50078320.lua) | 38 |
| Number 39: Utopia Beyond | `21521304` | [Scripts/c21521304.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c21521304.lua) | 38 |
| Hyper Psychic Blaster/Assault Mode | `37169670` | [Scripts/c37169670.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c37169670.lua) | 37 |
| Dark Magic Mirror Force | `59016454` | [Scripts/c59016454.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59016454.lua) | 35 |
| ...and 47 more |  |  |  |

## Script Examples

### Enneacraft - Archa.TAIL (`81237046`)

Source: [Scripts/c81237046.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c81237046.lua)

```lua
	if re:IsHasCategory(CATEGORY_NEGATE)
		and Duel.GetChainInfo(ev-1,CHAININFO_TRIGGERING_EFFECT):IsHasType(EFFECT_TYPE_ACTIVATE) then return false end
	local ex,tg,tc=Duel.GetOperationInfo(ev,CATEGORY_DESTROY)
	return ex and tg~=nil and tc+tg:FilterCount(Card.IsOnField,nil)-tg:GetCount()>0
		and ep~=tp and e:GetHandler():IsFacedown()
```

### Ruddy Rose Dragon (`40139997`)

Source: [Scripts/c40139997.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c40139997.lua)

```lua
function c40139997.discon(e,tp,eg,ep,ev,re,r,rp)
	if e:GetHandler():IsStatus(STATUS_BATTLE_DESTROYED) or not Duel.IsChainNegatable(ev) or ep==tp then return false end
	local ex,tg,tc=Duel.GetOperationInfo(ev,CATEGORY_DESTROY)
	return ex and (tg~=nil or tc>0)
end
```

### Raiza the Mega Monarch (`69327790`)

Source: [Scripts/c69327790.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c69327790.lua)

```lua
end
function c69327790.tdop(e,tp,eg,ep,ev,re,r,rp)
	local ex,g1=Duel.GetOperationInfo(0,CATEGORY_TODECK)
	local ex2,g2=Duel.GetOperationInfo(0,CATEGORY_TOHAND)
	if g1 then
```
