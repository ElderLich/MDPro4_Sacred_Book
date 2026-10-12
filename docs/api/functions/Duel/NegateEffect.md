# Duel.NegateEffect

## Signature

```lua
Duel.NegateEffect(int chainc, [bool forced]) -> bool
```

## Description

Attempts to negate the effect of a Chain Link without necessarily negating its activation, and returns true if the effect was successfully negated.
Use this for text such as "negate that effect". The optional forced argument requests a forced disable.
Use Duel.NegateActivation for activation negation and Duel.NegateSummon for Summon negation; those are different game events.

## How To Use It

Use this during resolution for effects that negate the effect of a Chain Link without treating the activation as negated.

```lua
if Duel.NegateEffect(ev) then
    -- follow-up that requires the effect to be negated
end
```

The optional `forced` argument is passed to the core disable-chain check. Activation-negation cards should usually use `Duel.NegateActivation` instead.

## Related Functions

- [Duel.IsChainDisablable](/api/functions/Duel/IsChainDisablable)
- [Duel.NegateActivation](/api/functions/Duel/NegateActivation)
- [Duel.GetChainInfo](/api/functions/Duel/GetChainInfo)

## Parameters

- `chainc` `int` - Chain Link number whose effect should be negated.
- `forced` `bool` optional - Optional forced-disable request.

## Returns

- `bool` - true if the Chain Link's effect was negated; false if it cannot be negated or the negation fails.

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4930`

## Guided Examples

Learn how to use this function in context:

- [Chain Timing And Activation Windows](/learn/chain-timing-and-activation-windows)
- [Common Script Errors And Debugging](/learn/common-script-errors-and-debugging)
- [Counter Traps](/learn/counter-traps)
- [Negation And Immunity](/learn/negation-and-immunity)

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **272** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Duel.NegateEffect) with `Duel.NegateEffect`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Enneacraft - Asta.PIXEA](/examples/cards/28454232) | `28454232` | [Scripts/c28454232.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c28454232.lua) | 1 |
| [W:P Fancy Ball](/examples/cards/4993187) | `4993187` | [Scripts/c4993187.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c4993187.lua) | 1 |
| Awakening of the Sacred Beasts | `53701259` | [Scripts/c53701259.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c53701259.lua) | 1 |
| Zoroa, the Magistus Verethragna | `37260677` | [Scripts/c37260677.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c37260677.lua) | 1 |
| Nervedo the Shadebeast Power Patron | `17473466` | [Scripts/c17473466.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c17473466.lua) | 1 |
| Beyond the Pendulum | `22125101` | [Scripts/c22125101.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c22125101.lua) | 1 |
| Number 38: Hope Harbinger Dragon Titanic Galaxy | `63767246` | [Scripts/c63767246.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c63767246.lua) | 1 |
| Shimmering Shatterer of the Sacred Beasts | `3441553` | [Scripts/c3441553.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c3441553.lua) | 1 |
| Supply Soldier of the Indestructible Insects | `23738096` | [Scripts/c23738096.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c23738096.lua) | 1 |
| Millennium-Eyes Restrict | `41578483` | [Scripts/c41578483.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c41578483.lua) | 1 |
| Tensei Ryu-Ge Anva | `56322832` | [Scripts/c56322832.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c56322832.lua) | 1 |
| Gilti-Gearfried the Magical Steel Knight | `49161188` | [Scripts/c49161188.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c49161188.lua) | 1 |
| Mind Scan | `34298391` | [Scripts/c34298391.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c34298391.lua) | 1 |
| D/D/D Duo-Dawn King Kali Yuga | `15939229` | [Scripts/c15939229.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c15939229.lua) | 1 |
| Solfachord Solfegia | `84693918` | [Scripts/c84693918.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c84693918.lua) | 1 |
| Horoscope Sorcerer, the Stargazer Magician | `1186447` | [Scripts/c1186447.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c1186447.lua) | 1 |
| Odd-Eyes Pendulumgraph Dragon | `66425726` | [Scripts/c66425726.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c66425726.lua) | 1 |
| Dinomist Rex | `63251695` | [Scripts/c63251695.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c63251695.lua) | 1 |
| Cubic Mandala | `8837932` | [Scripts/c8837932.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c8837932.lua) | 1 |
| Arrow of Regulus | `60439482` | [Scripts/c60439482.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c60439482.lua) | 1 |
| PenduLuMoon | `66150724` | [Scripts/c66150724.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c66150724.lua) | 1 |
| Penguin Sword | `69792699` | [Scripts/c69792699.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c69792699.lua) | 1 |
| Parasite Paranoid | `14457896` | [Scripts/c14457896.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c14457896.lua) | 1 |
| Volcanic Inferno | `84138874` | [Scripts/c84138874.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c84138874.lua) | 1 |
| ...and 248 more |  |  |  |

## Script Examples

### Enneacraft - Asta.PIXEA (`28454232`)

Source: [Scripts/c28454232.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c28454232.lua)

```lua
end
function s.disop(e,tp,eg,ep,ev,re,r,rp)
	if Duel.NegateEffect(ev)
		and Duel.IsExistingMatchingCard(Card.IsAbleToRemove,tp,0,LOCATION_HAND,1,nil,POS_FACEDOWN)
		and Duel.SelectYesNo(tp,aux.Stringid(id,3)) then
```

### W:P Fancy Ball (`4993187`)

Source: [Scripts/c4993187.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c4993187.lua)

```lua
end
function s.disop(e,tp,eg,ep,ev,re,r,rp)
	if Duel.NegateEffect(ev) and re:GetHandler():IsRelateToChain(ev) then
		Duel.Remove(eg,POS_FACEUP,REASON_EFFECT)
	end
```

### Awakening of the Sacred Beasts (`53701259`)

Source: [Scripts/c53701259.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c53701259.lua)

```lua
end
function c53701259.disop(e,tp,eg,ep,ev,re,r,rp)
	Duel.NegateEffect(ev)
end
function c53701259.rmtg(e,c)
```
