# RushDuel.CreateCannotActivateSameCodeEffect

Alias: `RD.CreateCannotActivateSameCodeEffect`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CreateCannotActivateSameCodeEffect(any e, any desc, any flag, any player, any code) -> any
```

## Description

Rush Duel helper declared in `RDLimit.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
创建限制: 这个回合，自己不能把「卡名」的效果发动
```

## Parameters

- `e` `any`: Type and behavior are not yet reviewed; see the source.
- `desc` `any`: Type and behavior are not yet reviewed; see the source.
- `flag` `any`: Type and behavior are not yet reviewed; see the source.
- `player` `any`: Type and behavior are not yet reviewed; see the source.
- `code` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDLimit.lua:346`

```lua
function RushDuel.CreateCannotActivateSameCodeEffect(e, desc, flag, player, code)
	if Duel.GetFlagEffect(player, flag) ~= 0 then
        return nil
    end
    local e1 = RushDuel.CreateCannotActivateMix(e, desc, player, 1, 0, RESET_PHASE + PHASE_END,
        function(e, re, tp)
	        return re:GetHandler():IsCode(code)
        end)
	Duel.RegisterFlagEffect(player, flag, RESET_PHASE + PHASE_END, 0, 1)
    return e1
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **59** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.CreateCannotActivateSameCodeEffect) with `RushDuel.CreateCannotActivateSameCodeEffect`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Wako Gozen Riletta](/examples/rush-cards/120309021) | `120309021` | [Rush/Scripts/c120309021.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120309021.lua) | 1 |
| [Fairy of the Stars](/examples/rush-cards/120305016) | `120305016` | [Rush/Scripts/c120305016.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120305016.lua) | 1 |
| [Rescue Rabbit](/examples/rush-cards/120109057) | `120109057` | [Rush/Scripts/c120109057.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120109057.lua) | 1 |
| [Crystal Seer](/examples/rush-cards/120109067) | `120109067` | [Rush/Scripts/c120109067.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120109067.lua) | 1 |
| Cosmostar the White Hole Polairy | `120293045` | [Rush/Scripts/c120293045.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120293045.lua) | 1 |
| Eria the Water Spiritualist | `120301010` | [Rush/Scripts/c120301010.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120301010.lua) | 1 |
| Sparkhearts Anesh | `120298022` | [Rush/Scripts/c120298022.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120298022.lua) | 1 |
| Goe Goe the Rumored Ninja | `120306029` | [Rush/Scripts/c120306029.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120306029.lua) | 1 |
| Speed Commander | `120301058` | [Rush/Scripts/c120301058.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120301058.lua) | 1 |
| Rescue Cat | `120307008` | [Rush/Scripts/c120307008.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120307008.lua) | 1 |
| Sparkhearts Hat | `120298026` | [Rush/Scripts/c120298026.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120298026.lua) | 1 |
| Red-Eyes Darkness Metal Dragon | `120294000` | [Rush/Scripts/c120294000.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120294000.lua) | 1 |
| Princess Cosmos the Trickster | `120293046` | [Rush/Scripts/c120293046.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120293046.lua) | 1 |
| Surtr the Brilliant Magical Sword | `120306100` | [Rush/Scripts/c120306100.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120306100.lua) | 1 |
| Onomatopitcher | `120305031` | [Rush/Scripts/c120305031.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120305031.lua) | 1 |
| Enceladustellime | `120304003` | [Rush/Scripts/c120304003.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120304003.lua) | 1 |
| Healthie Shanlong | `120306020` | [Rush/Scripts/c120306020.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120306020.lua) | 1 |
| Resurrection Heliacal Riser | `120304039` | [Rush/Scripts/c120304039.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120304039.lua) | 1 |
| Rising HERO Reglam | `120304024` | [Rush/Scripts/c120304024.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120304024.lua) | 1 |
| Gagaga Cheergirl | `120305033` | [Rush/Scripts/c120305033.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120305033.lua) | 1 |
| Aussa the Earth Spiritualist | `120301009` | [Rush/Scripts/c120301009.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120301009.lua) | 1 |
| Dark Magician of Chaos | `120307001` | [Rush/Scripts/c120307001.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120307001.lua) | 1 |
| Wynn the Wind Spiritualist | `120301012` | [Rush/Scripts/c120301012.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120301012.lua) | 1 |
| Sopla the Skullcrag Princess | `120298007` | [Rush/Scripts/c120298007.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120298007.lua) | 1 |
| ...and 35 more |  |  |  |

## Script Examples

### Wako Gozen Riletta (`120309021`)

Source: [Rush/Scripts/c120309021.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120309021.lua)

```lua
	if Duel.GetFlagEffect(tp,m)~=0 then return end
	RD.CreateRaceCannotAttackEffect(e,aux.Stringid(m,1),RACE_ALL-RACE_CYBERSE,tp,1,0,RESET_PHASE+PHASE_END)
	RD.CreateCannotActivateSameCodeEffect(e,aux.Stringid(m,2),m,tp,list[1])
	Duel.RegisterFlagEffect(tp,m,RESET_PHASE+PHASE_END,0,1)
end
```

### Fairy of the Stars (`120305016`)

Source: [Rush/Scripts/c120305016.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120305016.lua)

```lua
		end)
	end
	RD.CreateCannotActivateSameCodeEffect(e,aux.Stringid(m,3),m,tp,list[3])
end
```

### Rescue Rabbit (`120109057`)

Source: [Rush/Scripts/c120109057.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120109057.lua)

```lua
		end)
	end
	RD.CreateCannotActivateSameCodeEffect(e,aux.Stringid(m,2),m,tp,list[1])
end
function cm.desop(e,tp,eg,ep,ev,re,r,rp)
```
