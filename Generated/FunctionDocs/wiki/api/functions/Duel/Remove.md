# Duel.Remove

## Signature

```lua
Duel.Remove(Card|Group targets, int pos, int reason, [int reason_player]) -> int
```

## Description

Banishes targets in position pos for reason and returns the number of cards actually banished.
If reason includes REASON_TEMPORARY, the banish is treated as temporary and the card can later be returned with Duel.ReturnToField.
Use POS_FACEDOWN only when the effect requires a face-down banish; ordinary banish effects usually use POS_FACEUP.

## How To Use It

Use this for banishing cards. The second argument is the banished position, usually `POS_FACEUP` or `POS_FACEDOWN`.

```lua
if c:IsRelateToEffect(e) then
    Duel.Remove(c,POS_FACEUP,REASON_EFFECT)
end
```

For temporary banish effects, scripts commonly include `REASON_TEMPORARY`; those cards can later be returned with `Duel.ReturnToField`.

## Related Functions

- [Card.IsAbleToRemove](/api/functions/Card/IsAbleToRemove)
- [Duel.ReturnToField](/api/functions/Duel/ReturnToField)
- [Duel.SetOperationInfo](/api/functions/Duel/SetOperationInfo)

## Parameters

- `targets` `Card|Group`
- `pos` `int`
- `reason` `int`
- `reason_player` `int` optional

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4859`
