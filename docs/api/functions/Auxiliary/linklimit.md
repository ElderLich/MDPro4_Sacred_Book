# Auxiliary.linklimit

## Signature

```lua
Auxiliary.linklimit(Effect e, Effect se, any sp, any st) -> void
```

## Description

Simplified method for the filter function preventing summoning (broadly) by methods other than Link Summon, used in effect registration for SetValue
se is the effect used to summon the card, sp is the summoning player, st is the summon type
function aux.linklimit(e, se, sp, st)
  return st&SUMMON_TYPE_LINK==SUMMON_TYPE_LINK
end

## Parameters

- `e` `Effect`
- `se` `Effect`
- `sp` `any`
- `st` `any`

## Source

- `Utilities/procedure.lua:2309`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **8** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Auxiliary.linklimit`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Sky Striker Ace - Camellia | `63013339` | [Scripts/c63013339.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63013339.lua) | 48 |
| Scareclaw Tri-Heart | `59120809` | [Scripts/c59120809.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59120809.lua) | 48 |
| Sky Striker Ace - Azalea Temperance | `56741506` | [Scripts/c56741506.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c56741506.lua) | 47 |
| Prank-Kids Rip-Roarin-Roaster | `70875686` | [Scripts/c70875686.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c70875686.lua) | 47 |
| Sky Striker Ace - Zeke | `75147529` | [Scripts/c75147529.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c75147529.lua) | 46 |
| Five-Headed Link Dragon | `10669138` | [Scripts/c10669138.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c10669138.lua) | 45 |
| Sky Striker Ace - Azalea | `98462037` | [Scripts/c98462037.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c98462037.lua) | 39 |
| Surgical Striker - S.P.E.C.T.R.A. | `23530726` | [Scripts/c23530726.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c23530726.lua) | 37 |

## Script Examples

### Sky Striker Ace - Camellia (`63013339`)

Source: [Scripts/c63013339.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63013339.lua)

```lua
	e1:SetRange(LOCATION_EXTRA)
	e1:SetProperty(EFFECT_FLAG_SINGLE_RANGE+EFFECT_FLAG_CANNOT_DISABLE+EFFECT_FLAG_UNCOPYABLE)
	e1:SetValue(aux.linklimit)
	c:RegisterEffect(e1)
	--to grave
```

### Scareclaw Tri-Heart (`59120809`)

Source: [Scripts/c59120809.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59120809.lua)

```lua
	e1:SetProperty(EFFECT_FLAG_CANNOT_DISABLE+EFFECT_FLAG_UNCOPYABLE)
	e1:SetCode(EFFECT_SPSUMMON_CONDITION)
	e1:SetValue(aux.linklimit)
	c:RegisterEffect(e1)
	--position
```

### Sky Striker Ace - Azalea Temperance (`56741506`)

Source: [Scripts/c56741506.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c56741506.lua)

```lua
	e1:SetRange(LOCATION_EXTRA)
	e1:SetProperty(EFFECT_FLAG_SINGLE_RANGE+EFFECT_FLAG_CANNOT_DISABLE+EFFECT_FLAG_UNCOPYABLE)
	e1:SetValue(aux.linklimit)
	c:RegisterEffect(e1)
	--Equip
```
