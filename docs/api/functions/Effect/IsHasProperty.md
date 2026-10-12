# Effect.IsHasProperty

## Signature

```lua
Effect.IsHasProperty(Effect e, int prop1, [int prop2]) -> bool
```

## Description

Checks whether e contains the requested effect property flags.
prop1 is checked against the first property word and optional prop2 against the second property word. Passing 0 for a word makes that word pass.

## Parameters

- `e` `Effect` - Effect whose property words are checked.
- `prop1` `int` - Mask checked against the first property word. Use 0 to ignore this word.
- `prop2` `int` optional - Mask checked against the second property word. Omitted or 0 means this word passes.

## Returns

- `bool` - True when every nonzero requested property mask is present on e.

## Source

- `D:\Programs\GitHub\ygopro-core\libeffect.cpp:650`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **190** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Effect.IsHasProperty) with `Effect.IsHasProperty`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Levia-Dragoon - Daedalus](/examples/cards/78579058) | `78579058` | [Scripts/c78579058.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c78579058.lua) | 1 |
| [Azure Ocean Dragon Lord - Neo-Daedalus Rage](/examples/cards/41570943) | `41570943` | [Scripts/c41570943.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c41570943.lua) | 1 |
| [Enneacraft - Asta.PIXEA](/examples/cards/28454232) | `28454232` | [Scripts/c28454232.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c28454232.lua) | 1 |
| Red-Eyes Slash Dragon | `21140872` | [Scripts/c21140872.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c21140872.lua) | 1 |
| Frightfur March | `74416026` | [Scripts/c74416026.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c74416026.lua) | 1 |
| Ursarctic Grand Chariot | `80086070` | [Scripts/c80086070.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c80086070.lua) | 1 |
| Arcana Force EX - The Light Ruler | `5861892` | [Scripts/c5861892.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c5861892.lua) | 1 |
| Gilti-Gearfried the Magical Steel Knight | `49161188` | [Scripts/c49161188.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c49161188.lua) | 1 |
| VARefar, the Judge of Ball | `19743887` | [Scripts/c19743887.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c19743887.lua) | 1 |
| Arcana Extra Joker | `64454614` | [Scripts/c64454614.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c64454614.lua) | 1 |
| Machina Fortress | `5556499` | [Scripts/c5556499.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c5556499.lua) | 1 |
| Naturia White Oak | `24644634` | [Scripts/c24644634.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c24644634.lua) | 1 |
| Dinomist Rex | `63251695` | [Scripts/c63251695.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c63251695.lua) | 1 |
| Majestic Star Dragon | `7841112` | [Scripts/c7841112.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c7841112.lua) | 2 |
| Chaos Mystic Box | `75983808` | [Scripts/c75983808.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c75983808.lua) | 1 |
| Shooting Star Dragon T.G. EX | `63180841` | [Scripts/c63180841.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c63180841.lua) | 1 |
| Rokket Barrage | `53481938` | [Scripts/c53481938.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c53481938.lua) | 1 |
| Parasite Paranoid | `14457896` | [Scripts/c14457896.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c14457896.lua) | 1 |
| Imposter Shift | `89027418` | [Scripts/c89027418.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c89027418.lua) | 1 |
| Flash Charge Dragon | `95372220` | [Scripts/c95372220.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c95372220.lua) | 1 |
| Dyna Tank | `75780818` | [Scripts/c75780818.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c75780818.lua) | 1 |
| Rubysapphirus, the Adamant Jewel | `6906306` | [Scripts/c6906306.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c6906306.lua) | 1 |
| R.B. Last Stand | `43450363` | [Scripts/c43450363.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c43450363.lua) | 1 |
| Underworld Goddess of the Closed World | `98127546` | [Scripts/c98127546.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c98127546.lua) | 1 |
| ...and 166 more |  |  |  |

## Script Examples

### Levia-Dragoon - Daedalus (`78579058`)

Source: [Scripts/c78579058.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c78579058.lua)

```lua
end
function s.LConditionFilter(c,f,lc,e)
	return (c:IsFaceup() or not c:IsOnField() or e:IsHasProperty(EFFECT_FLAG_SET_AVAILABLE))
		and c:IsCanBeLinkMaterial(lc) and (not f or f(c))
end
```

### Azure Ocean Dragon Lord - Neo-Daedalus Rage (`41570943`)

Source: [Scripts/c41570943.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c41570943.lua)

```lua
end
function s.LConditionFilter(c,f,lc,e)
	return (c:IsFaceup() or not c:IsOnField() or e:IsHasProperty(EFFECT_FLAG_SET_AVAILABLE))
		and c:IsCanBeLinkMaterial(lc) and (not f or f(c))
end
```

### Enneacraft - Asta.PIXEA (`28454232`)

Source: [Scripts/c28454232.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c28454232.lua)

```lua
	local c=e:GetHandler()
	if c:IsStatus(STATUS_BATTLE_DESTROYED) then return false end
	if not re:IsHasProperty(EFFECT_FLAG_CARD_TARGET) then return false end
	local tg=Duel.GetChainInfo(ev,CHAININFO_TARGET_CARDS)
	return Duel.IsChainDisablable(ev) and tg and tg:IsExists(s.ccfilter,1,nil,tp) and ep~=tp and e:GetHandler():IsFacedown()
```
