# Duel.MoveToField

## Signature

```lua
Duel.MoveToField(Card c, int move_player, int target_player, int dest, int positions, bool enable, [int zone]) -> bool
```

## Description

Moves c onto target_player's field and returns true if the move succeeds.
dest is normally LOCATION_MZONE or LOCATION_SZONE. LOCATION_FZONE and LOCATION_PZONE are accepted and converted to the matching Spell & Trap Zone handling by the core.
For LOCATION_PZONE, the core requires a Pendulum Card, lets the player choose an open Pendulum Zone, and sends the card to the GY by rule if no matching Pendulum Zone is usable.

## How To Use It

Use this for effects that place an existing card directly onto the field, such as moving a card to the Field Zone, Pendulum Zone, or Spell & Trap Zone.

```lua
if tc:IsRelateToEffect(e) then
    Duel.MoveToField(tc,tp,tp,LOCATION_SZONE,POS_FACEUP,true)
end
```

`enable=true` applies the moved card's field effects immediately. The optional `zone` mask restricts which zone can be used.

## Related Functions

- [Duel.GetLocationCount](/api/functions/Duel/GetLocationCount)
- [Duel.GetSZoneCount](/api/functions/Duel/GetSZoneCount)
- [Duel.ReturnToField](/api/functions/Duel/ReturnToField)

## Parameters

- `c` `Card` - Card to move.
- `move_player` `int` - Player making the placement selection.
- `target_player` `int` - Player whose field receives the card.
- `dest` `int` - Destination location. LOCATION_PZONE is accepted for Pendulum Zone placement.
- `positions` `int` - Allowed position mask, commonly POS_FACEUP for Pendulum Zone placement.
- `enable` `bool` - Whether to enable the card's field effects after it moves. Local Pendulum placement scripts commonly pass true.
- `zone` `int` optional - Optional zone mask. For LOCATION_PZONE, low bit 0 allows the left Pendulum Zone and low bit 1 allows the right Pendulum Zone; omitted defaults to both.

## Returns

- `bool` - true if the move succeeds; false if the move is invalid or no usable zone is available.

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4882`
