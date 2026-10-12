# RushDuel.FusionToDeck

Alias: `RD.FusionToDeck`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.FusionToDeck(any tp, any mat) -> any
```

## Description

Rush Duel helper declared in `RDFusion.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
素材去向: 卡组
```

## Parameters

- `tp` `any`: Type and behavior are not yet reviewed; see the source.
- `mat` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDFusion.lua:624`

```lua
function RushDuel.FusionToDeck(tp, mat)
    local g = mat:Filter(Card.IsFacedown, nil)
    if #g > 0 then
        Duel.ConfirmCards(1 - tp, g)
    end
    Duel.SendtoDeck(mat, nil, SEQ_DECKSHUFFLE, REASON_EFFECT + REASON_MATERIAL + REASON_FUSION)
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **34** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.FusionToDeck) with `RushDuel.FusionToDeck`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Hybridrive Back Fusion](/examples/rush-cards/120261052) | `120261052` | [Rush/Scripts/c120261052.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120261052.lua) | 1 |
| Rising HERO Argent O | `120304042` | [Rush/Scripts/c120304042.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120304042.lua) | 1 |
| Plandolin-a-la-Mode | `120264042` | [Rush/Scripts/c120264042.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120264042.lua) | 1 |
| Battletested Curse of Dragon | `120249031` | [Rush/Scripts/c120249031.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120249031.lua) | 1 |
| Ultra Evolution Miracle | `120274051` | [Rush/Scripts/c120274051.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120274051.lua) | 1 |
| OuTerverSe Detonation Fusion | `120290058` | [Rush/Scripts/c120290058.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120290058.lua) | 1 |
| Battletested Gaia The Fierce Knight | `120249032` | [Rush/Scripts/c120249032.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120249032.lua) | 1 |
| Princess Cosmos the Trickster | `120293046` | [Rush/Scripts/c120293046.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120293046.lua) | 1 |
| The Draco | `120294002` | [Rush/Scripts/c120294002.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120294002.lua) | 1 |
| Destructor Integration Scrap Gate | `120264053` | [Rush/Scripts/c120264053.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120264053.lua) | 1 |
| Void Dust Fusion | `120277052` | [Rush/Scripts/c120277052.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120277052.lua) | 1 |
| Flash Memory Fusion | `120285062` | [Rush/Scripts/c120285062.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120285062.lua) | 1 |
| Rising Equip | `120304062` | [Rush/Scripts/c120304062.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120304062.lua) | 1 |
| Dragon Tribe Fusion | `120238024` | [Rush/Scripts/c120238024.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120238024.lua) | 1 |
| Pulsating Cocoon of Evolution | `120298036` | [Rush/Scripts/c120298036.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120298036.lua) | 1 |
| Transam Nebula Fusion | `120272048` | [Rush/Scripts/c120272048.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120272048.lua) | 1 |
| Skullcrag Incursion | `120298015` | [Rush/Scripts/c120298015.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120298015.lua) | 1 |
| Speed Sniper | `120301060` | [Rush/Scripts/c120301060.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120301060.lua) | 2 |
| Road Apostle Slinger | `120285032` | [Rush/Scripts/c120285032.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120285032.lua) | 1 |
| Imaginary Arc Surge | `120271040` | [Rush/Scripts/c120271040.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120271040.lua) | 1 |
| Gateway to the Wooly Wunderworld | `120293025` | [Rush/Scripts/c120293025.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120293025.lua) | 1 |
| Princess Cosmos Stirs | `120293054` | [Rush/Scripts/c120293054.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120293054.lua) | 1 |
| Cyber Rush Fusion | `120278029` | [Rush/Scripts/c120278029.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120278029.lua) | 1 |
| Elemental HERO Voltic Wingman | `120277065` | [Rush/Scripts/c120277065.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120277065.lua) | 1 |
| ...and 10 more |  |  |  |

## Script Examples

### Hybridrive Back Fusion (`120261052`)

Source: [Rush/Scripts/c120261052.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120261052.lua)

```lua
	if RD.SelectAndSpecialSummon(cm.filter,1-tp,LOCATION_GRAVE,0,1,1,nil,e,POS_FACEDOWN_DEFENSE)~=0 then
		RD.SetFusionSummonMaterialCount(e,2,2)
		RD.CanFusionSummon(aux.Stringid(m,1),aux.FALSE,nil,cm.exfilter,LOCATION_GRAVE,0,cm.matcheck,RD.FusionToDeck,e,tp,POS_FACEUP,true)
		RD.ResetFusionSummonMaterialCount(e)
	end
```

### Rising HERO Argent O (`120304042`)

Source: [Rush/Scripts/c120304042.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120304042.lua)

```lua
	RD.SelectAndDoAction(HINTMSG_DESTROY,nil,tp,0,LOCATION_ONFIELD,1,1,nil,function(g)
		if Duel.Destroy(g,REASON_EFFECT)~=0 then
			RD.CanFusionSummon(aux.Stringid(m,1),aux.FALSE,cm.spfilter,cm.exfilter,LOCATION_GRAVE,0,nil,RD.FusionToDeck,e,tp,POS_FACEUP_ATTACK,true)
		end
	end)
```

### Plandolin-a-la-Mode (`120264042`)

Source: [Rush/Scripts/c120264042.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120264042.lua)

```lua
function cm.operation(e,te,tp,tc,mat,sumtype)
	if mat:IsExists(Card.IsLocation,1,nil,LOCATION_GRAVE) then
		RD.FusionToDeck(tp,mat)
	else
		RD.FusionToGrave(tp,mat)
```
