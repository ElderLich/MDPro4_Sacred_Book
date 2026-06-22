# Duel.CheckPhaseActivity

## Signature

```lua
Duel.CheckPhaseActivity() -> bool
```

## Description

Returns whether an action has been recorded for the current phase.

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5067`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **25** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Duel.CheckPhaseActivity`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Ghostrick Renovation](/examples/cards/61818176) | `61818176` | [Scripts/c61818176.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c61818176.lua) | 65 |
| Favorite Hero | `11881272` | [Scripts/c11881272.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c11881272.lua) | 55 |
| Numeron Wall | `42352091` | [Scripts/c42352091.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c42352091.lua) | 50 |
| Rank-Up-Magic - The Seventh One | `57734012` | [Scripts/c57734012.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c57734012.lua) | 40 |
| Daidara-Bocchi | `69133798` | [Scripts/c69133798.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c69133798.lua) | 38 |
| Pot of Dichotomy | `98672567` | [Scripts/c98672567.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c98672567.lua) | 38 |
| Piri Reis Map | `33907039` | [Scripts/c33907039.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c33907039.lua) | 37 |
| Fish and Bids | `74271714` | [Scripts/c74271714.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74271714.lua) | 37 |
| Gordian Slicer | `66236707` | [Scripts/c66236707.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c66236707.lua) | 34 |
| Pot of Extravagance | `49238328` | [Scripts/c49238328.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c49238328.lua) | 33 |
| Metaverse | `89208725` | [Scripts/c89208725.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c89208725.lua) | 33 |
| Steelswarm Scout | `90727556` | [Scripts/c90727556.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c90727556.lua) | 31 |
| Abyss Actors' Dress Rehearsal | `6004133` | [Scripts/c6004133.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c6004133.lua) | 30 |
| Summon Over | `48015771` | [Scripts/c48015771.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c48015771.lua) | 28 |
| Pop-Up | `15248873` | [Scripts/c15248873.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c15248873.lua) | 28 |
| Mimir of the Nordic Ascendant | `76348260` | [Scripts/c76348260.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c76348260.lua) | 27 |
| Magical Mid-Breaker Field | `71650854` | [Scripts/c71650854.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71650854.lua) | 23 |
| Gravekeeper's Inscription | `59494222` | [Scripts/c59494222.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59494222.lua) | 21 |
| Bujin Regalia - The Mirror | `35183853` | [Scripts/c35183853.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c35183853.lua) | 20 |
| Soundproofed | `42314669` | [Scripts/c42314669.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c42314669.lua) | 17 |
| Cold Wave | `60682203` | [Scripts/c60682203.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c60682203.lua) | 17 |
| Heat Wave | `45141013` | [Scripts/c45141013.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c45141013.lua) | 17 |
| Amabie | `2139640` | [Scripts/c2139640.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c2139640.lua) | 16 |
| Quiet Life | `31980955` | [Scripts/c31980955.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c31980955.lua) | 15 |
| ...and 1 more |  |  |  |

## Script Examples

### Ghostrick Renovation (`61818176`)

Source: [Scripts/c61818176.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c61818176.lua)

```lua
	if chkc then return false end
	if chk==0 then return tc and tc:IsFaceup() and tc:IsSetCard(0x8d) and tc:IsAbleToHand() and tc:IsCanBeEffectTarget(e) end
	if not Duel.CheckPhaseActivity() then e:SetLabel(1) else e:SetLabel(0) end
	Duel.SetTargetCard(tc)
	Duel.SetOperationInfo(0,CATEGORY_TOHAND,tc,1,0,0)
```

### Favorite Hero (`11881272`)

Source: [Scripts/c11881272.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c11881272.lua)

```lua
function c11881272.acttg(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.IsExistingMatchingCard(c11881272.actfilter,tp,LOCATION_HAND+LOCATION_DECK,0,1,nil,tp) end
	if not Duel.CheckPhaseActivity() then e:SetLabel(1) else e:SetLabel(0) end
end
function c11881272.actop(e,tp,eg,ep,ev,re,r,rp)
```

### Numeron Wall (`42352091`)

Source: [Scripts/c42352091.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c42352091.lua)

```lua
function c42352091.acttg(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.IsExistingMatchingCard(c42352091.actfilter,tp,LOCATION_HAND+LOCATION_DECK,0,1,nil,tp) end
	if not Duel.CheckPhaseActivity() then e:SetLabel(1) else e:SetLabel(0) end
end
function c42352091.actop(e,tp,eg,ep,ev,re,r,rp)
```
