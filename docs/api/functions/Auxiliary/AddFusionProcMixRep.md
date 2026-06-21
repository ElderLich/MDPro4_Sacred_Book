# Auxiliary.AddFusionProcMixRep

## Signature

```lua
Auxiliary.AddFusionProcMixRep(Card fcard, bool sub, bool insf, number|function|table fun1, int minc, int maxc, ... number|function|table) -> void
```

## Description

Add a Fusion Summon procedure for c
Use minc-maxc monsters satisfying f1 and 1 of each monster in the additional parameters as Fusion Materials
Additional parameters can be function or card code (int code), where passing a code is equivalent to passing function(code) return c:IsFusionCode(code) end

## Parameters

- `fcard` `Card`
- `sub` `bool` - Can be fusion summoned with substitute material
- `insf` `bool` - Can be fusion summoned with no material (Instant Fusion)
- `fun1` `number|function|table`
- `minc` `int`
- `maxc` `int`
- `...` `number|function|table`

## Source

- `Utilities/procedure.lua:991`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **1** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Auxiliary.AddFusionProcMixRep`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Elemental HERO Divine Neos | `31111109` | [Scripts/c31111109.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c31111109.lua) | 41 |

## Script Examples

### Elemental HERO Divine Neos (`31111109`)

Source: [Scripts/c31111109.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c31111109.lua)

```lua
	--fusion material
	c:EnableReviveLimit()
	aux.AddFusionProcMixRep(c,true,true,c31111109.ffilter,2,2,c31111109.ffilter1,c31111109.ffilter2,c31111109.ffilter3)
	--copy
	local e2=Effect.CreateEffect(c)
```
