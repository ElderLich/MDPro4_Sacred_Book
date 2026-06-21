# Effect.SetCountLimit

## Signature

```lua
Effect.SetCountLimit(Effect e, int count, [int code]) -> void
```

## Description

Set the number of times a round can be launched count (only trigger type effect is valid), the same code (not equal to 0 or 1) share a number of times
The code contains the following values ​​that have special properties
EFFECT_COUNT_CODE_OATH The number of vows
EFFECT_COUNT_CODE_DUEL The number of times in the duel
EFFECT_COUNT_CODE_SINGLE the same card more than the number of public use of the effect (not the same name card)

## Parameters

- `e` `Effect`
- `count` `int` - default: 1
- `code` `int` optional - default: 0

## Source

- `D:\Programs\GitHub\ygopro-core\libeffect.cpp:617`
