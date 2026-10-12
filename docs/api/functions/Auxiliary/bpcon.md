# Auxiliary.bpcon

## Signature

```lua
Auxiliary.bpcon(Effect e, int tp, Group eg, int ep, any ev, Effect re, any r, int rp) -> void
```

## Description

Returns true if the player can enter the Battle Phase, or if the current phase is already within the Battle Phase window.

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

- `Utilities/utility.lua:809`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **43** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Auxiliary.bpcon) with `Auxiliary.bpcon`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Fiendsmith Kyrie | `26434972` | [Scripts/c26434972.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c26434972.lua) | 1 |
| D/D Extra Surveyor | `74387963` | [Scripts/c74387963.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c74387963.lua) | 1 |
| Earthbound Servant Geo Gremlina | `33202303` | [Scripts/c33202303.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c33202303.lua) | 1 |
| Majestic Absorption | `63144961` | [Scripts/c63144961.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c63144961.lua) | 3 |
| Mementotlan Akihiron | `54207171` | [Scripts/c54207171.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c54207171.lua) | 1 |
| Lunalight Kaleido Chick | `35618217` | [Scripts/c35618217.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c35618217.lua) | 1 |
| Mementotlan Bone Party | `80722024` | [Scripts/c80722024.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c80722024.lua) | 1 |
| Marincess Bubble Ring | `19712214` | [Scripts/c19712214.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c19712214.lua) | 1 |
| Drill Warrior | `3429238` | [Scripts/c3429238.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c3429238.lua) | 1 |
| Parallel Port Armor | `879958` | [Scripts/c879958.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c879958.lua) | 1 |
| D/D/D Wave King Caesar | `3758046` | [Scripts/c3758046.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c3758046.lua) | 1 |
| Tainted of the Tistina | `50281477` | [Scripts/c50281477.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c50281477.lua) | 1 |
| Pitknight Filly | `25919316` | [Scripts/c25919316.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c25919316.lua) | 1 |
| Vanquish Soul Pantera | `66401502` | [Scripts/c66401502.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c66401502.lua) | 1 |
| Scareclaw Sclash | `79552283` | [Scripts/c79552283.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c79552283.lua) | 1 |
| Final Cross | `35756798` | [Scripts/c35756798.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c35756798.lua) | 1 |
| Rise to Full Height | `19254117` | [Scripts/c19254117.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c19254117.lua) | 1 |
| Tri-Brigade Stand-Off | `25908748` | [Scripts/c25908748.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c25908748.lua) | 1 |
| Galaxy-Eyes Antimatter Dragon | `92517928` | [Scripts/c92517928.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c92517928.lua) | 1 |
| Mathmech Nabla | `53577438` | [Scripts/c53577438.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c53577438.lua) | 1 |
| Principug | `11496832` | [Scripts/c11496832.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c11496832.lua) | 1 |
| Primal Dragon, the Primordial | `64025981` | [Scripts/c64025981.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c64025981.lua) | 1 |
| Performapal Uni | `7714344` | [Scripts/c7714344.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c7714344.lua) | 1 |
| Superheavy Samurai Stealth Ninja | `50065971` | [Scripts/c50065971.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c50065971.lua) | 1 |
| ...and 19 more |  |  |  |

## Script Examples

### Fiendsmith Kyrie (`26434972`)

Source: [Scripts/c26434972.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c26434972.lua)

```lua
	e1:SetType(EFFECT_TYPE_ACTIVATE)
	e1:SetCode(EVENT_FREE_CHAIN)
	e1:SetCondition(aux.bpcon)
	e1:SetTarget(s.target)
	e1:SetOperation(s.activate)
```

### D/D Extra Surveyor (`74387963`)

Source: [Scripts/c74387963.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c74387963.lua)

```lua
function s.dacon(e,tp,eg,ep,ev,re,r,rp)
	return eg:IsExists(s.sfilter,1,nil,tp) and not eg:IsContains(e:GetHandler())
		and aux.bpcon(e,tp,eg,ep,ev,re,r,rp) and Duel.IsTurnPlayer(tp)
end
function s.dafilter(c)
```

### Earthbound Servant Geo Gremlina (`33202303`)

Source: [Scripts/c33202303.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c33202303.lua)

```lua
	e2:SetCountLimit(1,id+o)
	e2:SetProperty(EFFECT_FLAG_CARD_TARGET)
	e2:SetCondition(aux.bpcon)
	e2:SetTarget(s.dirtg)
	e2:SetOperation(s.dirop)
```
