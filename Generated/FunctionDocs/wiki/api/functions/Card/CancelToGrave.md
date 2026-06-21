# Card.CancelToGrave

## Signature

```lua
Card.CancelToGrave(Card c, [bool cancel]) -> void
```

## Description

Cancel to send to determine the state tomb, cancel = false to reset the tomb to determine the state
Note: to send the tomb to determine the state refers to the field to start without leaving field magic and traps, the state of these cards
Cards sent to the tomb determine the state can not return cards and cards, and sent to the cemetery at the end of the chain
The purpose of this function is to cancel this state to stay in the field, for the light of the sword and seal the Scarlet Scarlet card

## Parameters

- `c` `Card`
- `cancel` `bool` optional - default: true

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3651`
