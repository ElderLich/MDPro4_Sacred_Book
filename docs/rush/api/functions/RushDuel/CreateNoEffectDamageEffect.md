# RushDuel.CreateNoEffectDamageEffect

Alias: `RD.CreateNoEffectDamageEffect`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CreateNoEffectDamageEffect(any e, any desc, any value, any player, any s_range, any o_range, any reset) -> any
```

## Description

Rush Duel helper declared in `RDLimit.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
创建限制: 不会受到效果伤害
```

## Parameters

- `e` `any`: Type and behavior are not yet reviewed; see the source.
- `desc` `any`: Type and behavior are not yet reviewed; see the source.
- `value` `any`: Type and behavior are not yet reviewed; see the source.
- `player` `any`: Type and behavior are not yet reviewed; see the source.
- `s_range` `any`: Type and behavior are not yet reviewed; see the source.
- `o_range` `any`: Type and behavior are not yet reviewed; see the source.
- `reset` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDLimit.lua:411`

```lua
function RushDuel.CreateNoEffectDamageEffect(e, desc, value, player, s_range, o_range, reset)
    local e1 = Effect.CreateEffect(e:GetHandler())
    e1:SetDescription(desc)
    e1:SetType(EFFECT_TYPE_FIELD)
    e1:SetCode(EFFECT_CHANGE_DAMAGE)
    e1:SetProperty(EFFECT_FLAG_PLAYER_TARGET + EFFECT_FLAG_CLIENT_HINT)
    e1:SetTargetRange(s_range, o_range)
    e1:SetValue(value)
    e1:SetReset(reset)
    Duel.RegisterEffect(e1, player)
    local e2 = e1:Clone()
    e2:SetCode(EFFECT_NO_EFFECT_DAMAGE)
    Duel.RegisterEffect(e2, player)
    return e1, e2
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **4** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.CreateNoEffectDamageEffect) with `RushDuel.CreateNoEffectDamageEffect`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Skysavior Watch](/examples/rush-cards/120235053) | `120235053` | [Rush/Scripts/c120235053.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120235053.lua) | 1 |
| [Moonforce Timo](/examples/rush-cards/120300015) | `120300015` | [Rush/Scripts/c120300015.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120300015.lua) | 1 |
| Peace &amp; Rock n' Roll | `120253061` | [Rush/Scripts/c120253061.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120253061.lua) | 1 |
| Cyber Kirin | `120278008` | [Rush/Scripts/c120278008.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120278008.lua) | 1 |

## Script Examples

### Skysavior Watch (`120235053`)

Source: [Rush/Scripts/c120235053.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120235053.lua)

```lua
	RD.CreateHintEffect(e,aux.Stringid(m,1),tp,1,0,RESET_PHASE+PHASE_END)
	RD.CreateAttackLimitEffect(e,cm.atktg,tp,LOCATION_MZONE,0,RESET_PHASE+PHASE_END)
	RD.CreateNoEffectDamageEffect(e,aux.Stringid(m,2),cm.damval,tp,0,1,RESET_PHASE+PHASE_END)
	Duel.RegisterFlagEffect(tp,m,RESET_PHASE+PHASE_END,0,1)
end
```

### Moonforce Timo (`120300015`)

Source: [Rush/Scripts/c120300015.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120300015.lua)

```lua
	RD.CreateRaceCannotAttackEffect(e,aux.Stringid(m,1),RACE_ALL-RACE_GALAXY,tp,1,0,RESET_PHASE+PHASE_END)
	RD.CreateAttackLimitEffect(e,cm.atktg,tp,LOCATION_MZONE,0,RESET_PHASE+PHASE_END)
	RD.CreateNoEffectDamageEffect(e,aux.Stringid(m,2),cm.damval,tp,0,1,RESET_PHASE+PHASE_END)
	Duel.RegisterFlagEffect(tp,m,RESET_PHASE+PHASE_END,0,1)
end
```

### Peace & Rock n' Roll (`120253061`)

Source: [Rush/Scripts/c120253061.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120253061.lua)

```lua
		if Duel.Destroy(g,REASON_EFFECT)~=0 and Duel.GetLP(tp)<=2000 then
			RD.CreateNoBattleDamageEffect(e,aux.Stringid(m,1),tp,1,0,RESET_PHASE+PHASE_END)
			RD.CreateNoEffectDamageEffect(e,aux.Stringid(m,2),cm.damval,tp,1,0,RESET_PHASE+PHASE_END)
		end
	end)
```
