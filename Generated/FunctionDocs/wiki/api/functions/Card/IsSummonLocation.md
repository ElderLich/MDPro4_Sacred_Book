# Card.IsSummonLocation

## Signature

```lua
Card.IsSummonLocation(Card c, int loc) -> bool
```

## Description

Checks whether c's recorded Summon location contains loc. This reads the Summon information, not c's current location.

## Parameters

- `c` `Card` - Card whose recorded Summon location is checked.
- `loc` `int` - Location mask to test against the stored Summon location, such as LOCATION_EXTRA or LOCATION_GRAVE.

## Returns

- `bool` - True if any bit in loc is present in c's recorded Summon location.

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3557`
