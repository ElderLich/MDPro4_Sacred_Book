# RushDuel.SelectAndToHandOrSpecialSummon

Alias: `RD.SelectAndToHandOrSpecialSummon`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.SelectAndToHandOrSpecialSummon(any hint, any filter, any tp, any s_range, any o_range, any expect, any e, any pos, any break_effect, any target_player) -> any
```

## Description

Rush Duel helper declared in `RDAction.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
操作: 选择怪兽加入手卡或者特殊召唤 (限定 1 只怪兽)
```

## Parameters

- `hint` `any`: Type and behavior are not yet reviewed; see the source.
- `filter` `any`: Type and behavior are not yet reviewed; see the source.
- `tp` `any`: Type and behavior are not yet reviewed; see the source.
- `s_range` `any`: Type and behavior are not yet reviewed; see the source.
- `o_range` `any`: Type and behavior are not yet reviewed; see the source.
- `expect` `any`: Type and behavior are not yet reviewed; see the source.
- `e` `any`: Type and behavior are not yet reviewed; see the source.
- `pos` `any`: Type and behavior are not yet reviewed; see the source.
- `break_effect` `any`: Type and behavior are not yet reviewed; see the source.
- `target_player` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDAction.lua:158`

```lua
function RushDuel.SelectAndToHandOrSpecialSummon(hint, filter, tp, s_range, o_range, expect, e, pos, break_effect, target_player)
    return RushDuel._private_action_select_match(hint, filter, tp, s_range, o_range, 1, 1, expect, false, false, function(g)
        local tc = g:GetFirst()
        local ft = RushDuel.GetMZoneCount(target_player or tp, 1)
        if tc:IsAbleToHand() and (not RD.IsCanBeSpecialSummoned(tc, e, tp, pos) or ft <= 0 or Duel.SelectOption(tp, 1190, 1152) == 0) then
            if break_effect then
                Duel.BreakEffect()
            end
            return RushDuel.SendToHandAndExists(tc, e, tp, REASON_EFFECT)
        else
            return RushDuel._special_summon(tc, e, tp, pos, break_effect, target_player)~=0
        end
    end, e, tp)
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **4** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.SelectAndToHandOrSpecialSummon) with `RushDuel.SelectAndToHandOrSpecialSummon`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Bone Spine Whip | `120277064` | [Rush/Scripts/c120277064.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120277064.lua) | 1 |
| Hack for the Intel | `120290059` | [Rush/Scripts/c120290059.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120290059.lua) | 1 |
| Blaze Fiend Overlord Luciless | `120254036` | [Rush/Scripts/c120254036.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120254036.lua) | 1 |
| Wooly Wonderland Fluffy | `120293018` | [Rush/Scripts/c120293018.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120293018.lua) | 1 |

## Script Examples

### Bone Spine Whip (`120277064`)

Source: [Rush/Scripts/c120277064.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120277064.lua)

```lua
end
function cm.activate(e,tp,eg,ep,ev,re,r,rp)
	if RD.SelectAndToHandOrSpecialSummon(aux.Stringid(m,1),aux.NecroValleyFilter(cm.filter),tp,LOCATION_GRAVE,0,nil,e,POS_FACEUP)
		and Duel.IsExistingMatchingCard(cm.exfilter,tp,LOCATION_MZONE,0,1,nil) then
		RD.CanSelectAndDoAction(aux.Stringid(m,2),HINTMSG_RTOHAND,cm.thfilter,tp,0,LOCATION_MZONE,1,1,nil,function(sg)
```

### Hack for the Intel (`120290059`)

Source: [Rush/Scripts/c120290059.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120290059.lua)

```lua
end
function cm.activate(e,tp,eg,ep,ev,re,r,rp)
	if RD.SelectAndToHandOrSpecialSummon(aux.Stringid(m,1),aux.NecroValleyFilter(cm.filter),tp,LOCATION_GRAVE,0,nil,e,POS_FACEUP)
		and Duel.IsExistingMatchingCard(cm.exfilter,tp,LOCATION_MZONE,0,1,nil) then
		RD.CanSendOpponentHandToGrave(aux.Stringid(m,1),tp,aux.Stringid(m,2),1,1,true)
```

### Blaze Fiend Overlord Luciless (`120254036`)

Source: [Rush/Scripts/c120254036.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120254036.lua)

```lua
end
function cm.operation(e,tp,eg,ep,ev,re,r,rp)
	RD.SelectAndToHandOrSpecialSummon(aux.Stringid(m,2),aux.NecroValleyFilter(cm.filter),tp,LOCATION_GRAVE,0,nil,e,POS_FACEUP)
end
```
