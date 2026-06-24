# Auxiliary.AddSetNameMonsterList

## Signature

```lua
Auxiliary.AddSetNameMonsterList(Card c, ... any) -> void
```

## Description

Registers set codes of monsters listed by c, so Auxiliary.IsSetNameMonsterListed can check them later. Skipped while c is copying an effect.

## Parameters

- `c` `Card`
- `...` `any`

## Source

- `Utilities/utility.lua:553`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **39** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Auxiliary.AddSetNameMonsterList`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Eternal Favorite](/examples/cards/87532344) | `87532344` | [Scripts/c87532344.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c87532344.lua) | 73 |
| Contact Gate | `41933425` | [Scripts/c41933425.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c41933425.lua) | 52 |
| Blue-Eyes Toon Ultimate Dragon | `71808988` | [Scripts/c71808988.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71808988.lua) | 50 |
| Neos Fusion | `14088859` | [Scripts/c14088859.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c14088859.lua) | 49 |
| EN - Engage Neo Space | `80170678` | [Scripts/c80170678.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c80170678.lua) | 46 |
| Geistgrinder Golem | `26913989` | [Scripts/c26913989.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c26913989.lua) | 45 |
| Samsara D Lotus | `62318994` | [Scripts/c62318994.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c62318994.lua) | 44 |
| Favorite Contact | `75047173` | [Scripts/c75047173.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c75047173.lua) | 44 |
| EN Shuffle | `10186633` | [Scripts/c10186633.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c10186633.lua) | 44 |
| Protection of the Elements | `66367984` | [Scripts/c66367984.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c66367984.lua) | 43 |
| Mature Chronicle | `92650749` | [Scripts/c92650749.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92650749.lua) | 42 |
| Instant Contact | `16169772` | [Scripts/c16169772.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c16169772.lua) | 40 |
| Spirit of Yubel | `90829280` | [Scripts/c90829280.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c90829280.lua) | 39 |
| Over Fusion | `52553471` | [Scripts/c52553471.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c52553471.lua) | 39 |
| NEXT | `74414885` | [Scripts/c74414885.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74414885.lua) | 39 |
| Battle of Sleeping Spirits | `46570372` | [Scripts/c46570372.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c46570372.lua) | 36 |
| Neos Force | `47274077` | [Scripts/c47274077.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c47274077.lua) | 36 |
| D - Force | `6186304` | [Scripts/c6186304.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c6186304.lua) | 35 |
| Nightmare Pain | `65261141` | [Scripts/c65261141.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c65261141.lua) | 35 |
| Instant Neo Space | `11913700` | [Scripts/c11913700.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c11913700.lua) | 34 |
| Bubble Shuffle | `61968753` | [Scripts/c61968753.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c61968753.lua) | 34 |
| EN Wave | `89058026` | [Scripts/c89058026.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c89058026.lua) | 33 |
| Reverse of Neos | `18302224` | [Scripts/c18302224.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c18302224.lua) | 33 |
| Cyclone Boomerang | `29612557` | [Scripts/c29612557.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c29612557.lua) | 31 |
| ...and 15 more |  |  |  |

## Script Examples

### Eternal Favorite (`87532344`)

Source: [Scripts/c87532344.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c87532344.lua)

```lua
function s.initial_effect(c)
	aux.AddCodeList(c,78371393)
	aux.AddSetNameMonsterList(c,0x1a5)
	--Activate
	local e1=Effect.CreateEffect(c)
```

### Contact Gate (`41933425`)

Source: [Scripts/c41933425.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c41933425.lua)

```lua
function c41933425.initial_effect(c)
	aux.AddCodeList(c,89943723)
	aux.AddSetNameMonsterList(c,0x3008)
	--Activate
	local e1=Effect.CreateEffect(c)
```

### Blue-Eyes Toon Ultimate Dragon (`71808988`)

Source: [Scripts/c71808988.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71808988.lua)

```lua
	c:EnableReviveLimit()
	aux.AddMaterialCodeList(c,53183600)
	aux.AddSetNameMonsterList(c,0x62)
	aux.AddFusionProcFunFun(c,aux.FilterBoolFunction(Card.IsFusionCode,53183600),s.ffilter,2,true)
	aux.AddContactFusionProcedure(c,s.cfilter,LOCATION_HAND+LOCATION_MZONE+LOCATION_GRAVE,0,aux.ContactFusionSendToDeck(c))
```
