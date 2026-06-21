# Effect.SetTargetRange

## Signature

```lua
Effect.SetTargetRange(Effect e, int s_range, int o_range) -> void
```

## Description

Set the Target Range property for effect e
S_range refers to our area of ​​influence
The o_range value affects the partner area
If the EFFECT_FLAG_ABSOLUTE_RANGE flag is specified in the property property,
Then s_range refers to the player 1 affected area, o_range refers to player 2 affected area
If this is a call (cover) / limit call (cover) / special call procedure
(EFFECT_SUMMON_PROC / EFFECT_LIMIT_SUMMON_PROC / EFFECT_SPSUMMON_PROC, etc.)
And the property specifies the EFFECT_FLAG_SPSUM_PARAM flag,
Then s_range that special summoned to the players of the venue,
O_range represents a selectable representation

## Parameters

- `e` `Effect`
- `s_range` `int`
- `o_range` `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libeffect.cpp:615`
