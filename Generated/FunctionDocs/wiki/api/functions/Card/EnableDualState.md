# Card.EnableDualState

## Signature

```lua
Card.EnableDualState(Card c) -> void
```

## Description

Registers EFFECT_DUAL_STATUS on c so local Gemini/Dual checks treat it as having gained its effects.
This does not perform a Normal Summon or spend a Normal Summon. Use it only for effects that explicitly make a Gemini Monster be treated as having been Normal Summoned again.
The registered status effect includes the local client hint and resets with the normal card event reset.

## Parameters

- `c` `Card` - Gemini Monster that should immediately gain Dual State.

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3566`
