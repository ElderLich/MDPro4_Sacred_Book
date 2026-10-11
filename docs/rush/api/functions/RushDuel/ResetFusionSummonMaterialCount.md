# RushDuel.ResetFusionSummonMaterialCount

Alias: `RD.ResetFusionSummonMaterialCount`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.ResetFusionSummonMaterialCount(any e) -> any
```

## Description

Rush Duel helper declared in `RDFusion.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
重置进行融合召唤的素材数量限制 (需要使用 Property 和 Label)
```

## Parameters

- `e` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDFusion.lua:614`

```lua
function RushDuel.ResetFusionSummonMaterialCount(e)
    e:SetProperty(0)
    e:SetLabel(0)
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **6** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.ResetFusionSummonMaterialCount) with `RushDuel.ResetFusionSummonMaterialCount`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Hybridrive Back Fusion](/examples/rush-cards/120261052) | `120261052` | [Rush/Scripts/c120261052.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120261052.lua) | 1 |
| [Handy Girl](/examples/rush-cards/120290012) | `120290012` | [Rush/Scripts/c120290012.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120290012.lua) | 1 |
| Battletested Curse of Dragon | `120249031` | [Rush/Scripts/c120249031.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120249031.lua) | 1 |
| Ultra Evolution Miracle | `120274051` | [Rush/Scripts/c120274051.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120274051.lua) | 1 |
| Battletested Gaia The Fierce Knight | `120249032` | [Rush/Scripts/c120249032.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120249032.lua) | 1 |
| Princess Cosmos the Trickster | `120293046` | [Rush/Scripts/c120293046.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120293046.lua) | 1 |

## Script Examples

### Hybridrive Back Fusion (`120261052`)

Source: [Rush/Scripts/c120261052.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120261052.lua)

```lua
		RD.SetFusionSummonMaterialCount(e,2,2)
		RD.CanFusionSummon(aux.Stringid(m,1),aux.FALSE,nil,cm.exfilter,LOCATION_GRAVE,0,cm.matcheck,RD.FusionToDeck,e,tp,POS_FACEUP,true)
		RD.ResetFusionSummonMaterialCount(e)
	end
	if Duel.GetFlagEffect(tp,m)~=0 then return end
```

### Handy Girl (`120290012`)

Source: [Rush/Scripts/c120290012.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120290012.lua)

```lua
			RD.SetFusionSummonMaterialCount(e,2,2)
			RD.CanFusionSummon(aux.Stringid(m,1),cm.matfilter,nil,nil,0,0,nil,RD.FusionToGrave,e,tp,POS_FACEUP)
			RD.ResetFusionSummonMaterialCount(e)
		end
	end)
```

### Battletested Curse of Dragon (`120249031`)

Source: [Rush/Scripts/c120249031.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120249031.lua)

```lua
		RD.SetFusionSummonMaterialCount(e,2,2)
		RD.CanFusionSummon(aux.Stringid(m,2),cm.matfilter,nil,cm.exfilter,LOCATION_GRAVE,0,nil,RD.FusionToDeck,e,tp,POS_FACEUP,true,true)
		RD.ResetFusionSummonMaterialCount(e)
	end
end
```
