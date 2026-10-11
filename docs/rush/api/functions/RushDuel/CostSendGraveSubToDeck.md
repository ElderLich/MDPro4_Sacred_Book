# RushDuel.CostSendGraveSubToDeck

Alias: `RD.CostSendGraveSubToDeck`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CostSendGraveSubToDeck(any filter, any check, any min, any max, any set_label_before, any set_object_before, any set_label_after, any set_object_after) -> any
```

## Description

Rush Duel helper declared in `RDCost.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
代价: 让墓地的卡返回卡组 (子卡片组)
```

## Parameters

- `filter` `any`: Type and behavior are not yet reviewed; see the source.
- `check` `any`: Type and behavior are not yet reviewed; see the source.
- `min` `any`: Type and behavior are not yet reviewed; see the source.
- `max` `any`: Type and behavior are not yet reviewed; see the source.
- `set_label_before` `any`: Type and behavior are not yet reviewed; see the source.
- `set_object_before` `any`: Type and behavior are not yet reviewed; see the source.
- `set_label_after` `any`: Type and behavior are not yet reviewed; see the source.
- `set_object_after` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCost.lua:449`

```lua
function RushDuel.CostSendGraveSubToDeck(filter, check, min, max, set_label_before, set_object_before, set_label_after,
    set_object_after)
    return RushDuel.CostSendGroupToDeckSort(filter, check, LOCATION_GRAVE, min, max, false, SEQ_DECKSHUFFLE, false,
        true, set_label_before, set_object_before, set_label_after, set_object_after)
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **26** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.CostSendGraveSubToDeck) with `RushDuel.CostSendGraveSubToDeck`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Voidalfr Star Mayfly](/examples/rush-cards/120300034) | `120300034` | [Rush/Scripts/c120300034.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120300034.lua) | 1 |
| [Fuden Issen](/examples/rush-cards/120309034) | `120309034` | [Rush/Scripts/c120309034.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120309034.lua) | 1 |
| [Sparkhearts Makma](/examples/rush-cards/120298023) | `120298023` | [Rush/Scripts/c120298023.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120298023.lua) | 1 |
| [Fairy of the Stars](/examples/rush-cards/120305016) | `120305016` | [Rush/Scripts/c120305016.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120305016.lua) | 1 |
| [Star Cat Destronya](/examples/rush-cards/120235037) | `120235037` | [Rush/Scripts/c120235037.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120235037.lua) | 1 |
| Abysslayer Quintiamat | `120257021` | [Rush/Scripts/c120257021.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120257021.lua) | 1 |
| Finalize Phoenix | `120231046` | [Rush/Scripts/c120231046.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120231046.lua) | 1 |
| Pholus the Star Knight | `120203020` | [Rush/Scripts/c120203020.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120203020.lua) | 1 |
| Constructor Sentry Dragline | `120247042` | [Rush/Scripts/c120247042.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120247042.lua) | 1 |
| Black Luster Soljersey - Envoy of the Drying | `120228017` | [Rush/Scripts/c120228017.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120228017.lua) | 1 |
| Voidvelg Chaosmachia | `120254019` | [Rush/Scripts/c120254019.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120254019.lua) | 1 |
| Magical Warrior of Heritage | `120285030` | [Rush/Scripts/c120285030.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120285030.lua) | 1 |
| Darkness Paparazzi | `120253009` | [Rush/Scripts/c120253009.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120253009.lua) | 1 |
| Strange Attractor | `120260017` | [Rush/Scripts/c120260017.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120260017.lua) | 1 |
| Necromaid Re:D | `120294045` | [Rush/Scripts/c120294045.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120294045.lua) | 1 |
| Player #99: Grand Slam Dragon | `120199027` | [Rush/Scripts/c120199027.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120199027.lua) | 1 |
| Necromaid Lurker | `120294044` | [Rush/Scripts/c120294044.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120294044.lua) | 1 |
| Splame | `120244027` | [Rush/Scripts/c120244027.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120244027.lua) | 1 |
| Excutie Scout! | `120231038` | [Rush/Scripts/c120231038.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120231038.lua) | 1 |
| Justiciar of the Dragon Stream | `120272029` | [Rush/Scripts/c120272029.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120272029.lua) | 1 |
| Endless Romance Blitz | `120205034` | [Rush/Scripts/c120205034.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120205034.lua) | 1 |
| Skull Flower | `120272030` | [Rush/Scripts/c120272030.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120272030.lua) | 1 |
| Ancient Barrier | `120155040` | [Rush/Scripts/c120155040.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120155040.lua) | 1 |
| Explorer of the Temple | `120280010` | [Rush/Scripts/c120280010.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120280010.lua) | 1 |
| ...and 2 more |  |  |  |

## Script Examples

### Voidalfr Star Mayfly (`120300034`)

Source: [Rush/Scripts/c120300034.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120300034.lua)

```lua
	return RD.IsSpecialSummonMainPhase(e:GetHandler(),SUMMON_TYPE_FUSION)
end
cm.cost=RD.CostSendGraveSubToDeck(cm.costfilter,cm.check,3,3)
function cm.target(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.IsExistingMatchingCard(cm.filter,tp,0,LOCATION_MZONE,1,nil) end
```

### Fuden Issen (`120309034`)

Source: [Rush/Scripts/c120309034.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120309034.lua)

```lua
	return eg:IsExists(cm.confilter,1,nil,1-tp)
end
cm.cost=RD.CostSendGraveSubToDeck(cm.costfilter,cm.check,2,2)
function cm.target(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.IsExistingMatchingCard(cm.filter,tp,0,LOCATION_MZONE,1,nil,e,tp) end
```

### Sparkhearts Makma (`120298023`)

Source: [Rush/Scripts/c120298023.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120298023.lua)

```lua
	end
end
cm.cost=RD.CostSendGraveSubToDeck(cm.costfilter,cm.check,2,4)
function cm.target(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.IsExistingMatchingCard(cm.posfilter,tp,LOCATION_MZONE,LOCATION_MZONE,1,nil,e,tp) end
```
