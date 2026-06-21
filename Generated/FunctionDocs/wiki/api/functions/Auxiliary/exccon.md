# Auxiliary.exccon

## Signature

```lua
Auxiliary.exccon(Effect e) -> void
```

## Description

Simplified method for the condition that this card cannot activate its effect during the turn it was sent to the Graveyard, used for SetCondition
function aux.exccon(e)
  return Duel.GetTurnCount()~=e:GetHandler():GetTurnID() or e:GetHandler():IsReason(REASON_RETURN)
end

## Parameters

- `e` `Effect`

## Source

- `Utilities/utility.lua:802`
