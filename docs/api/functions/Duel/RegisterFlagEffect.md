# Duel.RegisterFlagEffect

## Signature

```lua
Duel.RegisterFlagEffect(int player, int code, int reset_flag, int property, int reset_count, [int label]) -> Effect
```

## Description

Registers a player/global flag effect on player and returns the created Effect.
The flag effect is player-targeted, field-only, cannot be disabled, and count=0 is treated as 1.

## Parameters

- `player` `int`
- `code` `int`
- `reset_flag` `int`
- `property` `int`
- `reset_count` `int` - default: 1
- `label` `int` optional

## Returns

- `Effect`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4853`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **329** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Duel.RegisterFlagEffect`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Artmage Non-Finito](/examples/cards/74631897) | `74631897` | [Scripts/c74631897.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74631897.lua) | 78 |
| [Pendulum Evolution](/examples/cards/55795155) | `55795155` | [Scripts/c55795155.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c55795155.lua) | 77 |
| [Eternal Favorite](/examples/cards/87532344) | `87532344` | [Scripts/c87532344.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c87532344.lua) | 73 |
| [Exciting Melffy Time](/examples/cards/58036097) | `58036097` | [Scripts/c58036097.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c58036097.lua) | 69 |
| [Mementotlan Fusion](/examples/cards/66518509) | `66518509` | [Scripts/c66518509.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c66518509.lua) | 67 |
| [Favorite HERO Flame Wingman](/examples/cards/13243124) | `13243124` | [Scripts/c13243124.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c13243124.lua) | 66 |
| [Gem-Knight Dispersion](/examples/cards/24220368) | `24220368` | [Scripts/c24220368.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24220368.lua) | 66 |
| [Ghostrick Renovation](/examples/cards/61818176) | `61818176` | [Scripts/c61818176.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c61818176.lua) | 65 |
| [Magnet Bonding](/examples/cards/65514302) | `65514302` | [Scripts/c65514302.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c65514302.lua) | 65 |
| [Hecahands Tartaros](/examples/cards/57809669) | `57809669` | [Scripts/c57809669.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c57809669.lua) | 65 |
| [Enneacraft - Archa.TAIL](/examples/cards/81237046) | `81237046` | [Scripts/c81237046.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c81237046.lua) | 63 |
| [D/D/D/D Dimensional King Arc Crisis](/examples/cards/71398055) | `71398055` | [Scripts/c71398055.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71398055.lua) | 63 |
| [Ultimate Crystal Rainbow Dragon Overdrive](/examples/cards/84544192) | `84544192` | [Scripts/c84544192.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c84544192.lua) | 62 |
| [Ashened to Endlessness](/examples/cards/34813443) | `34813443` | [Scripts/c34813443.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c34813443.lua) | 62 |
| [Penetration Fusion](/examples/cards/8778267) | `8778267` | [Scripts/c8778267.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c8778267.lua) | 62 |
| [Fiendsmith Kyrie](/examples/cards/26434972) | `26434972` | [Scripts/c26434972.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c26434972.lua) | 61 |
| [Chef de Nouvelles](/examples/cards/29251488) | `29251488` | [Scripts/c29251488.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c29251488.lua) | 60 |
| Artmage Pact -Awakening- | `23599634` | [Scripts/c23599634.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c23599634.lua) | 60 |
| Hunting Horn | `55421040` | [Scripts/c55421040.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c55421040.lua) | 59 |
| Echelon of the Fire Kings | `38798785` | [Scripts/c38798785.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c38798785.lua) | 59 |
| Double Interlock | `38129297` | [Scripts/c38129297.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c38129297.lua) | 59 |
| Mementotlan Shleepy | `50042011` | [Scripts/c50042011.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c50042011.lua) | 58 |
| K9-X Forced Release | `53792930` | [Scripts/c53792930.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c53792930.lua) | 58 |
| Dark Contact | `77124096` | [Scripts/c77124096.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c77124096.lua) | 58 |
| ...and 305 more |  |  |  |

## Script Examples

### Artmage Non-Finito (`74631897`)

Source: [Scripts/c74631897.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74631897.lua)

```lua
end
function s.regop(e,tp,eg,ep,ev,re,r,rp)
	Duel.RegisterFlagEffect(tp,id,RESET_PHASE+PHASE_END,0,1)
end
function s.spfilter(c,tp,sc)
```

### Pendulum Evolution (`55795155`)

Source: [Scripts/c55795155.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c55795155.lua)

```lua
	local tc=g:GetFirst()
	while tc do
		Duel.RegisterFlagEffect(tc:GetSummonPlayer(),55795155,RESET_PHASE+PHASE_END,0,1)
		tc=g:GetNext()
	end
```

### Eternal Favorite (`87532344`)

Source: [Scripts/c87532344.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c87532344.lua)

```lua
		and Duel.IsExistingMatchingCard(s.spfilter,tp,LOCATION_GRAVE+LOCATION_REMOVED,0,1,nil,e,tp) end
	Duel.Hint(HINT_OPSELECTED,1-tp,e:GetDescription())
	Duel.RegisterFlagEffect(tp,id,RESET_PHASE+PHASE_END,0,1)
	Duel.SetOperationInfo(0,CATEGORY_SPECIAL_SUMMON,nil,1,tp,LOCATION_GRAVE+LOCATION_REMOVED)
end
```
