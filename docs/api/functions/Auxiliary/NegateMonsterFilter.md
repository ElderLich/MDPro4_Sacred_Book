# Auxiliary.NegateMonsterFilter

## Signature

```lua
Auxiliary.NegateMonsterFilter(Card c) -> bool
```

## Description

Filter for effects that negate a face-up monster, such as Infinite Impermanence: c must be face-up, not already disabled, and be or originally be an Effect Monster.

## Parameters

- `c` `Card`

## Returns

- `bool` - true if c is a valid face-up monster to have its effects negated.

## Source

- `Utilities/utility.lua:747`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **68** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Auxiliary.NegateMonsterFilter) with `Auxiliary.NegateMonsterFilter`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [D/D/D/D Dimensional King Arc Crisis](/examples/cards/71398055) | `71398055` | [Scripts/c71398055.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71398055.lua) | 3 |
| [Starving Venemy Dragon](/examples/cards/93729065) | `93729065` | [Scripts/c93729065.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93729065.lua) | 1 |
| Starving Venom Fusion Dragon, Four Heavenly Dragons | `27118421` | [Scripts/c27118421.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c27118421.lua) | 1 |
| Dracotail Mululu | `7375867` | [Scripts/c7375867.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c7375867.lua) | 1 |
| Cyber Dragon, the Luminous Mech Dragon | `66664203` | [Scripts/c66664203.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c66664203.lua) | 3 |
| Power Tool Braver Dragon | `63265554` | [Scripts/c63265554.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63265554.lua) | 1 |
| Clear Wing Fast Dragon | `90036274` | [Scripts/c90036274.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c90036274.lua) | 1 |
| Dragunity Arma Gram | `53184342` | [Scripts/c53184342.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c53184342.lua) | 1 |
| D/D/D Super Doom King Bright Armageddon | `72402069` | [Scripts/c72402069.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c72402069.lua) | 1 |
| Dual Avatar Feet - Armored Un-Gyo | `7631534` | [Scripts/c7631534.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c7631534.lua) | 1 |
| Witchcrafter Madame Verre | `21522601` | [Scripts/c21522601.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c21522601.lua) | 3 |
| Primite Imperial Dragon | `81418467` | [Scripts/c81418467.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c81418467.lua) | 3 |
| Stellarnova Binding | `69678646` | [Scripts/c69678646.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c69678646.lua) | 3 |
| Ghost Mourner &amp; Moonlit Chill | `52038441` | [Scripts/c52038441.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c52038441.lua) | 1 |
| The Chaotic Phantasmal Sacred Beasts | `7894706` | [Scripts/c7894706.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c7894706.lua) | 3 |
| Majestic Star Dragon | `7841112` | [Scripts/c7841112.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c7841112.lua) | 3 |
| Seventh Eternity | `60158866` | [Scripts/c60158866.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c60158866.lua) | 1 |
| Magikey Mechmusket - Batosbuster | `19489718` | [Scripts/c19489718.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c19489718.lua) | 1 |
| Angel of Blue Tears | `91706817` | [Scripts/c91706817.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c91706817.lua) | 2 |
| Spell Shattering Sword | `77456448` | [Scripts/c77456448.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c77456448.lua) | 1 |
| Officiator of Doom Samuel | `76213610` | [Scripts/c76213610.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c76213610.lua) | 1 |
| Superheavy Samurai Commander Shanawo | `90587641` | [Scripts/c90587641.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c90587641.lua) | 1 |
| Greedy Venom Fusion Dragon | `51570882` | [Scripts/c51570882.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c51570882.lua) | 1 |
| Underworld Goddess of the Closed World | `98127546` | [Scripts/c98127546.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c98127546.lua) | 3 |
| ...and 44 more |  |  |  |

## Script Examples

### D/D/D/D Dimensional King Arc Crisis (`71398055`)

Source: [Scripts/c71398055.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71398055.lua)

```lua
end
function s.distg(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.IsExistingMatchingCard(aux.NegateMonsterFilter,tp,0,LOCATION_MZONE,1,nil) end
	local g=Duel.GetMatchingGroup(aux.NegateMonsterFilter,tp,0,LOCATION_MZONE,nil)
	Duel.SetOperationInfo(0,CATEGORY_DISABLE,g,g:GetCount(),0,0)
```

### Starving Venemy Dragon (`93729065`)

Source: [Scripts/c93729065.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93729065.lua)

```lua
		e4:SetCode(EFFECT_UPDATE_DEFENSE)
		tc:RegisterEffect(e4)
		if aux.NegateMonsterFilter(tc) then
			local e5=Effect.CreateEffect(c)
			e5:SetType(EFFECT_TYPE_SINGLE)
```

### Starving Venom Fusion Dragon, Four Heavenly Dragons (`27118421`)

Source: [Scripts/c27118421.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c27118421.lua)

```lua
end
function s.nefilter(c)
	return (aux.NegateMonsterFilter(c) or not c:IsAttack(0) or not c:IsAttribute(ATTRIBUTE_DARK)) and c:IsFaceup()
end
function s.distg(e,tp,eg,ep,ev,re,r,rp,chk,chkc)
```
