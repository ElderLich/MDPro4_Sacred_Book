# RushDuel.ChangeCode

Alias: `RD.ChangeCode`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.ChangeCode(any e, any card, any code, any reset, any forced) -> any
```

## Description

Rush Duel helper declared in `RDAttach.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
赋予: 改变卡名
```

## Parameters

- `e` `any`: Type and behavior are not yet reviewed; see the source.
- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `code` `any`: Type and behavior are not yet reviewed; see the source.
- `reset` `any`: Type and behavior are not yet reviewed; see the source.
- `forced` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDAttach.lua:234`

```lua
function RushDuel.ChangeCode(e, card, code, reset, forced)
    return RushDuel.CreateSingleEffect(e, nil, card, EFFECT_CHANGE_CODE, code, reset, forced)
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **69** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.ChangeCode) with `RushDuel.ChangeCode`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [The Noodle Art of Flavor Shift](/examples/rush-cards/120300053) | `120300053` | [Rush/Scripts/c120300053.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120300053.lua) | 1 |
| [Red-Eyes Mars Dragon](/examples/rush-cards/120306034) | `120306034` | [Rush/Scripts/c120306034.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120306034.lua) | 1 |
| [Botonaginata the Music Princess](/examples/rush-cards/120290009) | `120290009` | [Rush/Scripts/c120290009.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120290009.lua) | 1 |
| [Soleil, the Fairy of Skysavior](/examples/rush-cards/120235020) | `120235020` | [Rush/Scripts/c120235020.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120235020.lua) | 1 |
| Darkness Jointech Tyrant | `120257018` | [Rush/Scripts/c120257018.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120257018.lua) | 1 |
| Harpie Lady Feather Duster | `120279002` | [Rush/Scripts/c120279002.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120279002.lua) | 1 |
| Lua, the Fairy of Skysavior | `120235021` | [Rush/Scripts/c120235021.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120235021.lua) | 1 |
| Imaginary Leading Actor | `120271029` | [Rush/Scripts/c120271029.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120271029.lua) | 1 |
| Battletested Curse of Dragon | `120249031` | [Rush/Scripts/c120249031.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120249031.lua) | 1 |
| Voidvelg Whiterider | `120109060` | [Rush/Scripts/c120109060.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120109060.lua) | 1 |
| Accel Wonder Dark | `120285005` | [Rush/Scripts/c120285005.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120285005.lua) | 1 |
| Voidalfr Buprestruve | `120300003` | [Rush/Scripts/c120300003.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120300003.lua) | 1 |
| Blue-Eyes Vision Dragon | `120252004` | [Rush/Scripts/c120252004.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120252004.lua) | 1 |
| Vic Viper Beginning | `120294026` | [Rush/Scripts/c120294026.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120294026.lua) | 1 |
| Battletested Gaia The Fierce Knight | `120249032` | [Rush/Scripts/c120249032.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120249032.lua) | 1 |
| Cyber Processor | `120244021` | [Rush/Scripts/c120244021.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120244021.lua) | 1 |
| Skull Archfiend of Confusion | `120277023` | [Rush/Scripts/c120277023.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120277023.lua) | 1 |
| The Swordsman Who Doles Out Victory | `120290023` | [Rush/Scripts/c120290023.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120290023.lua) | 1 |
| Enceladustellime | `120304003` | [Rush/Scripts/c120304003.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120304003.lua) | 1 |
| Rare Dragorite | `120294008` | [Rush/Scripts/c120294008.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120294008.lua) | 1 |
| Vic Viper Spread Bomb | `120294025` | [Rush/Scripts/c120294025.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120294025.lua) | 1 |
| Etraynze the Sprinting Shadow Flower Ninja | `120285012` | [Rush/Scripts/c120285012.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120285012.lua) | 1 |
| The Draco | `120294002` | [Rush/Scripts/c120294002.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120294002.lua) | 1 |
| Resurrection Heliacal Riser | `120304039` | [Rush/Scripts/c120304039.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120304039.lua) | 1 |
| ...and 45 more |  |  |  |

## Script Examples

### The Noodle Art of Flavor Shift (`120300053`)

Source: [Rush/Scripts/c120300053.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120300053.lua)

```lua
	local filter=RD.Filter(cm.filter,tc)
	RD.SelectAndDoAction(aux.Stringid(m,1),filter,tp,LOCATION_MZONE,0,1,1,nil,function(g)
		RD.ChangeCode(e,g:GetFirst(),ac,RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END)
	end)
end
```

### Red-Eyes Mars Dragon (`120306034`)

Source: [Rush/Scripts/c120306034.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120306034.lua)

```lua
	local c=e:GetHandler()
	if c:IsFaceup() and c:IsRelateToEffect(e) then
		RD.ChangeCode(e,c,list[1],RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END)
		if Duel.IsExistingMatchingCard(cm.exfilter,tp,LOCATION_GRAVE,0,1,nil) then
			RD.CanDraw(aux.Stringid(m,2),tp,1)
```

### Botonaginata the Music Princess (`120290009`)

Source: [Rush/Scripts/c120290009.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120290009.lua)

```lua
	local c=e:GetHandler()
	if c:IsFaceup() and c:IsRelateToEffect(e) then
		RD.ChangeCode(e,c,list[1],RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END)
		RD.CanSelectAndDoAction(aux.Stringid(m,1),HINTMSG_ATOHAND,aux.NecroValleyFilter(cm.thfilter),tp,LOCATION_GRAVE,0,1,1,nil,function(g)
			Duel.BreakEffect()
```
