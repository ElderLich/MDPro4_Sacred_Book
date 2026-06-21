# Duel.DisableShuffleCheck

## Signature

```lua
Duel.DisableShuffleCheck([bool disable]) -> void
```

## Description

So that the next operation does not check for the need for a wash card set or a hand card
Note: If you do not call this function,
In addition to calling Duel.DiscardDeck and Duel.Draw remove the card from the card group or add the card to the card
Or the card is added to the deck (not the top or bottom), the system automatically cleans the card group or the hand card at the end of the effect process
If you do not want to do so, for example, from the top of the card group, except for a card and other operations, you need to call this function
This function only ensures that no subsequent scrub detection is performed in the next operation

## Parameters

- `disable` `bool` optional - default: true

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4912`
