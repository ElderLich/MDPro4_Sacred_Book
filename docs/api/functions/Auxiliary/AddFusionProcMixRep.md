# Auxiliary.AddFusionProcMixRep

## Signature

```lua
Auxiliary.AddFusionProcMixRep(Card fcard, bool sub, bool insf, number|function|table fun1, int minc, int maxc, ... number|function|table) -> void
```

## Description

Registers a mixed Fusion Material procedure with one repeated slot and any number of fixed slots.
fun1 is the repeated material requirement used minc to maxc times; additional arguments are fixed requirements. Each requirement may be a card code, filter function, or table of card codes and filters.

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
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Auxiliary.AddFusionProcMixRep) with `Auxiliary.AddFusionProcMixRep`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Elemental HERO Divine Neos | `31111109` | [Scripts/c31111109.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c31111109.lua) | 1 |

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
