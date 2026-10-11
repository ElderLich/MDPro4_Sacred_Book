# RushDuel.CostSendGraveToDeckBottom

Alias: `RD.CostSendGraveToDeckBottom`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CostSendGraveToDeckBottom(any filter, any min, any max, any set_label_before, any set_object_before, any set_label_after, any set_object_after) -> any
```

## Description

Rush Duel helper declared in `RDCost.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
代价: 让墓地的卡返回卡组下面
```

## Parameters

- `filter` `any`: Type and behavior are not yet reviewed; see the source.
- `min` `any`: Type and behavior are not yet reviewed; see the source.
- `max` `any`: Type and behavior are not yet reviewed; see the source.
- `set_label_before` `any`: Type and behavior are not yet reviewed; see the source.
- `set_object_before` `any`: Type and behavior are not yet reviewed; see the source.
- `set_label_after` `any`: Type and behavior are not yet reviewed; see the source.
- `set_object_after` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCost.lua:467`

```lua
function RushDuel.CostSendGraveToDeckBottom(filter, min, max, set_label_before, set_object_before, set_label_after,
    set_object_after)
    return RushDuel.CostSendMatchToDeckSort(filter, LOCATION_GRAVE, min, max, false, SEQ_DECKBOTTOM, false, true,
        set_label_before, set_object_before, set_label_after, set_object_after)
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **43** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.CostSendGraveToDeckBottom) with `RushDuel.CostSendGraveToDeckBottom`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Player #C39: Home Run Smasher V](/examples/rush-cards/120305028) | `120305028` | [Rush/Scripts/c120305028.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120305028.lua) | 1 |
| Lostream Reading | `120309043` | [Rush/Scripts/c120309043.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120309043.lua) | 1 |
| Voidalfr Star Stripe | `120300033` | [Rush/Scripts/c120300033.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120300033.lua) | 1 |
| Etraynze the Shadow Flower Restricter | `120254041` | [Rush/Scripts/c120254041.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120254041.lua) | 1 |
| Legendary Saber | `120238010` | [Rush/Scripts/c120238010.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120238010.lua) | 1 |
| Ritche of Hope | `120287072` | [Rush/Scripts/c120287072.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120287072.lua) | 1 |
| Star Sanctuary of Beginning | `120305027` | [Rush/Scripts/c120305027.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120305027.lua) | 1 |
| Shadow Flower Bedazzlement | `120285064` | [Rush/Scripts/c120285064.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120285064.lua) | 1 |
| Ice Age Catapult | `120170013` | [Rush/Scripts/c120170013.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120170013.lua) | 1 |
| Sea Dragon Kleindros | `120199031` | [Rush/Scripts/c120199031.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120199031.lua) | 1 |
| Wyrm Excavator the Heavy Cavalry Draco \[R\] | `120155023` | [Rush/Scripts/c120155023.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120155023.lua) | 1 |
| Twilight Companion - Dralia | `120304068` | [Rush/Scripts/c120304068.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120304068.lua) | 1 |
| Infernal Flame Emperor | `120109045` | [Rush/Scripts/c120109045.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120109045.lua) | 1 |
| Buried Shield | `120205060` | [Rush/Scripts/c120205060.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120205060.lua) | 1 |
| Dragon Roll the Sushi Fairy | `120151040` | [Rush/Scripts/c120151040.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120151040.lua) | 1 |
| Animagica Whip | `120277031` | [Rush/Scripts/c120277031.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120277031.lua) | 1 |
| Jinzo #7.7 | `120257026` | [Rush/Scripts/c120257026.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120257026.lua) | 1 |
| Mazera, Devil of the Den | `120290036` | [Rush/Scripts/c120290036.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120290036.lua) | 1 |
| Garland the True Shadow Flower Ninja | `120170031` | [Rush/Scripts/c120170031.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120170031.lua) | 1 |
| New Start | `120277061` | [Rush/Scripts/c120277061.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120277061.lua) | 1 |
| Kuzuha the Talismanic Master | `120228039` | [Rush/Scripts/c120228039.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120228039.lua) | 1 |
| Freed the Brave Wanderer | `120263013` | [Rush/Scripts/c120263013.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120263013.lua) | 1 |
| Offering to the Archfiend | `120277055` | [Rush/Scripts/c120277055.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120277055.lua) | 1 |
| Insurrection Dragon | `120155016` | [Rush/Scripts/c120155016.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120155016.lua) | 1 |
| ...and 19 more |  |  |  |

## Script Examples

### Player #C39: Home Run Smasher V (`120305028`)

Source: [Rush/Scripts/c120305028.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120305028.lua)

```lua
	return RD.IsSpecialSummonMainPhase(e:GetHandler())
end
cm.cost=RD.CostSendGraveToDeckBottom(cm.costfilter,1,1)
function cm.target(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.IsExistingMatchingCard(nil,tp,0,LOCATION_MZONE,1,nil) end
```

### Lostream Reading (`120309043`)

Source: [Rush/Scripts/c120309043.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120309043.lua)

```lua
	return RD.IsPlayerNoActivateInThisTurn(tp,list[1])
end
cm.cost=RD.CostSendGraveToDeckBottom(cm.costfilter,2,2)
function cm.target(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.IsExistingMatchingCard(cm.filter,tp,LOCATION_SZONE,0,1,nil) end
```

### Voidalfr Star Stripe (`120300033`)

Source: [Rush/Scripts/c120300033.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120300033.lua)

```lua
	return RD.IsSpecialSummonMainPhase(e:GetHandler(),SUMMON_TYPE_FUSION)
end
cm.cost=RD.CostSendGraveToDeckBottom(cm.costfilter,1,1,nil,nil,function(g)
	return g:GetSum(Card.GetLevel)
end)
```
