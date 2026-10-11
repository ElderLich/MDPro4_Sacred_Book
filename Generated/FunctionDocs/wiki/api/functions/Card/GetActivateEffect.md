# Card.GetActivateEffect

## Signature

```lua
Card.GetActivateEffect(Card c) -> Effect|nil
```

## Description

Returns c's activation effect, the effect with type EFFECT_TYPE_ACTIVATE. This is mainly used for Spell/Trap Cards.
Returns nil when the card has no registered activation effect, so guard the result before calling Effect methods.
Use the returned Effect to check whether a Field Spell or other Spell/Trap can be activated before moving or resolving it through another effect.

## Parameters

- `c` `Card`

## Returns

- `Effect|nil` - The activation effect registered on c, or nil if none is registered.

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3599`
