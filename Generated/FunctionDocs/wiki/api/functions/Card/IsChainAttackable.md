# Card.IsChainAttackable

## Signature

```lua
Card.IsChainAttackable(Card c, [int ac], [bool monsteronly]) -> bool
```

## Description

Check whether c can be a continuous attack, c the number of attacks declared&gt; = ac return false
Note: This function returns false when c has made multiple attacks due to effects such as flashing swords

## Parameters

- `c` `Card`
- `ac` `int` optional
- `monsteronly` `bool` optional

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3599`
