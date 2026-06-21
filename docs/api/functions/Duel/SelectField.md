# Duel.SelectField

## Signature

```lua
Duel.SelectField(int player, int count, int loc1, int loc2, int zone, [int code]) -> int
```

## Description

Have player select zones; flag1 is the low bit, flag2 is the high bit, together forming the selectable zones; count is the number of zones to choose
Return the selected zones

## Parameters

- `player` `int`
- `count` `int`
- `loc1` `int`
- `loc2` `int`
- `zone` `int`
- `code` `int` optional

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5027`
