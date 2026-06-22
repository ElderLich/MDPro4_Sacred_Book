# Effect.SetCode

## Signature

```lua
Effect.SetCode(Effect e, int code) -> void
```

## Description

Sets e's code. For triggered effects this is usually an event code; for continuous effects it is the effect code being applied.

## How To Use It

`SetCode` means different things depending on the effect type.

For trigger effects, it is usually the event that makes the effect eligible to activate:

```lua
e1:SetType(EFFECT_TYPE_SINGLE+EFFECT_TYPE_TRIGGER_O)
e1:SetCode(EVENT_SUMMON_SUCCESS)
```

For continuous or single effects, it is usually the effect code being applied:

```lua
e1:SetType(EFFECT_TYPE_SINGLE)
e1:SetCode(EFFECT_UPDATE_ATTACK)
e1:SetValue(500)
```

Choose the code to match the type. A valid callback with the wrong event or effect code will still feel like it never works.

## Related Functions

- [Effect.SetType](/api/functions/Effect/SetType)
- [Effect.SetRange](/api/functions/Effect/SetRange)

## Parameters

- `e` `Effect`
- `code` `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libeffect.cpp:613`
