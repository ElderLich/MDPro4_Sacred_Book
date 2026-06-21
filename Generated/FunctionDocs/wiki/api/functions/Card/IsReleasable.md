# Card.IsReleasable

## Signature

```lua
Card.IsReleasable(Card c, [int reason]) -> bool
```

## Description

检查c是否可以被以原因reason解放（非上级召唤用）

## Parameters

- `c` `Card`
- `reason` `int` optional - default: REASON_COST

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3595`
