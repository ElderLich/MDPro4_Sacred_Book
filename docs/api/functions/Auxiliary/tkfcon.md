# Auxiliary.tkfcon

## Signature

```lua
Auxiliary.tkfcon([Effect|nil e], [int|nil tp]) -> bool
```

## Description

Returns true if tp controls a Token on the field. If tp is omitted and e is provided, tp defaults to e's handler player.

## Parameters

- `e` `Effect|nil` optional
- `tp` `int|nil` optional

## Returns

- `bool` - true if tp controls a Token on the field.

## Source

- `Utilities/utility.lua:874`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **20** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Auxiliary.tkfcon`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Lost World | `17228908` | [Scripts/c17228908.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c17228908.lua) | 51 |
| Mecha Phantom Beast Coltwing | `94973028` | [Scripts/c94973028.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c94973028.lua) | 46 |
| Mecha Phantom Beast Harrliard | `20368763` | [Scripts/c20368763.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c20368763.lua) | 45 |
| Mecha Phantom Beast Hamstrat | `66200210` | [Scripts/c66200210.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c66200210.lua) | 44 |
| Mecha Phantom Beast Blackfalcon | `4417407` | [Scripts/c4417407.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c4417407.lua) | 42 |
| Mecha Phantom Beast Dracossack | `22110647` | [Scripts/c22110647.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c22110647.lua) | 42 |
| Mecha Phantom Beast Megaraptor | `31533704` | [Scripts/c31533704.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c31533704.lua) | 41 |
| Pacifis, the Phantasm City | `2819435` | [Scripts/c2819435.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c2819435.lua) | 40 |
| Mecha Phantom Beast Sabre Hawk | `15335853` | [Scripts/c15335853.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c15335853.lua) | 39 |
| Mecha Phantom Beast Kalgriffin | `41329458` | [Scripts/c41329458.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c41329458.lua) | 39 |
| Mecha Phantom Beast Stealthray | `30811116` | [Scripts/c30811116.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30811116.lua) | 38 |
| Mecha Phantom Beast Raiten | `44026393` | [Scripts/c44026393.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44026393.lua) | 38 |
| Mecha Phantom Beast Tetherwolf | `67922702` | [Scripts/c67922702.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c67922702.lua) | 35 |
| Mecha Phantom Beast Warbluran | `31480215` | [Scripts/c31480215.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c31480215.lua) | 34 |
| White Aura Bihamut | `89907227` | [Scripts/c89907227.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c89907227.lua) | 33 |
| Mecha Phantom Beast Aerosguin | `16943770` | [Scripts/c16943770.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c16943770.lua) | 33 |
| Mecha Phantom Beast O-Lion | `72291078` | [Scripts/c72291078.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c72291078.lua) | 31 |
| Generaider Boss Loot | `1942635` | [Scripts/c1942635.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c1942635.lua) | 27 |
| Mecha Phantom Beast Blue Impala | `67489919` | [Scripts/c67489919.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c67489919.lua) | 26 |
| Mecha Phantom Beast Turtletracer | `76902476` | [Scripts/c76902476.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c76902476.lua) | 19 |

## Script Examples

### Lost World (`17228908`)

Source: [Scripts/c17228908.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c17228908.lua)

```lua
function c17228908.tgcon(e)
	local tp=e:GetHandlerPlayer()
	return aux.tkfcon(e,1-tp)
end
function c17228908.tglimit(e,c)
```

### Mecha Phantom Beast Coltwing (`94973028`)

Source: [Scripts/c94973028.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c94973028.lua)

```lua
	e2:SetRange(LOCATION_MZONE)
	e2:SetCode(EFFECT_INDESTRUCTABLE_BATTLE)
	e2:SetCondition(aux.tkfcon)
	e2:SetValue(1)
	c:RegisterEffect(e2)
```

### Mecha Phantom Beast Harrliard (`20368763`)

Source: [Scripts/c20368763.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c20368763.lua)

```lua
	e2:SetRange(LOCATION_MZONE)
	e2:SetCode(EFFECT_INDESTRUCTABLE_BATTLE)
	e2:SetCondition(aux.tkfcon)
	e2:SetValue(1)
	c:RegisterEffect(e2)
```
