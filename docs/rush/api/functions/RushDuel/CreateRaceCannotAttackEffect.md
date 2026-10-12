# RushDuel.CreateRaceCannotAttackEffect

Alias: `RD.CreateRaceCannotAttackEffect`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CreateRaceCannotAttackEffect(any e, any desc, any race, any player, any s_range, any o_range, any reset) -> any
```

## Description

Rush Duel helper declared in `RDLimit.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
创建限制: 不能用某些种族攻击
```

## Parameters

- `e` `any`: Type and behavior are not yet reviewed; see the source.
- `desc` `any`: Type and behavior are not yet reviewed; see the source.
- `race` `any`: Type and behavior are not yet reviewed; see the source.
- `player` `any`: Type and behavior are not yet reviewed; see the source.
- `s_range` `any`: Type and behavior are not yet reviewed; see the source.
- `o_range` `any`: Type and behavior are not yet reviewed; see the source.
- `reset` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDLimit.lua:45`

```lua
function RushDuel.CreateRaceCannotAttackEffect(e, desc, race, player, s_range, o_range, reset)
    local s_target, o_traget = 0, 0
    if s_range == 1 then
        s_target = LOCATION_MZONE
    end
    if o_range == 1 then
        o_traget = LOCATION_MZONE
    end
    local e1 = Effect.CreateEffect(e:GetHandler())
    e1:SetType(EFFECT_TYPE_FIELD)
    e1:SetCode(EFFECT_CANNOT_ATTACK)
    e1:SetProperty(EFFECT_FLAG_IGNORE_IMMUNE)
    e1:SetTargetRange(s_target, o_traget)
    e1:SetTarget(function(e, c)
        return c:IsRace(race)
    end)
    e1:SetReset(reset)
    Duel.RegisterEffect(e1, player)
    local e2 = Effect.CreateEffect(e:GetHandler())
    e2:SetDescription(desc)
    e2:SetType(EFFECT_TYPE_FIELD)
    e2:SetCode(EFFECT_PLAYER_RACE_CANNOT_ATTACK)
    e2:SetProperty(EFFECT_FLAG_PLAYER_TARGET + EFFECT_FLAG_CLIENT_HINT)
    e2:SetTargetRange(s_range, o_range)
    e2:SetValue(race)
    e2:SetReset(reset)
    Duel.RegisterEffect(e2, player)
    return e1, e2
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **100** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.CreateRaceCannotAttackEffect) with `RushDuel.CreateRaceCannotAttackEffect`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Instant Gift](/examples/rush-cards/120306059) | `120306059` | [Rush/Scripts/c120306059.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120306059.lua) | 1 |
| [Freshberry Collaboration](/examples/rush-cards/120301071) | `120301071` | [Rush/Scripts/c120301071.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120301071.lua) | 1 |
| [Miracle Pick](/examples/rush-cards/120253052) | `120253052` | [Rush/Scripts/c120253052.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120253052.lua) | 1 |
| [Wako Gozen Riletta](/examples/rush-cards/120309021) | `120309021` | [Rush/Scripts/c120309021.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120309021.lua) | 1 |
| [Moonforce Timo](/examples/rush-cards/120300015) | `120300015` | [Rush/Scripts/c120300015.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120300015.lua) | 1 |
| [Moonforce Sheila](/examples/rush-cards/120300013) | `120300013` | [Rush/Scripts/c120300013.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120300013.lua) | 1 |
| [Dimension Oper](/examples/rush-cards/120309025) | `120309025` | [Rush/Scripts/c120309025.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120309025.lua) | 1 |
| [Necromaid Timer](/examples/rush-cards/120294014) | `120294014` | [Rush/Scripts/c120294014.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120294014.lua) | 1 |
| [Botonaginata the Music Princess](/examples/rush-cards/120290009) | `120290009` | [Rush/Scripts/c120290009.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120290009.lua) | 1 |
| Voidvelg Beyond Probe | `120300031` | [Rush/Scripts/c120300031.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120300031.lua) | 1 |
| Speed Carrier | `120301059` | [Rush/Scripts/c120301059.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120301059.lua) | 1 |
| Fiarma the Ally Spark | `120298025` | [Rush/Scripts/c120298025.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120298025.lua) | 1 |
| Goe Goe the Rumored Ninja | `120306029` | [Rush/Scripts/c120306029.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120306029.lua) | 1 |
| Peit the Ally Spark | `120298024` | [Rush/Scripts/c120298024.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120298024.lua) | 1 |
| Sparkhearts Familiar | `120298027` | [Rush/Scripts/c120298027.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120298027.lua) | 1 |
| Cornetlass the Music Princess | `120287066` | [Rush/Scripts/c120287066.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120287066.lua) | 1 |
| Lostream Reading | `120309043` | [Rush/Scripts/c120309043.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120309043.lua) | 1 |
| Dimension Pramma | `120309026` | [Rush/Scripts/c120309026.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120309026.lua) | 1 |
| Royal Rebel's Extreme | `120306006` | [Rush/Scripts/c120306006.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120306006.lua) | 1 |
| Voidalfr Star Stripe | `120300033` | [Rush/Scripts/c120300033.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120300033.lua) | 1 |
| Lostream Record | `120309044` | [Rush/Scripts/c120309044.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120309044.lua) | 1 |
| Legendary Saber | `120238010` | [Rush/Scripts/c120238010.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120238010.lua) | 1 |
| Accel Wonder Dark | `120285005` | [Rush/Scripts/c120285005.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120285005.lua) | 1 |
| Evil Star Beacon | `120155041` | [Rush/Scripts/c120155041.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120155041.lua) | 1 |
| ...and 76 more |  |  |  |

## Script Examples

### Instant Gift (`120306059`)

Source: [Rush/Scripts/c120306059.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120306059.lua)

```lua
	end
	if Duel.GetFlagEffect(tp,m)~=0 then return end
	RD.CreateRaceCannotAttackEffect(e,aux.Stringid(m,2),RACE_ALL-RACE_WARRIOR,tp,1,0,RESET_PHASE+PHASE_END)
	Duel.RegisterFlagEffect(tp,m,RESET_PHASE+PHASE_END,0,1)
end
```

### Freshberry Collaboration (`120301071`)

Source: [Rush/Scripts/c120301071.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120301071.lua)

```lua
	end)
	if Duel.GetFlagEffect(tp,m)~=0 then return end
	RD.CreateRaceCannotAttackEffect(e,aux.Stringid(m,2),RACE_ALL-RACE_AQUA,tp,1,0,RESET_PHASE+PHASE_END)
	Duel.RegisterFlagEffect(tp,m,RESET_PHASE+PHASE_END,0,1)
end
```

### Miracle Pick (`120253052`)

Source: [Rush/Scripts/c120253052.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120253052.lua)

```lua
	end
	if Duel.GetFlagEffect(tp,m)~=0 then return end
	RD.CreateRaceCannotAttackEffect(e,aux.Stringid(m,1),RACE_ALL-RACE_OMEGAPSYCHO-RACE_PSYCHO,tp,1,0,RESET_PHASE+PHASE_END)
	Duel.RegisterFlagEffect(tp,m,RESET_PHASE+PHASE_END,0,1)
end
```
