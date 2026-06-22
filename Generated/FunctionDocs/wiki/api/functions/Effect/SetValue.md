# Effect.SetValue

## Signature

```lua
Effect.SetValue(Effect e, function|int|bool val) -> void
```

## Description

Sets e's value field. The value can be a number, boolean, or callback function depending on the effect code.

## How To Use It

`SetValue` supplies the amount, flag, card code, or callback required by the effect code.

Simple stat changes usually use a number:

```lua
e1:SetCode(EFFECT_UPDATE_ATTACK)
e1:SetValue(500)
```

Some effect codes need a function instead:

```lua
e1:SetCode(EFFECT_EQUIP_LIMIT)
e1:SetValue(function(e,c) return c==e:GetLabelObject() end)
```

When a function is supplied, the core marks the effect as using a function value. Replacing it with a number or boolean clears that function-value flag.

## Related Functions

- [Effect.GetValue](/api/functions/Effect/GetValue)
- [Effect.SetCode](/api/functions/Effect/SetCode)

## Parameters

- `e` `Effect`
- `val` `function|int|bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libeffect.cpp:628`
