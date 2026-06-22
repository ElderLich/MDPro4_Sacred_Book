# Duel.Overlay

## Signature

```lua
Duel.Overlay(Card c, Card|Group ocard, [bool adjust]) -> void
```

## Description

Overlays ocard under c as Xyz Material.
By default the field is adjusted after the overlay. Pass adjust=false only when a larger procedure will adjust afterward.

## How To Use It

Use this when a procedure or effect turns cards into Xyz Materials under an Xyz Monster.

The first argument is the Xyz Monster that will receive the materials. The second argument can be one Card or a Group:

```lua
Duel.Overlay(xyzc,mg)
```

Leave `adjust` omitted for normal scripts. Pass `false` only inside a larger procedure that will adjust the field afterward.

## Related Functions

- [Duel.GetOverlayGroup](/api/functions/Duel/GetOverlayGroup)
- [Duel.RemoveOverlayCard](/api/functions/Duel/RemoveOverlayCard)
- [Card.GetOverlayGroup](/api/functions/Card/GetOverlayGroup)

## Parameters

- `c` `Card`
- `ocard` `Card|Group`
- `adjust` `bool` optional - default: true

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5014`
