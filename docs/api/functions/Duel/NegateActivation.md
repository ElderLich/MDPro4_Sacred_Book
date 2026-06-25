# Duel.NegateActivation

## Signature

```lua
Duel.NegateActivation(int chainc) -> bool
```

## Description

Attempts to negate the activation of a Chain Link and returns true only if the activation was successfully negated.
Use it in a resolving negation operation after checking activation legality, commonly with Duel.IsChainNegatable. Gate follow-up actions such as destroy, banish, or send to the GY behind the boolean return.
Use Duel.NegateEffect for "negate that effect" text where the activation itself is not negated.

## How To Use It

Use this during resolution for effects that negate the activation of a Chain Link.

```lua
if Duel.NegateActivation(ev) then
    Duel.Destroy(rc,REASON_EFFECT)
end
```

Gate follow-up actions behind the boolean return. Use `Duel.NegateEffect` when the effect is negated but the activation itself is not.

## Related Functions

- [Duel.IsChainNegatable](/api/functions/Duel/IsChainNegatable)
- [Duel.NegateEffect](/api/functions/Duel/NegateEffect)
- [Duel.GetChainInfo](/api/functions/Duel/GetChainInfo)

## Parameters

- `chainc` `int` - Chain Link number to negate, commonly ev in an EVENT_CHAINING operation.

## Returns

- `bool` - true if the activation was negated; false if the Chain Link cannot be negated or the negation fails.

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4929`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **387** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Duel.NegateActivation`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Enneacraft - Atil.SPIA](/examples/cards/71801447) | `71801447` | [Scripts/c71801447.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71801447.lua) | 62 |
| [Shooting Majestic Star Dragon](/examples/cards/40939228) | `40939228` | [Scripts/c40939228.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c40939228.lua) | 62 |
| Red-Eyes Slash Dragon | `21140872` | [Scripts/c21140872.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c21140872.lua) | 60 |
| A-to-Z-Dragon Buster Cannon | `65172015` | [Scripts/c65172015.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c65172015.lua) | 58 |
| Frightfur March | `74416026` | [Scripts/c74416026.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74416026.lua) | 58 |
| Enneacraft - Atori.MAR | `54842941` | [Scripts/c54842941.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c54842941.lua) | 57 |
| Dragon Master Magia | `12381100` | [Scripts/c12381100.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c12381100.lua) | 57 |
| Ursarctic Grand Chariot | `80086070` | [Scripts/c80086070.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c80086070.lua) | 57 |
| Endymion, the Mighty Master of Magic | `3611830` | [Scripts/c3611830.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c3611830.lua) | 56 |
| Arms of Genex Return Zero | `61775475` | [Scripts/c61775475.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c61775475.lua) | 56 |
| Emperor Charles the Great | `97864322` | [Scripts/c97864322.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c97864322.lua) | 56 |
| Toadally Awesome | `90809975` | [Scripts/c90809975.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c90809975.lua) | 56 |
| All-Eyes Phantom Dragon | `70335319` | [Scripts/c70335319.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c70335319.lua) | 55 |
| Arcana Force EX - The Light Ruler | `5861892` | [Scripts/c5861892.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c5861892.lua) | 55 |
| Drytron Meteonis DA Draconids | `56863746` | [Scripts/c56863746.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c56863746.lua) | 53 |
| Loki, Lord of the Aesir | `67098114` | [Scripts/c67098114.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c67098114.lua) | 51 |
| Fire King Avatar Arvata | `18621798` | [Scripts/c18621798.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c18621798.lua) | 51 |
| Immortal Phoenix Gearfried | `22091647` | [Scripts/c22091647.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c22091647.lua) | 51 |
| PSY-Framegear Gamma | `38814750` | [Scripts/c38814750.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c38814750.lua) | 51 |
| PSY-Framegear Delta | `74203495` | [Scripts/c74203495.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74203495.lua) | 51 |
| PSY-Framegear Epsilon | `1697104` | [Scripts/c1697104.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c1697104.lua) | 51 |
| Red-Eyes Dark Dragoon | `37818794` | [Scripts/c37818794.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c37818794.lua) | 50 |
| Whisker Blitzclique | `85523502` | [Scripts/c85523502.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c85523502.lua) | 50 |
| Eclipse, Dragon Ruler of Catastrophes | `30350202` | [Scripts/c30350202.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30350202.lua) | 50 |
| ...and 363 more |  |  |  |

## Script Examples

### Enneacraft - Atil.SPIA (`71801447`)

Source: [Scripts/c71801447.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71801447.lua)

```lua
	for i=1,ev do
		local te,tgp=Duel.GetChainInfo(i,CHAININFO_TRIGGERING_EFFECT,CHAININFO_TRIGGERING_PLAYER)
		if tgp~=tp and Duel.NegateActivation(i) then
			local tc=te:GetHandler()
			if tc:IsRelateToEffect(e) and tc:IsRelateToChain(i) then
```

### Shooting Majestic Star Dragon (`40939228`)

Source: [Scripts/c40939228.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c40939228.lua)

```lua
			Duel.RegisterEffect(e1,tp)
		end
		if Duel.NegateActivation(ev) and re:GetHandler():IsRelateToEffect(re) then
			Duel.Remove(eg,POS_FACEUP,REASON_EFFECT)
		end
```

### Red-Eyes Slash Dragon (`21140872`)

Source: [Scripts/c21140872.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c21140872.lua)

```lua
end
function c21140872.ngop(e,tp,eg,ep,ev,re,r,rp)
	if Duel.NegateActivation(ev) and re:GetHandler():IsRelateToEffect(re) then
		Duel.Destroy(eg,REASON_EFFECT)
	end
```
