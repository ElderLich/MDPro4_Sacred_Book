# RushDuel.SendToHandAndExists

Alias: `RD.SendToHandAndExists`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.SendToHandAndExists(Card|Group|Effect target, Effect effect, int player, int reason, [function|nil filter], [int count], [Card|Group|nil expect]) -> bool
```

## Description

Moves the supplied Card/Group/Effect handler toward its owner hand after applying the Rush EFFECT_CANNOT_TO_HAND_EFFECT protection filter and expanding Maximum components. After movement, confirms relevant cards from Deck/GY/banishment to the opponent.
The reason argument is forwarded to the Rush protection checks, but this pinned implementation calls Duel.SendtoHand with REASON_EFFECT unconditionally. It is not a generic cost-payment helper. player controls protection/confirmation context, not a forced hand destination: the native destination argument is nil.
Returns false if the eligible Group is empty or the core movement count is zero. Otherwise returns true when filter is nil, or checks at least count matching cards in Duel.GetOperatedGroup while excluding expect. This is a boolean, not a count, and the default does not prove every selected card reached the hand.

## Parameters

- `target` `Card|Group|Effect`: Cards to move; Effect input means its handler.
- `effect` `Effect`: Source effect used by Rush protection checks; required.
- `player` `int`: Player used for protection and confirmation context.
- `reason` `int`: Reason passed to protection checks; actual movement is always REASON_EFFECT in this snapshot.
- `filter` `function|nil` (optional): Optional predicate checked against the operated Group.
- `count` `int` (optional): Required match count when filter is supplied.
- `expect` `Card|Group|nil` (optional): Exclusion for the operated-Group check.

## Returns

- `bool`: Whether movement was nonzero and the optional operated-Group check passed.

## Source

`Rush/Utilities/RDAction.lua:277`

```lua
function RushDuel.SendToHandAndExists(target, effect, player, reason, filter, count, expect)
    local hints = Group.CreateGroup()
    local group = RushDuel.ToGroup(target):Filter(RushDuel.FilterToHandTarget, nil, effect, player, reason, hints)
    local g = RushDuel.ToMaximunGroup(group)
    local tc = hints:GetFirst()
    if tc then
        Duel.Hint(HINT_CARD, 0, tc:GetOriginalCode())
    end
    if #g == 0 then
        return false
    end
    if Duel.SendtoHand(g, nil, REASON_EFFECT) == 0 then
        return false
    end
    local cg = g:Filter(RushDuel.FilterToHandConfirm, nil, player)
    if #cg > 0 then
        Duel.ConfirmCards(1 - player, cg)
    end
    return RushDuel.IsOperatedGroupExists(filter, count, expect)
end
```
