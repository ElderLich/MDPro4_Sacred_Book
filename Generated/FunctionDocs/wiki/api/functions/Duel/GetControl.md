# Duel.GetControl

## Signature

```lua
Duel.GetControl(Card|Group targets, int player, [int reset_phase], [int reset_count], [int zone]) -> int
```

## Description

Moves control of targets to player and returns the number of cards whose control actually changed.
Use reset_phase and reset_count for temporary control, such as PHASE_END, 1. To pass only a zone mask, use 0, 0, zone.

## How To Use It

Use this when an effect takes control of cards.

For temporary control, pass a phase and count. For permanent control, omit those arguments. If you only need to restrict the destination zone, pass `0,0,zone` before the zone mask.

```lua
local tc=Duel.GetFirstTarget()
if tc and tc:IsRelateToEffect(e) then
    Duel.GetControl(tc,tp,PHASE_END,1)
end
```

The return value is the number of cards that actually changed control, so use `>0` when later logic depends on success.

## Related Functions

- [Card.IsControler](/api/functions/Card/IsControler)
- [Duel.SwapControl](/api/functions/Duel/SwapControl)
- [Duel.CheckLocation](/api/functions/Duel/CheckLocation)

## Parameters

- `targets` `Card|Group`
- `player` `int`
- `reset_phase` `int` optional - default: 0
- `reset_count` `int` optional - default: 0
- `zone` `int` optional - default: 0xff

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4906`
