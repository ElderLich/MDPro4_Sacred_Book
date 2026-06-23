# Auxiliary.CheckUnionEquip

## Signature

```lua
Auxiliary.CheckUnionEquip(Card uc, Card tc, [int exclude_modern_count]) -> bool
```

## Description

Checks whether Union Monster uc can be equipped to target tc under the local modern/old Union count rules.
Use exclude_modern_count when a replacement-style effect will remove an already equipped modern Union before equipping another one.

## Parameters

- `uc` `Card` - Union Monster that would become equipped.
- `tc` `Card` - Monster that would receive the Union card.
- `exclude_modern_count` `int` optional - Modern Union count to ignore while checking the target, commonly 1 when replacing the currently equipped Union.

## Returns

- `bool` - true if the target can receive this Union card under the count compatibility rule.

## Source

- `Utilities/utility.lua:335`
