# Card.SetUniqueOnField

## Signature

```lua
Card.SetUniqueOnField(Card c, int s, int o, function|int unique_code, [int unique_location]) -> void
```

## Description

Sets a uniqueness rule for c so only one card with unique_code can exist on the checked field, Monster Zone, or Spell & Trap Zone range.

## Parameters

- `c` `Card`
- `s` `int`
- `o` `int`
- `unique_code` `function|int`
- `unique_location` `int` optional - default: LOCATIOIN_ONFIELD

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3657`
