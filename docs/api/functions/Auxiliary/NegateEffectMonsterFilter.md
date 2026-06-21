# Auxiliary.NegateEffectMonsterFilter

## Signature

```lua
Auxiliary.NegateEffectMonsterFilter(Card c) -> bool
```

## Description

Filter for effects that negate an Effect Monster, such as Effect Veiler: c must be face-up, not already disabled, and currently an Effect Monster.

## Parameters

- `c` `Card`

## Returns

- `bool` - true if c is a valid Effect Monster to have its effects negated.

## Source

- `Utilities/utility.lua:748`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **60** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Auxiliary.NegateEffectMonsterFilter`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Shooting Majestic Star Dragon](/examples/cards/40939228) | `40939228` | [Scripts/c40939228.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c40939228.lua) | 62 |
| Weaver of Fairy Tails | `78021082` | [Scripts/c78021082.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c78021082.lua) | 53 |
| Ekto Enneacraft - "tromarIA" | `29570824` | [Scripts/c29570824.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c29570824.lua) | 52 |
| Groza, Tyrant of Thunder | `45420955` | [Scripts/c45420955.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c45420955.lua) | 51 |
| S-Force Justify | `35334193` | [Scripts/c35334193.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c35334193.lua) | 51 |
| Metaltronus | `64664373` | [Scripts/c64664373.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c64664373.lua) | 49 |
| Epurrely Beauty | `98049934` | [Scripts/c98049934.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c98049934.lua) | 49 |
| Zerrziel, Ruler of the Evil Eyed | `17739335` | [Scripts/c17739335.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c17739335.lua) | 48 |
| Runick Freezing Curses | `30430448` | [Scripts/c30430448.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30430448.lua) | 48 |
| Odd-Eyes Wing Dragon | `58074177` | [Scripts/c58074177.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c58074177.lua) | 47 |
| Aluber the Jester of Despia | `62962630` | [Scripts/c62962630.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c62962630.lua) | 47 |
| Realm Eulogy | `54851325` | [Scripts/c54851325.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c54851325.lua) | 47 |
| Ultimate Leo Utopia Ray | `68679595` | [Scripts/c68679595.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c68679595.lua) | 46 |
| Gorgon, Empress of the Evil Eyed | `29357687` | [Scripts/c29357687.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c29357687.lua) | 46 |
| Super Quantal Mech Beast Lusterrex | `57450198` | [Scripts/c57450198.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c57450198.lua) | 46 |
| Trivikarma | `7436169` | [Scripts/c7436169.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c7436169.lua) | 45 |
| Amaze Attraction Horror House | `92650018` | [Scripts/c92650018.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92650018.lua) | 45 |
| Time Thief Double Barrel | `91135480` | [Scripts/c91135480.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c91135480.lua) | 44 |
| Nemleria Repeter | `33499794` | [Scripts/c33499794.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c33499794.lua) | 44 |
| Rilliona, the Wondrous Magistus Witch Wardrobe | `74689476` | [Scripts/c74689476.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74689476.lua) | 44 |
| Fairy Tail Ball | `56725612` | [Scripts/c56725612.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c56725612.lua) | 44 |
| Myutant Clash | `5466615` | [Scripts/c5466615.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c5466615.lua) | 44 |
| Majestic Red Dragon | `67030233` | [Scripts/c67030233.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c67030233.lua) | 43 |
| Swordsoul Grandmaster - Chixiao | `69248256` | [Scripts/c69248256.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c69248256.lua) | 43 |
| ...and 36 more |  |  |  |

## Script Examples

### Shooting Majestic Star Dragon (`40939228`)

Source: [Scripts/c40939228.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c40939228.lua)

```lua
end
function c40939228.distg(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.IsExistingMatchingCard(aux.NegateEffectMonsterFilter,tp,0,LOCATION_MZONE,1,nil) end
	Duel.SetOperationInfo(0,CATEGORY_DISABLE,nil,1,tp,LOCATION_MZONE)
end
```

### Weaver of Fairy Tails (`78021082`)

Source: [Scripts/c78021082.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c78021082.lua)

```lua
end
function s.disfilter(c)
	return c:IsFaceup() and c:IsType(TYPE_EFFECT) and (aux.NegateEffectMonsterFilter(c) or not c:IsCode(19144623))
end
function s.distg(e,tp,eg,ep,ev,re,r,rp,chk,chkc)
```

### Ekto Enneacraft - "tromarIA" (`29570824`)

Source: [Scripts/c29570824.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c29570824.lua)

```lua
function s.distg(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return true end
	local g=Duel.GetMatchingGroup(aux.NegateEffectMonsterFilter,tp,0,LOCATION_MZONE,nil)
	if g:GetCount()>0 then
		Duel.SetOperationInfo(0,CATEGORY_DISABLE,g,1,0,0)
```
