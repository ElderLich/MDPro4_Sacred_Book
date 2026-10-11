# RushDuel.AttachCannotDirectAttack

Alias: `RD.AttachCannotDirectAttack`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.AttachCannotDirectAttack(any e, any card, any desc, any reset, any forced) -> any
```

## Description

Rush Duel helper declared in `RDAttach.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
赋予: 不能直接攻击
```

## Parameters

- `e` `any`: Type and behavior are not yet reviewed; see the source.
- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `desc` `any`: Type and behavior are not yet reviewed; see the source.
- `reset` `any`: Type and behavior are not yet reviewed; see the source.
- `forced` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDAttach.lua:174`

```lua
function RushDuel.AttachCannotDirectAttack(e, card, desc, reset, forced)
    return RushDuel.CreateSingleEffect(e, desc, card, EFFECT_CANNOT_DIRECT_ATTACK, nil, reset, forced)
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **13** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.AttachCannotDirectAttack) with `RushDuel.AttachCannotDirectAttack`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Etraynze the Shadow Flower Ninja | `120170029` | [Rush/Scripts/c120170029.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120170029.lua) | 1 |
| Black Luster Soljersey - Envoy of the Drying | `120228017` | [Rush/Scripts/c120228017.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120228017.lua) | 1 |
| Dark Matter Requiem Omega | `120264040` | [Rush/Scripts/c120264040.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120264040.lua) | 1 |
| Beast Gear King Convoy Liogon | `120145031` | [Rush/Scripts/c120145031.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120145031.lua) | 1 |
| Ever-Grace Princess Mai | `120287014` | [Rush/Scripts/c120287014.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120287014.lua) | 1 |
| Blue-Fang Concurrent Burst Dragon | `120109046` | [Rush/Scripts/c120109046.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120109046.lua) | 1 |
| Transam Power Linac | `120260058` | [Rush/Scripts/c120260058.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120260058.lua) | 1 |
| Shock Dragon | `120130021` | [Rush/Scripts/c120130021.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120130021.lua) | 1 |
| Supreme Skystream Magnum Overlord \[R\] | `120151003` | [Rush/Scripts/c120151003.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120151003.lua) | 1 |
| Dankus, the Knight of Skysavior | `120235025` | [Rush/Scripts/c120235025.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120235025.lua) | 1 |
| Reprinter | `120199049` | [Rush/Scripts/c120199049.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120199049.lua) | 1 |
| Music Princess's Breath | `120155045` | [Rush/Scripts/c120155045.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120155045.lua) | 1 |
| Dual Coratlus | `120225008` | [Rush/Scripts/c120225008.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120225008.lua) | 1 |

## Script Examples

### Etraynze the Shadow Flower Ninja (`120170029`)

Source: [Rush/Scripts/c120170029.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120170029.lua)

```lua
			RD.AttachEndPhase(e,tc,tp,m,cm.tdop,aux.Stringid(m,1))
			if c:IsFaceup() and c:IsRelateToEffect(e) then
				RD.AttachCannotDirectAttack(e,c,aux.Stringid(m,2),RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END)
			end
		end
```

### Black Luster Soljersey - Envoy of the Drying (`120228017`)

Source: [Rush/Scripts/c120228017.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120228017.lua)

```lua
		local c=e:GetHandler()
		if c:IsFaceup() and c:IsRelateToEffect(e) then
			RD.AttachCannotDirectAttack(e,c,aux.Stringid(m,1),RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END)
		end
	end)
```

### Dark Matter Requiem Omega (`120264040`)

Source: [Rush/Scripts/c120264040.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120264040.lua)

```lua
	if c:IsFaceup() and c:IsRelateToEffect(e) then
		RD.AttachAtkDef(e,c,1300,0,RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END)
		RD.AttachCannotDirectAttack(e,c,aux.Stringid(m,2),RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END)
	end
end
```
