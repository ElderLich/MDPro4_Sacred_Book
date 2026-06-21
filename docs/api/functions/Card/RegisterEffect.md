# Card.RegisterEffect

## Signature

```lua
Card.RegisterEffect(Card c, Effect e, [bool forced]) -> int
```

## Description

Register the effect e to c, return the global id of the effect, and set the Handler of e to c
By default, if c is registered with the effect of immune e then the registration will fail
If forced is true, the immune effect of c against e will not be checked

## Parameters

- `c` `Card`
- `e` `Effect`
- `forced` `bool` optional - default: false

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3548`
