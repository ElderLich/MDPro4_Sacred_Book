# RushDuel.IsPreviousAttack

Alias: `RD.IsPreviousAttack`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.IsPreviousAttack(any card, any atk) -> any
```

## Description

Rush Duel helper declared in `RDCondition.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
条件: 位置变化前的攻击力
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `atk` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCondition.lua:222`

```lua
function RushDuel.IsPreviousAttack(card, atk)
    return card:GetPreviousAttackOnField() == atk
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **1** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.IsPreviousAttack) with `RushDuel.IsPreviousAttack`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Collapsing Chairs | `120150041` | [Rush/Scripts/c120150041.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120150041.lua) | 1 |

## Script Examples

### Collapsing Chairs (`120150041`)

Source: [Rush/Scripts/c120150041.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120150041.lua)

```lua
		and c:IsPreviousPosition(POS_FACEUP_ATTACK)
		and RD.IsPreviousAttribute(c,ATTRIBUTE_DARK)
		and RD.IsPreviousAttack(c,0)
end
function cm.desfilter(c)
```
