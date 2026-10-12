# Duel.ChangeAttackTarget

## Signature

```lua
Duel.ChangeAttackTarget(Card|nil target) -> bool
```

## Description

Changes the current attack target to target, or to a direct attack when target is nil, and returns whether the change succeeded.
The current attacker must exist, be able to attack, and not have its attack canceled. A card target must be one of the current legal attack targets; direct attack requires that the attacker is not forbidden from attacking directly.

## Parameters

- `target` `Card|nil`

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4920`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **27** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Duel.ChangeAttackTarget) with `Duel.ChangeAttackTarget`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| X-Saber Gottoms | `8252010` | [Scripts/c8252010.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c8252010.lua) | 1 |
| Galactikuriboh | `46261704` | [Scripts/c46261704.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c46261704.lua) | 1 |
| Apple Magician Girl | `56132807` | [Scripts/c56132807.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c56132807.lua) | 1 |
| Mermail Abysstrite | `59170782` | [Scripts/c59170782.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c59170782.lua) | 1 |
| Ultimate Divine-Beast | `32247099` | [Scripts/c32247099.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c32247099.lua) | 1 |
| Chocolate Magician Girl | `7198399` | [Scripts/c7198399.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c7198399.lua) | 1 |
| Subterror Nemesis Defender | `68823957` | [Scripts/c68823957.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c68823957.lua) | 1 |
| Blackwing Tamer - Obsidian Hawk Joe | `81983656` | [Scripts/c81983656.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c81983656.lua) | 1 |
| Puppet Rook | `77590412` | [Scripts/c77590412.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c77590412.lua) | 1 |
| Lemon Magician Girl | `34318086` | [Scripts/c34318086.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c34318086.lua) | 1 |
| Krystal Avatar | `20960340` | [Scripts/c20960340.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c20960340.lua) | 1 |
| Clear Kuriboh | `46613515` | [Scripts/c46613515.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c46613515.lua) | 1 |
| Shift | `59560625` | [Scripts/c59560625.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c59560625.lua) | 1 |
| White Night Dragon | `79473793` | [Scripts/c79473793.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c79473793.lua) | 1 |
| Roulette Spider | `36708764` | [Scripts/c36708764.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c36708764.lua) | 1 |
| Card Blocker | `42256406` | [Scripts/c42256406.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c42256406.lua) | 1 |
| Dark Angel | `28593329` | [Scripts/c28593329.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c28593329.lua) | 1 |
| Neo-Spacian Twinkle Moss | `13857930` | [Scripts/c13857930.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c13857930.lua) | 1 |
| Neo-Spacian Glow Moss | `17732278` | [Scripts/c17732278.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c17732278.lua) | 1 |
| Staunch Defender | `92854392` | [Scripts/c92854392.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c92854392.lua) | 1 |
| Ghost Gardna | `59965151` | [Scripts/c59965151.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c59965151.lua) | 1 |
| Jam Defender | `21558682` | [Scripts/c21558682.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c21558682.lua) | 1 |
| Crystal Beast Amber Mammoth | `69937550` | [Scripts/c69937550.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c69937550.lua) | 1 |
| Doble Passe | `79997591` | [Scripts/c79997591.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c79997591.lua) | 1 |
| ...and 3 more |  |  |  |

## Script Examples

### X-Saber Gottoms (`8252010`)

Source: [Scripts/c8252010.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c8252010.lua)

```lua
		and a:IsAttackable() and a:IsRelateToBattle() and not a:IsImmuneToEffect(e) then
		Duel.BreakEffect()
		Duel.ChangeAttackTarget(c)
	end
end
```

### Galactikuriboh (`46261704`)

Source: [Scripts/c46261704.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c46261704.lua)

```lua
			Duel.BreakEffect()
			local mg=Duel.GetMatchingGroup(c46261704.mfilter,tp,LOCATION_MZONE,LOCATION_MZONE,nil)
			if Duel.ChangeAttackTarget(tc) and mg:GetCount()>0
				and c:IsRelateToChain() and c:IsLocation(LOCATION_GRAVE) and aux.NecroValleyFilter()(c)
				and c:IsCanOverlay() and Duel.SelectYesNo(tp,aux.Stringid(46261704,2)) then
```

### Apple Magician Girl (`56132807`)

Source: [Scripts/c56132807.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c56132807.lua)

```lua
		if a:IsAttackable() and not a:IsImmuneToEffect(e) and ag:IsContains(tc) then
			Duel.BreakEffect()
			Duel.ChangeAttackTarget(tc)
			local e1=Effect.CreateEffect(e:GetHandler())
			e1:SetType(EFFECT_TYPE_SINGLE)
```
