# bit.replace

## Signature

```lua
bit.replace(int r, int v, int field, [int width]) -> int
```

## Description

Returns r with width bits starting at field replaced by the low width bits of v. width defaults to 1.

## Parameters

- `r` `int`
- `v` `int`
- `field` `int`
- `width` `int` optional

## Returns

- `int` - r with the selected bit field replaced.

## Source

- `Utilities/utility.lua:45`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **6** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `bit.replace`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Cynet Circuit | `82886276` | [Scripts/c82886276.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c82886276.lua) | 52 |
| Firewall eXceed Dragon | `21065189` | [Scripts/c21065189.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c21065189.lua) | 42 |
| Centerfrog | `47346782` | [Scripts/c47346782.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c47346782.lua) | 39 |
| Procession of the Tea Jar | `12612470` | [Scripts/c12612470.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c12612470.lua) | 36 |
| Knightmare Corruptor Iblee | `10158145` | [Scripts/c10158145.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c10158145.lua) | 35 |
| Yajiro Invader | `10852583` | [Scripts/c10852583.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c10852583.lua) | 30 |

## Script Examples

### Cynet Circuit (`82886276`)

Source: [Scripts/c82886276.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c82886276.lua)

```lua
function s.get_zone(c,seq)
	local zone=0
	if seq<4 and c:IsLinkMarker(LINK_MARKER_LEFT) then zone=bit.replace(zone,0x1,seq+1) end
	if seq>0 and seq<5 and c:IsLinkMarker(LINK_MARKER_RIGHT) then zone=bit.replace(zone,0x1,seq-1) end
	if seq==5 and c:IsLinkMarker(LINK_MARKER_TOP_LEFT) then zone=bit.replace(zone,0x1,2) end
```

### Firewall eXceed Dragon (`21065189`)

Source: [Scripts/c21065189.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c21065189.lua)

```lua
function c21065189.get_zone(c,seq)
	local zone=0
	if seq<4 and c:IsLinkMarker(LINK_MARKER_LEFT) then zone=bit.replace(zone,0x1,seq+1) end
	if seq>0 and seq<5 and c:IsLinkMarker(LINK_MARKER_RIGHT) then zone=bit.replace(zone,0x1,seq-1) end
	if seq==5 and c:IsLinkMarker(LINK_MARKER_TOP_LEFT) then zone=bit.replace(zone,0x1,2) end
```

### Centerfrog (`47346782`)

Source: [Scripts/c47346782.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c47346782.lua)

```lua
		or (seq<4 and Duel.CheckLocation(1-tp,LOCATION_MZONE,seq+1)) then
		local zone=0
		if seq>0 and Duel.CheckLocation(1-tp,LOCATION_MZONE,seq-1) then zone=bit.replace(zone,0x1,seq-1) end
		if seq<4 and Duel.CheckLocation(1-tp,LOCATION_MZONE,seq+1) then zone=bit.replace(zone,0x1,seq+1) end
		if Duel.GetControl(c,1-tp,0,0,zone)==0 then return end
```
