# Duel.GetLocationCount

## Signature

```lua
Duel.GetLocationCount(int player, int location, [int use_player], [int reason], [int zone]) -> int
```

## Description

Returns the number of spaces available in the player's field
Location can only be LOCATION_MZONE or LOCATION_SZONE
Reason is LOCATION_REASON_TOFIELD or LOCATION_REASON_CONTROL

## Parameters

- `player` `int`
- `location` `int`
- `use_player` `int` optional
- `reason` `int` optional
- `zone` `int` optional - default: 0xff

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4935`
