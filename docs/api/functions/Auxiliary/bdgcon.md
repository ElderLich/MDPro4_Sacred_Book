# Auxiliary.bdgcon

## Signature

```lua
Auxiliary.bdgcon(Effect e, int tp, Group eg, int ep, int ev, Effect re, int r, int rp) -> bool
```

## Description

Battle-destroying condition helper for a handler whose battle target is a monster in the Graveyard.

## Parameters

- `e` `Effect`
- `tp` `int`
- `eg` `Group`
- `ep` `int`
- `ev` `int`
- `re` `Effect`
- `r` `int`
- `rp` `int`

## Returns

- `bool`

## Source

- `Utilities/utility.lua:774`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **12** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Auxiliary.bdgcon`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Alien Mother | `24104865` | [Scripts/c24104865.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24104865.lua) | 50 |
| Toy Parade | `92607427` | [Scripts/c92607427.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92607427.lua) | 46 |
| Number 39: Utopia the Envoy of Light | `76504386` | [Scripts/c76504386.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c76504386.lua) | 44 |
| Odd-Eyes Saber Dragon | `19221310` | [Scripts/c19221310.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c19221310.lua) | 38 |
| Draco Berserker of the Tenyi | `5041348` | [Scripts/c5041348.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c5041348.lua) | 34 |
| Stygian Street Patrol | `13521194` | [Scripts/c13521194.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c13521194.lua) | 32 |
| CXyz Skypalace Babylon | `49202331` | [Scripts/c49202331.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c49202331.lua) | 31 |
| Elemental HERO Shining Flare Wingman | `25366484` | [Scripts/c25366484.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c25366484.lua) | 30 |
| Divine Dragon - Excelion | `10032958` | [Scripts/c10032958.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c10032958.lua) | 29 |
| Cyber Angel Benten | `77235086` | [Scripts/c77235086.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c77235086.lua) | 29 |
| Evil HERO Inferno Wing | `22160245` | [Scripts/c22160245.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c22160245.lua) | 26 |
| Windaar, Sage of Gusto | `27944249` | [Scripts/c27944249.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c27944249.lua) | 25 |

## Script Examples

### Alien Mother (`24104865`)

Source: [Scripts/c24104865.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24104865.lua)

```lua
		e:SetLabel(c:GetFieldID())
	end
	if aux.bdgcon(e,tp,eg,ep,ev,re,r,rp) then
		g:AddCard(t)
		t:RegisterFlagEffect(24104865,RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_BATTLE,0,1)
```

### Toy Parade (`92607427`)

Source: [Scripts/c92607427.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92607427.lua)

```lua
end
function c92607427.atkcon(e,tp,eg,ep,ev,re,r,rp)
	return aux.bdgcon(e,tp,eg,ep,ev,re,r,rp) and e:GetHandler():IsChainAttackable(0)
end
function c92607427.atkop(e,tp,eg,ep,ev,re,r,rp)
```

### Number 39: Utopia the Envoy of Light (`76504386`)

Source: [Scripts/c76504386.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c76504386.lua)

```lua
			e2:SetCode(EVENT_BATTLE_DESTROYING)
			e2:SetType(EFFECT_TYPE_SINGLE+EFFECT_TYPE_TRIGGER_O)
			e2:SetCondition(aux.bdgcon)
			e2:SetTarget(s.sptg)
			e2:SetOperation(s.spop)
```
