# Debug.AddCard

## Signature

```lua
Debug.AddCard(int code, int owner, int player, int location, int seq, int pos, [bool proc]) -> Card
```

## Description

Add a card, the card number for the card holder is set to owner, to represent the form of pos placed in the player's field is located in the location on the seq seq grid
Proc = true then lifted the Soviet students limit

## Parameters

- `code` `int`
- `owner` `int`
- `player` `int`
- `location` `int`
- `seq` `int`
- `pos` `int`
- `proc` `bool` optional - default: false

## Returns

- `Card`

## Source

- `D:\Programs\GitHub\ygopro-core\libdebug.cpp:203`
