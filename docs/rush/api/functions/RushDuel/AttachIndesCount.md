# RushDuel.AttachIndesCount

Alias: `RD.AttachIndesCount`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.AttachIndesCount(any e, any card, any count, any value, any desc, any reset, any forced) -> any
```

## Description

Rush Duel helper declared in `RDAttach.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
赋予: 战斗, 效果破坏抗性 (有次数限制)
```

## Parameters

- `e` `any`: Type and behavior are not yet reviewed; see the source.
- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `count` `any`: Type and behavior are not yet reviewed; see the source.
- `value` `any`: Type and behavior are not yet reviewed; see the source.
- `desc` `any`: Type and behavior are not yet reviewed; see the source.
- `reset` `any`: Type and behavior are not yet reviewed; see the source.
- `forced` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDAttach.lua:85`

```lua
function RushDuel.AttachIndesCount(e, card, count, value, desc, reset, forced)
    local e1 = RushDuel.CreateSingleEffect(e, desc, card, EFFECT_INDESTRUCTABLE_COUNT, value, reset, forced)
    e1:SetCountLimit(count)
    return e1
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **1** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.AttachIndesCount) with `RushDuel.AttachIndesCount`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Insurrection Dragon | `120155016` | [Rush/Scripts/c120155016.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120155016.lua) | 1 |

## Script Examples

### Insurrection Dragon (`120155016`)

Source: [Rush/Scripts/c120155016.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120155016.lua)

```lua
		local atk=Duel.GetFieldGroupCount(tp,LOCATION_MZONE,LOCATION_MZONE)*700
		RD.AttachAtkDef(e,c,atk,0,RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END)
		RD.AttachIndesCount(e,c,1,cm.indval,aux.Stringid(m,1),RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END)
	end
end
```
