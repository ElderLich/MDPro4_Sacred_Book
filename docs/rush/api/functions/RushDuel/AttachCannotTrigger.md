# RushDuel.AttachCannotTrigger

Alias: `RD.AttachCannotTrigger`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.AttachCannotTrigger(any e, any card, any desc, any reset, any forced) -> any
```

## Description

Rush Duel helper declared in `RDAttach.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
赋予: 不能发动效果
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

`Rush/Utilities/RDAttach.lua:194`

```lua
function RushDuel.AttachCannotTrigger(e, card, desc, reset, forced)
    return RushDuel.CreateSingleEffect(e, desc, card, EFFECT_CANNOT_TRIGGER, nil, reset, forced)
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **15** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.AttachCannotTrigger) with `RushDuel.AttachCannotTrigger`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Invitation to a Delirious Dream](/examples/rush-cards/120261066) | `120261066` | [Rush/Scripts/c120261066.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120261066.lua) | 1 |
| Reshef the Dark Being | `120306069` | [Rush/Scripts/c120306069.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120306069.lua) | 1 |
| Healthie Tigasati | `120306042` | [Rush/Scripts/c120306042.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120306042.lua) | 1 |
| Lovely Sanctuary | `120260052` | [Rush/Scripts/c120260052.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120260052.lua) | 1 |
| King's Authority | `120254088` | [Rush/Scripts/c120254088.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120254088.lua) | 1 |
| Raging Rock | `120246072` | [Rush/Scripts/c120246072.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120246072.lua) | 1 |
| Spirit of Isyria | `120300061` | [Rush/Scripts/c120300061.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120300061.lua) | 1 |
| Yabume the Frost-Purifying Purebreed | `120298045` | [Rush/Scripts/c120298045.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120298045.lua) | 1 |
| Magma Dragon | `120109064` | [Rush/Scripts/c120109064.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120109064.lua) | 1 |
| Metarion Medustar | `120271018` | [Rush/Scripts/c120271018.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120271018.lua) | 1 |
| Brain Control | `120307003` | [Rush/Scripts/c120307003.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120307003.lua) | 1 |
| Thunderbeetle Crash | `120306007` | [Rush/Scripts/c120306007.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120306007.lua) | 1 |
| The Chop | `120294061` | [Rush/Scripts/c120294061.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120294061.lua) | 1 |
| Criatura Brazo | `120291005` | [Rush/Scripts/c120291005.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120291005.lua) | 1 |
| Ultimate Flag Beast Boltricorn | `120246013` | [Rush/Scripts/c120246013.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120246013.lua) | 1 |

## Script Examples

### Invitation to a Delirious Dream (`120261066`)

Source: [Rush/Scripts/c120261066.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120261066.lua)

```lua
		if Duel.GetControl(tc,tp)~=0 then
			RD.AttachCannotAttack(e,tc,aux.Stringid(m,1),RESET_EVENT+RESETS_STANDARD)
			RD.AttachCannotTrigger(e,tc,aux.Stringid(m,2),RESET_EVENT+RESETS_STANDARD)
		end
	end)
```

### Reshef the Dark Being (`120306069`)

Source: [Rush/Scripts/c120306069.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120306069.lua)

```lua
		local tc=g:GetFirst()
		if Duel.GetControl(tc,tp,PHASE_END,1)~=0 then
			RD.AttachCannotTrigger(e,tc,aux.Stringid(m,1),RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END)
		end
	end)
```

### Healthie Tigasati (`120306042`)

Source: [Rush/Scripts/c120306042.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120306042.lua)

```lua
				g:ForEach(function(tc)
					RD.AttachAtkDef(e,tc,400,0,RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END)
					RD.AttachCannotTrigger(e,tc,aux.Stringid(m,1),RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END)
				end)
			end
```
