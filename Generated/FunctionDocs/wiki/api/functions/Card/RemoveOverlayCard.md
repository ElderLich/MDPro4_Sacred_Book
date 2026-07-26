# Card.RemoveOverlayCard

## Signature

```lua
Card.RemoveOverlayCard(Card c, int player, int min, int max, int reason) -> int
```

## Description

Lets player remove between min and max Xyz Materials from c for reason and returns the number actually removed.
The core also offers applicable EFFECT_OVERLAY_REMOVE_REPLACE effects before selecting materials.

## Parameters

- `c` `Card`
- `player` `int`
- `min` `int`
- `max` `int`
- `reason` `int`

## Returns

- `int` - Number of Xyz Materials actually removed.

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3531`
