# Duel.GetOperationInfo

## Signature

```lua
Duel.GetOperationInfo(int chainc, int category) -> bool,Group|nil,int|nil,int|nil,int|nil
```

## Description

Returns operation information recorded for category on chainc.
The first return value is false when that category is not recorded. Otherwise, the remaining values correspond to Duel.SetOperationInfo: targets, count, target_player, and target_param.
Use this in response checks that need to inspect what a Chain Link announced, such as whether it is expected to destroy cards, move cards from a location, or change LP.

## How To Use It

Use this in response checks or follow-up operations that need to read what a Chain Link announced with `Duel.SetOperationInfo`.

```lua
local ex,g,ct,p,loc=Duel.GetOperationInfo(ev,CATEGORY_TOHAND)
if ex and bit.band(loc or 0,LOCATION_DECK)~=0 then
    -- the Chain Link announced adding from the Deck
end
```

The first return value is false when that category was not recorded. The remaining values mirror the `targets`, `count`, `target_player`, and `target_param` arguments.

## Related Functions

- [Duel.SetOperationInfo](/api/functions/Duel/SetOperationInfo)
- [Effect.SetCategory](/api/functions/Effect/SetCategory)
- [Duel.GetChainInfo](/api/functions/Duel/GetChainInfo)

## Parameters

- `chainc` `int` - Chain Link number to inspect. Use 0 for the current Chain Link.
- `category` `int` - CATEGORY_* flag whose operation info should be read.

## Returns

- `bool` - true if operation info for category exists; false if not.
- `Group|nil` - Recorded target cards, or nil when only count/player/param were recorded.
- `int|nil` - Recorded expected count.
- `int|nil` - Recorded target player.
- `int|nil` - Recorded category-specific parameter, often a location or amount.

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5009`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **71** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Duel.GetOperationInfo`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Enneacraft - Archa.TAIL](/examples/cards/81237046) | `81237046` | [Scripts/c81237046.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c81237046.lua) | 1 |
| Ruddy Rose Dragon | `40139997` | [Scripts/c40139997.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c40139997.lua) | 1 |
| Raiza the Mega Monarch | `69327790` | [Scripts/c69327790.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c69327790.lua) | 2 |
| Keaf, Murk of the Ghoti | `99529628` | [Scripts/c99529628.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c99529628.lua) | 2 |
| Meklord Emperor Wisel - Synchro Absorption | `30221870` | [Scripts/c30221870.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30221870.lua) | 1 |
| Underworld Goddess of the Closed World | `98127546` | [Scripts/c98127546.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c98127546.lua) | 1 |
| Shield Handler | `93655221` | [Scripts/c93655221.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93655221.lua) | 1 |
| Shooting Star Dragon | `24696097` | [Scripts/c24696097.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24696097.lua) | 1 |
| Evil★Twin GG EZ | `34365442` | [Scripts/c34365442.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c34365442.lua) | 1 |
| Stardust Dragon | `44508094` | [Scripts/c44508094.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44508094.lua) | 1 |
| Baxia, Brightness of the Yang Zing | `83755611` | [Scripts/c83755611.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c83755611.lua) | 2 |
| Salamangreat Charge | `83533296` | [Scripts/c83533296.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c83533296.lua) | 2 |
| Cyber Angel Vrash | `78316184` | [Scripts/c78316184.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c78316184.lua) | 1 |
| Van'Dalgyon the Dark Dragon Lord | `24857466` | [Scripts/c24857466.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24857466.lua) | 2 |
| Meklord Astro Dragon Asterisk | `38522377` | [Scripts/c38522377.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c38522377.lua) | 1 |
| Atomic Scrap Dragon | `92361635` | [Scripts/c92361635.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92361635.lua) | 2 |
| Scrap Twin Dragon | `50278554` | [Scripts/c50278554.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c50278554.lua) | 2 |
| Tip of the Tinying Tongue | `85640370` | [Scripts/c85640370.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c85640370.lua) | 1 |
| Vendread Chimera | `13482075` | [Scripts/c13482075.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c13482075.lua) | 1 |
| Reptilianne Recoil | `17000165` | [Scripts/c17000165.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c17000165.lua) | 2 |
| Engraver of the Mark | `50078320` | [Scripts/c50078320.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c50078320.lua) | 1 |
| Number 39: Utopia Beyond | `21521304` | [Scripts/c21521304.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c21521304.lua) | 2 |
| Hyper Psychic Blaster/Assault Mode | `37169670` | [Scripts/c37169670.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c37169670.lua) | 2 |
| Dark Magic Mirror Force | `59016454` | [Scripts/c59016454.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59016454.lua) | 1 |
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
