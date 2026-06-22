# Auxiliary.AddFusionProcCode2FunRep

## Signature

```lua
Auxiliary.AddFusionProcCode2FunRep(Card c, int|table code1, int|table code2, function|table f, int minc, int maxc, bool sub, bool insf) -> void
```

## Description

Registers a Fusion Material procedure requiring code1, code2, and between minc and maxc additional materials that satisfy f.

## Parameters

- `c` `Card`
- `code1` `int|table`
- `code2` `int|table`
- `f` `function|table`
- `minc` `int`
- `maxc` `int`
- `sub` `bool`
- `insf` `bool`

## Source

- `Utilities/procedure.lua:1336`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **1** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Auxiliary.AddFusionProcCode2FunRep`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Infernoid Tierra | `82734805` | [Scripts/c82734805.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c82734805.lua) | 34 |

## Script Examples

### Infernoid Tierra (`82734805`)

Source: [Scripts/c82734805.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c82734805.lua)

```lua
	--fusion material
	c:EnableReviveLimit()
	aux.AddFusionProcCode2FunRep(c,14799437,23440231,aux.FilterBoolFunction(Card.IsFusionSetCard,0xbb),1,127,true,true)
	--spsummon success
	local e2=Effect.CreateEffect(c)
```
