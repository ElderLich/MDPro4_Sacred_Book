# Duel.GetFlagEffect

## Signature

```lua
Duel.GetFlagEffect(int player, int code) -> int|nil
```

## Description

Returns how many player flag effects with code are registered on player.
The return value is a count, not a boolean; compare it with 0 when testing whether a player marker exists.

## How To Use It

Use this to count matching player markers.

```lua
if Duel.GetFlagEffect(tp,id)==0 then
    Duel.RegisterFlagEffect(tp,id,RESET_PHASE+PHASE_END,0,1)
end
```

The return value is a count. Use `Duel.GetFlagEffectLabel` when the marker's label value matters.

## Related Functions

- [Duel.RegisterFlagEffect](/api/functions/Duel/RegisterFlagEffect)
- [Duel.GetFlagEffectLabel](/api/functions/Duel/GetFlagEffectLabel)
- [Duel.ResetFlagEffect](/api/functions/Duel/ResetFlagEffect)

## Parameters

- `player` `int` - Player whose flag effects are counted.
- `code` `int` - Flag-effect code; the core masks it with MAX_CARD_ID and adds EFFECT_FLAG_EFFECT.

## Returns

- `int|nil` - Number of matching player flag effects, or nil if player is invalid.

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4854`
