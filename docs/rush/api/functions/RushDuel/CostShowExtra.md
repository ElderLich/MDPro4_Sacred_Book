# RushDuel.CostShowExtra

Alias: `RD.CostShowExtra`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CostShowExtra(any filter, any min, any max, any set_label, any set_object) -> any
```

## Description

Rush Duel helper declared in `RDCost.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
代价: 把额外卡组给对方观看
```

## Parameters

- `filter` `any`: Type and behavior are not yet reviewed; see the source.
- `min` `any`: Type and behavior are not yet reviewed; see the source.
- `max` `any`: Type and behavior are not yet reviewed; see the source.
- `set_label` `any`: Type and behavior are not yet reviewed; see the source.
- `set_object` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCost.lua:224`

```lua
function RushDuel.CostShowExtra(filter, min, max, set_label, set_object)
    return RushDuel._private_cost_select_match(HINTMSG_CONFIRM, filter, LOCATION_EXTRA, 0, min, max, false,
        function(g, e, tp, eg, ep, ev, re, r, rp)
            RushDuel.SetLabelAndObject(e, g, set_label, set_object)
            Duel.ConfirmCards(1 - tp, g)
        end)
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **9** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.CostShowExtra) with `RushDuel.CostShowExtra`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Instant Gift](/examples/rush-cards/120306059) | `120306059` | [Rush/Scripts/c120306059.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120306059.lua) | 1 |
| [The Noodle Art of Flavor Shift](/examples/rush-cards/120300053) | `120300053` | [Rush/Scripts/c120300053.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120300053.lua) | 1 |
| Variable Stellariser | `120277007` | [Rush/Scripts/c120277007.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120277007.lua) | 1 |
| Rising HERO Argent | `120263010` | [Rush/Scripts/c120263010.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120263010.lua) | 1 |
| Accel Wonder Dark | `120285005` | [Rush/Scripts/c120285005.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120285005.lua) | 1 |
| Rare Dragorite | `120294008` | [Rush/Scripts/c120294008.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120294008.lua) | 1 |
| Light-Calling Griffore | `120280008` | [Rush/Scripts/c120280008.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120280008.lua) | 1 |
| Phantasm Maskmaster | `120271028` | [Rush/Scripts/c120271028.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120271028.lua) | 1 |
| Elemental HERO Prisma | `120272065` | [Rush/Scripts/c120272065.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120272065.lua) | 1 |

## Script Examples

### Instant Gift (`120306059`)

Source: [Rush/Scripts/c120306059.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120306059.lua)

```lua
	return c:IsCode(code) and RD.IsCanBeSpecialSummoned(c,e,tp,POS_FACEUP)
end
cm.cost=RD.CostShowExtra(cm.costfilter,1,1,nil,Group.GetFirst)
function cm.target(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.GetMZoneCount(tp)>0 end
```

### The Noodle Art of Flavor Shift (`120300053`)

Source: [Rush/Scripts/c120300053.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120300053.lua)

```lua
	return RD.IsPlayerNoActivateInThisTurn(tp,list[1])
end
cm.cost=RD.CostShowExtra(cm.costfilter,1,1,nil,Group.GetFirst)
function cm.target(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return true end
```

### Variable Stellariser (`120277007`)

Source: [Rush/Scripts/c120277007.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120277007.lua)

```lua
		and RD.IsCanAnnounceFusionMaterialCode(e:GetHandler(),c)
end
cm.cost=RD.CostShowExtra(cm.costfilter,1,1,nil,Group.GetFirst)
function cm.target(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return true end
```
