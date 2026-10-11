# Auxiliary.NecroValleyNegateCheck

## Signature

```lua
Auxiliary.NecroValleyNegateCheck(Card|Group v) -> bool
```

## Description

Checks whether v, a Card or Group, contains a card affected by Necrovalley. If the current Chain is disablable and a matching card is found, it negates the current effect and returns true.

## Parameters

- `v` `Card|Group`

## Returns

- `bool` - true if the current effect was negated by the Necrovalley check.

## Source

- `Utilities/utility.lua:929`
