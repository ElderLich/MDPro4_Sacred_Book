# Duel.IsChainNegatable

## Signature

```lua
Duel.IsChainNegatable(int chainc) -> bool
```

## Description

Compatibility check for whether chainc's activation can be negated.
In this MDPro3 core binding, the function currently returns true for any chain count.
Local scripts still call it in negation conditions so the script expresses the intended activation-legality check.
Use it with Duel.NegateActivation, not as a substitute for effect-negation checks such as Duel.IsChainDisablable.

## How To Use It

Use this in activation-negation conditions to express that the responding effect only works on a Chain Link whose activation can be negated.

```lua
return Duel.IsChainNegatable(ev)
```

In the current MDPro3 core binding this function returns true for any chain count, but local scripts still use it as the activation-negation legality marker. Use `Duel.IsChainDisablable` when the operation is effect negation rather than activation negation.

## Related Functions

- [Duel.NegateActivation](/api/functions/Duel/NegateActivation)
- [Duel.GetCurrentChain](/api/functions/Duel/GetCurrentChain)
- [Duel.IsChainDisablable](/api/functions/Duel/IsChainDisablable)

## Parameters

- `chainc` `int` - Chain Link number to test, commonly the ev argument in an EVENT_CHAINING condition.

## Returns

- `bool` - true when this binding considers that Chain Link's activation negatable.

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5061`

## Guided Examples

Learn how to use this function in context:

- [Activated Effects](/learn/activated-effects)
- [Activation Legality](/learn/activation-legality)
- [Chain Timing And Activation Windows](/learn/chain-timing-and-activation-windows)
- [Counter Traps](/learn/counter-traps)
- [Negation And Immunity](/learn/negation-and-immunity)
- [Trap Card Patterns](/learn/trap-card-patterns)

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **385** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Duel.IsChainNegatable) with `Duel.IsChainNegatable`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Enneacraft - Archa.TAIL](/examples/cards/81237046) | `81237046` | [Scripts/c81237046.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c81237046.lua) | 1 |
| [Enneacraft - Atil.SPIA](/examples/cards/71801447) | `71801447` | [Scripts/c71801447.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71801447.lua) | 2 |
| [Shooting Majestic Star Dragon](/examples/cards/40939228) | `40939228` | [Scripts/c40939228.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c40939228.lua) | 1 |
| Red-Eyes Slash Dragon | `21140872` | [Scripts/c21140872.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c21140872.lua) | 1 |
| A-to-Z-Dragon Buster Cannon | `65172015` | [Scripts/c65172015.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c65172015.lua) | 1 |
| Frightfur March | `74416026` | [Scripts/c74416026.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74416026.lua) | 1 |
| Dragon Master Magia | `12381100` | [Scripts/c12381100.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c12381100.lua) | 1 |
| Ursarctic Grand Chariot | `80086070` | [Scripts/c80086070.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c80086070.lua) | 1 |
| Endymion, the Mighty Master of Magic | `3611830` | [Scripts/c3611830.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c3611830.lua) | 1 |
| Arms of Genex Return Zero | `61775475` | [Scripts/c61775475.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c61775475.lua) | 1 |
| Emperor Charles the Great | `97864322` | [Scripts/c97864322.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c97864322.lua) | 1 |
| Toadally Awesome | `90809975` | [Scripts/c90809975.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c90809975.lua) | 1 |
| All-Eyes Phantom Dragon | `70335319` | [Scripts/c70335319.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c70335319.lua) | 1 |
| Drytron Meteonis DA Draconids | `56863746` | [Scripts/c56863746.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c56863746.lua) | 1 |
| Machina Ruinforce | `46033517` | [Scripts/c46033517.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c46033517.lua) | 1 |
| Loki, Lord of the Aesir | `67098114` | [Scripts/c67098114.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c67098114.lua) | 1 |
| Fire King Avatar Arvata | `18621798` | [Scripts/c18621798.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c18621798.lua) | 1 |
| Immortal Phoenix Gearfried | `22091647` | [Scripts/c22091647.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c22091647.lua) | 1 |
| PSY-Framegear Gamma | `38814750` | [Scripts/c38814750.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c38814750.lua) | 1 |
| PSY-Framegear Delta | `74203495` | [Scripts/c74203495.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74203495.lua) | 1 |
| PSY-Framegear Epsilon | `1697104` | [Scripts/c1697104.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c1697104.lua) | 1 |
| Red-Eyes Dark Dragoon | `37818794` | [Scripts/c37818794.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c37818794.lua) | 1 |
| Whisker Blitzclique | `85523502` | [Scripts/c85523502.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c85523502.lua) | 1 |
| Eclipse, Dragon Ruler of Catastrophes | `30350202` | [Scripts/c30350202.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30350202.lua) | 1 |
| ...and 361 more |  |  |  |

## Script Examples

### Enneacraft - Archa.TAIL (`81237046`)

Source: [Scripts/c81237046.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c81237046.lua)

```lua
end
function s.indcon(e,tp,eg,ep,ev,re,r,rp)
	if e:GetHandler():IsStatus(STATUS_BATTLE_DESTROYED) or not Duel.IsChainNegatable(ev) then return false end
	if re:IsHasCategory(CATEGORY_NEGATE)
		and Duel.GetChainInfo(ev-1,CHAININFO_TRIGGERING_EFFECT):IsHasType(EFFECT_TYPE_ACTIVATE) then return false end
```

### Enneacraft - Atil.SPIA (`71801447`)

Source: [Scripts/c71801447.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71801447.lua)

```lua
	for i=1,ev do
		local tgp=Duel.GetChainInfo(i,CHAININFO_TRIGGERING_PLAYER)
		if tgp~=tp and Duel.IsChainNegatable(i) then
			return Duel.GetCurrentChain()>2
		end
```

### Shooting Majestic Star Dragon (`40939228`)

Source: [Scripts/c40939228.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c40939228.lua)

```lua
end
function c40939228.negcon(e,tp,eg,ep,ev,re,r,rp)
	return not e:GetHandler():IsStatus(STATUS_BATTLE_DESTROYED) and Duel.IsChainNegatable(ev) and rp==1-tp
end
function c40939228.negtg(e,tp,eg,ep,ev,re,r,rp,chk)
```
