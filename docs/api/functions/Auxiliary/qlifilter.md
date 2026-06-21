# Auxiliary.qlifilter

## Signature

```lua
Auxiliary.qlifilter(Effect e, Effect te) -> void
```

## Description

Simplified method for the filter function for Qli Monster general immunity (unaffected by effects of monsters with lower original Level/Rank than this card's Level), used in effect registration for SetValue
te is the effect that would affect e:GetHandler()
function aux.qlifilter(e, te)
  if te:IsActiveType(TYPE_MONSTER) and te:IsActivated() then
    local lv=e:GetHandler():GetLevel()
    local ec=te:GetOwner()
    if ec:IsType(TYPE_LINK) then
      return false
    elseif ec:IsType(TYPE_XYZ) then
      return ec:GetOriginalRank()&lt;lv
    else
      return ec:GetOriginalLevel()&lt;lv
    end
  else
    return false
  end
end

## Parameters

- `e` `Effect`
- `te` `Effect`

## Source

- `Utilities/utility.lua:892`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **9** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Auxiliary.qlifilter`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [El Shaddoll Meshachrer](/examples/cards/32467459) | `32467459` | [Scripts/c32467459.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c32467459.lua) | 61 |
| Qliphort Disk | `64496451` | [Scripts/c64496451.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c64496451.lua) | 50 |
| Qliphort Stealth | `13073850` | [Scripts/c13073850.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c13073850.lua) | 38 |
| Apoqliphort Towers | `27279764` | [Scripts/c27279764.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c27279764.lua) | 38 |
| Apoqliphort Skybase | `40061558` | [Scripts/c40061558.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c40061558.lua) | 34 |
| Qliphort Cephalopod | `87588741` | [Scripts/c87588741.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c87588741.lua) | 32 |
| Qliphort Carrier | `91907707` | [Scripts/c91907707.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c91907707.lua) | 32 |
| Qliphort Helix | `37991342` | [Scripts/c37991342.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c37991342.lua) | 31 |
| Qliphort Shell | `90885155` | [Scripts/c90885155.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c90885155.lua) | 26 |

## Script Examples

### El Shaddoll Meshachrer (`32467459`)

Source: [Scripts/c32467459.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c32467459.lua)

```lua
		return true
	else
		return aux.qlifilter(e,te)
	end
end
```

### Qliphort Disk (`64496451`)

Source: [Scripts/c64496451.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c64496451.lua)

```lua
	e7:SetRange(LOCATION_MZONE)
	e7:SetCondition(c64496451.immcon)
	e7:SetValue(aux.qlifilter)
	c:RegisterEffect(e7)
	--summon success
```

### Qliphort Stealth (`13073850`)

Source: [Scripts/c13073850.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c13073850.lua)

```lua
	e7:SetRange(LOCATION_MZONE)
	e7:SetCondition(c13073850.immcon)
	e7:SetValue(aux.qlifilter)
	c:RegisterEffect(e7)
	--tohand
```
