# Duel.MoveToField

## Signature

```lua
Duel.MoveToField(Card c, int move_player, int target_player, int dest, int pos, bool enable, [int zone]) -> bool
```

## Description

Moves c onto target_player's field and returns true if the move succeeds.
dest is normally LOCATION_MZONE or LOCATION_SZONE. LOCATION_FZONE and LOCATION_PZONE are accepted and converted to the matching Spell & Trap Zone handling by the core.

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

- `c` `Card`
- `move_player` `int`
- `target_player` `int`
- `dest` `int`
- `pos` `int`
- `enable` `bool`
- `zone` `int` optional

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4882`
