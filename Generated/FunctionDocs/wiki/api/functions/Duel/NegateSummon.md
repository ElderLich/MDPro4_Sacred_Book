# Duel.NegateSummon

## Signature

```lua
Duel.NegateSummon(Card|Group targets) -> void
```

## Description

Negates a current Normal Summon, Flip Summon, or Special Summon for targets.
targets may be a Card or Group. Normal and Flip Summon negation require a single card; Special Summon negation can process a group and only negates cards whose Summon is negatable by the current reason effect. The core raises the matching *_SUMMON_NEGATED event and returns no Lua value.
This is Summon negation, not Chain activation negation; pass the Summoned card or Group, not a Chain Link number.

## How To Use It

Use this for effects that negate a Summon before it becomes successful.

```lua
local g=eg
Duel.NegateSummon(g)
Duel.Destroy(g,REASON_EFFECT)
```

This is separate from Chain negation. It expects the Card or Group being Summoned, not a Chain Link number.

## Related Functions

- [Duel.GetCurrentChain](/api/functions/Duel/GetCurrentChain)
- [Duel.NegateActivation](/api/functions/Duel/NegateActivation)
- [Duel.Destroy](/api/functions/Duel/Destroy)

## Parameters

- `targets` `Card|Group`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4932`
