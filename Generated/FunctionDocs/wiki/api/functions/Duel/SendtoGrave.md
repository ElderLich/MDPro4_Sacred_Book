# Duel.SendtoGrave

## Signature

```lua
Duel.SendtoGrave(Card|Group targets, int reason, [int reason_player]) -> int
```

## Description

Sends targets to the Graveyard for reason, optionally treating reason_player as the player that moved them, and returns the number actually moved.

## How To Use It

Use this for sending cards to the Graveyard by effect, cost, discard, or material handling.

```lua
if #g>0 then
    Duel.SendtoGrave(g,REASON_EFFECT)
end
```

This is not the same as destroying. A card sent to the Graveyard by `Duel.SendtoGrave` was not destroyed unless the reason and prior action also say it was destroyed.

## Related Functions

- [Card.IsAbleToGrave](/api/functions/Card/IsAbleToGrave)
- [Duel.SetOperationInfo](/api/functions/Duel/SetOperationInfo)
- [Duel.Destroy](/api/functions/Duel/Destroy)

## Parameters

- `targets` `Card|Group`
- `reason` `int`
- `reason_player` `int` optional

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4860`
