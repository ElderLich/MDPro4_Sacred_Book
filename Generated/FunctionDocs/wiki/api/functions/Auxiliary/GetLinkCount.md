# Auxiliary.GetLinkCount

## Signature

```lua
Auxiliary.GetLinkCount(Card c) -> int
```

## Description

Returns the encoded material value used by Link procedure sum checks.
Ordinary materials and Link-1 monsters count as 1. A Link Monster with Link Rating greater than 1 encodes the choice to count as either 1 or its Link Rating for Group.CheckWithSumEqual.

## Parameters

- `c` `Card` - Candidate Link Material.

## Returns

- `int` - 1, or an encoded 1-or-Link-Rating value for Link Monsters with Link Rating greater than 1.

## Source

- `Utilities/procedure.lua:2158`
