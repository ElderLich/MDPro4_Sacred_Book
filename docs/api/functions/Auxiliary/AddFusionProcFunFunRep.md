# Auxiliary.AddFusionProcFunFunRep

## Signature

```lua
Auxiliary.AddFusionProcFunFunRep(Card c, any f1, any f2, any minc, any maxc, any insf) -> void
```

## Description

Add a Fusion Summon procedure for c
Use 1 monster satisfying filter condition f1 and minc-maxc monsters satisfying filter condition f2 as Fusion Materials
Equivalent to aux.AddFusionProcMixRep(c, false, insf, f2, minc, maxc, f1)

## Parameters

- `c` `Card`
- `f1` `any`
- `f2` `any`
- `minc` `any`
- `maxc` `any`
- `insf` `any`

## Source

- `Utilities/procedure.lua:1313`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **10** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Auxiliary.AddFusionProcFunFunRep`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Flowering Etoile the Melodious Magnificat | `83793721` | [Scripts/c83793721.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c83793721.lua) | 60 |
| Dracotail Arthalion | `33760966` | [Scripts/c33760966.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c33760966.lua) | 56 |
| Dangerous Frightfur Nightmary | `58468105` | [Scripts/c58468105.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c58468105.lua) | 42 |
| GMX - COMPREX | `75191028` | [Scripts/c75191028.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c75191028.lua) | 42 |
| Wake Up Your Elemental HERO | `32828466` | [Scripts/c32828466.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c32828466.lua) | 40 |
| Primite Dragon Nether Berzelius | `26462013` | [Scripts/c26462013.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c26462013.lua) | 40 |
| Yubel - The Loving Defender Forever | `47172959` | [Scripts/c47172959.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c47172959.lua) | 39 |
| Frightfur Sabre-Tooth | `80889750` | [Scripts/c80889750.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c80889750.lua) | 37 |
| Bloom Prima the Melodious Choir | `24672164` | [Scripts/c24672164.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24672164.lua) | 33 |
| Chimeratech Megafleet Dragon | `87116928` | [Scripts/c87116928.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c87116928.lua) | 20 |

## Script Examples

### Flowering Etoile the Melodious Magnificat (`83793721`)

Source: [Scripts/c83793721.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c83793721.lua)

```lua
	--fusion material
	c:EnableReviveLimit()
	aux.AddFusionProcFunFunRep(c,aux.FilterBoolFunction(Card.IsFusionSetCard,0x109b),aux.FilterBoolFunction(Card.IsFusionSetCard,0x9b),2,2,true)
	--remove
	local e1=Effect.CreateEffect(c)
```

### Dracotail Arthalion (`33760966`)

Source: [Scripts/c33760966.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c33760966.lua)

```lua
function s.initial_effect(c)
	--fusion material
	aux.AddFusionProcFunFunRep(c,aux.FilterBoolFunction(Card.IsFusionSetCard,0x1c9),aux.FilterBoolFunction(Card.IsLocation,LOCATION_HAND),1,127,true)
	c:EnableReviveLimit()
	--tohand
```

### Dangerous Frightfur Nightmary (`58468105`)

Source: [Scripts/c58468105.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c58468105.lua)

```lua
	--fusion material
	c:EnableReviveLimit()
	aux.AddFusionProcFunFunRep(c,aux.FilterBoolFunction(Card.IsFusionSetCard,0xc3),aux.FilterBoolFunction(Card.IsFusionSetCard,0xa9),2,2,true)
	--atkup
	local e1=Effect.CreateEffect(c)
```
