# Auxiliary.IsCodeListed

## Signature

```lua
Auxiliary.IsCodeListed(Card c, int code) -> bool|nil
```

## Description

Checks whether code is registered in c's card_code_list by Auxiliary.AddCodeList or a related helper.
The Lua helper returns true for a listed code and nil otherwise, so it is normally used as a truthy check.

## Parameters

- `c` `Card`
- `code` `int`

## Returns

- `bool|nil` - true if code is listed by c; nil otherwise.

## Source

- `Utilities/utility.lua:547`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **170** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Auxiliary.IsCodeListed`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Shooting Majestic Star Dragon](/examples/cards/40939228) | `40939228` | [Scripts/c40939228.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c40939228.lua) | 62 |
| [Transonic Bird](/examples/cards/34072799) | `34072799` | [Scripts/c34072799.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c34072799.lua) | 61 |
| Angelica, Princess of Noble Arms | `36320744` | [Scripts/c36320744.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c36320744.lua) | 59 |
| Chaos Hats | `2372506` | [Scripts/c2372506.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c2372506.lua) | 59 |
| Ancient Gear Duel | `53541822` | [Scripts/c53541822.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c53541822.lua) | 58 |
| Defense of the Temple | `96687733` | [Scripts/c96687733.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c96687733.lua) | 58 |
| Divine Serpent Apophis | `97800311` | [Scripts/c97800311.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c97800311.lua) | 58 |
| Purrely | `25550531` | [Scripts/c25550531.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c25550531.lua) | 56 |
| Masterflare Hyperion | `63101468` | [Scripts/c63101468.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63101468.lua) | 53 |
| Max Metalmorph | `89812483` | [Scripts/c89812483.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c89812483.lua) | 53 |
| Gunkan Suship Shari Red | `63748694` | [Scripts/c63748694.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63748694.lua) | 52 |
| Neiroy, the Dream Mirror Traitor | `90176467` | [Scripts/c90176467.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c90176467.lua) | 52 |
| Black Chaos the Ultimate Magical Swordsman | `98684220` | [Scripts/c98684220.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c98684220.lua) | 51 |
| Salamandra Fusion | `9102835` | [Scripts/c9102835.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c9102835.lua) | 51 |
| Ancient Gear Advance | `4064925` | [Scripts/c4064925.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c4064925.lua) | 51 |
| Synchro Fellowship | `43834302` | [Scripts/c43834302.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c43834302.lua) | 51 |
| Eclipse, Dragon Ruler of Catastrophes | `30350202` | [Scripts/c30350202.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30350202.lua) | 50 |
| Timaeus the United Dragon | `3078380` | [Scripts/c3078380.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c3078380.lua) | 50 |
| Exosister Vadis | `77891946` | [Scripts/c77891946.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c77891946.lua) | 50 |
| Mystic Box of Chaos | `75983808` | [Scripts/c75983808.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c75983808.lua) | 49 |
| Skull Archfiend of Chaos | `24088928` | [Scripts/c24088928.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24088928.lua) | 49 |
| Mystical Celtic Sage | `50073633` | [Scripts/c50073633.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c50073633.lua) | 49 |
| Gold Pride - It's Neck and Neck! | `90164606` | [Scripts/c90164606.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c90164606.lua) | 49 |
| Evil HERO Inferno Wing - Backfire | `59893882` | [Scripts/c59893882.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59893882.lua) | 49 |
| ...and 146 more |  |  |  |

## Script Examples

### Shooting Majestic Star Dragon (`40939228`)

Source: [Scripts/c40939228.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c40939228.lua)

```lua
end
function c40939228.atkfilter(c)
	return c:IsCode(44508094) or aux.IsCodeListed(c,44508094) and c:IsType(TYPE_SYNCHRO)
end
function c40939228.atkval(e,c)
```

### Transonic Bird (`34072799`)

Source: [Scripts/c34072799.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c34072799.lua)

```lua
end
function c34072799.thfilter(c,mc)
	return bit.band(c:GetType(),0x81)==0x81 and c:IsAbleToHand() and aux.IsCodeListed(mc,c:GetCode())
end
function c34072799.thtg(e,tp,eg,ep,ev,re,r,rp,chk)
```

### Angelica, Princess of Noble Arms (`36320744`)

Source: [Scripts/c36320744.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c36320744.lua)

```lua
end
function s.thfilter(c)
	return (c:IsCode(55749927) or aux.IsCodeListed(c,77656797)) and c:IsAbleToHand()
end
function s.thtg(e,tp,eg,ep,ev,re,r,rp,chk)
```
