# RushDuel.IsPreviousAttackAbove

Alias: `RD.IsPreviousAttackAbove`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.IsPreviousAttackAbove(any card, any atk) -> any
```

## Description

Rush Duel helper declared in `RDCondition.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
条件: 位置变化前的攻击力大于
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `atk` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCondition.lua:226`

```lua
function RushDuel.IsPreviousAttackAbove(card, atk)
    return card:GetPreviousAttackOnField() >= atk
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **1** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.IsPreviousAttackAbove) with `RushDuel.IsPreviousAttackAbove`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Dark Nebula | `120235059` | [Rush/Scripts/c120235059.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120235059.lua) | 1 |

## Script Examples

### Dark Nebula (`120235059`)

Source: [Rush/Scripts/c120235059.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120235059.lua)

```lua
		and RD.IsPreviousAttribute(c,ATTRIBUTE_DARK)
		and RD.IsPreviousRace(c,RACE_GALAXY)
		and RD.IsPreviousAttackAbove(c,1500)
end
function cm.spfilter(c,e,tp)
```
