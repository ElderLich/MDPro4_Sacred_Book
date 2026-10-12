# Auxiliary.ContactFusionSendToDeck

## Signature

```lua
Auxiliary.ContactFusionSendToDeck(Card c) -> function
```

## Description

Returns a Contact Fusion material operation that reveals face-down materials when needed, hints Graveyard/banished materials, and shuffles all materials into the Deck as cost.

## Parameters

- `c` `Card`

## Returns

- `function` - Material operation that shuffles materials into the Deck.

## Source

- `Utilities/procedure.lua:1734`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **23** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Auxiliary.ContactFusionSendToDeck) with `Auxiliary.ContactFusionSendToDeck`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Gladiator Beast Gaiodiaz | `90957527` | [Scripts/c90957527.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c90957527.lua) | 1 |
| Gladiator Beast Gyzarus | `48156348` | [Scripts/c48156348.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c48156348.lua) | 1 |
| Blue-Eyes Toon Ultimate Dragon | `71808988` | [Scripts/c71808988.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c71808988.lua) | 1 |
| Gladiator Beast Claudius | `48958757` | [Scripts/c48958757.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c48958757.lua) | 1 |
| Gladiator Beast Andabata | `3779662` | [Scripts/c3779662.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c3779662.lua) | 1 |
| Gladiator Beast Domitianus | `33652635` | [Scripts/c33652635.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c33652635.lua) | 1 |
| Gladiator Beast Tamer Editor | `30864377` | [Scripts/c30864377.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c30864377.lua) | 1 |
| Gladiator Beast Nerokius | `29357956` | [Scripts/c29357956.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c29357956.lua) | 1 |
| Phantom of Yubel | `80453041` | [Scripts/c80453041.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c80453041.lua) | 1 |
| Elemental HERO Nebula Neos | `40080312` | [Scripts/c40080312.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c40080312.lua) | 1 |
| Elemental HERO Chaos Neos | `17032740` | [Scripts/c17032740.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c17032740.lua) | 1 |
| Elemental HERO Glow Neos | `85507811` | [Scripts/c85507811.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c85507811.lua) | 1 |
| Elemental HERO Cosmo Neos | `90050480` | [Scripts/c90050480.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c90050480.lua) | 1 |
| Elemental HERO Dark Neos | `28677304` | [Scripts/c28677304.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c28677304.lua) | 1 |
| Gladiator Beast Heraklinos | `27346636` | [Scripts/c27346636.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c27346636.lua) | 1 |
| Elemental HERO Storm Neos | `49352945` | [Scripts/c49352945.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c49352945.lua) | 1 |
| Elemental HERO Magma Neos | `78512663` | [Scripts/c78512663.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c78512663.lua) | 1 |
| Elemental HERO Grand Neos | `48996569` | [Scripts/c48996569.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c48996569.lua) | 1 |
| Elemental HERO Aqua Neos | `55171412` | [Scripts/c55171412.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c55171412.lua) | 1 |
| Elemental HERO Marine Neos | `5128859` | [Scripts/c5128859.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c5128859.lua) | 1 |
| Elemental HERO Air Neos | `11502550` | [Scripts/c11502550.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c11502550.lua) | 1 |
| Elemental HERO Flare Neos | `81566151` | [Scripts/c81566151.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c81566151.lua) | 1 |
| Gladiator Beast Essedarii | `73285669` | [Scripts/c73285669.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c73285669.lua) | 1 |

## Script Examples

### Gladiator Beast Gaiodiaz (`90957527`)

Source: [Scripts/c90957527.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c90957527.lua)

```lua
	c:EnableReviveLimit()
	aux.AddFusionProcCodeFun(c,79580323,aux.FilterBoolFunction(Card.IsFusionSetCard,0x1019),1,true,true)
	aux.AddContactFusionProcedure(c,c90957527.cfilter,LOCATION_ONFIELD,0,aux.ContactFusionSendToDeck(c))
	--spsummon condition
	local e1=Effect.CreateEffect(c)
```

### Gladiator Beast Gyzarus (`48156348`)

Source: [Scripts/c48156348.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c48156348.lua)

```lua
	c:EnableReviveLimit()
	aux.AddFusionProcCodeFun(c,41470137,aux.FilterBoolFunction(Card.IsFusionSetCard,0x1019),1,true,true)
	aux.AddContactFusionProcedure(c,c48156348.cfilter,LOCATION_ONFIELD,0,aux.ContactFusionSendToDeck(c))
	--spsummon condition
	local e1=Effect.CreateEffect(c)
```

### Blue-Eyes Toon Ultimate Dragon (`71808988`)

Source: [Scripts/c71808988.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c71808988.lua)

```lua
	aux.AddSetNameMonsterList(c,0x62)
	aux.AddFusionProcFunFun(c,aux.FilterBoolFunction(Card.IsFusionCode,53183600),s.ffilter,2,true)
	aux.AddContactFusionProcedure(c,s.cfilter,LOCATION_HAND+LOCATION_MZONE+LOCATION_GRAVE,0,aux.ContactFusionSendToDeck(c))
	--cannot special summon
	local e1=Effect.CreateEffect(c)
```
