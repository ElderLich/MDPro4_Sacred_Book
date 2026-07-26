# Card.IsCanAddCounter

## Signature

```lua
Card.IsCanAddCounter(Card c, int countertype, int count, [bool singly], [int loc]) -> bool
```

## Description

Checks whether the current reason player can place count counters of countertype on c.
When loc is 0, c must currently be face-up on the field. When loc is nonzero, the counter permit range is checked against loc instead. If singly is true, counter limits are tested as current count + 1 rather than current count + count.

## Parameters

- `c` `Card`
- `countertype` `int`
- `count` `int`
- `singly` `bool` optional - default: false
- `loc` `int` optional - default: 0

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3638`
