# Duel.IsChainDisablable

## Signature

```lua
Duel.IsChainDisablable(int chainc) -> bool
```

## Description

Checks whether chainc's effect can be negated.
While a Chain is resolving, this asks the core whether that Chain link can currently be disabled; outside Chain resolution it returns true.

## Related Functions

- [Duel.NegateEffect](/api/functions/Duel/NegateEffect)
- [Duel.IsChainDisabled](/api/functions/Duel/IsChainDisabled)
- [Duel.GetChainInfo](/api/functions/Duel/GetChainInfo)

## Parameters

- `chainc` `int`

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5062`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **166** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Duel.IsChainDisablable) with `Duel.IsChainDisablable`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Enneacraft - Asta.PIXEA](/examples/cards/28454232) | `28454232` | [Scripts/c28454232.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c28454232.lua) | 1 |
| [W:P Fancy Ball](/examples/cards/4993187) | `4993187` | [Scripts/c4993187.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c4993187.lua) | 1 |
| Nervedo the Shadebeast Power Patron | `17473466` | [Scripts/c17473466.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c17473466.lua) | 1 |
| Number 38: Hope Harbinger Dragon Titanic Galaxy | `63767246` | [Scripts/c63767246.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c63767246.lua) | 1 |
| Shimmering Shatterer of the Sacred Beasts | `3441553` | [Scripts/c3441553.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c3441553.lua) | 2 |
| Tensei Ryu-Ge Anva | `56322832` | [Scripts/c56322832.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c56322832.lua) | 1 |
| Gilti-Gearfried the Magical Steel Knight | `49161188` | [Scripts/c49161188.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c49161188.lua) | 1 |
| Solfachord Solfegia | `84693918` | [Scripts/c84693918.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c84693918.lua) | 1 |
| Horoscope Sorcerer, the Stargazer Magician | `1186447` | [Scripts/c1186447.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c1186447.lua) | 1 |
| Odd-Eyes Pendulumgraph Dragon | `66425726` | [Scripts/c66425726.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c66425726.lua) | 1 |
| Dinomist Rex | `63251695` | [Scripts/c63251695.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c63251695.lua) | 1 |
| Stardust Dragon - Victim Sanctuary | `76636978` | [Scripts/c76636978.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c76636978.lua) | 1 |
| Arrow of Regulus | `60439482` | [Scripts/c60439482.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c60439482.lua) | 1 |
| Volcanic Inferno | `84138874` | [Scripts/c84138874.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c84138874.lua) | 1 |
| Dragunity Lord - Georgius | `70522875` | [Scripts/c70522875.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c70522875.lua) | 1 |
| Rindbrumm the Striking Dragon | `51409648` | [Scripts/c51409648.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c51409648.lua) | 1 |
| Imposter Shift | `89027418` | [Scripts/c89027418.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c89027418.lua) | 1 |
| Stardust Sifr Divine Dragon | `26268488` | [Scripts/c26268488.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c26268488.lua) | 1 |
| Marincess Aqua Argonaut | `20934852` | [Scripts/c20934852.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c20934852.lua) | 1 |
| Rubysapphirus, the Adamant Jewel | `6906306` | [Scripts/c6906306.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c6906306.lua) | 1 |
| Dragon's Light and Darkness | `63295720` | [Scripts/c63295720.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c63295720.lua) | 1 |
| Master Peace, the True Dracoverlord | `12800564` | [Scripts/c12800564.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c12800564.lua) | 1 |
| Odd-Eyes Override Dragon | `58083496` | [Scripts/c58083496.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c58083496.lua) | 1 |
| Mystical Elf - White Lightning | `15613529` | [Scripts/c15613529.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c15613529.lua) | 1 |
| ...and 142 more |  |  |  |

## Script Examples

### Enneacraft - Asta.PIXEA (`28454232`)

Source: [Scripts/c28454232.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c28454232.lua)

```lua
	if not re:IsHasProperty(EFFECT_FLAG_CARD_TARGET) then return false end
	local tg=Duel.GetChainInfo(ev,CHAININFO_TARGET_CARDS)
	return Duel.IsChainDisablable(ev) and tg and tg:IsExists(s.ccfilter,1,nil,tp) and ep~=tp and e:GetHandler():IsFacedown()
end
function s.discost(e,tp,eg,ep,ev,re,r,rp,chk)
```

### W:P Fancy Ball (`4993187`)

Source: [Scripts/c4993187.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c4993187.lua)

```lua
	local loc=Duel.GetChainInfo(ev,CHAININFO_TRIGGERING_LOCATION)
	return ep~=tp and (LOCATION_ONFIELD+LOCATION_GRAVE)&loc~=0
		and re:IsActiveType(TYPE_MONSTER) and Duel.IsChainDisablable(ev)
end
function s.discost(e,tp,eg,ep,ev,re,r,rp,chk)
```

### Nervedo the Shadebeast Power Patron (`17473466`)

Source: [Scripts/c17473466.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c17473466.lua)

```lua
		and re:IsActiveType(TYPE_MONSTER)
		and Duel.GetFlagEffect(tp,id)==0
		and Duel.IsChainDisablable(ev) and not Duel.IsChainDisabled(ev)
end
function s.negop(e,tp,eg,ep,ev,re,r,rp)
```
