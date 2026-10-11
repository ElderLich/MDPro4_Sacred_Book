# Auxiliary.qlifilter

## Signature

```lua
Auxiliary.qlifilter(Effect e, Effect te) -> bool
```

## Description

Qli immunity value helper.
It accepts activated monster effects from monsters whose original Level or Rank is lower than the handler's current Level, and rejects Link Monsters.

## Parameters

- `e` `Effect`
- `te` `Effect`

## Returns

- `bool`

## Source

- `Utilities/utility.lua:895`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **9** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Auxiliary.qlifilter) with `Auxiliary.qlifilter`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| El Shaddoll Meshachrer | `32467459` | [Scripts/c32467459.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c32467459.lua) | 1 |
| Qliphort Disk | `64496451` | [Scripts/c64496451.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c64496451.lua) | 1 |
| Qliphort Stealth | `13073850` | [Scripts/c13073850.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c13073850.lua) | 1 |
| Apoqliphort Towers | `27279764` | [Scripts/c27279764.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c27279764.lua) | 1 |
| Apoqliphort Skybase | `40061558` | [Scripts/c40061558.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c40061558.lua) | 1 |
| Qliphort Cephalopod | `87588741` | [Scripts/c87588741.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c87588741.lua) | 1 |
| Qliphort Carrier | `91907707` | [Scripts/c91907707.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c91907707.lua) | 1 |
| Qliphort Helix | `37991342` | [Scripts/c37991342.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c37991342.lua) | 1 |
| Qliphort Shell | `90885155` | [Scripts/c90885155.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c90885155.lua) | 1 |

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
