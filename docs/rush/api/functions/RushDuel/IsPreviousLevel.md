# RushDuel.IsPreviousLevel

Alias: `RD.IsPreviousLevel`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.IsPreviousLevel(any card, any level) -> any
```

## Description

Rush Duel helper declared in `RDCondition.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
条件: 位置变化前的等级
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `level` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCondition.lua:210`

```lua
function RushDuel.IsPreviousLevel(card, level)
    return card:GetPreviousLevelOnField() == level
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **1** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.IsPreviousLevel) with `RushDuel.IsPreviousLevel`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Executie Emergency! | `120231040` | [Rush/Scripts/c120231040.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120231040.lua) | 1 |

## Script Examples

### Executie Emergency! (`120231040`)

Source: [Rush/Scripts/c120231040.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120231040.lua)

```lua
--Activate
function cm.confilter(c,tp,rp)
	return c:IsPreviousPosition(POS_FACEUP) and RD.IsPreviousLevel(c,6)
		and RD.IsPreviousControler(c,tp) and c:IsPreviousLocation(LOCATION_MZONE)
		and ((rp==1-tp and c:IsReason(REASON_EFFECT)) or c==Duel.GetAttackTarget())
```
