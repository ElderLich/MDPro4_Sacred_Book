# Duel.GetTargetsRelateToChain

## Signature

```lua
Duel.GetTargetsRelateToChain() -> Group
```

## Description

Returns all target cards currently related to the resolving Chain.
This is the relation-aware helper for multi-target operations; targets that left their expected place are omitted from the returned Group.

## Returns

- `Group` - New Group containing the current Chain targets whose Chain relation is still valid; empty when none qualify.

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4950`
