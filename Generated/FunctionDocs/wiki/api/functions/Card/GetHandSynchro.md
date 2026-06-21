# Card.GetHandSynchro

## Signature

```lua
Card.GetHandSynchro(Card c) -> nil|Effect,function|nil,int|nil,int|nil
```

## Description

If card c is affected by the hand Synchro effect EFFECT_HAND_SYNCHRO, return Effect e, function target, int min, int max; otherwise return nil

## Parameters

- `c` `Card`

## Returns

- `nil|Effect`
- `function|nil`
- `int|nil`
- `int|nil`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3547`
