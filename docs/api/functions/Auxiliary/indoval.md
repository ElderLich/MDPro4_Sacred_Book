# Auxiliary.indoval

## Signature

```lua
Auxiliary.indoval(Effect e, Effect re, int rp) -> bool
```

## Description

Value helper for indestructibility against opponent's effects; it returns true when rp is the opponent of e's handler player.

## Parameters

- `e` `Effect`
- `re` `Effect`
- `rp` `int`

## Returns

- `bool`

## Source

- `Utilities/utility.lua:831`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **113** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Auxiliary.indoval) with `Auxiliary.indoval`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Prank-Kids Bow-Wow-Bark | `43886072` | [Scripts/c43886072.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c43886072.lua) | 1 |
| Sea Stealth Attack | `19089195` | [Scripts/c19089195.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c19089195.lua) | 1 |
| Endymion, the Mighty Master of Magic | `3611830` | [Scripts/c3611830.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c3611830.lua) | 1 |
| Neo Super Quantal Mech King Blaster Magna | `95493471` | [Scripts/c95493471.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c95493471.lua) | 1 |
| Drytron Meteonis DA Draconids | `56863746` | [Scripts/c56863746.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c56863746.lua) | 1 |
| Red Hypernova Dragon | `30698243` | [Scripts/c30698243.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c30698243.lua) | 1 |
| Majesty Pegasus, the Dracoslayer | `92332424` | [Scripts/c92332424.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c92332424.lua) | 1 |
| Groza, Tyrant of Thunder | `45420955` | [Scripts/c45420955.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c45420955.lua) | 1 |
| Supreme King Z-ARC | `13331639` | [Scripts/c13331639.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c13331639.lua) | 1 |
| Icejade Gymir Aegirine | `86682165` | [Scripts/c86682165.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c86682165.lua) | 1 |
| Stand Up Centur-Ion! | `41371602` | [Scripts/c41371602.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c41371602.lua) | 1 |
| Tailwind of Gusto | `1187243` | [Scripts/c1187243.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c1187243.lua) | 1 |
| Angelechy Bastion | `28904860` | [Scripts/c28904860.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c28904860.lua) | 1 |
| Wind Unicorn Parallel, the Dracoslayer | `39016067` | [Scripts/c39016067.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c39016067.lua) | 1 |
| Red Supernova Dragon | `99585850` | [Scripts/c99585850.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c99585850.lua) | 1 |
| Sunavalon Dryatrentiay | `92770064` | [Scripts/c92770064.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c92770064.lua) | 1 |
| Twilight Specter Rayrage | `71222649` | [Scripts/c71222649.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c71222649.lua) | 1 |
| Cyberdark Inferno | `44352516` | [Scripts/c44352516.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c44352516.lua) | 1 |
| Giant Beetrooper Invincible Atlas | `38229962` | [Scripts/c38229962.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c38229962.lua) | 1 |
| Evil Eye of Selene | `44133040` | [Scripts/c44133040.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c44133040.lua) | 1 |
| Ancient Warriors - Ambitious Cao De | `33545259` | [Scripts/c33545259.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c33545259.lua) | 1 |
| War Rock Meteoragon | `10497636` | [Scripts/c10497636.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c10497636.lua) | 1 |
| Signal Warrior | `9634146` | [Scripts/c9634146.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c9634146.lua) | 1 |
| B.E.F. Zelos | `975299` | [Scripts/c975299.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c975299.lua) | 1 |
| ...and 89 more |  |  |  |

## Script Examples

### Prank-Kids Bow-Wow-Bark (`43886072`)

Source: [Scripts/c43886072.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c43886072.lua)

```lua
	e1:SetReset(RESET_PHASE+PHASE_END)
	e1:SetTarget(c43886072.indtg)
	e1:SetValue(aux.indoval)
	Duel.RegisterEffect(e1,tp)
end
```

### Sea Stealth Attack (`19089195`)

Source: [Scripts/c19089195.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c19089195.lua)

```lua
	e1:SetTargetRange(LOCATION_ONFIELD,0)
	e1:SetTarget(aux.TargetBoolFunction(Card.IsType,TYPE_SPELL+TYPE_TRAP))
	e1:SetValue(aux.indoval)
	e1:SetReset(RESET_PHASE+PHASE_END)
	Duel.RegisterEffect(e1,tp)
```

### Endymion, the Mighty Master of Magic (`3611830`)

Source: [Scripts/c3611830.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c3611830.lua)

```lua
	e4:SetRange(LOCATION_MZONE)
	e4:SetCondition(c3611830.ctcon)
	e4:SetValue(aux.indoval)
	c:RegisterEffect(e4)
	--search
```
