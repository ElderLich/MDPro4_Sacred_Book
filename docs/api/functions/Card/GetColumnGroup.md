# Card.GetColumnGroup

## Signature

```lua
Card.GetColumnGroup(Card c, [int left], [int right]) -> Group
```

## Description

Return the group of cards in the same column as card c, excluding c, the last two parameters include all cards in the left columns and right columns from c
For example, if c is in the middle zone, c:GetColumnGroup(2,2) is equivalent to retrieving all cards on the field except the Field Spell

## Parameters

- `c` `Card`
- `left` `int` optional - default: 0
- `right` `int` optional - default: 0

## Returns

- `Group`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3427`
