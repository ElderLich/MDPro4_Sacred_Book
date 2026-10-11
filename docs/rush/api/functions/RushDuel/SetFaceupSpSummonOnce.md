# RushDuel.SetFaceupSpSummonOnce

Alias: `RD.SetFaceupSpSummonOnce`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.SetFaceupSpSummonOnce(any code, any hint) -> any
```

## Description

Rush Duel helper declared in `RDBase.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
创建效果: 这个卡名1回合只能有1次表侧表示的特殊召唤
```

## Parameters

- `code` `any`: Type and behavior are not yet reviewed; see the source.
- `hint` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDBase.lua:102`

```lua
function RushDuel.SetFaceupSpSummonOnce(code, hint)
    local filter = function (c, p)
        return c:IsFaceup() and c:IsCode(code) and c:GetSummonPlayer() == p
    end
    local sumlimit = function (e, c, sump, sumtype, sumpos, targetp, se)
        return c:IsCode(code) and sumpos&POS_FACEUP == POS_FACEUP
    end
    local e=Effect.GlobalEffect()
    e:SetType(EFFECT_TYPE_FIELD+EFFECT_TYPE_CONTINUOUS)
    e:SetCode(EVENT_SPSUMMON_SUCCESS)
    e:SetOperation(function (e, tp, eg, ep, ev, re, r, rp)
        if eg:IsExists(filter, 1, nil, 0) then
            RD.CreateCannotSpecialSummonEffect(e, hint, sumlimit, 0, 1, 0, RESET_PHASE + PHASE_END)
        end
        if eg:IsExists(filter, 1, nil, 1) then
            RD.CreateCannotSpecialSummonEffect(e, hint, sumlimit, 1, 1, 0, RESET_PHASE + PHASE_END)
        end
    end)
    Duel.RegisterEffect(e,0)
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **1** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.SetFaceupSpSummonOnce) with `RushDuel.SetFaceupSpSummonOnce`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [The Black Witch Facing the Temple](/examples/rush-cards/120309048) | `120309048` | [Rush/Scripts/c120309048.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120309048.lua) | 1 |

## Script Examples

### The Black Witch Facing the Temple (`120309048`)

Source: [Rush/Scripts/c120309048.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120309048.lua)

```lua
	RD.AddCodeList(c,list)
	--Special Summon Once
	RD.SetFaceupSpSummonOnce(list[1],aux.Stringid(m,0))
	--Special Summon Procedure
	RD.AddHandSpecialSummonProcedure(c,aux.Stringid(m,1),cm.spcon,cm.sptg,cm.spop)
```
