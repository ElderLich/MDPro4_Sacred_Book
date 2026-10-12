# RushDuel.AttachCannotBeRitualMaterial

Alias: `RD.AttachCannotBeRitualMaterial`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.AttachCannotBeRitualMaterial(any e, any card, any value, any desc, any reset, any forced) -> any
```

## Description

Rush Duel helper declared in `RDAttach.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
赋予: 不能作为仪式术召唤的素材
```

## Parameters

- `e` `any`: Type and behavior are not yet reviewed; see the source.
- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `value` `any`: Type and behavior are not yet reviewed; see the source.
- `desc` `any`: Type and behavior are not yet reviewed; see the source.
- `reset` `any`: Type and behavior are not yet reviewed; see the source.
- `forced` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDAttach.lua:190`

```lua
function RushDuel.AttachCannotBeRitualMaterial(e, card, value, desc, reset, forced)
    return RushDuel.CreateSingleEffect(e, desc, card, EFFECT_CANNOT_BE_RITUAL_MATERIAL, value, reset, forced)
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **1** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.AttachCannotBeRitualMaterial) with `RushDuel.AttachCannotBeRitualMaterial`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Necromaid Trickment](/examples/rush-cards/120294063) | `120294063` | [Rush/Scripts/c120294063.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120294063.lua) | 1 |

## Script Examples

### Necromaid Trickment (`120294063`)

Source: [Rush/Scripts/c120294063.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120294063.lua)

```lua
			local e1=RD.AttachCannotTribute(e,tc,cm.sumlimit,aux.Stringid(m,1),RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END)
			e1:SetLabel(tp)
			local e2=RD.AttachCannotBeRitualMaterial(e,tc,cm.ritlimit,aux.Stringid(m,2),RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END)
			e2:SetLabel(tp)
		end)
```
