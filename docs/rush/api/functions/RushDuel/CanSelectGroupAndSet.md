# RushDuel.CanSelectGroupAndSet

Alias: `RD.CanSelectGroupAndSet`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CanSelectGroupAndSet(any desc, any filter, any check, any tp, any s_range, any o_range, any min, any max, any expect, any e, any break_effect) -> any
```

## Description

Rush Duel helper declared in `RDAction.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
可选操作: 选择魔法, 陷阱卡盖放 (子卡片组)
```

## Parameters

- `desc` `any`: Type and behavior are not yet reviewed; see the source.
- `filter` `any`: Type and behavior are not yet reviewed; see the source.
- `check` `any`: Type and behavior are not yet reviewed; see the source.
- `tp` `any`: Type and behavior are not yet reviewed; see the source.
- `s_range` `any`: Type and behavior are not yet reviewed; see the source.
- `o_range` `any`: Type and behavior are not yet reviewed; see the source.
- `min` `any`: Type and behavior are not yet reviewed; see the source.
- `max` `any`: Type and behavior are not yet reviewed; see the source.
- `expect` `any`: Type and behavior are not yet reviewed; see the source.
- `e` `any`: Type and behavior are not yet reviewed; see the source.
- `break_effect` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDAction.lua:212`

```lua
function RushDuel.CanSelectGroupAndSet(desc, filter, check, tp, s_range, o_range, min, max, expect, e, break_effect)
    local ct = RushDuel.GetSZoneCount(tp, max)
    if ct >= min then
        return RushDuel._private_action_can_select_group(desc, HINTMSG_SET, filter, check, tp, s_range, o_range, min, ct, expect, false, false, RushDuel._set_spell_trap, e, tp, break_effect)
    end
    return 0
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **2** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.CanSelectGroupAndSet) with `RushDuel.CanSelectGroupAndSet`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Sparkhearts Girl | `120145014` | [Rush/Scripts/c120145014.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120145014.lua) | 1 |
| Extra Meat the Special Noodle Ninja | `120199038` | [Rush/Scripts/c120199038.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120199038.lua) | 1 |

## Script Examples

### Sparkhearts Girl (`120145014`)

Source: [Rush/Scripts/c120145014.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120145014.lua)

```lua
	RD.SelectAndDoAction(aux.Stringid(m,1),Card.IsFaceup,tp,0,LOCATION_MZONE,1,1,nil,function(g)
		RD.AttachAtkDef(e,g:GetFirst(),-500,0,RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END)
		RD.CanSelectGroupAndSet(aux.Stringid(m,2),aux.NecroValleyFilter(cm.setfilter),aux.dncheck,tp,LOCATION_GRAVE,0,1,2,nil,e,true)
	end)
end
```

### Extra Meat the Special Noodle Ninja (`120199038`)

Source: [Rush/Scripts/c120199038.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120199038.lua)

```lua
function cm.operation(e,tp,eg,ep,ev,re,r,rp)
	if Duel.Damage(1-tp,1000,REASON_EFFECT)~=0 and Duel.Draw(tp,1,REASON_EFFECT)~=0 then
		RD.CanSelectGroupAndSet(aux.Stringid(m,2),aux.NecroValleyFilter(cm.setfilter),aux.dncheck,tp,LOCATION_GRAVE,0,1,2,nil,e)
	end
end
```
