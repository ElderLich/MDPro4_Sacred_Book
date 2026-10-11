# RushDuel.AttachDoubleTribute

Alias: `RD.AttachDoubleTribute`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.AttachDoubleTribute(any e, any card, any value, any desc, any reset, any forced) -> any
```

## Description

Rush Duel helper declared in `RDAttach.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
赋予: 双重解放
```

## Parameters

- `e` `any`: Type and behavior are not yet reviewed; see the source.
- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `value` `any`: Type and behavior are not yet reviewed; see the source.
- `desc` `any`: Type and behavior are not yet reviewed; see the source.
- `reset` `any`: Type and behavior are not yet reviewed; see the source.
- `forced` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDAttach.lua:42`

```lua
function RushDuel.AttachDoubleTribute(e, card, value, desc, reset, forced)
    return RushDuel.CreateSingleEffect(e, desc, card, EFFECT_DOUBLE_TRIBUTE, value, reset, forced)
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **30** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.AttachDoubleTribute) with `RushDuel.AttachDoubleTribute`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Darkness Doom Giant | `120253035` | [Rush/Scripts/c120253035.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120253035.lua) | 1 |
| Legendary Scout | `120271047` | [Rush/Scripts/c120271047.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120271047.lua) | 1 |
| Voidalfr Antromeda | `120300005` | [Rush/Scripts/c120300005.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120300005.lua) | 1 |
| Bikuribot | `120109043` | [Rush/Scripts/c120109043.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120109043.lua) | 1 |
| Cosmo Predictor | `120236001` | [Rush/Scripts/c120236001.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120236001.lua) | 1 |
| Furtunate Cat | `120246016` | [Rush/Scripts/c120246016.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120246016.lua) | 1 |
| Green-Eyes Star Cat | `120235015` | [Rush/Scripts/c120235015.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120235015.lua) | 1 |
| Spark Voltegg | `120246006` | [Rush/Scripts/c120246006.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120246006.lua) | 1 |
| Civil Twirider | `120304004` | [Rush/Scripts/c120304004.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120304004.lua) | 1 |
| Chaos Coolstars | `120277004` | [Rush/Scripts/c120277004.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120277004.lua) | 2 |
| Mamabot | `120285008` | [Rush/Scripts/c120285008.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120285008.lua) | 1 |
| OuTerverSe Needle Maker | `120290005` | [Rush/Scripts/c120290005.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120290005.lua) | 1 |
| Bluegrass Stealer | `120228022` | [Rush/Scripts/c120228022.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120228022.lua) | 1 |
| Footsoldier of Demolition | `120253011` | [Rush/Scripts/c120253011.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120253011.lua) | 1 |
| Dice Key Lilith | `120272009` | [Rush/Scripts/c120272009.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120272009.lua) | 1 |
| Excutie Power Up! | `120208052` | [Rush/Scripts/c120208052.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120208052.lua) | 1 |
| Lily Slayer | `120261008` | [Rush/Scripts/c120261008.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120261008.lua) | 1 |
| Hybridrive Scale | `120261003` | [Rush/Scripts/c120261003.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120261003.lua) | 1 |
| Double Twin Dragon | `120231051` | [Rush/Scripts/c120231051.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120231051.lua) | 1 |
| Royal Rebel's Guardian | `120254078` | [Rush/Scripts/c120254078.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120254078.lua) | 1 |
| Twin Coolstars | `120254075` | [Rush/Scripts/c120254075.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120254075.lua) | 1 |
| Delirium Teega | `120300025` | [Rush/Scripts/c120300025.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120300025.lua) | 1 |
| Researching the Clad Dragondom | `120304052` | [Rush/Scripts/c120304052.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120304052.lua) | 1 |
| Voidvelg Globule | `120227015` | [Rush/Scripts/c120227015.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120227015.lua) | 1 |
| ...and 6 more |  |  |  |

## Script Examples

### Darkness Doom Giant (`120253035`)

Source: [Rush/Scripts/c120253035.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120253035.lua)

```lua
		local c=e:GetHandler()
		if RD.SendToHandAndExists(g,e,tp,REASON_EFFECT) and c:IsFaceup() and c:IsRelateToEffect(e) then
			RD.AttachDoubleTribute(e,c,cm.trival,aux.Stringid(m,1),RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END)
			RD.AttachTripleTribute(e,c,cm.trival,aux.Stringid(m,2),aux.Stringid(m,3),RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END)
		end
```

### Legendary Scout (`120271047`)

Source: [Rush/Scripts/c120271047.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120271047.lua)

```lua
	local c=e:GetHandler()
	if c:IsFaceup() and c:IsRelateToEffect(e) then
		RD.AttachDoubleTribute(e,c,cm.trival,aux.Stringid(m,1),RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END)
	end
end
```

### Voidalfr Antromeda (`120300005`)

Source: [Rush/Scripts/c120300005.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120300005.lua)

```lua
	local c=e:GetHandler()
	if c:IsFaceup() and c:IsRelateToEffect(e) then
		RD.AttachDoubleTribute(e,c,cm.trival,aux.Stringid(m,2),RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END)
		RD.CanSelectAndDoAction(aux.Stringid(m,3),HINTMSG_ATOHAND,aux.NecroValleyFilter(cm.thfilter),tp,LOCATION_GRAVE,0,1,1,nil,function(g)
			RD.SendToHandAndExists(g,e,tp,REASON_EFFECT)
```
