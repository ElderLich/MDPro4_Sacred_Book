# Card.CheckRemoveOverlayCard

## Signature

```lua
Card.CheckRemoveOverlayCard(Card c, int player, int count, int reason) -> bool
```

## Description

Checks whether player can remove at least count Xyz Materials from c for reason.
Replacement effects with EFFECT_OVERLAY_REMOVE_REPLACE can make this return true even when c itself has too few materials.

## Parameters

- `c` `Card`
- `player` `int`
- `count` `int`
- `reason` `int`

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3527`
