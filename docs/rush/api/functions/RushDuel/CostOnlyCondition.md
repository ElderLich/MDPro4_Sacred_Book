# RushDuel.CostOnlyCondition

Alias: `RD.CostOnlyCondition`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CostOnlyCondition(any condition) -> any
```

## Description

Rush Duel helper declared in `RDCost.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
代价: 只有条件
```

## Parameters

- `condition` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCost.lua:140`

```lua
function RushDuel.CostOnlyCondition(condition)
    return function(e, tp, eg, ep, ev, re, r, rp, chk)
        return condition(e, tp, eg, ep, ev, re, r, rp, chk)
    end
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **1** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.CostOnlyCondition) with `RushDuel.CostOnlyCondition`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Ace Sword Slash | `120294052` | [Rush/Scripts/c120294052.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120294052.lua) | 1 |

## Script Examples

### Ace Sword Slash (`120294052`)

Source: [Rush/Scripts/c120294052.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120294052.lua)

```lua
end
cm.cost1=RD.CostSendHandToGrave(Card.IsAbleToGraveAsCost,2,2)
cm.cost2=RD.CostOnlyCondition(cm.condition)
cm.cost=RD.CostChoose(aux.Stringid(m,0),cm.cost1,aux.Stringid(m,1),cm.cost2)
function cm.target(e,tp,eg,ep,ev,re,r,rp,chk)
```
