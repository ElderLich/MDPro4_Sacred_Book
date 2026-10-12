# RushDuel.CannotSpecialSummon

Alias: `RD.CannotSpecialSummon`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CannotSpecialSummon(any card, any range) -> any
```

## Description

Rush Duel helper declared in `RDBase.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
创建效果: 这张卡不能特殊召唤
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `range` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDBase.lua:73`

```lua
function RushDuel.CannotSpecialSummon(card, range)
    local e1 = Effect.CreateEffect(card)
    e1:SetType(EFFECT_TYPE_SINGLE)
    e1:SetCode(EFFECT_SPSUMMON_CONDITION)
    if range then
        e1:SetProperty(EFFECT_FLAG_CANNOT_DISABLE + EFFECT_FLAG_UNCOPYABLE + EFFECT_FLAG_SINGLE_RANGE)
        e1:SetRange(range)
    else
        e1:SetProperty(EFFECT_FLAG_CANNOT_DISABLE + EFFECT_FLAG_UNCOPYABLE)
    end
    card:RegisterEffect(e1)
    return e1
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **7** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.CannotSpecialSummon) with `RushDuel.CannotSpecialSummon`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Gilford the Legend | `120235029` | [Rush/Scripts/c120235029.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120235029.lua) | 1 |
| Infernal Flame Emperor | `120109045` | [Rush/Scripts/c120109045.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120109045.lua) | 1 |
| The Creator | `120205000` | [Rush/Scripts/c120205000.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120205000.lua) | 1 |
| Gilford the Rising | `120235028` | [Rush/Scripts/c120235028.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120235028.lua) | 1 |
| Vanity's Fiend | `120238008` | [Rush/Scripts/c120238008.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120238008.lua) | 1 |
| Ancient Gear Golem | `120271004` | [Rush/Scripts/c120271004.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120271004.lua) | 1 |
| Ancient Gear Beast | `120271007` | [Rush/Scripts/c120271007.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120271007.lua) | 1 |

## Script Examples

### Gilford the Legend (`120235029`)

Source: [Rush/Scripts/c120235029.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120235029.lua)

```lua
function cm.initial_effect(c)
	--Cannot Special Summon
	RD.CannotSpecialSummon(c)
	--Equip
	local e1=Effect.CreateEffect(c)
```

### Infernal Flame Emperor (`120109045`)

Source: [Rush/Scripts/c120109045.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120109045.lua)

```lua
function cm.initial_effect(c)
	--Cannot Special Summon
	RD.CannotSpecialSummon(c)
	--Destroy
	local e1=Effect.CreateEffect(c)
```

### The Creator (`120205000`)

Source: [Rush/Scripts/c120205000.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120205000.lua)

```lua
function cm.initial_effect(c)
	--Cannot Special Summon
	RD.CannotSpecialSummon(c,LOCATION_GRAVE)
	--Special Summon
	local e1=Effect.CreateEffect(c)
```
