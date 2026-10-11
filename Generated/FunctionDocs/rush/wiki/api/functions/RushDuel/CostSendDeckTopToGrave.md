# RushDuel.CostSendDeckTopToGrave

Alias: `RD.CostSendDeckTopToGrave`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CostSendDeckTopToGrave(int count, [function|nil set_label], [function|nil set_object]) -> function
```

## Description

Returns a cost callback that checks whether the player can send count cards from the Deck as cost, then calls Duel.DiscardDeck with REASON_COST. Optional callbacks store information from the operated Group on the Effect.

## Parameters

- `count` `int`: Cards to send from the Deck top.
- `set_label` `function|nil` (optional): Computes a numeric label from the operated Group.
- `set_object` `function|nil` (optional): Computes a label object from the operated Group.

## Returns

- `function`: Cost callback.

## Source

`Rush/Utilities/RDCost.lua:240`

```lua
function RushDuel.CostSendDeckTopToGrave(count, set_label, set_object)
    return function(e, tp, eg, ep, ev, re, r, rp, chk)
        if chk == 0 then
            return Duel.IsPlayerCanDiscardDeckAsCost(tp, count)
        end
        if Duel.DiscardDeck(tp, count, REASON_COST) ~= 0 and (set_label ~= nil or set_object ~= nil) then
            local og = Duel.GetOperatedGroup()
            RushDuel.SetLabelAndObject(e, og, set_label, set_object)
        end
        return true
    end
end
```
