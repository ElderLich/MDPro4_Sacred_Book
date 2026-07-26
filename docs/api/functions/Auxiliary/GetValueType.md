# Auxiliary.GetValueType

## Signature

```lua
Auxiliary.GetValueType(any v) -> string
```

## Description

Returns Lua's type string for ordinary values, or Card, Group, or Effect for those userdata objects.

## Parameters

- `v` `any`

## Returns

- `string`

## Source

- `Utilities/utility.lua:472`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **4** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Auxiliary.GetValueType`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Lunalight Masquerade | `2344618` | [Scripts/c2344618.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c2344618.lua) | 1 |
| Amazoness Secret Arts | `86758746` | [Scripts/c86758746.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c86758746.lua) | 1 |
| Cyberdark Chimera | `5370235` | [Scripts/c5370235.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c5370235.lua) | 1 |
| Curse of Dragon, the Magical Knight Dragon | `72064891` | [Scripts/c72064891.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c72064891.lua) | 1 |

## Script Examples

### Lunalight Masquerade (`2344618`)

Source: [Scripts/c2344618.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c2344618.lua)

```lua
		_SendtoGrave=Duel.SendtoGrave
		function Duel.SendtoGrave(tg,reason)
			if reason~=REASON_EFFECT+REASON_MATERIAL+REASON_FUSION or aux.GetValueType(tg)~="Group" then
				return _SendtoGrave(tg,reason)
			end
```

### Amazoness Secret Arts (`86758746`)

Source: [Scripts/c86758746.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c86758746.lua)

```lua
		_SendtoGrave=Duel.SendtoGrave
		function Duel.SendtoGrave(tg,reason)
			if reason~=REASON_EFFECT+REASON_MATERIAL+REASON_FUSION or aux.GetValueType(tg)~="Group" then
				return _SendtoGrave(tg,reason)
			end
```

### Cyberdark Chimera (`5370235`)

Source: [Scripts/c5370235.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c5370235.lua)

```lua
		_SendtoGrave=Duel.SendtoGrave
		function Duel.SendtoGrave(tg,reason)
			if reason~=REASON_EFFECT+REASON_MATERIAL+REASON_FUSION or aux.GetValueType(tg)~="Group" then
				return _SendtoGrave(tg,reason)
			end
```
