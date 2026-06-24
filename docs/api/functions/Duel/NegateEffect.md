# Duel.NegateEffect

## Signature

```lua
Duel.NegateEffect(int chainc, [bool forced]) -> bool
```

## Description

Attempts to negate the effect of a Chain Link without necessarily negating its activation, and returns true if the effect was successfully negated.
Use this for text such as "negate that effect". The optional forced argument requests a forced disable.

## Parameters

- `chainc` `int` - Chain Link number whose effect should be negated.
- `forced` `bool` optional - Optional forced-disable request.

## Returns

- `bool` - true if the Chain Link's effect was negated; false if it cannot be negated or the negation fails.

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4930`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **261** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Duel.NegateEffect`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Enneacraft - Asta.PIXEA](/examples/cards/28454232) | `28454232` | [Scripts/c28454232.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c28454232.lua) | 64 |
| [W:P Fancy Ball](/examples/cards/4993187) | `4993187` | [Scripts/c4993187.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c4993187.lua) | 61 |
| Awakening of the Sacred Beasts | `53701259` | [Scripts/c53701259.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c53701259.lua) | 57 |
| Zoroa, the Magistus Verethragna | `37260677` | [Scripts/c37260677.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c37260677.lua) | 57 |
| Nervedo the Shadebeast Power Patron | `17473466` | [Scripts/c17473466.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c17473466.lua) | 56 |
| Beyond the Pendulum | `22125101` | [Scripts/c22125101.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c22125101.lua) | 56 |
| Number 38: Hope Harbinger Dragon Titanic Galaxy | `63767246` | [Scripts/c63767246.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63767246.lua) | 56 |
| Supply Soldier of the Indestructible Insects | `23738096` | [Scripts/c23738096.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c23738096.lua) | 53 |
| Millennium-Eyes Restrict | `41578483` | [Scripts/c41578483.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c41578483.lua) | 53 |
| Tensei Ryu-Ge Anva | `56322832` | [Scripts/c56322832.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c56322832.lua) | 52 |
| Gilti-Gearfried the Magical Steel Knight | `49161188` | [Scripts/c49161188.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c49161188.lua) | 51 |
| Mind Scan | `34298391` | [Scripts/c34298391.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c34298391.lua) | 51 |
| D/D/D Duo-Dawn King Kali Yuga | `15939229` | [Scripts/c15939229.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c15939229.lua) | 51 |
| Solfachord Solfegia | `84693918` | [Scripts/c84693918.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c84693918.lua) | 50 |
| Horoscope Sorcerer, the Stargazer Magician | `1186447` | [Scripts/c1186447.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c1186447.lua) | 49 |
| Odd-Eyes Pendulumgraph Dragon | `66425726` | [Scripts/c66425726.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c66425726.lua) | 49 |
| Dinomist Rex | `63251695` | [Scripts/c63251695.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63251695.lua) | 49 |
| Cubic Mandala | `8837932` | [Scripts/c8837932.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c8837932.lua) | 49 |
| Arrow of Regulus | `60439482` | [Scripts/c60439482.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c60439482.lua) | 49 |
| PenduLuMoon | `66150724` | [Scripts/c66150724.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c66150724.lua) | 48 |
| Penguin Sword | `69792699` | [Scripts/c69792699.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c69792699.lua) | 48 |
| Parasite Paranoid | `14457896` | [Scripts/c14457896.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c14457896.lua) | 48 |
| Volcanic Inferno | `84138874` | [Scripts/c84138874.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c84138874.lua) | 48 |
| Update Jammer | `88093706` | [Scripts/c88093706.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c88093706.lua) | 47 |
| ...and 237 more |  |  |  |

## Script Examples

### Enneacraft - Asta.PIXEA (`28454232`)

Source: [Scripts/c28454232.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c28454232.lua)

```lua
end
function s.disop(e,tp,eg,ep,ev,re,r,rp)
	if Duel.NegateEffect(ev)
		and Duel.IsExistingMatchingCard(Card.IsAbleToRemove,tp,0,LOCATION_HAND,1,nil,POS_FACEDOWN)
		and Duel.SelectYesNo(tp,aux.Stringid(id,3)) then
```

### W:P Fancy Ball (`4993187`)

Source: [Scripts/c4993187.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c4993187.lua)

```lua
end
function s.disop(e,tp,eg,ep,ev,re,r,rp)
	if Duel.NegateEffect(ev) and re:GetHandler():IsRelateToChain(ev) then
		Duel.Remove(eg,POS_FACEUP,REASON_EFFECT)
	end
```

### Awakening of the Sacred Beasts (`53701259`)

Source: [Scripts/c53701259.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c53701259.lua)

```lua
end
function c53701259.disop(e,tp,eg,ep,ev,re,r,rp)
	Duel.NegateEffect(ev)
end
function c53701259.rmtg(e,c)
```
