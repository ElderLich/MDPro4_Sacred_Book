# RushDuel.FusionSummon

Alias: `RD.FusionSummon`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.FusionSummon(any matfilter, any spfilter, any exfilter, any s_range, any o_range, any mat_check, any mat_move, any e, any tp, any pos, any break_effect, any including_self, any self_leave) -> any
```

## Description

Rush Duel helper declared in `RDFusion.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
强制进行融合召唤
```

## Parameters

- `matfilter` `any`: Type and behavior are not yet reviewed; see the source.
- `spfilter` `any`: Type and behavior are not yet reviewed; see the source.
- `exfilter` `any`: Type and behavior are not yet reviewed; see the source.
- `s_range` `any`: Type and behavior are not yet reviewed; see the source.
- `o_range` `any`: Type and behavior are not yet reviewed; see the source.
- `mat_check` `any`: Type and behavior are not yet reviewed; see the source.
- `mat_move` `any`: Type and behavior are not yet reviewed; see the source.
- `e` `any`: Type and behavior are not yet reviewed; see the source.
- `tp` `any`: Type and behavior are not yet reviewed; see the source.
- `pos` `any`: Type and behavior are not yet reviewed; see the source.
- `break_effect` `any`: Type and behavior are not yet reviewed; see the source.
- `including_self` `any`: Type and behavior are not yet reviewed; see the source.
- `self_leave` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDFusion.lua:570`

```lua
function RushDuel.FusionSummon(matfilter, spfilter, exfilter, s_range, o_range, mat_check, mat_move, e, tp, pos, break_effect, including_self, self_leave)
    local include = including_self or false
    local leave = self_leave or false
    RushDuel.FusionExtraChecker = RushDuel.FusionCheckLocation(e, self_leave, mat_check)
    local fusionable, list, chkf, gc = RushDuel.GetFusionSummonData(e, tp, pos, matfilter, spfilter, exfilter, s_range, o_range, include, leave, nil, e)
    local fc = nil
    if fusionable then
        if break_effect then
            Duel.BreakEffect()
        end
        fc = RushDuel.ExecuteFusionSummon(e, tp, pos, list, chkf, gc, mat_move)
    end
    RushDuel.FusionExtraChecker = nil
    return fc
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **1** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.FusionSummon) with `RushDuel.FusionSummon`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Dice Key Mix | `120272007` | [Rush/Scripts/c120272007.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120272007.lua) | 1 |

## Script Examples

### Dice Key Mix (`120272007`)

Source: [Rush/Scripts/c120272007.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120272007.lua)

```lua
		end)
	elseif d>=2 and d<=6 then
		local fc=RD.FusionSummon(cm.matfilter,nil,nil,0,0,nil,RD.FusionToGrave,e,tp,POS_FACEUP)
		if fc and fc:IsFaceup() and d==5 or d==6 then
			RD.AttachEffectIndes(e,fc,cm.indval,aux.Stringid(m,1),RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END)
```
