# RushDuel.FusionToDeckBottom

Alias: `RD.FusionToDeckBottom`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.FusionToDeckBottom(any tp, any mat) -> any
```

## Description

Rush Duel helper declared in `RDFusion.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
素材去向: 卡组下面
```

## Parameters

- `tp` `any`: Type and behavior are not yet reviewed; see the source.
- `mat` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDFusion.lua:632`

```lua
function RushDuel.FusionToDeckBottom(tp, mat)
    local g = mat:Filter(Card.IsFacedown, nil)
    if #g > 0 then
        Duel.ConfirmCards(1 - tp, g)
    end
    Auxiliary.PlaceCardsOnDeckBottom(tp, mat, REASON_EFFECT + REASON_MATERIAL + REASON_FUSION)
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **4** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.FusionToDeckBottom) with `RushDuel.FusionToDeckBottom`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Slay the Star Protector's Gunslinger | `120306010` | [Rush/Scripts/c120306010.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120306010.lua) | 1 |
| Y-Trial Dragon | `120305009` | [Rush/Scripts/c120305009.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120305009.lua) | 1 |
| Z-Trial Tank | `120305010` | [Rush/Scripts/c120305010.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120305010.lua) | 1 |
| Miracle Fusion | `120263031` | [Rush/Scripts/c120263031.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120263031.lua) | 1 |

## Script Examples

### Slay the Star Protector's Gunslinger (`120306010`)

Source: [Rush/Scripts/c120306010.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120306010.lua)

```lua
	if RD.SendDeckTopToGraveAndExists(tp,1,cm.filter,1,nil)
		and c:IsFaceup() and c:IsRelateToEffect(e) then
		RD.CanFusionSummon(aux.Stringid(m,1),cm.matfilter,cm.spfilter,cm.exfilter,LOCATION_GRAVE,0,nil,RD.FusionToDeckBottom,e,tp,POS_FACEUP,true,true)
	end
end
```

### Y-Trial Dragon (`120305009`)

Source: [Rush/Scripts/c120305009.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120305009.lua)

```lua
	if c:IsFaceup() and c:IsRelateToEffect(e) then
		RD.ChangeCode(e,c,list[1],RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END)
		RD.CanFusionSummon(aux.Stringid(m,1),cm.matfilter,cm.spfilter,cm.exfilter,LOCATION_GRAVE,0,nil,RD.FusionToDeckBottom,e,tp,POS_FACEUP,true,true)
	end
end
```

### Z-Trial Tank (`120305010`)

Source: [Rush/Scripts/c120305010.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120305010.lua)

```lua
	if c:IsFaceup() and c:IsRelateToEffect(e) then
		RD.ChangeCode(e,c,list[1],RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END)
		RD.CanFusionSummon(aux.Stringid(m,1),cm.matfilter,cm.spfilter,cm.exfilter,LOCATION_GRAVE,0,nil,RD.FusionToDeckBottom,e,tp,POS_FACEUP,true,true)
	end
end
```
