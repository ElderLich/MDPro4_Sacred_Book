# RushDuel.CreateCannotSpecialSummonEffect

Alias: `RD.CreateCannotSpecialSummonEffect`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CreateCannotSpecialSummonEffect(any e, any desc, any target, any player, any s_range, any o_range, any reset) -> any
```

## Description

Rush Duel helper declared in `RDLimit.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
创建限制: 不能特殊召唤怪兽
```

## Parameters

- `e` `any`: Type and behavior are not yet reviewed; see the source.
- `desc` `any`: Type and behavior are not yet reviewed; see the source.
- `target` `any`: Type and behavior are not yet reviewed; see the source.
- `player` `any`: Type and behavior are not yet reviewed; see the source.
- `s_range` `any`: Type and behavior are not yet reviewed; see the source.
- `o_range` `any`: Type and behavior are not yet reviewed; see the source.
- `reset` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDLimit.lua:149`

```lua
function RushDuel.CreateCannotSpecialSummonEffect(e, desc, target, player, s_range, o_range, reset)
    local e1 = Effect.CreateEffect(e:GetHandler())
    e1:SetDescription(desc)
    e1:SetType(EFFECT_TYPE_FIELD)
    e1:SetCode(EFFECT_CANNOT_SPECIAL_SUMMON)
    e1:SetProperty(EFFECT_FLAG_PLAYER_TARGET + EFFECT_FLAG_CLIENT_HINT)
    e1:SetTargetRange(s_range, o_range)
    if target ~= nil then
        e1:SetTarget(target)
    end
    e1:SetReset(reset)
    Duel.RegisterEffect(e1, player)
    return e1
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **10** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.CreateCannotSpecialSummonEffect) with `RushDuel.CreateCannotSpecialSummonEffect`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Pot of Duality](/examples/rush-cards/120271002) | `120271002` | [Rush/Scripts/c120271002.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120271002.lua) | 1 |
| Jointech Nesstrydar Tank | `120257017` | [Rush/Scripts/c120257017.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120257017.lua) | 1 |
| X-Trial Cannon | `120305008` | [Rush/Scripts/c120305008.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120305008.lua) | 1 |
| Star Replacer | `120244022` | [Rush/Scripts/c120244022.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120244022.lua) | 1 |
| Skysavior Aspiration | `120301051` | [Rush/Scripts/c120301051.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120301051.lua) | 1 |
| Koi of Winter Wonder | `120246047` | [Rush/Scripts/c120246047.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120246047.lua) | 1 |
| Thunderbeetle Storm | `120150034` | [Rush/Scripts/c120150034.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120150034.lua) | 1 |
| Cyber Variation | `120278028` | [Rush/Scripts/c120278028.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120278028.lua) | 1 |
| Tiger Roll the Sushi Fairy | `120151041` | [Rush/Scripts/c120151041.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120151041.lua) | 1 |
| The Monarchs Stormforth | `120291022` | [Rush/Scripts/c120291022.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120291022.lua) | 1 |

## Script Examples

### Pot of Duality (`120271002`)

Source: [Rush/Scripts/c120271002.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120271002.lua)

```lua
	Duel.ShuffleDeck(p)
	if Duel.GetFlagEffect(tp,m)~=0 then return end
	RD.CreateCannotSpecialSummonEffect(e,aux.Stringid(m,1),nil,tp,1,0,RESET_PHASE+PHASE_END)
	RD.CreateCannotActivateEffect(e,aux.Stringid(m,2),cm.aclimit,tp,1,0,RESET_PHASE+PHASE_END)
	Duel.RegisterFlagEffect(tp,m,RESET_PHASE+PHASE_END,0,1)
```

### Jointech Nesstrydar Tank (`120257017`)

Source: [Rush/Scripts/c120257017.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120257017.lua)

```lua
	RD.SelectAndSpecialSummon(aux.NecroValleyFilter(cm.spfilter),tp,LOCATION_GRAVE,0,1,1,nil,e,POS_FACEUP)
	if Duel.GetFlagEffect(tp,m)~=0 then return end
	RD.CreateCannotSpecialSummonEffect(e,aux.Stringid(m,1),cm.sumlimit,tp,1,0,RESET_PHASE+PHASE_END)
	RD.CreateCannotActivateEffect(e,aux.Stringid(m,2),cm.aclimit,tp,1,0,RESET_PHASE+PHASE_END)
	Duel.RegisterFlagEffect(tp,m,RESET_PHASE+PHASE_END,0,1)
```

### X-Trial Cannon (`120305008`)

Source: [Rush/Scripts/c120305008.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120305008.lua)

```lua
	end
	if Duel.GetFlagEffect(tp,m)~=0 then return end
	RD.CreateCannotSpecialSummonEffect(e,aux.Stringid(m,2),cm.sumlimit,tp,1,0,RESET_PHASE+PHASE_END)
end
function cm.sumlimit(e,c)
```
