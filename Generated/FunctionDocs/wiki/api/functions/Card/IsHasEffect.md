# Card.IsHasEffect

## Signature

```lua
Card.IsHasEffect(Card c, int code, [int player]) -> Effect|nil,... Effect
```

## Description

Returns the effects currently affecting c with effect code code, or nil if none match.
When player is supplied, only effects whose count limit can still be used by that player are returned. Multiple matching effects are returned as multiple Lua return values.

## Parameters

- `c` `Card`
- `code` `int`
- `player` `int` optional

## Returns

- `Effect|nil`
- `... Effect` - Additional matching effects, if any.

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3552`
