# RushDuel.SelectGroupAndSet

Alias: `RD.SelectGroupAndSet`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.SelectGroupAndSet(any filter, any check, any tp, any s_range, any o_range, any min, any max, any expect, any e, any break_effect) -> any
```

## Description

Rush Duel helper declared in `RDAction.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
操作: 选择魔法, 陷阱卡盖放 (子卡片组)
```

## Parameters

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

`Rush/Utilities/RDAction.lua:204`

```lua
function RushDuel.SelectGroupAndSet(filter, check, tp, s_range, o_range, min, max, expect, e, break_effect)
    local ct = RushDuel.GetSZoneCount(tp, max)
    if ct >= min then
        return RushDuel._private_action_select_group(HINTMSG_SET, filter, check, tp, s_range, o_range, min, ct, expect, false, false, RushDuel._set_spell_trap, e, tp, break_effect)
    end
    return 0
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **5** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.SelectGroupAndSet) with `RushDuel.SelectGroupAndSet`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Secret Service Shine Guard | `120183023` | [Rush/Scripts/c120183023.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120183023.lua) | 1 |
| Worker Warrior - Sinister CEO | `120183024` | [Rush/Scripts/c120183024.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120183024.lua) | 1 |
| Alpha the Magnet Cavalry | `120260026` | [Rush/Scripts/c120260026.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120260026.lua) | 1 |
| Fiend's Mirage | `120304031` | [Rush/Scripts/c120304031.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120304031.lua) | 1 |
| Bat of the Twin Blaze Fiends | `120290025` | [Rush/Scripts/c120290025.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120290025.lua) | 1 |

## Script Examples

### Secret Service Shine Guard (`120183023`)

Source: [Rush/Scripts/c120183023.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120183023.lua)

```lua
end
function cm.operation(e,tp,eg,ep,ev,re,r,rp)
	RD.SelectGroupAndSet(aux.NecroValleyFilter(cm.setfilter),aux.dncheck,tp,LOCATION_GRAVE,0,1,2,nil,e)
	if Duel.GetFlagEffect(tp,m)~=0 then return end
	RD.CreateRaceCannotAttackEffect(e,aux.Stringid(m,1),RACE_ALL-RACE_MACHINE,tp,1,0,RESET_PHASE+PHASE_END)
```

### Worker Warrior - Sinister CEO (`120183024`)

Source: [Rush/Scripts/c120183024.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120183024.lua)

```lua
end
function cm.operation(e,tp,eg,ep,ev,re,r,rp)
	RD.SelectGroupAndSet(aux.NecroValleyFilter(cm.setfilter),aux.dncheck,tp,LOCATION_GRAVE,0,1,2,nil,e)
end
```

### Alpha the Magnet Cavalry (`120260026`)

Source: [Rush/Scripts/c120260026.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120260026.lua)

```lua
end
function cm.operation(e,tp,eg,ep,ev,re,r,rp)
	RD.SelectGroupAndSet(aux.NecroValleyFilter(cm.setfilter),aux.dncheck,tp,LOCATION_GRAVE,0,1,2,nil,e)
end
```
