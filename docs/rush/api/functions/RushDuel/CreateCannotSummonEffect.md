# RushDuel.CreateCannotSummonEffect

Alias: `RD.CreateCannotSummonEffect`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CreateCannotSummonEffect(any e, any desc, any target, any player, any s_range, any o_range, any reset) -> any
```

## Description

Rush Duel helper declared in `RDLimit.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
创建限制: 不能召唤怪兽
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

`Rush/Utilities/RDLimit.lua:109`

```lua
function RushDuel.CreateCannotSummonEffect(e, desc, target, player, s_range, o_range, reset)
    local e1 = Effect.CreateEffect(e:GetHandler())
    e1:SetDescription(desc)
    e1:SetType(EFFECT_TYPE_FIELD)
    e1:SetCode(EFFECT_CANNOT_SUMMON)
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
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.CreateCannotSummonEffect) with `RushDuel.CreateCannotSummonEffect`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Devil Foolish](/examples/rush-cards/120244026) | `120244026` | [Rush/Scripts/c120244026.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120244026.lua) | 1 |
| Eria the Water Spiritualist | `120301010` | [Rush/Scripts/c120301010.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120301010.lua) | 1 |
| Super Electromagnetic Maximum | `120239024` | [Rush/Scripts/c120239024.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120239024.lua) | 1 |
| Maginical Fantastick | `120283044` | [Rush/Scripts/c120283044.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120283044.lua) | 1 |
| Destructor Soldier Haken | `120264012` | [Rush/Scripts/c120264012.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120264012.lua) | 1 |
| Koi of Winter Wonder | `120246047` | [Rush/Scripts/c120246047.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120246047.lua) | 1 |
| Hybridrive Screwdriver | `120261006` | [Rush/Scripts/c120261006.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120261006.lua) | 1 |
| Thunderbeetle Storm | `120150034` | [Rush/Scripts/c120150034.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120150034.lua) | 1 |
| Engine Reviver | `120235027` | [Rush/Scripts/c120235027.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120235027.lua) | 1 |
| Tiger Roll the Sushi Fairy | `120151041` | [Rush/Scripts/c120151041.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120151041.lua) | 1 |

## Script Examples

### Devil Foolish (`120244026`)

Source: [Rush/Scripts/c120244026.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120244026.lua)

```lua
	RD.SelectAndSpecialSummon(aux.NecroValleyFilter(cm.spfilter),tp,LOCATION_GRAVE,0,ct,ct,nil,e,POS_FACEDOWN_DEFENSE)
	if Duel.GetFlagEffect(tp,m)~=0 then return end
	RD.CreateCannotSummonEffect(e,aux.Stringid(m,1),cm.sumlimit,tp,1,0,RESET_PHASE+PHASE_END)
	RD.CreateCannotSetMonsterEffect(e,aux.Stringid(m,2),cm.setlimit,tp,1,0,RESET_PHASE+PHASE_END)
	Duel.RegisterFlagEffect(tp,m,RESET_PHASE+PHASE_END,0,1)
```

### Eria the Water Spiritualist (`120301010`)

Source: [Rush/Scripts/c120301010.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120301010.lua)

```lua
			return RD.IsSameOriginalCode(c,tc)
		end
		RD.CreateCannotSummonEffect(e,aux.Stringid(m,1),sumlimit,tp,0,1,RESET_PHASE+PHASE_END+RESET_OPPO_TURN)
		RD.CreateCannotFaceupSpecialSummonEffect(e,aux.Stringid(m,2),sumlimit,tp,0,1,RESET_PHASE+PHASE_END+RESET_OPPO_TURN)
	end)
```

### Super Electromagnetic Maximum (`120239024`)

Source: [Rush/Scripts/c120239024.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120239024.lua)

```lua
	RD.SelectAndDoAction(HINTMSG_ATOHAND,aux.NecroValleyFilter(cm.thfilter),tp,LOCATION_GRAVE,0,1,2,nil,function(g)
		if RD.SendToHandAndExists(g,e,tp,REASON_EFFECT) and Duel.GetFlagEffect(tp,m)==0 then
			RD.CreateCannotSummonEffect(e,aux.Stringid(m,1),cm.sumlimit,tp,1,0,RESET_PHASE+PHASE_END)
			RD.CreateCannotSetMonsterEffect(e,aux.Stringid(m,2),cm.sumlimit,tp,1,0,RESET_PHASE+PHASE_END)
			Duel.RegisterFlagEffect(tp,m,RESET_PHASE+PHASE_END,0,1)
```
