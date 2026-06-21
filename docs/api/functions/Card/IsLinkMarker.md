# Card.IsLinkMarker

## Signature

```lua
Card.IsLinkMarker(Card c, int dir) -> bool
```

## Description

Check if card c has a Link Marker in direction dir
dir values are:
LINK_MARKER_BOTTOM_LEFT =0x001 -- ↙
LINK_MARKER_BOTTOM      =0x002 -- ↓
LINK_MARKER_BOTTOM_RIGHT=0x004 -- ↘
LINK_MARKER_LEFT        =0x008 -- ←
LINK_MARKER_RIGHT       =0x020 -- →
LINK_MARKER_TOP_LEFT    =0x040 -- ↖
LINK_MARKER_TOP         =0x080 -- ↑
LINK_MARKER_TOP_RIGHT   =0x100 -- ↗

## Parameters

- `c` `Card`
- `dir` `int`

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3418`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **3** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.IsLinkMarker`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Cynet Circuit | `82886276` | [Scripts/c82886276.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c82886276.lua) | 52 |
| Firewall eXceed Dragon | `21065189` | [Scripts/c21065189.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c21065189.lua) | 42 |
| Knightmare Corruptor Iblee | `10158145` | [Scripts/c10158145.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c10158145.lua) | 35 |

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

### Knightmare Corruptor Iblee (`10158145`)

Source: [Scripts/c10158145.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c10158145.lua)

```lua
function c10158145.get_zone(c,seq)
	local zone=0
	if seq<4 and c:IsLinkMarker(LINK_MARKER_LEFT) then zone=bit.replace(zone,0x1,seq+1) end
	if seq>0 and seq<5 and c:IsLinkMarker(LINK_MARKER_RIGHT) then zone=bit.replace(zone,0x1,seq-1) end
	return zone
```
