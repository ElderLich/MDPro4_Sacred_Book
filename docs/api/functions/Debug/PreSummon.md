# Debug.PreSummon

## Signature

```lua
Debug.PreSummon(Card c, int sum_type, [int sum_location]) -> void
```

## Description

Sets c's stored summon information to summon_type plus optional summon_location in the high word.

## Parameters

- `c` `Card`
- `sum_type` `int`
- `sum_location` `int` optional - default: 0

## Source

- `D:\Programs\GitHub\ygopro-core\libdebug.cpp:205`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

No indexed local card script currently calls this function.

This can mean the function is unused in the current script set, is only called through an alias, or is available for future/manual scripts.
