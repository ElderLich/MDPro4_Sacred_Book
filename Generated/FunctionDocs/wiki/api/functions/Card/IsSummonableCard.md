# Card.IsSummonableCard

## Signature

```lua
Card.IsSummonableCard(Card c) -> bool
```

## Description

Checks whether c's card data represents a monster that is allowed to be Normal Summoned or Set by card kind.
This rejects non-monsters, Extra Deck monsters, Ritual Monsters, Special Summon-only monsters, and Tokens. It does not check current costs, Summon count, locations, or player restrictions.

## Parameters

- `c` `Card`

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3575`
