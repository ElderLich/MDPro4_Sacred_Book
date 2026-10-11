# Card.RemoveCounter

## Signature

```lua
Card.RemoveCounter(Card c, int player, int countertype, int count, int reason) -> bool|nil
```

## Description

Removes count counters of countertype from c for reason, using player as the removing player.
When countertype is 0, the core clears every counter on c and returns no Lua value. Otherwise it yields and returns whether the requested counters were removed.

## Parameters

- `c` `Card`
- `player` `int`
- `countertype` `int`
- `count` `int`
- `reason` `int`

## Returns

- `bool|nil`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3684`
