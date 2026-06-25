# Duel.SendtoHand

## Signature

```lua
Duel.SendtoHand(Card|Group targets, [int|nil player], int reason, [int reason_player]) -> int
```

## Description

Sends targets to a hand for reason and returns the number of cards actually moved.
Pass nil for player to use the normal return destination. Pass a specific player only when the effect says the cards go to that player's hand.
When a hidden card is added and must be shown, confirm the moved card after this call succeeds.

## How To Use It

Use this for adding or returning cards to the hand.

Pass nil for `player` when the card should go to its normal return destination. Pass a specific player only when the effect explicitly sends the card to that player's hand.

```lua
if Duel.SendtoHand(sg,nil,REASON_EFFECT)>0 then
    Duel.ConfirmCards(1-tp,sg)
end
```

When the card came from a hidden location and must be shown, reveal the result with `Duel.ConfirmCards` after it reaches the hand.

## Related Functions

- [Card.IsAbleToHand](/api/functions/Card/IsAbleToHand)
- [Duel.SetOperationInfo](/api/functions/Duel/SetOperationInfo)

## Parameters

- `targets` `Card|Group`
- `player` `int|nil` optional
- `reason` `int`
- `reason_player` `int` optional

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4861`
