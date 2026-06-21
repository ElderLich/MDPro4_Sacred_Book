# Card.SetUniqueOnField

## Signature

```lua
Card.SetUniqueOnField(Card c, int s, int o, function|int unique_code, [int unique_location]) -> void
```

## Description

Set c to unique_code only in the field [or monster area or magic trap area, determined by the unique_location] can only exist one
S is not 0 will check the uniqueness of their field, o is not 0 check the other field uniqueness

## Parameters

- `c` `Card`
- `s` `int`
- `o` `int`
- `unique_code` `function|int`
- `unique_location` `int` optional - default: LOCATIOIN_ONFIELD

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3657`
