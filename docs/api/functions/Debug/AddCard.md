# Debug.AddCard

## Signature

```lua
Debug.AddCard(int code, int owner, int player, int location, int seq, int pos, [bool proc]) -> Card|nil
```

## Description

Creates a card with code and places it in the requested test field location, or attaches it as Xyz Material if an occupied Monster Zone contains an Xyz Monster; proc marks its procedure complete.

## Parameters

- `code` `int`
- `owner` `int`
- `player` `int`
- `location` `int`
- `seq` `int`
- `pos` `int`
- `proc` `bool` optional

## Returns

- `Card|nil`

## Source

- `D:\Programs\GitHub\ygopro-core\libdebug.cpp:203`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

No indexed local card script currently calls this function.

This can mean the function is unused in the current script set, is only called through an alias, or is available for future/manual scripts.
