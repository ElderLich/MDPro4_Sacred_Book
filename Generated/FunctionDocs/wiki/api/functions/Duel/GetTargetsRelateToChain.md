# Duel.GetTargetsRelateToChain

## Signature

```lua
Duel.GetTargetsRelateToChain() -> Group
```

## Description

Returns all target cards currently related to the resolving Chain.
This is the relation-aware helper for multi-target operations; targets that left their expected place are omitted from the returned Group.
The returned Group can be empty, so check its count before applying a follow-up action.

## How To Use It

Use this during resolution when a targeting effect selected more than one card and only the targets still related to the Chain should be affected.

```lua
local g=Duel.GetTargetsRelateToChain()
if #g>0 then
    Duel.Destroy(g,REASON_EFFECT)
end
```

The returned Group can be empty. It is built from the current Chain's target cards and relation state, so it is usually clearer than manually filtering `CHAININFO_TARGET_CARDS`.

## Related Functions

- [Duel.SelectTarget](/api/functions/Duel/SelectTarget)
- [Duel.GetFirstTarget](/api/functions/Duel/GetFirstTarget)
- [Card.IsRelateToEffect](/api/functions/Card/IsRelateToEffect)

## Returns

- `Group` - New Group containing the current Chain targets whose Chain relation is still valid; empty when none qualify.

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4950`
