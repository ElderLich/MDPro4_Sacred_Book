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

## Guided Examples

Learn how to use this function in context:

- [Archetypes and Set Codes](/learn/archetypes-and-setcodes)

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **193** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Auxiliary.IsCodeListed) with `Auxiliary.IsCodeListed`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Levia-Dragoon - Daedalus](/examples/cards/78579058) | `78579058` | [Scripts/c78579058.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c78579058.lua) | 1 |
| [Azure Ocean Dragon Lord - Neo-Daedalus Rage](/examples/cards/41570943) | `41570943` | [Scripts/c41570943.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c41570943.lua) | 1 |
| [Shooting Majestic Star Dragon](/examples/cards/40939228) | `40939228` | [Scripts/c40939228.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c40939228.lua) | 1 |
| [Transonic Bird](/examples/cards/34072799) | `34072799` | [Scripts/c34072799.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c34072799.lua) | 1 |
| Angelica, Princess of Noble Arms | `36320744` | [Scripts/c36320744.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c36320744.lua) | 1 |
| Chaos Magical Hats | `2372506` | [Scripts/c2372506.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c2372506.lua) | 1 |
| Ancient Gear Duel | `53541822` | [Scripts/c53541822.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c53541822.lua) | 2 |
| Defense of the Temple | `96687733` | [Scripts/c96687733.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c96687733.lua) | 1 |
| Divine Serpent Apophis | `97800311` | [Scripts/c97800311.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c97800311.lua) | 1 |
| Purrely | `25550531` | [Scripts/c25550531.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c25550531.lua) | 1 |
| Sleepy Scapegoats | `3129527` | [Scripts/c3129527.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c3129527.lua) | 2 |
| Masterflare Hyperion | `63101468` | [Scripts/c63101468.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63101468.lua) | 1 |
| Max Metalmorph | `89812483` | [Scripts/c89812483.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c89812483.lua) | 1 |
| Gunkan Suship Shari Red | `63748694` | [Scripts/c63748694.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63748694.lua) | 1 |
| Neiroy, the Dream Mirror Traitor | `90176467` | [Scripts/c90176467.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c90176467.lua) | 4 |
| Red-Eyes Black Dragon Exceed | `17242022` | [Scripts/c17242022.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c17242022.lua) | 1 |
| Black Chaos | `98684220` | [Scripts/c98684220.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c98684220.lua) | 1 |
| Salamandra Fusion | `9102835` | [Scripts/c9102835.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c9102835.lua) | 1 |
| Ancient Gear Advance | `4064925` | [Scripts/c4064925.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c4064925.lua) | 1 |
| Synchro Fellowship | `43834302` | [Scripts/c43834302.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c43834302.lua) | 4 |
| Reversal Box | `2606417` | [Scripts/c2606417.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c2606417.lua) | 1 |
| Eclipse, Dragon Ruler of Catastrophes | `30350202` | [Scripts/c30350202.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30350202.lua) | 1 |
| Blue-Eyes Toon Ultimate Dragon | `71808988` | [Scripts/c71808988.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71808988.lua) | 1 |
| Timaeus the United Dragon | `3078380` | [Scripts/c3078380.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c3078380.lua) | 1 |
| ...and 169 more |  |  |  |

## Script Examples

### Levia-Dragoon - Daedalus (`78579058`)

Source: [Scripts/c78579058.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c78579058.lua)

```lua
end
function s.spfilter(c,e,tp)
	return aux.IsCodeListed(c,38391684) and c:IsCanBeSpecialSummoned(e,0,tp,false,false)
end
function s.sptg(e,tp,eg,ep,ev,re,r,rp,chk)
```

### Azure Ocean Dragon Lord - Neo-Daedalus Rage (`41570943`)

Source: [Scripts/c41570943.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c41570943.lua)

```lua
end
function s.spfilter1(c,e,tp,zone)
	return aux.IsCodeListed(c,38391684) and c:IsCanBeSpecialSummoned(e,0,tp,false,false,POS_FACEUP,tp,zone)
end
function s.sptg(e,tp,eg,ep,ev,re,r,rp,chk)
```

### Shooting Majestic Star Dragon (`40939228`)

Source: [Scripts/c40939228.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c40939228.lua)

```lua
end
function c40939228.atkfilter(c)
	return c:IsCode(44508094) or aux.IsCodeListed(c,44508094) and c:IsType(TYPE_SYNCHRO)
end
function c40939228.atkval(e,c)
```
