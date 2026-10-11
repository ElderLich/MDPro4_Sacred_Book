# RushDuel.NoCostCheck

Alias: `RD.NoCostCheck`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.NoCostCheck(function cost, int flag_effect) -> function
```

## Description

Wraps a cost callback with a Rush cost-waiver check. An applicable player effect with the specified code waives the cost when its value is 1 or its value callback returns true; otherwise the original cost callback receives all arguments.

## Parameters

- `cost` `function`: Cost callback to invoke when no waiver applies.
- `flag_effect` `int`: Player-effect code that can waive this cost.

## Returns

- `function`: Wrapped cost callback.

## Source

`Rush/Utilities/RDCost.lua:124`

```lua
function RushDuel.NoCostCheck(cost, flag_effect)
    return function(e, tp, eg, ep, ev, re, r, rp, chk)
        local effects = {Duel.IsPlayerAffectedByEffect(tp, flag_effect)}
        for _, effect in ipairs(effects) do
            local val = effect:GetValue()
            if val == 1 then
                return true
            elseif val(effect, e, tp, eg, ep, ev, re, r, rp) then
                return true
            end
        end
        return cost(e, tp, eg, ep, ev, re, r, rp, chk)
    end
end
```
