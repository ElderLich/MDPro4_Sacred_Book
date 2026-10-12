# Card.IsAttackable

## Signature

```lua
Card.IsAttackable(Card c) -> bool
```

## Description

Checks whether c currently satisfies the core's basic attack-capable conditions.
The card must be face-up Attack Position, or face-up Defense Position with EFFECT_DEFENSE_ATTACK, and it must not be forbidden, unable to attack, attack-disabled, or under a skipped Battle Phase. This does not check attack-announcement costs.

## Parameters

- `c` `Card`

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3653`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **54** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Card.IsAttackable) with `Card.IsAttackable`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Number 38: Hope Harbinger Dragon Titanic Galaxy | `63767246` | [Scripts/c63767246.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c63767246.lua) | 1 |
| X-Saber Gottoms | `8252010` | [Scripts/c8252010.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c8252010.lua) | 1 |
| Galactikuriboh | `46261704` | [Scripts/c46261704.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c46261704.lua) | 1 |
| Apple Magician Girl | `56132807` | [Scripts/c56132807.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c56132807.lua) | 1 |
| Number 53: Heart-eartH | `23998625` | [Scripts/c23998625.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c23998625.lua) | 1 |
| Inzektor Hopper | `52601736` | [Scripts/c52601736.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c52601736.lua) | 1 |
| Chocolate Magician Girl | `7198399` | [Scripts/c7198399.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c7198399.lua) | 1 |
| Kunai with Chain | `37390589` | [Scripts/c37390589.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c37390589.lua) | 1 |
| Gladiator Beast Noxious | `67385964` | [Scripts/c67385964.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c67385964.lua) | 1 |
| Puppet Rook | `77590412` | [Scripts/c77590412.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c77590412.lua) | 1 |
| Butterflyoke | `75987257` | [Scripts/c75987257.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c75987257.lua) | 1 |
| Eye of Illusion | `23446369` | [Scripts/c23446369.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c23446369.lua) | 1 |
| Cubic Ascension | `2434862` | [Scripts/c2434862.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c2434862.lua) | 1 |
| Dark Spirit of Banishment | `51993760` | [Scripts/c51993760.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c51993760.lua) | 1 |
| Raptor's Ultimate Mace | `87609391` | [Scripts/c87609391.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c87609391.lua) | 1 |
| Performapal Odd-Eyes Unicorn | `86157908` | [Scripts/c86157908.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c86157908.lua) | 1 |
| Krystal Avatar | `20960340` | [Scripts/c20960340.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c20960340.lua) | 1 |
| Giant Kra-Corn | `8170654` | [Scripts/c8170654.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c8170654.lua) | 1 |
| Gagaga Samurai | `91499077` | [Scripts/c91499077.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c91499077.lua) | 1 |
| Last Counter | `86049351` | [Scripts/c86049351.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c86049351.lua) | 1 |
| Cybernetic Hidden Technology | `92773018` | [Scripts/c92773018.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c92773018.lua) | 1 |
| Memory of an Adversary | `60080151` | [Scripts/c60080151.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c60080151.lua) | 1 |
| Infected Mail | `6430659` | [Scripts/c6430659.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c6430659.lua) | 1 |
| Ancient Lamp | `54912977` | [Scripts/c54912977.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c54912977.lua) | 1 |
| ...and 30 more |  |  |  |

## Script Examples

### Number 38: Hope Harbinger Dragon Titanic Galaxy (`63767246`)

Source: [Scripts/c63767246.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c63767246.lua)

```lua
	if c:IsRelateToEffect(e) then
		local at=Duel.GetAttacker()
		if at:IsAttackable() and not at:IsImmuneToEffect(e) then
			Duel.CalculateDamage(at,c)
		end
```

### X-Saber Gottoms (`8252010`)

Source: [Scripts/c8252010.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c8252010.lua)

```lua
	local a=Duel.GetAttacker()
	if c:IsRelateToChain() and aux.NecroValleyFilter()(c) and Duel.SpecialSummon(c,0,tp,tp,false,false,POS_FACEUP)~=0
		and a:IsAttackable() and a:IsRelateToBattle() and not a:IsImmuneToEffect(e) then
		Duel.BreakEffect()
		Duel.ChangeAttackTarget(c)
```

### Galactikuriboh (`46261704`)

Source: [Scripts/c46261704.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c46261704.lua)

```lua
	if tc and Duel.SpecialSummon(tc,0,tp,tp,false,false,POS_FACEUP)>0 and tc:IsLocation(LOCATION_MZONE) then
		local a=Duel.GetAttacker()
		if a:IsAttackable() and not a:IsImmuneToEffect(e) then
			Duel.BreakEffect()
			local mg=Duel.GetMatchingGroup(c46261704.mfilter,tp,LOCATION_MZONE,LOCATION_MZONE,nil)
```
