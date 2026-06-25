# Duel.SendtoGrave

## Signature

```lua
Duel.SendtoGrave(Card|Group targets, int reason, [int reason_player]) -> int
```

## Description

Sends targets to the GY for reason, optionally treating reason_player as the player that moved them, and returns the number actually moved.
This is not destruction by itself. Use Duel.Destroy for destroy effects, or include the correct discard/material/release reason flags when the card text or mechanic requires them.

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

- `targets` `Card|Group` - Card or Group to send to the Graveyard.
- `reason` `int` - REASON_* flags recorded for the move.
- `reason_player` `int` optional - Player recorded as the reason player; defaults to the core's current reason player.

## Returns

- `int` - Number of cards actually sent to the Graveyard.

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4860`
