# Duel.GetLocationCount

## Signature

```lua
Duel.GetLocationCount(int player, int location, [int use_player], [int reason], [int zone]) -> int,int
```

## Description

Returns how many zones of location are available on player's field and the corresponding usable zone mask.
location is normally LOCATION_MZONE or LOCATION_SZONE. use_player, reason, and zone are used by effects that restrict where cards can be placed, such as Kaiser Colosseum-style restrictions.
The count can be negative, so scripts that free a zone as a cost sometimes check ft &gt; -1 instead of ft &gt; 0.

## Parameters

- `player` `int` - Player whose field is checked.
- `location` `int` - Location to count, normally LOCATION_MZONE or LOCATION_SZONE.
- `use_player` `int` optional - Player treated as placing the card. Defaults to the current reason player.
- `reason` `int` optional - Placement reason such as LOCATION_REASON_TOFIELD or LOCATION_REASON_CONTROL. Defaults to LOCATION_REASON_TOFIELD.
- `zone` `int` optional - Zone mask to restrict the count. Defaults to 0xff.

## Returns

- `int` - Available zone count. The core comment notes this can be negative.
- `int` - Usable zone mask.

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4935`
