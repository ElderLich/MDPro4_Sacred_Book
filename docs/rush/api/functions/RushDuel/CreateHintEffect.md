# RushDuel.CreateHintEffect

Alias: `RD.CreateHintEffect`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CreateHintEffect(any e, any desc, any player, any s_range, any o_range, any reset) -> any
```

## Description

Rush Duel helper declared in `RDBase.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
创建效果: 在LP槽显示提示信息
```

## Parameters

- `e` `any`: Type and behavior are not yet reviewed; see the source.
- `desc` `any`: Type and behavior are not yet reviewed; see the source.
- `player` `any`: Type and behavior are not yet reviewed; see the source.
- `s_range` `any`: Type and behavior are not yet reviewed; see the source.
- `o_range` `any`: Type and behavior are not yet reviewed; see the source.
- `reset` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDBase.lua:152`

```lua
function RushDuel.CreateHintEffect(e, desc, player, s_range, o_range, reset)
    local e1 = Effect.CreateEffect(e:GetHandler())
    e1:SetDescription(desc)
    e1:SetType(EFFECT_TYPE_FIELD)
    e1:SetProperty(EFFECT_FLAG_PLAYER_TARGET + EFFECT_FLAG_CLIENT_HINT)
    e1:SetTargetRange(s_range, o_range)
    e1:SetReset(reset)
    Duel.RegisterEffect(e1, player)
    return e1
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **70** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.CreateHintEffect) with `RushDuel.CreateHintEffect`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Skysavior Watch](/examples/rush-cards/120235053) | `120235053` | [Rush/Scripts/c120235053.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120235053.lua) | 1 |
| [Voidalfr Star Mayfly](/examples/rush-cards/120300034) | `120300034` | [Rush/Scripts/c120300034.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120300034.lua) | 1 |
| [Analyze Phlogiston](/examples/rush-cards/120226001) | `120226001` | [Rush/Scripts/c120226001.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120226001.lua) | 1 |
| [Star Protector's Protection](/examples/rush-cards/120253065) | `120253065` | [Rush/Scripts/c120253065.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120253065.lua) | 1 |
| [Hybridrive Back Fusion](/examples/rush-cards/120261052) | `120261052` | [Rush/Scripts/c120261052.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120261052.lua) | 1 |
| [Madrhea Amelo](/examples/rush-cards/120300028) | `120300028` | [Rush/Scripts/c120300028.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120300028.lua) | 1 |
| [Ecliceras Drakon](/examples/rush-cards/120109033) | `120109033` | [Rush/Scripts/c120109033.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120109033.lua) | 1 |
| Soul Drake | `120252007` | [Rush/Scripts/c120252007.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120252007.lua) | 1 |
| Excutie Lumière | `120231031` | [Rush/Scripts/c120231031.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120231031.lua) | 1 |
| Joining Chairs | `120151028` | [Rush/Scripts/c120151028.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120151028.lua) | 1 |
| Heavy Cavalry Tactics | `120155046` | [Rush/Scripts/c120155046.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120155046.lua) | 1 |
| Sword Skill - Ruler's Slash | `120208046` | [Rush/Scripts/c120208046.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120208046.lua) | 1 |
| Excutie Leya Frontier | `120293069` | [Rush/Scripts/c120293069.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120293069.lua) | 1 |
| Masenkou, the Lashing Light | `120238044` | [Rush/Scripts/c120238044.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120238044.lua) | 1 |
| Spiral Geyser | `120199064` | [Rush/Scripts/c120199064.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120199064.lua) | 1 |
| Sea Dragon Kleindros | `120199031` | [Rush/Scripts/c120199031.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120199031.lua) | 1 |
| Gatling the Shadow Flower Shinobi | `120170032` | [Rush/Scripts/c120170032.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120170032.lua) | 1 |
| Mr. Alchemy | `120196020` | [Rush/Scripts/c120196020.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120196020.lua) | 1 |
| Mezame the Ringing Alarm | `120199015` | [Rush/Scripts/c120199015.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120199015.lua) | 1 |
| Gogogo Umpire | `120199026` | [Rush/Scripts/c120199026.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120199026.lua) | 1 |
| Beast Gear King Convoy Liogon | `120145031` | [Rush/Scripts/c120145031.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120145031.lua) | 1 |
| Wrath of Light | `120205061` | [Rush/Scripts/c120205061.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120205061.lua) | 1 |
| Koumori Dragon the Magical Dragon | `120309011` | [Rush/Scripts/c120309011.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120309011.lua) | 1 |
| Rapid Carriearth | `120208027` | [Rush/Scripts/c120208027.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120208027.lua) | 1 |
| ...and 46 more |  |  |  |

## Script Examples

### Skysavior Watch (`120235053`)

Source: [Rush/Scripts/c120235053.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120235053.lua)

```lua
	end
	if Duel.GetFlagEffect(tp,m)~=0 then return end
	RD.CreateHintEffect(e,aux.Stringid(m,1),tp,1,0,RESET_PHASE+PHASE_END)
	RD.CreateAttackLimitEffect(e,cm.atktg,tp,LOCATION_MZONE,0,RESET_PHASE+PHASE_END)
	RD.CreateNoEffectDamageEffect(e,aux.Stringid(m,2),cm.damval,tp,0,1,RESET_PHASE+PHASE_END)
```

### Voidalfr Star Mayfly (`120300034`)

Source: [Rush/Scripts/c120300034.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120300034.lua)

```lua
	end)
	if Duel.GetFlagEffect(tp,m)~=0 then return end
	RD.CreateHintEffect(e,aux.Stringid(m,1),tp,1,0,RESET_PHASE+PHASE_END)
	RD.CreateOnlySoleAttackEffect(e,20300034,tp,LOCATION_MZONE,0,RESET_PHASE+PHASE_END)
	Duel.RegisterFlagEffect(tp,m,RESET_PHASE+PHASE_END,0,1)
```

### Analyze Phlogiston (`120226001`)

Source: [Rush/Scripts/c120226001.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120226001.lua)

```lua
	end)
	if Duel.GetFlagEffect(tp,m)~=0 then return end
	RD.CreateHintEffect(e,aux.Stringid(m,1),tp,1,0,RESET_PHASE+PHASE_END)
	RD.CreateOnlySoleAttackEffect(e,20226001,tp,LOCATION_MZONE,0,RESET_PHASE+PHASE_END)
	Duel.RegisterFlagEffect(tp,m,RESET_PHASE+PHASE_END,0,1)
```
