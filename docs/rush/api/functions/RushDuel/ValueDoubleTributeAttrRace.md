# RushDuel.ValueDoubleTributeAttrRace

Alias: `RD.ValueDoubleTributeAttrRace`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.ValueDoubleTributeAttrRace(any attribute, any race, any ignore) -> any
```

## Description

Rush Duel helper declared in `RDValue.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
效果值: 双重解放 属性/种族
```

## Parameters

- `attribute` `any`: Type and behavior are not yet reviewed; see the source.
- `race` `any`: Type and behavior are not yet reviewed; see the source.
- `ignore` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDValue.lua:65`

```lua
function RushDuel.ValueDoubleTributeAttrRace(attribute, race, ignore)
    return RushDuel.ValueDoubleTributeMix(ignore, nil, attribute, nil, nil, race, nil, nil)
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **21** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.ValueDoubleTributeAttrRace) with `RushDuel.ValueDoubleTributeAttrRace`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Voidalfr Antromeda | `120300005` | [Rush/Scripts/c120300005.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120300005.lua) | 1 |
| Spark Voltegg | `120246006` | [Rush/Scripts/c120246006.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120246006.lua) | 1 |
| Civil Twirider | `120304004` | [Rush/Scripts/c120304004.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120304004.lua) | 1 |
| Cat in Cobra's Clothing | `120276001` | [Rush/Scripts/c120276001.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120276001.lua) | 1 |
| Mamabot | `120285008` | [Rush/Scripts/c120285008.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120285008.lua) | 1 |
| Bluegrass Stealer | `120228022` | [Rush/Scripts/c120228022.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120228022.lua) | 1 |
| Footsoldier of Demolition | `120253011` | [Rush/Scripts/c120253011.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120253011.lua) | 1 |
| Dice Key Lilith | `120272009` | [Rush/Scripts/c120272009.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120272009.lua) | 1 |
| Lily Slayer | `120261008` | [Rush/Scripts/c120261008.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120261008.lua) | 1 |
| Hybridrive Scale | `120261003` | [Rush/Scripts/c120261003.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120261003.lua) | 1 |
| Royal Rebel's Guardian | `120254078` | [Rush/Scripts/c120254078.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120254078.lua) | 1 |
| Twin Coolstars | `120254075` | [Rush/Scripts/c120254075.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120254075.lua) | 1 |
| Delirium Teega | `120300025` | [Rush/Scripts/c120300025.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120300025.lua) | 1 |
| Researching the Clad Dragondom | `120304052` | [Rush/Scripts/c120304052.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120304052.lua) | 1 |
| Voidvelg Globule | `120227015` | [Rush/Scripts/c120227015.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120227015.lua) | 1 |
| Dododo Second | `120199025` | [Rush/Scripts/c120199025.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120199025.lua) | 1 |
| Ultimate Flag Beast Surge Bicorn | `120181011` | [Rush/Scripts/c120181011.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120181011.lua) | 1 |
| Blasting Bird | `120170033` | [Rush/Scripts/c120170033.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120170033.lua) | 1 |
| Card 120135002 | `120135002` | [Rush/Scripts/c120135002.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120135002.lua) | 1 |
| Necromaid Guard | `120294012` | [Rush/Scripts/c120294012.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120294012.lua) | 1 |
| Flame Ruler | `120223103` | [Rush/Scripts/c120223103.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120223103.lua) | 1 |

## Script Examples

### Voidalfr Antromeda (`120300005`)

Source: [Rush/Scripts/c120300005.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120300005.lua)

```lua
end
--Extra Tribute
cm.trival=RD.ValueDoubleTributeAttrRace(nil,RACE_GALAXY)
function cm.thfilter(c)
	return c:IsCode(list[1]) and c:IsAbleToHand()
```

### Spark Voltegg (`120246006`)

Source: [Rush/Scripts/c120246006.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120246006.lua)

```lua
end
--Extra Tribute
cm.trival=RD.ValueDoubleTributeAttrRace(ATTRIBUTE_LIGHT,RACE_WINDBEAST)
function cm.costfilter(c)
	return c:IsAttribute(ATTRIBUTE_LIGHT) and c:IsAbleToDeckOrExtraAsCost()
```

### Civil Twirider (`120304004`)

Source: [Rush/Scripts/c120304004.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120304004.lua)

```lua
end
--Extra Tribute
cm.trival=RD.ValueDoubleTributeAttrRace(ATTRIBUTE_LIGHT,RACE_GALAXY)
function cm.costfilter(c)
	return c:IsRace(RACE_GALAXY) and c:IsAbleToDeckOrExtraAsCost()
```
