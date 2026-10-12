# RushDuel.AttachExtraAttackMonster

Alias: `RD.AttachExtraAttackMonster`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.AttachExtraAttackMonster(any e, any card, any value, any desc, any reset, any forced) -> any
```

## Description

Rush Duel helper declared in `RDAttach.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
赋予: 多次攻击 (怪兽限定)
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

`Rush/Utilities/RDAttach.lua:30`

```lua
function RushDuel.AttachExtraAttackMonster(e, card, value, desc, reset, forced)
    return RushDuel.CreateSingleEffect(e, desc, card, EFFECT_EXTRA_ATTACK_MONSTER, value, reset, forced)
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **30** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.AttachExtraAttackMonster) with `RushDuel.AttachExtraAttackMonster`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Dark Matter Transcend Dragon | `120272044` | [Rush/Scripts/c120272044.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120272044.lua) | 1 |
| Celeb Rose Influencers | `120257044` | [Rush/Scripts/c120257044.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120257044.lua) | 1 |
| Illusion Strike Dragon Miragias | `120145025` | [Rush/Scripts/c120145025.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120145025.lua) | 1 |
| Meet and Greed | `120208044` | [Rush/Scripts/c120208044.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120208044.lua) | 1 |
| Mega Jointech Fortrex \[L\] | `120249003` | [Rush/Scripts/c120249003.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120249003.lua) | 1 |
| Dual Space Yggdrago | `120260008` | [Rush/Scripts/c120260008.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120260008.lua) | 2 |
| Sacrificial Summon | `120217094` | [Rush/Scripts/c120217094.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120217094.lua) | 1 |
| Nullstrike Dragon Zerogias | `120180001` | [Rush/Scripts/c120180001.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120180001.lua) | 1 |
| Celeb Rose Luxury Magicians | `120244042` | [Rush/Scripts/c120244042.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120244042.lua) | 1 |
| Cross Lostream Melutine | `120309036` | [Rush/Scripts/c120309036.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120309036.lua) | 1 |
| Blue-Fang Concurrent Burst Dragon | `120109046` | [Rush/Scripts/c120109046.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120109046.lua) | 1 |
| Mega Multistrike Dragon Dragias Burst \[L\] | `120210001` | [Rush/Scripts/c120210001.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120210001.lua) | 1 |
| Void Strike Dragon Zerogaigias | `120211001` | [Rush/Scripts/c120211001.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120211001.lua) | 1 |
| Twin Edge Phantom Dragon | `120261030` | [Rush/Scripts/c120261030.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120261030.lua) | 1 |
| Sevensgias the Magical Dragon Knight | `120208037` | [Rush/Scripts/c120208037.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120208037.lua) | 1 |
| Grand Legendary Saber | `120271041` | [Rush/Scripts/c120271041.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120271041.lua) | 1 |
| Solid Strike Dragon Metagiastar F | `120217004` | [Rush/Scripts/c120217004.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120217004.lua) | 1 |
| Ever-Grace Princess Mari | `120287015` | [Rush/Scripts/c120287015.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120287015.lua) | 1 |
| Steel Strike Dragon Metagias | `120183017` | [Rush/Scripts/c120183017.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120183017.lua) | 1 |
| Hyperstrike Dragon Dragiastar F | `120196022` | [Rush/Scripts/c120196022.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120196022.lua) | 1 |
| Elemental HERO Sky Neos | `120272066` | [Rush/Scripts/c120272066.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120272066.lua) | 1 |
| Polygon Butterfly | `120249033` | [Rush/Scripts/c120249033.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120249033.lua) | 1 |
| Transam Jelai | `120223011` | [Rush/Scripts/c120223011.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120223011.lua) | 1 |
| Gilford the Rising | `120235028` | [Rush/Scripts/c120235028.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120235028.lua) | 1 |
| ...and 6 more |  |  |  |

## Script Examples

### Dark Matter Transcend Dragon (`120272044`)

Source: [Rush/Scripts/c120272044.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120272044.lua)

```lua
	local c=e:GetHandler()
	if c:IsFaceup() and c:IsRelateToEffect(e) then
		RD.AttachExtraAttackMonster(e,c,2,aux.Stringid(m,2),RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END)
		RD.AttachPierce(e,c,aux.Stringid(m,3),RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END)
		RD.CanSelectAndSpecialSummon(aux.Stringid(m,4),aux.NecroValleyFilter(cm.spfilter),tp,0,LOCATION_GRAVE,1,3,nil,e,POS_FACEDOWN_DEFENSE,false,1-tp)
```

### Celeb Rose Influencers (`120257044`)

Source: [Rush/Scripts/c120257044.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120257044.lua)

```lua
			if c:GetEquipCount()~=0 then
				RD.AttachEffectIndes(e,c,cm.indval,aux.Stringid(m,1),RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END)
				RD.AttachExtraAttackMonster(e,c,1,aux.Stringid(m,2),RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END)
			end
		end
```

### Illusion Strike Dragon Miragias (`120145025`)

Source: [Rush/Scripts/c120145025.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120145025.lua)

```lua
			e1:SetReset(RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END)
			c:RegisterEffect(e1)
			local e2=RD.AttachExtraAttackMonster(e,c,1,aux.Stringid(m,2),RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END)
			e2:SetCondition(cm.atkcon)
		end
```
