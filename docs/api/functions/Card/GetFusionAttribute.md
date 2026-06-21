# Card.GetFusionAttribute

## Signature

```lua
Card.GetFusionAttribute(Card c, [int player]) -> int
```

## Description

Return the Attribute of card c when used as Fusion Material \[for a Fusion Summon by player\]

## Parameters

- `c` `Card`
- `player` `int` optional

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3433`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **17** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.GetFusionAttribute`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Lady's Dragonmaid](/examples/cards/48658295) | `48658295` | [Scripts/c48658295.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c48658295.lua) | 75 |
| [El Shaddoll Apkallone](/examples/cards/50907446) | `50907446` | [Scripts/c50907446.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c50907446.lua) | 68 |
| [Favorite HERO Flame Wingman](/examples/cards/13243124) | `13243124` | [Scripts/c13243124.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c13243124.lua) | 66 |
| Gilti-Gearfried the Magical Steel Knight | `49161188` | [Scripts/c49161188.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c49161188.lua) | 51 |
| Fata Dragna | `41763141` | [Scripts/c41763141.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c41763141.lua) | 51 |
| Elemental HERO Sunrise | `22908820` | [Scripts/c22908820.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c22908820.lua) | 48 |
| Elemental HERO Flame Wingman - Infernal Rage | `93347961` | [Scripts/c93347961.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93347961.lua) | 47 |
| Elemental HERO Thunder Giant - Voltic Thunder | `19222426` | [Scripts/c19222426.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c19222426.lua) | 47 |
| Clown Crew Diabolo | `31533473` | [Scripts/c31533473.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c31533473.lua) | 47 |
| Myutant Synthesis | `79194594` | [Scripts/c79194594.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c79194594.lua) | 45 |
| Secret Six Samurai - Rihan | `33964637` | [Scripts/c33964637.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c33964637.lua) | 43 |
| Aerial Eater | `28143384` | [Scripts/c28143384.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c28143384.lua) | 43 |
| Oneiros, the Dream Mirror Erlking | `35187185` | [Scripts/c35187185.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c35187185.lua) | 41 |
| Oneiros, the Dream Mirror Tormentor | `37678339` | [Scripts/c37678339.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c37678339.lua) | 36 |
| Elemental HERO Cosmo Neos | `90050480` | [Scripts/c90050480.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c90050480.lua) | 35 |
| Mudragon of the Swamp | `54757758` | [Scripts/c54757758.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c54757758.lua) | 32 |
| Garura, Wings of Resonant Life | `11765832` | [Scripts/c11765832.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c11765832.lua) | 30 |

## Script Examples

### Lady's Dragonmaid (`48658295`)

Source: [Scripts/c48658295.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c48658295.lua)

```lua
	if not sg then return true end
	return not sg:IsExists(Card.IsLevel,1,c,c:GetLevel())
		and sg:IsExists(Card.IsFusionAttribute,1,c,c:GetFusionAttribute())
end
function s.splimit(e,se,sp,st)
```

### El Shaddoll Apkallone (`50907446`)

Source: [Scripts/c50907446.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c50907446.lua)

```lua
end
function c50907446.FShaddollFilter1(c,g)
	return c:IsFusionSetCard(0x9d) and g:IsExists(c50907446.FShaddollFilter2,1,c) and not g:IsExists(Card.IsFusionAttribute,1,c,c:GetFusionAttribute())
end
function c50907446.FShaddollFilter2(c)
```

### Favorite HERO Flame Wingman (`13243124`)

Source: [Scripts/c13243124.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c13243124.lua)

```lua
	return not sg or sg:FilterCount(aux.TRUE,c)==0
		or (sg:IsExists(Card.IsRace,1,c,c:GetRace())
			and not sg:IsExists(Card.IsFusionAttribute,1,c,c:GetFusionAttribute()))
end
function s.atkcon(e,tp,eg,ep,ev,re,r,rp)
```
