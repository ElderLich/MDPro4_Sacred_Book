# RushDuel.RitualToDeck

Alias: `RD.RitualToDeck`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.RitualToDeck(any tp, any mat) -> any
```

## Description

Rush Duel helper declared in `RDRitual.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

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

`Rush/Utilities/RDRitual.lua:445`

```lua
function RushDuel.RitualToDeck(tp, mat)
    local g = mat:Filter(Card.IsFacedown, nil)
    if #g > 0 then
        Duel.ConfirmCards(1 - tp, g)
    end
    Duel.SendtoDeck(mat, nil, SEQ_DECKSHUFFLE, REASON_EFFECT + REASON_MATERIAL + REASON_RITUAL)
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **2** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.RitualToDeck) with `RushDuel.RitualToDeck`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| The Eternal Land -Spectrika- | `120300052` | [Rush/Scripts/c120300052.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120300052.lua) | 1 |
| Endless Partner | `120300050` | [Rush/Scripts/c120300050.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120300050.lua) | 1 |

## Script Examples

### The Eternal Land -Spectrika- (`120300052`)

Source: [Rush/Scripts/c120300052.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120300052.lua)

```lua
end
function cm.operation(e,te,tp,tc,mat,sumtype)
	RD.RitualToDeck(tp,mat)
end
```

### Endless Partner (`120300050`)

Source: [Rush/Scripts/c120300050.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120300050.lua)

```lua
function cm.initial_effect(c)
	--Activate
	local e1=RD.CreateRitualEffect(c,RITUAL_CURRENT_LEVEL_EQUAL,cm.matfilter,cm.spfilter,nil,0,0,nil,RD.RitualToDeck,nil,cm.operation)
	e1:SetCategory(CATEGORY_SPECIAL_SUMMON)
	e1:SetType(EFFECT_TYPE_ACTIVATE)
```
