# Card.GetFieldID

## Signature

```lua
Card.GetFieldID(Card c) -> int
```

## Description

Returns the time stamp of the transition to the current position
This value is unique, the smaller the c is the earlier appear in that position
Opening the card from the inside will also change this value

## Parameters

- `c` `Card`

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3477`
