# Auxiliary.bdogcon

## Signature

```lua
Auxiliary.bdogcon(Effect e, int tp, Group eg, int ep, any ev, Effect re, any r, int rp) -> void
```

## Description

Check if e:GetHandler() is related to the current battle, typically used for EVENT_BATTLE_DESTROYING, when battling an opponent's monster and destroying it by battle, sending it to the Graveyard, as a condition
function Auxiliary.bdogcon(e, tp, eg, ep, ev, re, r, rp)
  local c=e:GetHandler()
  local bc=c:GetBattleTarget()
  return c:IsRelateToBattle() and c:IsStatus(STATUS_OPPO_BATTLE) and bc:IsLocation(LOCATION_GRAVE) and bc:IsType(TYPE_MONSTER)
end

## Parameters

- `e` `Effect`
- `tp` `int`
- `eg` `Group`
- `ep` `int`
- `ev` `any`
- `re` `Effect`
- `r` `any`
- `rp` `int`

## Source

- `Utilities/utility.lua:780`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **29** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Auxiliary.bdogcon`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Sunvine Thrasher | `91557476` | [Scripts/c91557476.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c91557476.lua) | 47 |
| Ancient Warriors - Ambitious Cao De | `33545259` | [Scripts/c33545259.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c33545259.lua) | 45 |
| Beginning Knight | `6628343` | [Scripts/c6628343.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c6628343.lua) | 42 |
| Blackwing - Boreastorm the Wicked Wind | `10602628` | [Scripts/c10602628.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c10602628.lua) | 42 |
| Goyo King | `84305651` | [Scripts/c84305651.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c84305651.lua) | 40 |
| Dragon Knight of Creation | `87835759` | [Scripts/c87835759.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c87835759.lua) | 39 |
| Vector Scare Archfiend | `13452889` | [Scripts/c13452889.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c13452889.lua) | 36 |
| Black Luster Soldier - Super Soldier | `54484652` | [Scripts/c54484652.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c54484652.lua) | 34 |
| Gladiator Beast Samnite | `2619149` | [Scripts/c2619149.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c2619149.lua) | 33 |
| Goyo Chaser | `63364266` | [Scripts/c63364266.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63364266.lua) | 33 |
| BOXer | `61156777` | [Scripts/c61156777.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c61156777.lua) | 32 |
| Masked HERO Divine Wind | `22093873` | [Scripts/c22093873.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c22093873.lua) | 30 |
| Goyo Predator | `98637386` | [Scripts/c98637386.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c98637386.lua) | 27 |
| Number 14: Greedy Sarameya | `21313376` | [Scripts/c21313376.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c21313376.lua) | 26 |
| Sylvan Bladefender | `11682713` | [Scripts/c11682713.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c11682713.lua) | 26 |
| Mermail Abyssnose | `282886` | [Scripts/c282886.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c282886.lua) | 26 |
| Heroic Challenger - War Hammer | `26885836` | [Scripts/c26885836.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c26885836.lua) | 26 |
| Crimson Blader | `80321197` | [Scripts/c80321197.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c80321197.lua) | 26 |
| Inferno Hammer | `17185260` | [Scripts/c17185260.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c17185260.lua) | 24 |
| Blackwing - Shura the Blue Flame | `58820853` | [Scripts/c58820853.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c58820853.lua) | 24 |
| Goyo Guardian | `7391448` | [Scripts/c7391448.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c7391448.lua) | 24 |
| The Fabled Kokkator | `26704411` | [Scripts/c26704411.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c26704411.lua) | 24 |
| Performapal Handsamuraiger | `55997110` | [Scripts/c55997110.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c55997110.lua) | 22 |
| Flamvell Firedog | `23297235` | [Scripts/c23297235.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c23297235.lua) | 22 |
| ...and 5 more |  |  |  |

## Script Examples

### Sunvine Thrasher (`91557476`)

Source: [Scripts/c91557476.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c91557476.lua)

```lua
	e3:SetCode(EVENT_BATTLE_DESTROYING)
	e3:SetType(EFFECT_TYPE_SINGLE+EFFECT_TYPE_TRIGGER_O)
	e3:SetCondition(aux.bdogcon)
	e3:SetTarget(c91557476.sptg)
	e3:SetOperation(c91557476.spop)
```

### Ancient Warriors - Ambitious Cao De (`33545259`)

Source: [Scripts/c33545259.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c33545259.lua)

```lua
	e4:SetCode(EVENT_BATTLE_DESTROYING)
	e4:SetCountLimit(1,33545260)
	e4:SetCondition(aux.bdogcon)
	e4:SetTarget(c33545259.sptg2)
	e4:SetOperation(c33545259.spop2)
```

### Beginning Knight (`6628343`)

Source: [Scripts/c6628343.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c6628343.lua)

```lua
end
function c6628343.atcon(e,tp,eg,ep,ev,re,r,rp)
	return aux.bdogcon(e,tp,eg,ep,ev,re,r,rp) and e:GetHandler():IsChainAttackable()
end
function c6628343.atop(e,tp,eg,ep,ev,re,r,rp)
```
