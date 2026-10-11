# Duel.CalculateDamage

## Signature

```lua
Duel.CalculateDamage(Card attacker, Card|nil attack_target, [bool new_attack]) -> void
```

## Description

Starts damage calculation between attacker and attack_target, or a direct attack when attack_target is nil.
new_attack is optional and is passed to the damage-step processor. If attacker and attack_target are the same card, the binding returns no value and does not start damage calculation.

## Parameters

- `attacker` `Card`
- `attack_target` `Card|nil`
- `new_attack` `bool` optional - default: false

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4921`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **28** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Duel.CalculateDamage) with `Duel.CalculateDamage`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Number 38: Hope Harbinger Dragon Titanic Galaxy | `63767246` | [Scripts/c63767246.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63767246.lua) | 1 |
| Dice Roll Battle | `88482761` | [Scripts/c88482761.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c88482761.lua) | 1 |
| Gladiator Beast Noxious | `67385964` | [Scripts/c67385964.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c67385964.lua) | 1 |
| Eye of Illusion | `23446369` | [Scripts/c23446369.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c23446369.lua) | 1 |
| Cubic Ascension | `2434862` | [Scripts/c2434862.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c2434862.lua) | 1 |
| Dark Spirit of Banishment | `51993760` | [Scripts/c51993760.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c51993760.lua) | 1 |
| Giant Kra-Corn | `8170654` | [Scripts/c8170654.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c8170654.lua) | 1 |
| Gagaga Samurai | `91499077` | [Scripts/c91499077.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c91499077.lua) | 1 |
| Last Counter | `86049351` | [Scripts/c86049351.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c86049351.lua) | 1 |
| Ancient Lamp | `54912977` | [Scripts/c54912977.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c54912977.lua) | 1 |
| Last Turn | `28566710` | [Scripts/c28566710.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c28566710.lua) | 1 |
| Roulette Spider | `36708764` | [Scripts/c36708764.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c36708764.lua) | 2 |
| Mutant Mindmaster | `11508758` | [Scripts/c11508758.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c11508758.lua) | 1 |
| Superheavy Samurai Blowtorch | `7864030` | [Scripts/c7864030.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c7864030.lua) | 2 |
| Double Dragon Descent | `13166648` | [Scripts/c13166648.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c13166648.lua) | 1 |
| Dispatchparazzi | `64966519` | [Scripts/c64966519.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c64966519.lua) | 1 |
| Equip Shot | `62878208` | [Scripts/c62878208.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c62878208.lua) | 1 |
| Heroic Advance | `21924381` | [Scripts/c21924381.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c21924381.lua) | 1 |
| Performapal Kuribohble | `69181753` | [Scripts/c69181753.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c69181753.lua) | 1 |
| Decoy Dragon | `2732323` | [Scripts/c2732323.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c2732323.lua) | 1 |
| Magical Arm Shield | `96008713` | [Scripts/c96008713.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c96008713.lua) | 1 |
| Evolutionary Bridge | `93504463` | [Scripts/c93504463.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93504463.lua) | 1 |
| Attack Guidance Armor | `3103067` | [Scripts/c3103067.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c3103067.lua) | 1 |
| Construction Train Signal Red | `34475451` | [Scripts/c34475451.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c34475451.lua) | 1 |
| ...and 4 more |  |  |  |

## Script Examples

### Number 38: Hope Harbinger Dragon Titanic Galaxy (`63767246`)

Source: [Scripts/c63767246.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63767246.lua)

```lua
		local at=Duel.GetAttacker()
		if at:IsAttackable() and not at:IsImmuneToEffect(e) then
			Duel.CalculateDamage(at,c)
		end
	end
```

### Dice Roll Battle (`88482761`)

Source: [Scripts/c88482761.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c88482761.lua)

```lua
		if c1:IsControler(1-tp) and c1:IsPosition(POS_FACEUP_ATTACK) and not c1:IsImmuneToEffect(e)
			and c2:IsControler(tp) then
			Duel.CalculateDamage(c1,c2,true)
		end
	end
```

### Gladiator Beast Noxious (`67385964`)

Source: [Scripts/c67385964.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c67385964.lua)

```lua
			e1:SetReset(RESET_PHASE+PHASE_DAMAGE)
			c:RegisterEffect(e1)
			Duel.CalculateDamage(a,c)
		end
	end
```
