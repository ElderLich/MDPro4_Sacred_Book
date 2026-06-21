# Card.CancelToGrave

## Signature

```lua
Card.CancelToGrave(Card c, [bool cancel]) -> void
```

## Description

Cancels the confirmed-to-Graveyard state for c. If cancel is false, sets that state again.
This state is used for non-continuous Spell/Trap Cards activated on the field before they leave the field; while set, they cannot return to the hand or Deck and are sent to the Graveyard when the Chain ends.
Use this helper to keep such cards on the field, as with Swords of Revealing Light or Scrap-Iron Scarecrow.

## Parameters

- `c` `Card`
- `cancel` `bool` optional - default: true

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3651`
