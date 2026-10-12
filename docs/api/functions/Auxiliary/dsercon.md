# Auxiliary.dsercon

## Signature

```lua
Auxiliary.dsercon(Effect e, int tp, Group eg, int ep, any ev, Effect re, any r, int rp) -> void
```

## Description

Condition for EVENT_DAMAGE_STEP_END effects; true if the handler is still related to battle or was battle destroyed.

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

- `Utilities/utility.lua:789`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **34** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Auxiliary.dsercon) with `Auxiliary.dsercon`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Geira Guile the Cubic King | `40392714` | [Scripts/c40392714.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c40392714.lua) | 1 |
| Blue-Eyes Tyrant Dragon | `11443677` | [Scripts/c11443677.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c11443677.lua) | 1 |
| Timelord Progenitor Vorpgate | `67508932` | [Scripts/c67508932.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c67508932.lua) | 1 |
| Brave-Eyes Pendulum Dragon | `88305705` | [Scripts/c88305705.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c88305705.lua) | 1 |
| Tilting Entrainment | `77855162` | [Scripts/c77855162.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c77855162.lua) | 1 |
| Neos Wiseman | `5126490` | [Scripts/c5126490.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c5126490.lua) | 1 |
| Yubel - The Loving Defender Forever | `47172959` | [Scripts/c47172959.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c47172959.lua) | 1 |
| Ancient Gear Reactor Dragon | `44874522` | [Scripts/c44874522.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c44874522.lua) | 1 |
| Hyper Psychic Blaster/Assault Mode | `37169670` | [Scripts/c37169670.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c37169670.lua) | 1 |
| Perfectron Hydradrive Dragon | `13203964` | [Scripts/c13203964.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c13203964.lua) | 1 |
| Ancient Gear Hydra | `81269231` | [Scripts/c81269231.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c81269231.lua) | 1 |
| Elemental HERO Neo Bubbleman | `5285665` | [Scripts/c5285665.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c5285665.lua) | 1 |
| Ancient Gear Engineer | `1953925` | [Scripts/c1953925.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c1953925.lua) | 1 |
| Dragonecro Nethersoul Dragon | `8198620` | [Scripts/c8198620.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c8198620.lua) | 1 |
| Blackwing Armor Master | `69031175` | [Scripts/c69031175.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c69031175.lua) | 1 |
| The Six Samurai - Zanji | `95519486` | [Scripts/c95519486.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c95519486.lua) | 1 |
| Lunalight Leo Dancer | `24550676` | [Scripts/c24550676.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c24550676.lua) | 1 |
| Chimera the Illusion Beast | `38264974` | [Scripts/c38264974.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c38264974.lua) | 1 |
| Worm Solid | `3204467` | [Scripts/c3204467.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c3204467.lua) | 1 |
| Blue-Eyes Twin Burst Dragon | `2129638` | [Scripts/c2129638.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c2129638.lua) | 1 |
| Hyper Psychic Blaster | `95526884` | [Scripts/c95526884.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c95526884.lua) | 1 |
| Number F0: Utopic Future | `65305468` | [Scripts/c65305468.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c65305468.lua) | 1 |
| Yubel - The Ultimate Nightmare | `31764700` | [Scripts/c31764700.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c31764700.lua) | 1 |
| Nightmare Magician | `40221691` | [Scripts/c40221691.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c40221691.lua) | 1 |
| ...and 10 more |  |  |  |

## Script Examples

### Geira Guile the Cubic King (`40392714`)

Source: [Scripts/c40392714.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c40392714.lua)

```lua
	e4:SetCode(EVENT_DAMAGE_STEP_END)
	e4:SetProperty(EFFECT_FLAG_CARD_TARGET)
	e4:SetCondition(aux.dsercon)
	e4:SetTarget(c40392714.sptg2)
	e4:SetOperation(c40392714.spop2)
```

### Blue-Eyes Tyrant Dragon (`11443677`)

Source: [Scripts/c11443677.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c11443677.lua)

```lua
end
function c11443677.setcon(e,tp,eg,ep,ev,re,r,rp)
	return e:GetHandler():GetFlagEffect(11443677)==0 and aux.dsercon(e,tp,eg,ep,ev,re,r,rp)
end
function c11443677.setfilter(c)
```

### Timelord Progenitor Vorpgate (`67508932`)

Source: [Scripts/c67508932.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c67508932.lua)

```lua
function c67508932.rmcond(e,tp,eg,ep,ev,re,r,rp)
	local c=e:GetHandler()
	return aux.dsercon(e,tp,eg,ep,ev,re,r,rp) and c:IsSummonLocation(LOCATION_EXTRA) and c:GetBattledGroupCount()>0
end
function c67508932.rmtg(e,tp,eg,ep,ev,re,r,rp,chk)
```
