# RushDuel.AttachTripleTribute

Alias: `RD.AttachTripleTribute`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.AttachTripleTribute(any e, any card, any value, any desc1, any desc2, any reset, any forced) -> any
```

## Description

Rush Duel helper declared in `RDAttach.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
赋予: 三重解放
```

## Parameters

- `e` `any`: Type and behavior are not yet reviewed; see the source.
- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `value` `any`: Type and behavior are not yet reviewed; see the source.
- `desc1` `any`: Type and behavior are not yet reviewed; see the source.
- `desc2` `any`: Type and behavior are not yet reviewed; see the source.
- `reset` `any`: Type and behavior are not yet reviewed; see the source.
- `forced` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDAttach.lua:46`

```lua
function RushDuel.AttachTripleTribute(e, card, value, desc1, desc2, reset, forced)
    local e1 = RushDuel.CreateSingleEffect(e, desc1, card, EFFECT_TRIPLE_TRIBUTE, value, reset, forced)
    local e2 = RushDuel.CreateTripleTribute(e:GetHandler(), card, desc2, value, forced)
    e2:SetReset(reset)
    return e1, e2
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **1** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.AttachTripleTribute) with `RushDuel.AttachTripleTribute`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Darkness Doom Giant | `120253035` | [Rush/Scripts/c120253035.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120253035.lua) | 1 |

## Script Examples

### Darkness Doom Giant (`120253035`)

Source: [Rush/Scripts/c120253035.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120253035.lua)

```lua
		if RD.SendToHandAndExists(g,e,tp,REASON_EFFECT) and c:IsFaceup() and c:IsRelateToEffect(e) then
			RD.AttachDoubleTribute(e,c,cm.trival,aux.Stringid(m,1),RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END)
			RD.AttachTripleTribute(e,c,cm.trival,aux.Stringid(m,2),aux.Stringid(m,3),RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END)
		end
	end)
```
