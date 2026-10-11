# RushDuel.AttachExtraAttack

Alias: `RD.AttachExtraAttack`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.AttachExtraAttack(any e, any card, any value, any desc, any reset, any forced) -> any
```

## Description

Rush Duel helper declared in `RDAttach.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
赋予: 多次攻击
```

## Parameters

- `e` `any`: Type and behavior are not yet reviewed; see the source.
- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `value` `any`: Type and behavior are not yet reviewed; see the source.
- `desc` `any`: Type and behavior are not yet reviewed; see the source.
- `reset` `any`: Type and behavior are not yet reviewed; see the source.
- `forced` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDAttach.lua:26`

```lua
function RushDuel.AttachExtraAttack(e, card, value, desc, reset, forced)
    return RushDuel.CreateSingleEffect(e, desc, card, EFFECT_EXTRA_ATTACK, value, reset, forced)
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **26** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.AttachExtraAttack) with `RushDuel.AttachExtraAttack`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Volcalizing Salamandeus](/examples/rush-cards/120272039) | `120272039` | [Rush/Scripts/c120272039.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120272039.lua) | 1 |
| The Trinity Dragiastar | `120109031` | [Rush/Scripts/c120109031.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120109031.lua) | 1 |
| The Dragiastar | `120235035` | [Rush/Scripts/c120235035.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120235035.lua) | 1 |
| Voidvelg Chrysaor | `120244008` | [Rush/Scripts/c120244008.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120244008.lua) | 1 |
| Mega Jointech Fortrex \[L\] | `120249003` | [Rush/Scripts/c120249003.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120249003.lua) | 1 |
| Transam Variable Linac | `120245002` | [Rush/Scripts/c120245002.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120245002.lua) | 1 |
| Metarion King Cobrastar | `120205039` | [Rush/Scripts/c120205039.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120205039.lua) | 1 |
| Gias x Gias | `120246032` | [Rush/Scripts/c120246032.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120246032.lua) | 1 |
| Lightning Volteagle | `120246001` | [Rush/Scripts/c120246001.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120246001.lua) | 1 |
| Purple-Eyes Star Cat | `120235014` | [Rush/Scripts/c120235014.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120235014.lua) | 1 |
| Voidvelg Gigantomachia | `120244040` | [Rush/Scripts/c120244040.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120244040.lua) | 1 |
| Dark Matter Enigmight Geodiver | `120264041` | [Rush/Scripts/c120264041.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120264041.lua) | 1 |
| Madrhea Aquila | `120244030` | [Rush/Scripts/c120244030.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120244030.lua) | 1 |
| Solid Strike Dragon Metagiastar F | `120217004` | [Rush/Scripts/c120217004.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120217004.lua) | 1 |
| Double Chill Dragons | `120235034` | [Rush/Scripts/c120235034.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120235034.lua) | 1 |
| Steel Steed Martin Vainari | `120238016` | [Rush/Scripts/c120238016.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120238016.lua) | 1 |
| Ghost Vicious | `120228033` | [Rush/Scripts/c120228033.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120228033.lua) | 1 |
| Hyperstrike Dragon Dragiastar F | `120196022` | [Rush/Scripts/c120196022.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120196022.lua) | 1 |
| Cybersepice Queen Turmeric | `120264044` | [Rush/Scripts/c120264044.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120264044.lua) | 1 |
| Multistrike Dragon Dragias | `120110001` | [Rush/Scripts/c120110001.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120110001.lua) | 1 |
| Vice Jacker | `120170025` | [Rush/Scripts/c120170025.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120170025.lua) | 1 |
| Digracheon the Skysavior Radiaknight | `120301036` | [Rush/Scripts/c120301036.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120301036.lua) | 1 |
| Abad the Negahell Emperor | `120290100` | [Rush/Scripts/c120290100.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120290100.lua) | 1 |
| Hydra Viper | `120109047` | [Rush/Scripts/c120109047.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120109047.lua) | 1 |
| ...and 2 more |  |  |  |

## Script Examples

### Volcalizing Salamandeus (`120272039`)

Source: [Rush/Scripts/c120272039.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120272039.lua)

```lua
	if c:IsFaceup() and c:IsRelateToEffect(e) 
		and RD.IsSpecialSummonMainPhase(c) and e:GetLabel()==1 then
		RD.AttachExtraAttack(e,c,2,aux.Stringid(m,3),RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END)
	end
end
```

### The Trinity Dragiastar (`120109031`)

Source: [Rush/Scripts/c120109031.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120109031.lua)

```lua
	local c=e:GetHandler()
	if c:IsFaceup() and c:IsRelateToEffect(e) then
		RD.AttachExtraAttack(e,c,2,aux.Stringid(m,3),RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END)
	end
end
```

### The Dragiastar (`120235035`)

Source: [Rush/Scripts/c120235035.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120235035.lua)

```lua
	RD.SelectGroupAndDoAction(aux.Stringid(m,3),cm.filter1,cm.check,tp,LOCATION_MZONE,0,2,2,nil,function(g)
		g:ForEach(function(tc)
			RD.AttachExtraAttack(e,tc,1,aux.Stringid(m,4),RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END)
		end)
	end)
```
