# Card.CreateEffectRelation

## Signature

```lua
Card.CreateEffectRelation(Card c, Effect e) -> void
```

## Description

Creates a relation between c and effect e.
If e is the triggering effect of a current Chain Link, the relation is tied to that Chain Link; otherwise the core stores a direct effect relation.

## Parameters

- `c` `Card`
- `e` `Effect`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3562`
