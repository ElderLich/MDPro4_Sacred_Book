# RushDuel.AttachCannotAttack

Alias: `RD.AttachCannotAttack`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.AttachCannotAttack(any e, any card, any desc, any reset, any forced) -> any
```

## Description

Rush Duel helper declared in `RDAttach.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
赋予: 不能攻击
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

`Rush/Utilities/RDAttach.lua:170`

```lua
function RushDuel.AttachCannotAttack(e, card, desc, reset, forced)
    return RushDuel.CreateSingleEffect(e, desc, card, EFFECT_CANNOT_ATTACK, nil, reset, forced)
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **9** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.AttachCannotAttack) with `RushDuel.AttachCannotAttack`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Invitation to a Delirious Dream](/examples/rush-cards/120261066) | `120261066` | [Rush/Scripts/c120261066.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120261066.lua) | 1 |
| Instant Fusion | `120305053` | [Rush/Scripts/c120305053.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120305053.lua) | 1 |
| The Swordsman Who Doles Out Victory | `120290023` | [Rush/Scripts/c120290023.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120290023.lua) | 1 |
| Summoner Monk | `120307009` | [Rush/Scripts/c120307009.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120307009.lua) | 1 |
| Harpie Lady 3 | `120247006` | [Rush/Scripts/c120247006.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120247006.lua) | 1 |
| Tribute Doll | `120214009` | [Rush/Scripts/c120214009.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120214009.lua) | 1 |
| Super Conductor Tyranno | `120274078` | [Rush/Scripts/c120274078.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120274078.lua) | 1 |
| Mind Control | `120280029` | [Rush/Scripts/c120280029.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120280029.lua) | 1 |
| Silent Doom | `120234004` | [Rush/Scripts/c120234004.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120234004.lua) | 1 |

## Script Examples

### Invitation to a Delirious Dream (`120261066`)

Source: [Rush/Scripts/c120261066.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120261066.lua)

```lua
		local tc=g:GetFirst()
		if Duel.GetControl(tc,tp)~=0 then
			RD.AttachCannotAttack(e,tc,aux.Stringid(m,1),RESET_EVENT+RESETS_STANDARD)
			RD.AttachCannotTrigger(e,tc,aux.Stringid(m,2),RESET_EVENT+RESETS_STANDARD)
		end
```

### Instant Fusion (`120305053`)

Source: [Rush/Scripts/c120305053.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120305053.lua)

```lua
		tc:SetMaterial(nil)
		if Duel.SpecialSummon(tc,SUMMON_TYPE_FUSION,tp,tp,false,false,POS_FACEUP)~=0 then
			RD.AttachCannotAttack(e,tc,aux.Stringid(m,1),RESET_EVENT+RESETS_STANDARD)
			RD.AttachEndPhase(e,tc,tp,m,cm.tgop,aux.Stringid(m,2),true)
		end
```

### The Swordsman Who Doles Out Victory (`120290023`)

Source: [Rush/Scripts/c120290023.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120290023.lua)

```lua
			RD.SendToHandAndExists(g,e,tp,REASON_EFFECT)
		end)
		RD.AttachCannotAttack(e,c,aux.Stringid(m,2),RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END)
	end
end
```
