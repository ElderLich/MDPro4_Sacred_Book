# Card.IsChainAttackable

## Signature

```lua
Card.IsChainAttackable(Card c, [int ac], [bool monsteronly]) -> bool
```

## Description

Checks whether the current attacker can make another attack under chain-attack rules.
This core binding validates c but tests the duel's current attacker. ac defaults to 2, and monsteronly requires an attack target instead of allowing a direct attack.

## Parameters

- `c` `Card`
- `ac` `int` optional - default: 2
- `monsteronly` `bool` optional - default: false

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3599`
