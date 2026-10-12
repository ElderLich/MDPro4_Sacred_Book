# RushDuel.CreateCannotFaceupSpecialSummonEffect

Alias: `RD.CreateCannotFaceupSpecialSummonEffect`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CreateCannotFaceupSpecialSummonEffect(any e, any desc, any target, any player, any s_range, any o_range, any reset) -> any
```

## Description

Rush Duel helper declared in `RDLimit.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
创建限制: 不能表侧特殊召唤怪兽
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

`Rush/Utilities/RDLimit.lua:164`

```lua
function RushDuel.CreateCannotFaceupSpecialSummonEffect(e, desc, target, player, s_range, o_range, reset)
    local e1 = Effect.CreateEffect(e:GetHandler())
    e1:SetDescription(desc)
    e1:SetType(EFFECT_TYPE_FIELD)
    e1:SetCode(EFFECT_LIMIT_SPECIAL_SUMMON_POSITION)
    e1:SetProperty(EFFECT_FLAG_PLAYER_TARGET + EFFECT_FLAG_CLIENT_HINT)
    e1:SetTargetRange(s_range, o_range)
    e1:SetTarget(function(e, c, sump, sumtype, sumpos, targetp)
        return sumpos & POS_FACEUP > 0 and (not target or target(e, c))
    end)
    e1:SetReset(reset)
    Duel.RegisterEffect(e1, player)
    return e1
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **3** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.CreateCannotFaceupSpecialSummonEffect) with `RushDuel.CreateCannotFaceupSpecialSummonEffect`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Eria the Water Spiritualist | `120301010` | [Rush/Scripts/c120301010.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120301010.lua) | 1 |
| Destructor Soldier Haken | `120264012` | [Rush/Scripts/c120264012.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120264012.lua) | 1 |
| Hybridrive Screwdriver | `120261006` | [Rush/Scripts/c120261006.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120261006.lua) | 1 |

## Script Examples

### Eria the Water Spiritualist (`120301010`)

Source: [Rush/Scripts/c120301010.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120301010.lua)

```lua
		end
		RD.CreateCannotSummonEffect(e,aux.Stringid(m,1),sumlimit,tp,0,1,RESET_PHASE+PHASE_END+RESET_OPPO_TURN)
		RD.CreateCannotFaceupSpecialSummonEffect(e,aux.Stringid(m,2),sumlimit,tp,0,1,RESET_PHASE+PHASE_END+RESET_OPPO_TURN)
	end)
	RD.CreateCannotActivateSameCodeEffect(e,aux.Stringid(m,3),m,tp,list[1])
```

### Destructor Soldier Haken (`120264012`)

Source: [Rush/Scripts/c120264012.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120264012.lua)

```lua
	if Duel.GetFlagEffect(tp,m)~=0 then return end
	RD.CreateCannotSummonEffect(e,aux.Stringid(m,1),cm.sumlimit,tp,1,0,RESET_PHASE+PHASE_END)
	RD.CreateCannotFaceupSpecialSummonEffect(e,aux.Stringid(m,2),cm.sumlimit,tp,1,0,RESET_PHASE+PHASE_END)
	RD.CreateOnlySoleAttackEffect(e,20264012,tp,LOCATION_MZONE,0,RESET_PHASE+PHASE_END)
	Duel.RegisterFlagEffect(tp,m,RESET_PHASE+PHASE_END,0,1)
```

### Hybridrive Screwdriver (`120261006`)

Source: [Rush/Scripts/c120261006.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120261006.lua)

```lua
			end
			RD.CreateCannotSummonEffect(e,aux.Stringid(m,1),sumlimit,tp,1,1,RESET_PHASE+PHASE_END+RESET_OPPO_TURN)
			RD.CreateCannotFaceupSpecialSummonEffect(e,aux.Stringid(m,2),sumlimit,tp,1,1,RESET_PHASE+PHASE_END+RESET_OPPO_TURN)
		end
	end)
```
