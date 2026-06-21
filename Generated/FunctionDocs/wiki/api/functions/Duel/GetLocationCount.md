# Duel.GetLocationCount

## Signature

```lua
Duel.GetLocationCount(int player, int location, [int use_player], [int reason], [int zone]) -> int,int
```

## Description

Returns how many zones of location are available on player's field and the corresponding usable zone mask.
location is normally LOCATION_MZONE or LOCATION_SZONE. use_player, reason, and zone are used by effects that restrict where cards can be placed, such as Kaiser Colosseum-style restrictions.

## Parameters

- `player` `int`
- `location` `int`
- `use_player` `int` optional
- `reason` `int` optional
- `zone` `int` optional

## Returns

- `int`
- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4935`
