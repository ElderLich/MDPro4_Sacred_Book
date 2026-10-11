# RushDuel.AddHandToGraveSpecialSummonProcedure

Alias: `RD.AddHandToGraveSpecialSummonProcedure`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.AddHandToGraveSpecialSummonProcedure(Card card, int desc, function filter, int count, [int|function value], [int position]) -> Effect
```

## Description

Registers a hand Special Summon procedure requiring count matching other cards from hand. The condition checks capacity and candidates; the target step uses cancelable exact-count selection and retains the Group; the operation sends that Group with REASON_SPSUMMON and deletes the retained Group.
The filter must include the intended payment legality. This registers a procedure and returns its Effect; it does not perform an effect Special Summon immediately.

## Parameters

- `card` `Card`: Monster receiving the procedure.
- `desc` `int`: Summon option description identifier.
- `filter` `function`: Hand-card predicate; receives candidate, effect, player. The summoning card is excluded.
- `count` `int`: Exact number of other hand cards to send.
- `value` `int|function` (optional): Optional summon-procedure value.
- `position` `int` (optional): Optional summon position; supplied through EFFECT_FLAG_SPSUM_PARAM.

## Returns

- `Effect`: Registered hand Special Summon procedure.

## Source

`Rush/Utilities/RDSummon.lua:448`

```lua
function RushDuel.AddHandToGraveSpecialSummonProcedure(card, desc, filter, count, value, position)
    local con = RushDuel.HandToGraveSpecialSummonCondition(filter, count)
    local tg = RushDuel.HandToGraveSpecialSummonTarget(filter, count)
    local op = RushDuel.HandToGraveSpecialSummonOperation
    local e1 = RD.AddHandSpecialSummonProcedure(card, desc, con, tg, op, value, position)
    return e1
end
```
