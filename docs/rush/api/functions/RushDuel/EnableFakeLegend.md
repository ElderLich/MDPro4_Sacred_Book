# RushDuel.EnableFakeLegend

Alias: `RD.EnableFakeLegend`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.EnableFakeLegend(any card, any location) -> any
```

## Description

Rush Duel helper declared in `RDLegend.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
当作传说卡 (赝品)
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `location` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDLegend.lua:63`

```lua
function RushDuel.EnableFakeLegend(card, location)
    local e1 = Effect.CreateEffect(card)
    e1:SetType(EFFECT_TYPE_SINGLE)
    e1:SetCode(EFFECT_LEGEND_CARD)
    e1:SetProperty(EFFECT_FLAG_CANNOT_DISABLE + EFFECT_FLAG_UNCOPYABLE + EFFECT_FLAG_SET_AVAILABLE + EFFECT_FLAG_SINGLE_RANGE)
    e1:SetRange(location)
    e1:SetValue(0)
    card:RegisterEffect(e1, true)
    return e1
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **15** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.EnableFakeLegend) with `RushDuel.EnableFakeLegend`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Fate of the World | `120271054` | [Rush/Scripts/c120271054.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120271054.lua) | 1 |
| Grand Legendary Priest | `120271043` | [Rush/Scripts/c120271043.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120271043.lua) | 1 |
| Reminiscence of the Epic Tale | `120272054` | [Rush/Scripts/c120272054.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120272054.lua) | 1 |
| Grand Legendar Saber Spirit | `120293067` | [Rush/Scripts/c120293067.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120293067.lua) | 1 |
| Legendary Lineage Saber | `120285049` | [Rush/Scripts/c120285049.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120285049.lua) | 1 |
| Grand Legendary Party | `120309060` | [Rush/Scripts/c120309060.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120309060.lua) | 1 |
| Grand Legendary Saber | `120271041` | [Rush/Scripts/c120271041.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120271041.lua) | 1 |
| Grand Legendary Magician | `120271042` | [Rush/Scripts/c120271042.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120271042.lua) | 1 |
| Legendary Priest | `120271044` | [Rush/Scripts/c120271044.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120271044.lua) | 1 |
| Legendary Party | `120309061` | [Rush/Scripts/c120309061.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120309061.lua) | 1 |
| Legendary Necromancer | `120293066` | [Rush/Scripts/c120293066.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120293066.lua) | 1 |
| Ancient Final Battle | `120271050` | [Rush/Scripts/c120271050.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120271050.lua) | 1 |
| Legend Possessed | `120293068` | [Rush/Scripts/c120293068.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120293068.lua) | 1 |
| Legendary Lineage Magician | `120293065` | [Rush/Scripts/c120293065.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120293065.lua) | 1 |
| Legendary Advent | `120285059` | [Rush/Scripts/c120285059.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120285059.lua) | 1 |

## Script Examples

### Fate of the World (`120271054`)

Source: [Rush/Scripts/c120271054.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120271054.lua)

```lua
function cm.initial_effect(c)
	--Fake Legend
	RD.EnableFakeLegend(c,LOCATION_HAND+LOCATION_GRAVE)
	--Activate
	local e1=Effect.CreateEffect(c)
```

### Grand Legendary Priest (`120271043`)

Source: [Rush/Scripts/c120271043.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120271043.lua)

```lua
	RD.AddCodeList(c,list)
	--Fake Legend
	RD.EnableFakeLegend(c,LOCATION_HAND+LOCATION_GRAVE)
	--Destroy
	local e1=Effect.CreateEffect(c)
```

### Reminiscence of the Epic Tale (`120272054`)

Source: [Rush/Scripts/c120272054.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120272054.lua)

```lua
function cm.initial_effect(c)
	--Fake Legend
	RD.EnableFakeLegend(c,LOCATION_HAND+LOCATION_GRAVE)
	--Activate
	local e1=Effect.CreateEffect(c)
```
