# RushDuel.IsCanAttachDisableContinuous

Alias: `RD.IsCanAttachDisableContinuous`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.IsCanAttachDisableContinuous(any card) -> any
```

## Description

Rush Duel helper declared in `RDCondition.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
条件: 可否赋予效果 - 永续效果无效化
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDCondition.lua:346`

```lua
function RushDuel.IsCanAttachDisableContinuous(card)
    return RushDuel.IsHasContinuousEffect(card) and not card:IsHasEffect(EFFECT_DISABLE)
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **1** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.IsCanAttachDisableContinuous) with `RushDuel.IsCanAttachDisableContinuous`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Darkness Galactica Oblivion | `120253036` | [Rush/Scripts/c120253036.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120253036.lua) | 1 |

## Script Examples

### Darkness Galactica Oblivion (`120253036`)

Source: [Rush/Scripts/c120253036.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120253036.lua)

```lua
		local atk=tc:GetBaseAttack()
		RD.AttachAtkDef(e,tc,-atk,0,RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END)
		if RD.IsCanAttachDisableContinuous(tc) and Duel.SelectYesNo(tp,aux.Stringid(m,2)) then
			RD.AttachDisableContinuous(e,tc,aux.Stringid(m,3),RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END)
		end
```
