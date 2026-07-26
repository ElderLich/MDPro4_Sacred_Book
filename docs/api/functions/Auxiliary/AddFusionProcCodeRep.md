# Auxiliary.AddFusionProcCodeRep

## Signature

```lua
Auxiliary.AddFusionProcCodeRep(Card c, int code1, int cc, bool sub, bool insf) -> void
```

## Description

Registers a fixed-count Fusion Material procedure requiring cc monsters with card code code1.

## Parameters

- `c` `Card`
- `code1` `int`
- `cc` `int`
- `sub` `bool`
- `insf` `bool`

## Source

- `Utilities/procedure.lua:1239`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **11** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Auxiliary.AddFusionProcCodeRep`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Blue-Eyes Alternative Ultimate Dragon | `43228023` | [Scripts/c43228023.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c43228023.lua) | 1 |
| Neo Blue-Eyes Ultimate Dragon | `56532353` | [Scripts/c56532353.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c56532353.lua) | 1 |
| Crimson Nova Trinity the Dark Cubic Lord | `72664875` | [Scripts/c72664875.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c72664875.lua) | 1 |
| Blue-Eyes Twin Burst Dragon | `2129638` | [Scripts/c2129638.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c2129638.lua) | 1 |
| Mokey Mokey King | `13803864` | [Scripts/c13803864.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c13803864.lua) | 1 |
| Cyber Ogre 2 | `37057012` | [Scripts/c37057012.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c37057012.lua) | 1 |
| D.3.S. Frog | `9910360` | [Scripts/c9910360.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c9910360.lua) | 1 |
| Cyber Twin Dragon | `74157028` | [Scripts/c74157028.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74157028.lua) | 1 |
| Cyber End Dragon | `1546123` | [Scripts/c1546123.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c1546123.lua) | 1 |
| Blue-Eyes Ultimate Dragon | `23995346` | [Scripts/c23995346.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c23995346.lua) | 1 |
| Twin-Headed Thunder Dragon | `54752875` | [Scripts/c54752875.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c54752875.lua) | 1 |

## Script Examples

### Blue-Eyes Alternative Ultimate Dragon (`43228023`)

Source: [Scripts/c43228023.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c43228023.lua)

```lua
	--fusion material
	c:EnableReviveLimit()
	aux.AddFusionProcCodeRep(c,89631139,3,true,true)
	--cannot be target/effect indestructable
	local e1=Effect.CreateEffect(c)
```

### Neo Blue-Eyes Ultimate Dragon (`56532353`)

Source: [Scripts/c56532353.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c56532353.lua)

```lua
	--fusion material
	c:EnableReviveLimit()
	aux.AddFusionProcCodeRep(c,89631139,3,true,true)
	--chain attack
	local e1=Effect.CreateEffect(c)
```

### Crimson Nova Trinity the Dark Cubic Lord (`72664875`)

Source: [Scripts/c72664875.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c72664875.lua)

```lua
	--fusion material
	c:EnableReviveLimit()
	aux.AddFusionProcCodeRep(c,30270176,3,false,false)
	--spsummon condition
	local e0=Effect.CreateEffect(c)
```
