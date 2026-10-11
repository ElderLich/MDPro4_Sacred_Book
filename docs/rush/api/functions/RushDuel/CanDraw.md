# RushDuel.CanDraw

Alias: `RD.CanDraw`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CanDraw(any desc, any player, any count, any break_effect) -> any
```

## Description

Rush Duel helper declared in `RDAction.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
可选操作: 抽卡
```

## Parameters

- `desc` `any`: Type and behavior are not yet reviewed; see the source.
- `player` `any`: Type and behavior are not yet reviewed; see the source.
- `count` `any`: Type and behavior are not yet reviewed; see the source.
- `break_effect` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDAction.lua:570`

```lua
function RushDuel.CanDraw(desc, player, count, break_effect)
    if Duel.IsPlayerCanDraw(player, count) and Duel.SelectYesNo(player, desc) then
        if break_effect then
            Duel.BreakEffect()
        end
        return Duel.Draw(player, count, REASON_EFFECT)
    end
    return 0
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **87** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.CanDraw) with `RushDuel.CanDraw`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Instant Gift](/examples/rush-cards/120306059) | `120306059` | [Rush/Scripts/c120306059.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120306059.lua) | 1 |
| [Red-Eyes Mars Dragon](/examples/rush-cards/120306034) | `120306034` | [Rush/Scripts/c120306034.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120306034.lua) | 1 |
| Sparkhearts Familiar | `120298027` | [Rush/Scripts/c120298027.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120298027.lua) | 1 |
| Worker Warrior - Sinister Chairman | `120196038` | [Rush/Scripts/c120196038.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120196038.lua) | 1 |
| Surtr the Brilliant Magical Sword | `120306100` | [Rush/Scripts/c120306100.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120306100.lua) | 1 |
| Ancient Gear Supplier | `120271010` | [Rush/Scripts/c120271010.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120271010.lua) | 1 |
| Sevens Road Wiz | `120183014` | [Rush/Scripts/c120183014.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120183014.lua) | 1 |
| Mr. Alchemy | `120196020` | [Rush/Scripts/c120196020.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120196020.lua) | 1 |
| Wyrm Excavator the Heavy Cavalry Draco \[R\] | `120155023` | [Rush/Scripts/c120155023.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120155023.lua) | 1 |
| King's Greed | `120254083` | [Rush/Scripts/c120254083.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120254083.lua) | 1 |
| Space Call | `120260018` | [Rush/Scripts/c120260018.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120260018.lua) | 1 |
| Ancient Gear Medic | `120271009` | [Rush/Scripts/c120271009.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120271009.lua) | 1 |
| Master Craftsman Kotetsu | `120238036` | [Rush/Scripts/c120238036.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120238036.lua) | 1 |
| Voidalfr Heavenstar | `120300006` | [Rush/Scripts/c120300006.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120300006.lua) | 1 |
| Darkness Ri-chair-al | `120151027` | [Rush/Scripts/c120151027.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120151027.lua) | 1 |
| Imaginary Reactor | `120271025` | [Rush/Scripts/c120271025.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120271025.lua) | 1 |
| Freshberry Rich | `120264027` | [Rush/Scripts/c120264027.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120264027.lua) | 1 |
| Progress Potter | `120217035` | [Rush/Scripts/c120217035.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120217035.lua) | 1 |
| Spirit of Isyria | `120300061` | [Rush/Scripts/c120300061.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120300061.lua) | 1 |
| Yewearth the Planetairy | `120293051` | [Rush/Scripts/c120293051.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120293051.lua) | 1 |
| Back Beat | `120199053` | [Rush/Scripts/c120199053.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120199053.lua) | 1 |
| Moonforce Rifet | `120300012` | [Rush/Scripts/c120300012.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120300012.lua) | 1 |
| Sevens Paladin | `120196015` | [Rush/Scripts/c120196015.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120196015.lua) | 1 |
| Imaginary Arc Actor | `120271037` | [Rush/Scripts/c120271037.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120271037.lua) | 1 |
| ...and 63 more |  |  |  |

## Script Examples

### Instant Gift (`120306059`)

Source: [Rush/Scripts/c120306059.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120306059.lua)

```lua
	local filter=RD.Filter(cm.spfilter,e,tp,code)
	if RD.SelectAndSpecialSummon(aux.NecroValleyFilter(filter),tp,LOCATION_GRAVE,0,1,1,nil,e,POS_FACEUP)~=0 then
		RD.CanDraw(aux.Stringid(m,1),tp,1,true)
	end
	if Duel.GetFlagEffect(tp,m)~=0 then return end
```

### Red-Eyes Mars Dragon (`120306034`)

Source: [Rush/Scripts/c120306034.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120306034.lua)

```lua
		RD.ChangeCode(e,c,list[1],RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END)
		if Duel.IsExistingMatchingCard(cm.exfilter,tp,LOCATION_GRAVE,0,1,nil) then
			RD.CanDraw(aux.Stringid(m,2),tp,1)
		end
	end
```

### Sparkhearts Familiar (`120298027`)

Source: [Rush/Scripts/c120298027.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120298027.lua)

```lua
		if Duel.SendtoGrave(g,REASON_EFFECT)~=0
			and Duel.IsExistingMatchingCard(cm.exfilter,tp,LOCATION_GRAVE,0,1,nil) then
			RD.CanDraw(aux.Stringid(m,1),tp,2)
		end
	end)
```
