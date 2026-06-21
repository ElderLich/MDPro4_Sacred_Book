# Duel.IsPlayerCanDiscardDeckAsCost

## Signature

```lua
Duel.IsPlayerCanDiscardDeckAsCost(int player, int count) -> bool
```

## Description

Checks whether player can send count cards from the top of the Deck to the Graveyard as a cost.

## Parameters

- `player` `int`
- `count` `int`

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5046`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **26** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Duel.IsPlayerCanDiscardDeckAsCost`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Deep Sea Minstrel | `71978434` | [Scripts/c71978434.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71978434.lua) | 58 |
| Naturia Mole Cricket | `93454062` | [Scripts/c93454062.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93454062.lua) | 48 |
| Deep Sea Sentry | `45483489` | [Scripts/c45483489.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c45483489.lua) | 48 |
| Deep Sea Artisan | `8495780` | [Scripts/c8495780.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c8495780.lua) | 43 |
| Naturia Ladybug | `19605133` | [Scripts/c19605133.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c19605133.lua) | 39 |
| Dante, Traveler of the Burning Abyss | `83531441` | [Scripts/c83531441.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c83531441.lua) | 38 |
| Driangle, Dragon of the Dark Deep | `98248208` | [Scripts/c98248208.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c98248208.lua) | 37 |
| Mythical Bestiary | `38325384` | [Scripts/c38325384.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c38325384.lua) | 35 |
| Rainbow Neos | `86346643` | [Scripts/c86346643.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c86346643.lua) | 34 |
| Celestia, Lightsworn Angel | `94381039` | [Scripts/c94381039.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c94381039.lua) | 34 |
| Naturia Sunflower | `7478431` | [Scripts/c7478431.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c7478431.lua) | 34 |
| Cupid Volley | `11851647` | [Scripts/c11851647.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c11851647.lua) | 33 |
| Naturia Vein | `16940215` | [Scripts/c16940215.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c16940215.lua) | 33 |
| Naturia Horneedle | `84905691` | [Scripts/c84905691.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c84905691.lua) | 33 |
| Orbital Hydralander | `44009443` | [Scripts/c44009443.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44009443.lua) | 32 |
| Card Blocker | `42256406` | [Scripts/c42256406.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c42256406.lua) | 32 |
| Naturia Exterio | `99916754` | [Scripts/c99916754.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c99916754.lua) | 30 |
| Card Trooper | `85087012` | [Scripts/c85087012.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c85087012.lua) | 30 |
| Naturia Beast | `33198837` | [Scripts/c33198837.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c33198837.lua) | 28 |
| Hidden Armory | `52105192` | [Scripts/c52105192.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c52105192.lua) | 28 |
| Laval Blaster | `11834972` | [Scripts/c11834972.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c11834972.lua) | 26 |
| Battlin' Boxing Spirits | `36916401` | [Scripts/c36916401.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c36916401.lua) | 24 |
| Lightsworn Barrier | `22201234` | [Scripts/c22201234.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c22201234.lua) | 24 |
| Naturia Rock | `54161401` | [Scripts/c54161401.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c54161401.lua) | 20 |
| ...and 2 more |  |  |  |

## Script Examples

### Deep Sea Minstrel (`71978434`)

Source: [Scripts/c71978434.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71978434.lua)

```lua
end
function c71978434.tdcost(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.IsPlayerCanDiscardDeckAsCost(tp,3) end
	Duel.DiscardDeck(tp,3,REASON_COST)
end
```

### Naturia Mole Cricket (`93454062`)

Source: [Scripts/c93454062.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93454062.lua)

```lua
	local c=e:GetHandler()
	local fe=Duel.IsPlayerAffectedByEffect(tp,29942771)
	local b1=fe and Duel.IsPlayerCanDiscardDeckAsCost(tp,2) and Duel.GetMZoneCount(tp)>0
	local b2=c:IsReleasable() and Duel.GetMZoneCount(tp,c)>0
	if chk==0 then return b1 or b2 end
```

### Deep Sea Sentry (`45483489`)

Source: [Scripts/c45483489.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c45483489.lua)

```lua
end
function c45483489.thcost(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.IsPlayerCanDiscardDeckAsCost(tp,2) end
	Duel.DiscardDeck(tp,2,REASON_COST)
end
```
