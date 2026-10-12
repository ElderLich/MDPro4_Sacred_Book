# RushDuel.IsPreviousCode

Alias: `RD.IsPreviousCode`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.IsPreviousCode(any card, any code) -> any
```

## Description

Rush Duel helper declared in `RDCondition.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
条件: 位置变化前的类型
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `code` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCondition.lua:194`

```lua
function RushDuel.IsPreviousCode(card, code)
    return card:GetPreviousCodeOnField() == code
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **1** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.IsPreviousCode) with `RushDuel.IsPreviousCode`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Archfiend's Revival | `120170062` | [Rush/Scripts/c120170062.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120170062.lua) | 1 |

## Script Examples

### Archfiend's Revival (`120170062`)

Source: [Rush/Scripts/c120170062.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120170062.lua)

```lua
--Activate
function cm.confilter(c,tp)
	return (RD.IsLegendCode(c,list[1]) or RD.IsPreviousCode(c,list[1]) or (
			RD.IsPreviousType(c,TYPE_NORMAL) and RD.IsPreviousLevelAbove(c,7) and RD.IsPreviousRace(c,RACE_FIEND)
		)) and RD.IsPreviousControler(c,tp) and c==Duel.GetAttackTarget()
```
