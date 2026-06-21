# Duel.CheckTribute

## Signature

```lua
Duel.CheckTribute(Card c, int min, [int|nil max], [Group|nil mg], [int|nil toplayer], [int|nil zone]) -> Group
```

## Description

Check if there are min \[to max\] Tributes on the field \[or in mg\] for Normal Summoning c \[to toplayer's field in zone\]

## Parameters

- `c` `Card`
- `min` `int`
- `max` `int|nil` optional - default: min
- `mg` `Group|nil` optional
- `toplayer` `int|nil` optional - default: c:GetControler()
- `zone` `int|nil` optional - default: 0x1f

## Returns

- `Group`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4982`
