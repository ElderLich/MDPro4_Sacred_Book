# RushDuel.AttachAtkDef

Alias: `RD.AttachAtkDef`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.AttachAtkDef(Effect e, Card card, int|function|nil atk, int|function|nil def, [int reset], [bool forced]) -> void
```

## Description

Registers a single-card EFFECT_UPDATE_ATTACK effect for nonzero, non-nil atk, and an EFFECT_UPDATE_DEFENSE effect for nonzero, non-nil def only when RD.IsCanChangeDef(card) passes. That predicate is card:IsDefenseAbove(0) and not RD.IsMaximumMode(card): it requires the core's valid, nonnegative DEF check and excludes Maximum-mode monsters. It does not block the ATK branch.
Both modifiers are created through RD.CreateSingleEffect with e:GetHandler() as owner, FLAG_ATTACH_EFFECT as label, and the supplied reset/forced values. No automatic duration is added when reset is omitted. Pass RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END for the usual until-End-Phase card modifier.
This helper returns no values and does not report whether the card's final stats changed. forced is passed to Card.RegisterEffect; leave it nil/false for normal effect-immunity handling.

## Parameters

- `e` `Effect`: Resolving source effect; its handler owns the modifiers.
- `card` `Card`: Card receiving the modifiers.
- `atk` `int|function|nil`: ATK delta or value callback; nil and numeric 0 skip this branch.
- `def` `int|function|nil`: DEF delta or value callback; nil and numeric 0 skip this branch, and RD.IsCanChangeDef must pass.
- `reset` `int` (optional): Explicit reset mask shared by both modifiers. Omitting it adds no reset policy.
- `forced` `bool` (optional): Passed to Card.RegisterEffect. Normally omit it rather than bypassing immunity.

## Returns

No return values.

## Example

```lua
RD.AttachAtkDef(e, tc, 1000, 0,
    RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END)
```

## Source

`Rush/Utilities/RDAttach.lua:5`

```lua
function RushDuel.AttachAtkDef(e, card, atk, def, reset, forced)
    if atk ~= nil and atk ~= 0 then
        RushDuel.CreateSingleEffect(e, nil, card, EFFECT_UPDATE_ATTACK, atk, reset, forced)
    end
    if def ~= nil and def ~= 0 and RushDuel.IsCanChangeDef(card) then
        RushDuel.CreateSingleEffect(e, nil, card, EFFECT_UPDATE_DEFENSE, def, reset, forced)
    end
end
```
