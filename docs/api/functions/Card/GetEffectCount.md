# Card.GetEffectCount

## Signature

```lua
Card.GetEffectCount(Card c, int code) -> int
```

## Description

Returns the number of effects that c is affected by the type of code

## Parameters

- `c` `Card`
- `code` `int`

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3551`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **20** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.GetEffectCount`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| ZW - Leo Arms | `60992364` | [Scripts/c60992364.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c60992364.lua) | 48 |
| Inzektor Hopper | `52601736` | [Scripts/c52601736.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c52601736.lua) | 45 |
| Galaxy-Eyes Antimatter Dragon | `92517928` | [Scripts/c92517928.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92517928.lua) | 41 |
| Dragunity Pilum | `52977572` | [Scripts/c52977572.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c52977572.lua) | 36 |
| Pegasus Wing | `72083436` | [Scripts/c72083436.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c72083436.lua) | 36 |
| Gagaga Samurai | `91499077` | [Scripts/c91499077.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c91499077.lua) | 35 |
| Cyberse Accelerator | `89238128` | [Scripts/c89238128.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c89238128.lua) | 35 |
| Yosenju Kama 2 | `92246806` | [Scripts/c92246806.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92246806.lua) | 33 |
| Masked HERO Anki | `59642500` | [Scripts/c59642500.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59642500.lua) | 32 |
| Lineage of Destruction | `29307554` | [Scripts/c29307554.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c29307554.lua) | 32 |
| Infernity Queen | `53246495` | [Scripts/c53246495.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c53246495.lua) | 31 |
| Hi-Five the Sky | `91677585` | [Scripts/c91677585.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c91677585.lua) | 30 |
| Psychic Snail | `58453942` | [Scripts/c58453942.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c58453942.lua) | 28 |
| Baby Tiragon | `12533811` | [Scripts/c12533811.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c12533811.lua) | 27 |
| Number 28: Titanic Moth | `53701457` | [Scripts/c53701457.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c53701457.lua) | 24 |
| Crystal Beast Amethyst Cat | `32933942` | [Scripts/c32933942.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c32933942.lua) | 18 |
| Submarineroid | `99861526` | [Scripts/c99861526.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c99861526.lua) | 18 |
| Elemental HERO Rampart Blaster | `47737087` | [Scripts/c47737087.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c47737087.lua) | 18 |
| Fortune Chariot | `39299733` | [Scripts/c39299733.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c39299733.lua) | 14 |
| Sonic Shooter | `40384720` | [Scripts/c40384720.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c40384720.lua) | 13 |

## Script Examples

### ZW - Leo Arms (`60992364`)

Source: [Scripts/c60992364.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c60992364.lua)

```lua
function c60992364.attg(e,tp,eg,ep,ev,re,r,rp,chk)
	local eqc=e:GetHandler():GetEquipTarget()
	if chk==0 then return eqc and eqc:GetAttackedCount()==1 and eqc:GetEffectCount(EFFECT_EXTRA_ATTACK)==0 end
	Duel.SetTargetCard(e:GetLabelObject())
end
```

### Inzektor Hopper (`52601736`)

Source: [Scripts/c52601736.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c52601736.lua)

```lua
	local tc=e:GetHandler():GetEquipTarget()
	return Duel.IsAbleToEnterBP()
		and tc and tc:IsAttackable() and tc:GetEffectCount(EFFECT_DIRECT_ATTACK)==0
end
function c52601736.ftarget(e,c)
```

### Galaxy-Eyes Antimatter Dragon (`92517928`)

Source: [Scripts/c92517928.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92517928.lua)

```lua
end
function s.atktg(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return e:GetHandler():GetEffectCount(EFFECT_EXTRA_ATTACK)==0
		and e:GetHandler():GetEffectCount(EFFECT_EXTRA_ATTACK_MONSTER)==0 end
	if e:GetLabel()~=0 then
```
