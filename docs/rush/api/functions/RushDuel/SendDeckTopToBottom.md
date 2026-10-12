# RushDuel.SendDeckTopToBottom

Alias: `RD.SendDeckTopToBottom`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.SendDeckTopToBottom(any player, any count) -> any
```

## Description

Rush Duel helper declared in `RDFunction.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
将玩家卡组最上面的N张卡移到卡组最下面
```

## Parameters

- `player` `any`: Type and behavior are not yet reviewed; see the source.
- `count` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDFunction.lua:139`

```lua
function RushDuel.SendDeckTopToBottom(player, count)
    for i = 1, count do
        Duel.MoveSequence(Duel.GetDecktopGroup(player, 1):GetFirst(), 1)
    end
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **58** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.SendDeckTopToBottom) with `RushDuel.SendDeckTopToBottom`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Skysavior Watch](/examples/rush-cards/120235053) | `120235053` | [Rush/Scripts/c120235053.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120235053.lua) | 1 |
| [Moonforce Sheila](/examples/rush-cards/120300013) | `120300013` | [Rush/Scripts/c120300013.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120300013.lua) | 1 |
| [Soleil, the Fairy of Skysavior](/examples/rush-cards/120235020) | `120235020` | [Rush/Scripts/c120235020.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120235020.lua) | 1 |
| [Crystal Seer](/examples/rush-cards/120109067) | `120109067` | [Rush/Scripts/c120109067.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120109067.lua) | 1 |
| Hydrangea the Shadow Flower Tea Master | `120304029` | [Rush/Scripts/c120304029.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120304029.lua) | 1 |
| Abysslayer Quintiamat | `120257021` | [Rush/Scripts/c120257021.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120257021.lua) | 1 |
| Rurigra the Eternal | `120285028` | [Rush/Scripts/c120285028.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120285028.lua) | 1 |
| Cornetlass the Music Princess | `120287066` | [Rush/Scripts/c120287066.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120287066.lua) | 1 |
| Rising HERO Argent | `120263010` | [Rush/Scripts/c120263010.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120263010.lua) | 1 |
| Lostream Record | `120309044` | [Rush/Scripts/c120309044.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120309044.lua) | 1 |
| Lovely Ange | `120272026` | [Rush/Scripts/c120272026.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120272026.lua) | 1 |
| Voidvelg Whiterider | `120109060` | [Rush/Scripts/c120109060.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120109060.lua) | 1 |
| Hybridrive Orbuster | `120264007` | [Rush/Scripts/c120264007.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120264007.lua) | 1 |
| Memory of Sunlit | `120300051` | [Rush/Scripts/c120300051.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120300051.lua) | 1 |
| Machine Inspector | `120257057` | [Rush/Scripts/c120257057.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120257057.lua) | 2 |
| Scissor Hercules | `120298038` | [Rush/Scripts/c120298038.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120298038.lua) | 1 |
| Power Capsule Red | `120294056` | [Rush/Scripts/c120294056.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120294056.lua) | 1 |
| Fist the Star Protector's Roaring Gauntlet | `120306011` | [Rush/Scripts/c120306011.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120306011.lua) | 1 |
| Leave it to the Sparkhearts! | `120298021` | [Rush/Scripts/c120298021.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120298021.lua) | 1 |
| Weaksauce Brassdes | `120304066` | [Rush/Scripts/c120304066.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120304066.lua) | 1 |
| Gravitiara Eye | `120254027` | [Rush/Scripts/c120254027.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120254027.lua) | 2 |
| Imaginary Arc Actor | `120271037` | [Rush/Scripts/c120271037.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120271037.lua) | 1 |
| Encounter of the Stars | `120305025` | [Rush/Scripts/c120305025.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120305025.lua) | 1 |
| Dice Key Mekuru | `120261010` | [Rush/Scripts/c120261010.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120261010.lua) | 1 |
| ...and 34 more |  |  |  |

## Script Examples

### Skysavior Watch (`120235053`)

Source: [Rush/Scripts/c120235053.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120235053.lua)

```lua
	if ct>0 then
		Duel.SortDecktop(tp,p,ct)
		RD.SendDeckTopToBottom(p,ct)
	end
	if Duel.GetFlagEffect(tp,m)~=0 then return end
```

### Moonforce Sheila (`120300013`)

Source: [Rush/Scripts/c120300013.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120300013.lua)

```lua
	if ct>0 then
		Duel.SortDecktop(tp,tp,ct)
		RD.SendDeckTopToBottom(tp,ct)
	end
	if Duel.GetFlagEffect(tp,m)~=0 then return end
```

### Soleil, the Fairy of Skysavior (`120235020`)

Source: [Rush/Scripts/c120235020.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120235020.lua)

```lua
		if ct>0 then
			Duel.SortDecktop(tp,tp,ct)
			RD.SendDeckTopToBottom(tp,ct)
		end
	end
```
