# RushDuel.IsSameCode

Alias: `RD.IsSameCode`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.IsSameCode(any card1, any card2) -> any
```

## Description

Rush Duel helper declared in `RDLegend.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
条件: 是否为同名卡
```

## Parameters

- `card1` `any`: Type and behavior are not yet reviewed; see the source.
- `card2` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDLegend.lua:36`

```lua
function RushDuel.IsSameCode(card1, card2)
    return card1:IsCode(card2:GetCode())
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **6** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.IsSameCode) with `RushDuel.IsSameCode`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| The Dragiastar | `120235035` | [Rush/Scripts/c120235035.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120235035.lua) | 2 |
| Back To The Fusion | `120235047` | [Rush/Scripts/c120235047.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120235047.lua) | 2 |
| Dragon Double-Doom | `120235060` | [Rush/Scripts/c120235060.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120235060.lua) | 1 |
| Sea Dragon Knight | `120199032` | [Rush/Scripts/c120199032.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120199032.lua) | 1 |
| The Copy | `120235046` | [Rush/Scripts/c120235046.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120235046.lua) | 1 |
| Bislasher | `120235048` | [Rush/Scripts/c120235048.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120235048.lua) | 1 |

## Script Examples

### The Dragiastar (`120235035`)

Source: [Rush/Scripts/c120235035.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120235035.lua)

```lua
end
function cm.confilter2(c,tc)
	return c:IsType(TYPE_NORMAL) and RD.IsSameCode(c,tc)
end
function cm.check(g)
```

### Back To The Fusion (`120235047`)

Source: [Rush/Scripts/c120235047.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120235047.lua)

```lua
end
function cm.exfilter(c,tc)
	return c:IsType(TYPE_NORMAL) and RD.IsSameCode(c,tc)
end
function cm.check(g)
```

### Dragon Double-Doom (`120235060`)

Source: [Rush/Scripts/c120235060.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120235060.lua)

```lua
end
function cm.check(g)
	return g:GetCount()==2 and RD.IsSameCode(g:GetFirst(),g:GetNext())
end
function cm.condition(e,tp,eg,ep,ev,re,r,rp)
```
