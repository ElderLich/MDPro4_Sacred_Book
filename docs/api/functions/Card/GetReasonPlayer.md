# Card.GetReasonPlayer

## Signature

```lua
Card.GetReasonPlayer(Card c) -> int
```

## Description

Returns c's current reason player, the player recorded in c's current reason state.

## Parameters

- `c` `Card`

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3461`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **167** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.GetReasonPlayer`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Flowering Etoile the Melodious Magnificat | `83793721` | [Scripts/c83793721.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c83793721.lua) | 60 |
| Gravity Balance | `37930737` | [Scripts/c37930737.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c37930737.lua) | 60 |
| Cyberse Reminder | `56337500` | [Scripts/c56337500.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c56337500.lua) | 58 |
| Dragon Master Magia | `12381100` | [Scripts/c12381100.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c12381100.lua) | 57 |
| Gunkan Sushipyard Seaside Supper Spot | `62200831` | [Scripts/c62200831.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c62200831.lua) | 54 |
| Synchro Panic | `83962752` | [Scripts/c83962752.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c83962752.lua) | 54 |
| Neo Super Quantal Mech King Blaster Magna | `95493471` | [Scripts/c95493471.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c95493471.lua) | 53 |
| World Legacy Collapse | `36197902` | [Scripts/c36197902.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c36197902.lua) | 53 |
| Zefra Metaltron | `85216896` | [Scripts/c85216896.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c85216896.lua) | 52 |
| Pendulum Witch | `43502497` | [Scripts/c43502497.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c43502497.lua) | 51 |
| Dream Tower of Princess Nemleria | `18458255` | [Scripts/c18458255.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c18458255.lua) | 51 |
| Ultimate Crystal Magic | `36328300` | [Scripts/c36328300.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c36328300.lua) | 51 |
| X-Krawler Qualiark | `92781606` | [Scripts/c92781606.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92781606.lua) | 51 |
| Icejade Erosion | `53742162` | [Scripts/c53742162.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c53742162.lua) | 51 |
| Loris, Lady of Lament | `50699850` | [Scripts/c50699850.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c50699850.lua) | 51 |
| Stardust Warrior | `74892653` | [Scripts/c74892653.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74892653.lua) | 50 |
| Hidden Village of Ninjitsu Arts | `26232916` | [Scripts/c26232916.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c26232916.lua) | 50 |
| Red-Eyes Retro Dragon | `53485634` | [Scripts/c53485634.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c53485634.lua) | 50 |
| Icejade Gymir Aegirine | `86682165` | [Scripts/c86682165.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c86682165.lua) | 49 |
| Mirrorjade the Iceblade Dragon | `44146295` | [Scripts/c44146295.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44146295.lua) | 49 |
| Galactikuriboh | `46261704` | [Scripts/c46261704.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c46261704.lua) | 49 |
| Chronomaly Acambaro Figures | `24506253` | [Scripts/c24506253.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24506253.lua) | 49 |
| Rayrage, the Twilight Fiend | `71222649` | [Scripts/c71222649.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71222649.lua) | 47 |
| Lancea, Ancestral Dragon of the Ice Mountain | `96402918` | [Scripts/c96402918.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c96402918.lua) | 47 |
| ...and 143 more |  |  |  |

## Script Examples

### Flowering Etoile the Melodious Magnificat (`83793721`)

Source: [Scripts/c83793721.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c83793721.lua)

```lua
	local c=e:GetHandler()
	return c:IsPreviousPosition(POS_FACEUP) and c:IsSummonType(SUMMON_TYPE_FUSION) and c:IsPreviousLocation(LOCATION_MZONE)
		and c:IsPreviousControler(tp) and c:GetReasonPlayer()==1-tp
end
function s.spfilter(c,e,tp)
```

### Gravity Balance (`37930737`)

Source: [Scripts/c37930737.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c37930737.lua)

```lua
function c37930737.repfilter(c,tp)
	return c:IsFaceup() and c:IsLocation(LOCATION_MZONE) and c:IsControler(tp) and c:IsSetCard(0x186)
		and (c:IsReason(REASON_BATTLE) or (c:IsReason(REASON_EFFECT) and c:GetReasonPlayer()==1-tp)) and not c:IsReason(REASON_REPLACE)
end
function c37930737.reptg(e,tp,eg,ep,ev,re,r,rp,chk)
```

### Cyberse Reminder (`56337500`)

Source: [Scripts/c56337500.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c56337500.lua)

```lua
function c56337500.spcon(e,tp,eg,ep,ev,re,r,rp)
	local c=e:GetHandler()
	return (c:IsReason(REASON_BATTLE) or (c:IsReason(REASON_EFFECT) and c:GetReasonPlayer()==1-tp and c:IsPreviousControler(tp)))
		and c:IsPreviousLocation(LOCATION_MZONE) and c:IsSummonType(SUMMON_TYPE_XYZ)
end
```
