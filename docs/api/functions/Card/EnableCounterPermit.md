# Card.EnableCounterPermit

## Signature

```lua
Card.EnableCounterPermit(Card c, int countertype, [int location], [function condition]) -> void
```

## Description

Allow c \[to be placed in the location location\] that can be placed "can be placed on the counter countertype
The default value of location depends on the type of c, and the monster needs to specify whether it can place a pointer in a monster or pendulum area

## Parameters

- `c` `Card`
- `countertype` `int`
- `location` `int` optional
- `condition` `function` optional

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3631`
