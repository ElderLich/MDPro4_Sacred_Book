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
