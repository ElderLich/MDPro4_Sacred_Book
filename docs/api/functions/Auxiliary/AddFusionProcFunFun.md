# Auxiliary.AddFusionProcFunFun

## Signature

```lua
Auxiliary.AddFusionProcFunFun(Card c, function|table f1, function|table f2, int cc, bool insf) -> void
```

## Description

Registers a Fusion procedure requiring one material satisfying f1 and cc materials satisfying f2.

## Parameters

- `c` `Card`
- `f1` `function|table`
- `f2` `function|table`
- `cc` `int`
- `insf` `bool`

## Source

- `Utilities/procedure.lua:1305`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **7** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Auxiliary.AddFusionProcFunFun`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Ultimate Crystal Rainbow Dragon Overdrive](/examples/cards/84544192) | `84544192` | [Scripts/c84544192.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c84544192.lua) | 1 |
| Blue-Eyes Toon Ultimate Dragon | `71808988` | [Scripts/c71808988.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71808988.lua) | 1 |
| Necroquip Princess | `93860227` | [Scripts/c93860227.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93860227.lua) | 1 |
| Cyber Eternity Dragon | `82315403` | [Scripts/c82315403.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c82315403.lua) | 1 |
| Phantom of Yubel | `80453041` | [Scripts/c80453041.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c80453041.lua) | 1 |
| Denial Deity Dotan | `12890860` | [Scripts/c12890860.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c12890860.lua) | 1 |
| Metalfoes Crimsonite | `54401832` | [Scripts/c54401832.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c54401832.lua) | 1 |

## Script Examples

### Ultimate Crystal Rainbow Dragon Overdrive (`84544192`)

Source: [Scripts/c84544192.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c84544192.lua)

```lua
	--fusion material
	c:EnableReviveLimit()
	aux.AddFusionProcFunFun(c,aux.FilterBoolFunction(Card.IsFusionSetCard,0x2034),aux.FilterBoolFunction(Card.IsFusionSetCard,0x1034),7,true)
	--cannot special summon
	local e0=Effect.CreateEffect(c)
```

### Blue-Eyes Toon Ultimate Dragon (`71808988`)

Source: [Scripts/c71808988.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71808988.lua)

```lua
	aux.AddMaterialCodeList(c,53183600)
	aux.AddSetNameMonsterList(c,0x62)
	aux.AddFusionProcFunFun(c,aux.FilterBoolFunction(Card.IsFusionCode,53183600),s.ffilter,2,true)
	aux.AddContactFusionProcedure(c,s.cfilter,LOCATION_HAND+LOCATION_MZONE+LOCATION_GRAVE,0,aux.ContactFusionSendToDeck(c))
	--cannot special summon
```

### Necroquip Princess (`93860227`)

Source: [Scripts/c93860227.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93860227.lua)

```lua
	c:SetUniqueOnField(1,0,id)
	c:EnableReviveLimit()
	aux.AddFusionProcFunFun(c,s.ffilter1,s.ffilter2,1,true)
	aux.AddContactFusionProcedure(c,Card.IsAbleToGraveAsCost,LOCATION_ONFIELD+LOCATION_HAND,0,Duel.SendtoGrave,REASON_COST)
	--special summon condition
```
