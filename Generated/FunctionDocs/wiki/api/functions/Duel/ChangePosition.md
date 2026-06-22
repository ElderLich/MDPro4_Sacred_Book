# Duel.ChangePosition

## Signature

```lua
Duel.ChangePosition(Card|Group targets, int au, [int ad], [int du], [int dd], [bool noflip]) -> int
```

## Description

Changes the battle position of targets and returns the number of cards whose position actually changed.
The position arguments map by current position: au for face-up Attack Position, ad for face-down Attack Position, du for face-up Defense Position, and dd for face-down Defense Position. Omitted values use au.

## How To Use It

Use this when an effect changes battle position during resolution.

The short form changes every target to the same position:

```lua
if tc:IsRelateToEffect(e) then
    Duel.ChangePosition(tc,POS_FACEUP_DEFENSE)
end
```

For mixed current positions, pass the destination for face-up Attack, face-down Attack, face-up Defense, and face-down Defense in that order. MDPro3's core does not read the old seventh `setavailable` argument.

## Related Functions

- [Card.IsCanChangePosition](/api/functions/Card/IsCanChangePosition)
- [Card.IsPosition](/api/functions/Card/IsPosition)

## Parameters

- `targets` `Card|Group`
- `au` `int`
- `ad` `int` optional - default: au
- `du` `int` optional - default: au
- `dd` `int` optional - default: au
- `noflip` `bool` optional - default: false

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4880`
