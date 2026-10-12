# RushDuel.AttachBattleIndes

Alias: `RD.AttachBattleIndes`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.AttachBattleIndes(any e, any card, any value, any desc, any reset, any forced) -> any
```

## Description

Rush Duel helper declared in `RDAttach.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
赋予: 效果战斗抗性
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

`Rush/Utilities/RDAttach.lua:75`

```lua
function RushDuel.AttachBattleIndes(e, card, value, desc, reset, forced)
    return RushDuel.CreateSingleEffect(e, desc, card, EFFECT_INDESTRUCTABLE_BATTLE, value, reset, forced)
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **27** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.AttachBattleIndes) with `RushDuel.AttachBattleIndes`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Valkyrian Guard](/examples/rush-cards/120231066) | `120231066` | [Rush/Scripts/c120231066.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120231066.lua) | 1 |
| [Star Protector Recapture](/examples/rush-cards/120306063) | `120306063` | [Rush/Scripts/c120306063.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120306063.lua) | 1 |
| Fusionic Defense | `120257064` | [Rush/Scripts/c120257064.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120257064.lua) | 1 |
| Skysavior Defense | `120301054` | [Rush/Scripts/c120301054.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120301054.lua) | 1 |
| Abysskite Ultimail | `120239048` | [Rush/Scripts/c120239048.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120239048.lua) | 1 |
| Abysskite Kaleido-Dress | `120290061` | [Rush/Scripts/c120290061.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120290061.lua) | 1 |
| Looter Force | `120228064` | [Rush/Scripts/c120228064.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120228064.lua) | 1 |
| Transam Variable Linac | `120245002` | [Rush/Scripts/c120245002.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120245002.lua) | 1 |
| Supreme Dog Ropero | `120239022` | [Rush/Scripts/c120239022.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120239022.lua) | 1 |
| Destined Doom of the Defiant Souls | `120298016` | [Rush/Scripts/c120298016.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120298016.lua) | 1 |
| Flower Fan Clematis | `120254072` | [Rush/Scripts/c120254072.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120254072.lua) | 1 |
| Dark Matter Enigmight Geodiver | `120264041` | [Rush/Scripts/c120264041.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120264041.lua) | 1 |
| Jointech Great Wall | `120235057` | [Rush/Scripts/c120235057.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120235057.lua) | 1 |
| Featuring Omega | `120217049` | [Rush/Scripts/c120217049.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120217049.lua) | 1 |
| Solid Strike Dragon Metagiastar F | `120217004` | [Rush/Scripts/c120217004.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120217004.lua) | 1 |
| Steel Strike Dragon Metagias | `120183017` | [Rush/Scripts/c120183017.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120183017.lua) | 1 |
| Jointech Ignition | `120249058` | [Rush/Scripts/c120249058.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120249058.lua) | 1 |
| Rocket Warrior | `120307023` | [Rush/Scripts/c120307023.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120307023.lua) | 1 |
| Magic Fire Guard | `120217023` | [Rush/Scripts/c120217023.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120217023.lua) | 1 |
| Rolled Sticky Save | `120151046` | [Rush/Scripts/c120151046.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120151046.lua) | 1 |
| Transam Lightning | `120235056` | [Rush/Scripts/c120235056.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120235056.lua) | 1 |
| Ninjitsu Art of Ultimate Transformation | `120306056` | [Rush/Scripts/c120306056.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120306056.lua) | 1 |
| Salary Slash | `120183062` | [Rush/Scripts/c120183062.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120183062.lua) | 2 |
| LED Pigeon | `120259003` | [Rush/Scripts/c120259003.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120259003.lua) | 1 |
| ...and 3 more |  |  |  |

## Script Examples

### Valkyrian Guard (`120231066`)

Source: [Rush/Scripts/c120231066.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120231066.lua)

```lua
				og:ForEach(function(tc)
					if tc:IsPosition(POS_FACEUP_DEFENSE) then
						local buff=RD.AttachBattleIndes(e,tc,1,aux.Stringid(m,2),RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END)
						buff:SetCondition(cm.buffcon)
					end
```

### Star Protector Recapture (`120306063`)

Source: [Rush/Scripts/c120306063.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120306063.lua)

```lua
			and RD.CanSelectAndSpecialSummon(aux.Stringid(m,1),aux.NecroValleyFilter(cm.spfilter),tp,LOCATION_GRAVE,0,1,1,nil,e,POS_FACEUP)~=0 then
			local tc=Duel.GetOperatedGroup():GetFirst()
			RD.AttachBattleIndes(e,tc,1,aux.Stringid(m,2),RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END)
		end
	end)
```

### Fusionic Defense (`120257064`)

Source: [Rush/Scripts/c120257064.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120257064.lua)

```lua
			Duel.BreakEffect()
			local tc=g:GetFirst()
			RD.AttachBattleIndes(e,tc,1,aux.Stringid(m,3),RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END)
			RD.AttachEffectIndes(e,tc,cm.indval,aux.Stringid(m,4),RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END)
		end)
```
