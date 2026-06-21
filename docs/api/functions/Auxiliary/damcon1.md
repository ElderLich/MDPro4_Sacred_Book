# Auxiliary.damcon1

## Signature

```lua
Auxiliary.damcon1(Effect e, int tp, Group eg, int ep, any ev, Effect re, any r, int rp) -> void
```

## Description

Simplified method for the condition of player tp taking damage, used in effect registration for SetCondition
function aux.damcon1(e, tp, eg, ep, ev, re, r, rp)
  local e1=Duel.IsPlayerAffectedByEffect(tp, EFFECT_REVERSE_DAMAGE)
  local e2=Duel.IsPlayerAffectedByEffect(tp, EFFECT_REVERSE_RECOVER)
  local rd=e1 and not e2
  local rr=not e1 and e2
  local ex,cg,ct,cp,cv=Duel.GetOperationInfo(ev, CATEGORY_DAMAGE)
  if ex and (cp==tp or cp==PLAYER_ALL) and not rd and not Duel.IsPlayerAffectedByEffect(tp, EFFECT_NO_EFFECT_DAMAGE) then
    return true
  end
  ex,cg,ct,cp,cv=Duel.GetOperationInfo(ev, CATEGORY_RECOVER)
  return ex and (cp==tp or cp==PLAYER_ALL) and rr and not Duel.IsPlayerAffectedByEffect(tp, EFFECT_NO_EFFECT_DAMAGE)
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

- `Utilities/utility.lua:879`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **21** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Auxiliary.damcon1`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Destiny HERO - Decider | `64184058` | [Scripts/c64184058.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c64184058.lua) | 40 |
| D/D Savant Newton | `19302550` | [Scripts/c19302550.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c19302550.lua) | 39 |
| Gouki Octostretch | `85008676` | [Scripts/c85008676.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c85008676.lua) | 38 |
| Performage Damage Juggler | `68819554` | [Scripts/c68819554.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c68819554.lua) | 37 |
| D/D Savant Copernicus | `46796664` | [Scripts/c46796664.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c46796664.lua) | 36 |
| Performapal Rain Goat | `16617334` | [Scripts/c16617334.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c16617334.lua) | 36 |
| Clear Kuriboh | `46613515` | [Scripts/c46613515.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c46613515.lua) | 35 |
| Dream Shark | `6180710` | [Scripts/c6180710.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c6180710.lua) | 32 |
| Performage Flame Eater | `4807253` | [Scripts/c4807253.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c4807253.lua) | 32 |
| Donyoribo @Ignister | `14146794` | [Scripts/c14146794.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c14146794.lua) | 31 |
| Performage Stilts Launcher | `4081665` | [Scripts/c4081665.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c4081665.lua) | 31 |
| Sargasso Lighthouse | `37511832` | [Scripts/c37511832.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c37511832.lua) | 31 |
| Performage Hat Tricker | `31292357` | [Scripts/c31292357.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c31292357.lua) | 30 |
| Curse Reflection Doll | `33391067` | [Scripts/c33391067.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c33391067.lua) | 26 |
| Link Restart | `27664101` | [Scripts/c27664101.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c27664101.lua) | 24 |
| Crimson Fire | `24566654` | [Scripts/c24566654.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24566654.lua) | 23 |
| Junkuriboh | `38491199` | [Scripts/c38491199.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c38491199.lua) | 20 |
| Ring of Defense | `58641905` | [Scripts/c58641905.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c58641905.lua) | 19 |
| Achacha Chanbara | `62476197` | [Scripts/c62476197.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c62476197.lua) | 18 |
| Energy-Absorbing Monolith | `57006589` | [Scripts/c57006589.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c57006589.lua) | 18 |
| Spell of Pain | `76714458` | [Scripts/c76714458.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c76714458.lua) | 18 |

## Script Examples

### Destiny HERO - Decider (`64184058`)

Source: [Scripts/c64184058.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c64184058.lua)

```lua
	e4:SetRange(LOCATION_GRAVE)
	e4:SetCountLimit(1,64184059+EFFECT_COUNT_CODE_DUEL)
	e4:SetCondition(aux.damcon1)
	e4:SetTarget(c64184058.damtg)
	e4:SetOperation(c64184058.damop)
```

### D/D Savant Newton (`19302550`)

Source: [Scripts/c19302550.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c19302550.lua)

```lua
function c19302550.discon(e,tp,eg,ep,ev,re,r,rp)
	return Duel.IsChainDisablable(ev) and not Duel.IsChainDisabled(ev)
		and re:IsActiveType(TYPE_TRAP) and aux.damcon1(e,tp,eg,ep,ev,re,r,rp) and e:GetHandler():GetFlagEffect(19302550)==0
end
function c19302550.disop(e,tp,eg,ep,ev,re,r,rp)
```

### Gouki Octostretch (`85008676`)

Source: [Scripts/c85008676.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c85008676.lua)

```lua
end
function c85008676.damcon2(e,tp,eg,ep,ev,re,r,rp)
	return ep~=tp and aux.damcon1(e,tp,eg,ep,ev,re,r,rp)
end
function c85008676.damop2(e,tp,eg,ep,ev,re,r,rp)
```
