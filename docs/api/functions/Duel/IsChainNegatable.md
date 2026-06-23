# Duel.IsChainNegatable

## Signature

```lua
Duel.IsChainNegatable(int chainc) -> bool
```

## Description

Compatibility check for whether chainc's activation can be negated.
In this MDPro3 core binding, the function currently returns true for any chain count.
Local scripts still call it in negation conditions so the script expresses the intended activation-legality check.

## Parameters

- `chainc` `int` - Chain Link number to test, commonly the ev argument in an EVENT_CHAINING condition.

## Returns

- `bool` - true when this binding considers that Chain Link's activation negatable.

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5061`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **379** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Duel.IsChainNegatable`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Enneacraft - Archa.TAIL](/examples/cards/81237046) | `81237046` | [Scripts/c81237046.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c81237046.lua) | 63 |
| [Enneacraft - Atil.SPIA](/examples/cards/71801447) | `71801447` | [Scripts/c71801447.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71801447.lua) | 62 |
| [Shooting Majestic Star Dragon](/examples/cards/40939228) | `40939228` | [Scripts/c40939228.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c40939228.lua) | 62 |
| Red-Eyes Slash Dragon | `21140872` | [Scripts/c21140872.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c21140872.lua) | 60 |
| A-to-Z-Dragon Buster Cannon | `65172015` | [Scripts/c65172015.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c65172015.lua) | 58 |
| Frightfur March | `74416026` | [Scripts/c74416026.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74416026.lua) | 58 |
| Dragon Master Magia | `12381100` | [Scripts/c12381100.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c12381100.lua) | 57 |
| Ursarctic Grand Chariot | `80086070` | [Scripts/c80086070.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c80086070.lua) | 57 |
| Endymion, the Mighty Master of Magic | `3611830` | [Scripts/c3611830.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c3611830.lua) | 56 |
| Arms of Genex Return Zero | `61775475` | [Scripts/c61775475.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c61775475.lua) | 56 |
| Emperor Charles the Great | `97864322` | [Scripts/c97864322.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c97864322.lua) | 56 |
| Toadally Awesome | `90809975` | [Scripts/c90809975.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c90809975.lua) | 56 |
| All-Eyes Phantom Dragon | `70335319` | [Scripts/c70335319.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c70335319.lua) | 55 |
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
| Machina Ruinforce | `46033517` | [Scripts/c46033517.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c46033517.lua) | 50 |
| ...and 355 more |  |  |  |

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
