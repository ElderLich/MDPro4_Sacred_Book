# Auxiliary.AddFusionProcFunRep2

## Signature

```lua
Auxiliary.AddFusionProcFunRep2(Card c, function|table f, int minc, int maxc, bool insf) -> void
```

## Description

Registers a Fusion procedure requiring between minc and maxc materials that satisfy f.

## Parameters

- `c` `Card`
- `f` `function|table`
- `minc` `int`
- `maxc` `int`
- `insf` `bool`

## Source

- `Utilities/procedure.lua:1296`

## Guided Examples

Learn how to use this function in context:

- [Fusion Procedure Guide](/learn/fusion-procedure)

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **4** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Auxiliary.AddFusionProcFunRep2) with `Auxiliary.AddFusionProcFunRep2`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Worm Zero | `74506079` | [Scripts/c74506079.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c74506079.lua) | 1 |
| Charmers of the Grand Circle | `48016074` | [Scripts/c48016074.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c48016074.lua) | 1 |
| Chimeratech Rampage Dragon | `84058253` | [Scripts/c84058253.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c84058253.lua) | 1 |
| Extox Hydra | `26050548` | [Scripts/c26050548.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c26050548.lua) | 1 |

## Script Examples

### Worm Zero (`74506079`)

Source: [Scripts/c74506079.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c74506079.lua)

```lua
	--fusion material
	c:EnableReviveLimit()
	aux.AddFusionProcFunRep2(c,c74506079.ffilter,2,127,true)
	--summon success
	local e2=Effect.CreateEffect(c)
```

### Charmers of the Grand Circle (`48016074`)

Source: [Scripts/c48016074.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c48016074.lua)

```lua
	--fusion material
	c:EnableReviveLimit()
	aux.AddFusionProcFunRep2(c,s.ffilter,2,127,true)
	--summon success
	local e1=Effect.CreateEffect(c)
```

### Chimeratech Rampage Dragon (`84058253`)

Source: [Scripts/c84058253.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c84058253.lua)

```lua
	--fusion material
	c:EnableReviveLimit()
	aux.AddFusionProcFunRep2(c,aux.FilterBoolFunction(Card.IsFusionSetCard,0x1093),2,127,false)
	--destroy
	local e2=Effect.CreateEffect(c)
```
