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
