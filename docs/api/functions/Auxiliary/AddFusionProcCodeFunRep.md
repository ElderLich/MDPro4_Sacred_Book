# Auxiliary.AddFusionProcCodeFunRep

## Signature

```lua
Auxiliary.AddFusionProcCodeFunRep(Card c, int|table code1, function|table f, int minc, int maxc, bool sub, bool insf) -> void
```

## Description

Add a Fusion Summon procedure for c
Use 1 monster with code and minc-maxc monsters satisfying filter condition f as Fusion Materials
Equivalent to aux.AddFusionProcMixRep(c, sub, insf, f, minc, maxc, code1)

## Parameters

- `c` `Card`
- `code1` `int|table`
- `f` `function|table`
- `minc` `int`
- `maxc` `int`
- `sub` `bool`
- `insf` `bool`

## Source

- `Utilities/procedure.lua:1324`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **10** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Auxiliary.AddFusionProcCodeFunRep`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Cyberse Clock Dragon | `42717221` | [Scripts/c42717221.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c42717221.lua) | 48 |
| Gold Pride - Pin Baller | `28497830` | [Scripts/c28497830.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c28497830.lua) | 45 |
| Alba-Lenatus the Abyss Dragon | `3410461` | [Scripts/c3410461.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c3410461.lua) | 41 |
| Clorless, Chaos King of Dark World | `22723778` | [Scripts/c22723778.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c22723778.lua) | 41 |
| Veidos the Dragon of Endless Darkness | `8540986` | [Scripts/c8540986.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c8540986.lua) | 34 |
| Frightfur Tiger | `464362` | [Scripts/c464362.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c464362.lua) | 33 |
| Chimera the Illusion Beast | `38264974` | [Scripts/c38264974.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c38264974.lua) | 32 |
| Chimeratech Overdragon | `64599569` | [Scripts/c64599569.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c64599569.lua) | 23 |
| Chimeratech Fortress Dragon | `79229522` | [Scripts/c79229522.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c79229522.lua) | 19 |
| Frightfur Wolf | `11039171` | [Scripts/c11039171.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c11039171.lua) | 15 |

## Script Examples

### Cyberse Clock Dragon (`42717221`)

Source: [Scripts/c42717221.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c42717221.lua)

```lua
	--fusion material
	c:EnableReviveLimit()
	aux.AddFusionProcCodeFunRep(c,21830679,aux.FilterBoolFunction(Card.IsFusionType,TYPE_LINK),1,127,true,true)
	--mill + atk
	local e1=Effect.CreateEffect(c)
```

### Gold Pride - Pin Baller (`28497830`)

Source: [Scripts/c28497830.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c28497830.lua)

```lua
	c:EnableReviveLimit()
	--material
	aux.AddFusionProcCodeFunRep(c,92003832,aux.FilterBoolFunction(Card.IsFusionSetCard,0x192),1,127,true,true)
	--equip
	local e1=Effect.CreateEffect(c)
```

### Alba-Lenatus the Abyss Dragon (`3410461`)

Source: [Scripts/c3410461.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c3410461.lua)

```lua
	--fusion material
	c:EnableReviveLimit()
	aux.AddFusionProcCodeFunRep(c,68468459,aux.FilterBoolFunction(Card.IsRace,RACE_DRAGON),1,127,true,true)
	aux.AddContactFusionProcedure(c,c3410461.cfilter,LOCATION_MZONE,LOCATION_MZONE,Duel.SendtoGrave,REASON_COST)
	--spsummon condition
```
