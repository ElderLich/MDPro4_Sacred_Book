# Effect.IsHasProperty

## Signature

```lua
Effect.IsHasProperty(Effect e, int prop1, [int prop2]) -> bool
```

## Description

Checks whether e contains the requested effect property flags.
prop1 is checked against the first property word and optional prop2 against the second property word. Passing 0 for a word makes that word pass.

## Parameters

- `e` `Effect`
- `prop1` `int`
- `prop2` `int` optional

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libeffect.cpp:650`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **187** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Effect.IsHasProperty`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Enneacraft - Asta.PIXEA](/examples/cards/28454232) | `28454232` | [Scripts/c28454232.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c28454232.lua) | 64 |
| Red-Eyes Slash Dragon | `21140872` | [Scripts/c21140872.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c21140872.lua) | 60 |
| Frightfur March | `74416026` | [Scripts/c74416026.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74416026.lua) | 58 |
| Ursarctic Grand Chariot | `80086070` | [Scripts/c80086070.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c80086070.lua) | 57 |
| Arcana Force EX - The Light Ruler | `5861892` | [Scripts/c5861892.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c5861892.lua) | 55 |
| Gilti-Gearfried the Magical Steel Knight | `49161188` | [Scripts/c49161188.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c49161188.lua) | 51 |
| VARefar, the Judge of Ball | `19743887` | [Scripts/c19743887.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c19743887.lua) | 50 |
| Arcana Extra Joker | `64454614` | [Scripts/c64454614.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c64454614.lua) | 50 |
| Machina Fortress | `5556499` | [Scripts/c5556499.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c5556499.lua) | 50 |
| Naturia White Oak | `24644634` | [Scripts/c24644634.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24644634.lua) | 50 |
| Dinomist Rex | `63251695` | [Scripts/c63251695.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63251695.lua) | 49 |
| Majestic Star Dragon | `7841112` | [Scripts/c7841112.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c7841112.lua) | 49 |
| Mystic Box of Chaos | `75983808` | [Scripts/c75983808.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c75983808.lua) | 49 |
| Shooting Star Dragon T.G. EX | `63180841` | [Scripts/c63180841.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63180841.lua) | 49 |
| Rokket Barrage | `53481938` | [Scripts/c53481938.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c53481938.lua) | 48 |
| Parasite Paranoid | `14457896` | [Scripts/c14457896.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c14457896.lua) | 48 |
| Flash Charge Dragon | `95372220` | [Scripts/c95372220.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c95372220.lua) | 47 |
| Dyna Tank | `75780818` | [Scripts/c75780818.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c75780818.lua) | 46 |
| Rubysapphirus, the Adamant Jewel | `6906306` | [Scripts/c6906306.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c6906306.lua) | 46 |
| R.B. Last Stand | `43450363` | [Scripts/c43450363.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c43450363.lua) | 46 |
| Underworld Goddess of the Closed World | `98127546` | [Scripts/c98127546.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c98127546.lua) | 46 |
| Dragon's Light and Darkness | `63295720` | [Scripts/c63295720.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63295720.lua) | 46 |
| Number 99: Utopic Dragon | `51543904` | [Scripts/c51543904.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c51543904.lua) | 45 |
| Hollowrokket Dragon | `51548207` | [Scripts/c51548207.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c51548207.lua) | 45 |
| ...and 163 more |  |  |  |

## Script Examples

### Enneacraft - Asta.PIXEA (`28454232`)

Source: [Scripts/c28454232.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c28454232.lua)

```lua
	local c=e:GetHandler()
	if c:IsStatus(STATUS_BATTLE_DESTROYED) then return false end
	if not re:IsHasProperty(EFFECT_FLAG_CARD_TARGET) then return false end
	local tg=Duel.GetChainInfo(ev,CHAININFO_TARGET_CARDS)
	return Duel.IsChainDisablable(ev) and tg and tg:IsExists(s.ccfilter,1,nil,tp) and ep~=tp and e:GetHandler():IsFacedown()
```

### Red-Eyes Slash Dragon (`21140872`)

Source: [Scripts/c21140872.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c21140872.lua)

```lua
end
function c21140872.ngcon(e,tp,eg,ep,ev,re,r,rp)
	if not re:IsHasProperty(EFFECT_FLAG_CARD_TARGET) then return false end
	local g=Duel.GetChainInfo(ev,CHAININFO_TARGET_CARDS)
	return g and g:IsExists(c21140872.ngcfilter,1,nil,tp) and Duel.IsChainNegatable(ev)
```

### Frightfur March (`74416026`)

Source: [Scripts/c74416026.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74416026.lua)

```lua
end
function c74416026.condition(e,tp,eg,ep,ev,re,r,rp)
	if rp==tp or not re:IsHasProperty(EFFECT_FLAG_CARD_TARGET) then return false end
	local g=Duel.GetChainInfo(ev,CHAININFO_TARGET_CARDS)
	return g and g:IsExists(c74416026.filter,1,nil,tp)
```
