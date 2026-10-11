# Auxiliary.DrytronSpSummonType

## Signature

```lua
Auxiliary.DrytronSpSummonType(Card c) -> bool
```

## Description

Returns whether c is a Special Summon procedure monster, used by Drytron Special Summon helpers.

## Parameters

- `c` `Card`

## Returns

- `bool`

## Source

- `Utilities/utility.lua:1082`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **3** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Auxiliary.DrytronSpSummonType) with `Auxiliary.DrytronSpSummonType`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Drytron Meteonis Quadrantids | `95209656` | [Scripts/c95209656.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c95209656.lua) | 3 |
| Drytron Nova | `94187078` | [Scripts/c94187078.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c94187078.lua) | 3 |
| Drytron Gamma Eltanin | `60037599` | [Scripts/c60037599.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c60037599.lua) | 3 |

## Script Examples

### Drytron Meteonis Quadrantids (`95209656`)

Source: [Scripts/c95209656.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c95209656.lua)

```lua
function c95209656.spfilter(c,e,tp)
	return c:IsSetCard(0x154) and c:IsAttackAbove(1) and not c:IsCode(95209656)
		and c:IsCanBeSpecialSummoned(e,0,tp,false,aux.DrytronSpSummonType(c))
end
function c95209656.fselect(g)
```

### Drytron Nova (`94187078`)

Source: [Scripts/c94187078.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c94187078.lua)

```lua
end
function c94187078.filter(c,e,tp)
	return c:IsSetCard(0x154) and c:IsCanBeSpecialSummoned(e,0,tp,false,aux.DrytronSpSummonType(c))
end
function c94187078.target(e,tp,eg,ep,ev,re,r,rp,chk)
```

### Drytron Gamma Eltanin (`60037599`)

Source: [Scripts/c60037599.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c60037599.lua)

```lua
end
function c60037599.rbfilter(c,e,tp)
	return c:IsSetCard(0x154) and c:IsAttack(2000) and not c:IsCode(60037599) and c:IsCanBeSpecialSummoned(e,0,tp,false,aux.DrytronSpSummonType(c))
end
function c60037599.extraop(e,tp)
```
