# RushDuel.CostSendHandToGrave

Alias: `RD.CostSendHandToGrave`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CostSendHandToGrave(function filter, int|function min, int|function max, [function|nil set_label_before], [function|nil set_object_before], [function|nil set_label_after], [function|nil set_object_after]) -> function
```

## Description

Returns a cost callback that selects min to max matching cards from the controller's hand and sends them to the Graveyard with REASON_COST, excluding the effect handler. The filter must include any required cost-legality check such as Card.IsAbleToGraveAsCost; this wrapper does not add that predicate.
The callback honors EFFECT_NO_COST_SEND_HAND_TO_GRAVE through RD.NoCostCheck. min and max can be numbers or callbacks evaluated with the cost arguments. Optional label callbacks receive the selected Group before sending or the operated Group after a successful send.

## Parameters

- `filter` `function`: Card filter receiving card, effect, player and remaining cost callback arguments.
- `min` `int|function`: Minimum count or callback computing it.
- `max` `int|function`: Maximum count or callback computing it.
- `set_label_before` `function|nil` (optional): Computes the effect label from the selected Group before sending.
- `set_object_before` `function|nil` (optional): Computes the label object from the selected Group before sending.
- `set_label_after` `function|nil` (optional): Computes the effect label from the operated Group after a successful send.
- `set_object_after` `function|nil` (optional): Computes the label object from the operated Group after a successful send.

## Returns

- `function`: Cost callback for Effect.SetCost; tests availability for chk==0, then performs payment.

## Example

```lua
e1:SetCost(RD.CostSendHandToGrave(Card.IsAbleToGraveAsCost, 1, 1))
```

## Source

`Rush/Utilities/RDCost.lua:299`

```lua
function RushDuel.CostSendHandToGrave(filter, min, max, set_label_before, set_object_before, set_label_after,
    set_object_after)
    local cost = RushDuel.CostSendMatchToGrave(filter, LOCATION_HAND, min, max, true, false, false, set_label_before,
        set_object_before, set_label_after, set_object_after)
    return RushDuel.NoCostCheck(cost, EFFECT_NO_COST_SEND_HAND_TO_GRAVE)
end
```
