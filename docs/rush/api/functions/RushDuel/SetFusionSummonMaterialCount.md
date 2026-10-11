# RushDuel.SetFusionSummonMaterialCount

Alias: `RD.SetFusionSummonMaterialCount`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.SetFusionSummonMaterialCount(any e, any min, any max) -> any
```

## Description

Rush Duel helper declared in `RDFusion.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
设置进行融合召唤的素材数量限制 (需要使用 Property 和 Label)
```

## Parameters

- `e` `any`: Type and behavior are not yet reviewed; see the source.
- `min` `any`: Type and behavior are not yet reviewed; see the source.
- `max` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDFusion.lua:608`

```lua
function RushDuel.SetFusionSummonMaterialCount(e, min, max)
    e:SetProperty(EFFECT_FLAG_SPSUM_PARAM)
    e:SetLabel(min, max)
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **6** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.SetFusionSummonMaterialCount) with `RushDuel.SetFusionSummonMaterialCount`.

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
function cm.activate(e,tp,eg,ep,ev,re,r,rp)
	if RD.SelectAndSpecialSummon(cm.filter,1-tp,LOCATION_GRAVE,0,1,1,nil,e,POS_FACEDOWN_DEFENSE)~=0 then
		RD.SetFusionSummonMaterialCount(e,2,2)
		RD.CanFusionSummon(aux.Stringid(m,1),aux.FALSE,nil,cm.exfilter,LOCATION_GRAVE,0,cm.matcheck,RD.FusionToDeck,e,tp,POS_FACEUP,true)
		RD.ResetFusionSummonMaterialCount(e)
```

### Handy Girl (`120290012`)

Source: [Rush/Scripts/c120290012.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120290012.lua)

```lua
		RD.SendToHandAndExists(g,e,tp,REASON_EFFECT)
		if not Duel.IsExistingMatchingCard(cm.exfilter,tp,LOCATION_MZONE,0,1,nil) then
			RD.SetFusionSummonMaterialCount(e,2,2)
			RD.CanFusionSummon(aux.Stringid(m,1),cm.matfilter,nil,nil,0,0,nil,RD.FusionToGrave,e,tp,POS_FACEUP)
			RD.ResetFusionSummonMaterialCount(e)
```

### Battletested Curse of Dragon (`120249031`)

Source: [Rush/Scripts/c120249031.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120249031.lua)

```lua
	if c:IsFaceup() and c:IsRelateToEffect(e) then
		RD.ChangeCode(e,c,list[1],RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END)
		RD.SetFusionSummonMaterialCount(e,2,2)
		RD.CanFusionSummon(aux.Stringid(m,2),cm.matfilter,nil,cm.exfilter,LOCATION_GRAVE,0,nil,RD.FusionToDeck,e,tp,POS_FACEUP,true,true)
		RD.ResetFusionSummonMaterialCount(e)
```
