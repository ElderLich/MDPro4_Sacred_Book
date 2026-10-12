# Auxiliary.tgoval

## Signature

```lua
Auxiliary.tgoval(Effect e, Effect re, int rp) -> void
```

## Description

Shared value function for EFFECT_CANNOT_BE_EFFECT_TARGET effects that protect against the opponent's effects.
It returns true when the reason player rp is the opponent of e's handler player.

## Parameters

- `e` `Effect`
- `re` `Effect`
- `rp` `int`

## Source

- `Utilities/utility.lua:839`

## Guided Examples

Learn how to use this function in context:

- [Negation And Immunity](/learn/negation-and-immunity)

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **237** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Auxiliary.tgoval) with `Auxiliary.tgoval`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Fiendsmith's Sequence](/examples/cards/49867899) | `49867899` | [Scripts/c49867899.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c49867899.lua) | 1 |
| [Enneacraft - Asta.PIXEA](/examples/cards/28454232) | `28454232` | [Scripts/c28454232.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c28454232.lua) | 1 |
| Duel Link Dragon, the Duel Dragon | `60025883` | [Scripts/c60025883.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c60025883.lua) | 1 |
| Endymion, the Mighty Master of Magic | `3611830` | [Scripts/c3611830.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c3611830.lua) | 1 |
| Favorite Hero | `11881272` | [Scripts/c11881272.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c11881272.lua) | 1 |
| Galaxy-Eyes Cipher X Dragon | `28346136` | [Scripts/c28346136.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c28346136.lua) | 1 |
| Red Hypernova Dragon | `30698243` | [Scripts/c30698243.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c30698243.lua) | 1 |
| D/D/D Super Doom King Bright Armageddon | `72402069` | [Scripts/c72402069.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c72402069.lua) | 1 |
| Daigusto Laplampilica | `76937326` | [Scripts/c76937326.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c76937326.lua) | 1 |
| Egyptian God Slime | `42166000` | [Scripts/c42166000.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c42166000.lua) | 1 |
| Majesty Pegasus, the Dracoslayer | `92332424` | [Scripts/c92332424.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c92332424.lua) | 1 |
| Groza, Tyrant of Thunder | `45420955` | [Scripts/c45420955.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c45420955.lua) | 1 |
| Lost World | `17228908` | [Scripts/c17228908.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c17228908.lua) | 1 |
| Gagaga Utopic Tactics | `75956913` | [Scripts/c75956913.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c75956913.lua) | 1 |
| Fata Dragna | `41763141` | [Scripts/c41763141.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c41763141.lua) | 1 |
| Gergonne's End | `59490397` | [Scripts/c59490397.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c59490397.lua) | 1 |
| The Winged Dragon of Ra - Sphere Mode | `10000080` | [Scripts/c10000080.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c10000080.lua) | 1 |
| Supreme King Z-ARC | `13331639` | [Scripts/c13331639.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c13331639.lua) | 1 |
| Noble Arms - Excaliburn | `46008667` | [Scripts/c46008667.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c46008667.lua) | 1 |
| Drytron Meteonis Draconids | `69815951` | [Scripts/c69815951.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c69815951.lua) | 1 |
| DoomZ Command "D.O.O.M.D.U.R.G." | `68831625` | [Scripts/c68831625.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c68831625.lua) | 1 |
| Guardian Chimera | `11321089` | [Scripts/c11321089.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c11321089.lua) | 1 |
| Drytron Meteonis Quadrantids | `95209656` | [Scripts/c95209656.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c95209656.lua) | 1 |
| Darklord Eveningstar | `10136446` | [Scripts/c10136446.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c10136446.lua) | 1 |
| ...and 213 more |  |  |  |

## Script Examples

### Fiendsmith's Sequence (`49867899`)

Source: [Scripts/c49867899.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c49867899.lua)

```lua
		e2:SetType(EFFECT_TYPE_EQUIP)
		e2:SetCode(EFFECT_CANNOT_BE_EFFECT_TARGET)
		e2:SetValue(aux.tgoval)
		e2:SetReset(RESET_EVENT+RESETS_STANDARD)
		c:RegisterEffect(e2)
```

### Enneacraft - Asta.PIXEA (`28454232`)

Source: [Scripts/c28454232.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c28454232.lua)

```lua
	e5:SetTargetRange(LOCATION_ONFIELD+LOCATION_GRAVE,LOCATION_ONFIELD+LOCATION_GRAVE)
	e5:SetCondition(s.effcon)
	e5:SetValue(aux.tgoval)
	c:RegisterEffect(e5)
	Duel.AddCustomActivityCounter(id,ACTIVITY_SPSUMMON,s.counterfilter)
```

### Duel Link Dragon, the Duel Dragon (`60025883`)

Source: [Scripts/c60025883.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c60025883.lua)

```lua
	local e3=e2:Clone()
	e3:SetCode(EFFECT_CANNOT_BE_EFFECT_TARGET)
	e3:SetValue(aux.tgoval)
	c:RegisterEffect(e3)
end
```
