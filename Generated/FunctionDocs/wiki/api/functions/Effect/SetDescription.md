# Effect.SetDescription

## Signature

```lua
Effect.SetDescription(Effect e, int desc) -> void
```

## Description

Sets e's description id, usually produced with Auxiliary.Stringid for card text choices.

## How To Use It

Descriptions are integer string ids, not raw text.

Most card scripts use `aux.Stringid(id,n)` to point at the nth string for that card:

```lua
e1:SetDescription(aux.Stringid(id,0))
```

Descriptions are commonly shown for optional triggers, selectable effects, and effects registered to Spell/Trap activations.

## Related Functions

- [Auxiliary.Stringid](/api/functions/Auxiliary/Stringid)
- [Duel.Hint](/api/functions/Duel/Hint)

## Parameters

- `e` `Effect`
- `desc` `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libeffect.cpp:612`
