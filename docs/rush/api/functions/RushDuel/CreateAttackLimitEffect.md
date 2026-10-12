# RushDuel.CreateAttackLimitEffect

Alias: `RD.CreateAttackLimitEffect`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CreateAttackLimitEffect(any e, any target, any player, any s_range, any o_range, any reset) -> any
```

## Description

Rush Duel helper declared in `RDLimit.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
创建限制: 只能用特定类型的怪兽攻击
```

## Parameters

- `e` `any`: Type and behavior are not yet reviewed; see the source.
- `target` `any`: Type and behavior are not yet reviewed; see the source.
- `player` `any`: Type and behavior are not yet reviewed; see the source.
- `s_range` `any`: Type and behavior are not yet reviewed; see the source.
- `o_range` `any`: Type and behavior are not yet reviewed; see the source.
- `reset` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDLimit.lua:5`

```lua
function RushDuel.CreateAttackLimitEffect(e, target, player, s_range, o_range, reset)
    local e1 = Effect.CreateEffect(e:GetHandler())
    e1:SetType(EFFECT_TYPE_FIELD)
    e1:SetCode(EFFECT_CANNOT_ATTACK)
    e1:SetProperty(EFFECT_FLAG_IGNORE_IMMUNE)
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

- Detected in **81** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.CreateAttackLimitEffect) with `RushDuel.CreateAttackLimitEffect`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Skysavior Watch](/examples/rush-cards/120235053) | `120235053` | [Rush/Scripts/c120235053.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120235053.lua) | 1 |
| [Hybridrive Back Fusion](/examples/rush-cards/120261052) | `120261052` | [Rush/Scripts/c120261052.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120261052.lua) | 1 |
| [Moonforce Timo](/examples/rush-cards/120300015) | `120300015` | [Rush/Scripts/c120300015.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120300015.lua) | 1 |
| [Moonforce Sheila](/examples/rush-cards/120300013) | `120300013` | [Rush/Scripts/c120300013.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120300013.lua) | 1 |
| [Dimension Oper](/examples/rush-cards/120309025) | `120309025` | [Rush/Scripts/c120309025.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120309025.lua) | 1 |
| [Madrhea Amelo](/examples/rush-cards/120300028) | `120300028` | [Rush/Scripts/c120300028.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120300028.lua) | 1 |
| [Botonaginata the Music Princess](/examples/rush-cards/120290009) | `120290009` | [Rush/Scripts/c120290009.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120290009.lua) | 1 |
| [Ecliceras Drakon](/examples/rush-cards/120109033) | `120109033` | [Rush/Scripts/c120109033.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120109033.lua) | 1 |
| Voidvelg Beyond Probe | `120300031` | [Rush/Scripts/c120300031.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120300031.lua) | 1 |
| Soul Drake | `120252007` | [Rush/Scripts/c120252007.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120252007.lua) | 1 |
| Fiarma the Ally Spark | `120298025` | [Rush/Scripts/c120298025.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120298025.lua) | 1 |
| Goe Goe the Rumored Ninja | `120306029` | [Rush/Scripts/c120306029.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120306029.lua) | 1 |
| Peit the Ally Spark | `120298024` | [Rush/Scripts/c120298024.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120298024.lua) | 1 |
| Sparkhearts Familiar | `120298027` | [Rush/Scripts/c120298027.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120298027.lua) | 1 |
| Cornetlass the Music Princess | `120287066` | [Rush/Scripts/c120287066.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120287066.lua) | 1 |
| Lostream Reading | `120309043` | [Rush/Scripts/c120309043.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120309043.lua) | 1 |
| Excutie Lumière | `120231031` | [Rush/Scripts/c120231031.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120231031.lua) | 1 |
| Dimension Pramma | `120309026` | [Rush/Scripts/c120309026.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120309026.lua) | 1 |
| Heavy Cavalry Tactics | `120155046` | [Rush/Scripts/c120155046.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120155046.lua) | 1 |
| Lostream Record | `120309044` | [Rush/Scripts/c120309044.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120309044.lua) | 1 |
| Excutie Leya Frontier | `120293069` | [Rush/Scripts/c120293069.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120293069.lua) | 1 |
| Masenkou, the Lashing Light | `120238044` | [Rush/Scripts/c120238044.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120238044.lua) | 1 |
| Memory of Sunlit | `120300051` | [Rush/Scripts/c120300051.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120300051.lua) | 1 |
| Sea Dragon Kleindros | `120199031` | [Rush/Scripts/c120199031.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120199031.lua) | 1 |
| ...and 57 more |  |  |  |

## Script Examples

### Skysavior Watch (`120235053`)

Source: [Rush/Scripts/c120235053.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120235053.lua)

```lua
	if Duel.GetFlagEffect(tp,m)~=0 then return end
	RD.CreateHintEffect(e,aux.Stringid(m,1),tp,1,0,RESET_PHASE+PHASE_END)
	RD.CreateAttackLimitEffect(e,cm.atktg,tp,LOCATION_MZONE,0,RESET_PHASE+PHASE_END)
	RD.CreateNoEffectDamageEffect(e,aux.Stringid(m,2),cm.damval,tp,0,1,RESET_PHASE+PHASE_END)
	Duel.RegisterFlagEffect(tp,m,RESET_PHASE+PHASE_END,0,1)
```

### Hybridrive Back Fusion (`120261052`)

Source: [Rush/Scripts/c120261052.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120261052.lua)

```lua
	if Duel.GetFlagEffect(tp,m)~=0 then return end
	RD.CreateHintEffect(e,aux.Stringid(m,2),tp,1,0,RESET_PHASE+PHASE_END)
	RD.CreateAttackLimitEffect(e,cm.atktg,tp,LOCATION_MZONE,0,RESET_PHASE+PHASE_END)
	Duel.RegisterFlagEffect(tp,m,RESET_PHASE+PHASE_END,0,1)
end
```

### Moonforce Timo (`120300015`)

Source: [Rush/Scripts/c120300015.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120300015.lua)

```lua
	if Duel.GetFlagEffect(tp,m)~=0 then return end
	RD.CreateRaceCannotAttackEffect(e,aux.Stringid(m,1),RACE_ALL-RACE_GALAXY,tp,1,0,RESET_PHASE+PHASE_END)
	RD.CreateAttackLimitEffect(e,cm.atktg,tp,LOCATION_MZONE,0,RESET_PHASE+PHASE_END)
	RD.CreateNoEffectDamageEffect(e,aux.Stringid(m,2),cm.damval,tp,0,1,RESET_PHASE+PHASE_END)
	Duel.RegisterFlagEffect(tp,m,RESET_PHASE+PHASE_END,0,1)
```
