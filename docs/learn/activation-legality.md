# Activation Legality

Activation legality is the part of a script that answers: "May this effect be
activated right now?"

Most of that work happens in `condition`, `cost`, and `target`.

## `chk==0`

In target and cost functions, `chk==0` means the engine is asking if activation
is legal. Do not pay costs or move cards in this branch.

```lua
function s.target(e,tp,eg,ep,ev,re,r,rp,chk)
  if chk==0 then
    return Duel.IsExistingMatchingCard(s.filter,tp,LOCATION_MZONE,0,1,nil)
  end
  Duel.SetOperationInfo(0,CATEGORY_DESTROY,nil,1,tp,LOCATION_MZONE)
end
```

## Common Legality Questions

| Question | Typical check |
| --- | --- |
| Is the handler in the right place? | `SetRange`, `c:IsLocation(...)` |
| Is the phase right? | `Duel.IsMainPhase()`, `Duel.IsBattlePhase()`, `Duel.IsPhase(...)` |
| Is a card available? | `Duel.IsExistingMatchingCard(...)` |
| Can the player perform the action? | `Duel.IsPlayerCanDraw(...)`, `Duel.GetLocationCount(...)` |
| Can the cost be paid? | `Duel.CheckReleaseGroup(...)`, filter checks |
| Is the target legal? | `Duel.IsExistingTarget(...)`, `chkc` branch |

## Resolution Is Separate

Legal activation does not guarantee successful resolution. Cards may move, be
flipped face-down, or stop being related to the effect.

```lua
local tc=Duel.GetFirstTarget()
if tc and tc:IsRelateToEffect(e) then
  Duel.Destroy(tc,REASON_EFFECT)
end
```

Use activation checks to make the effect legal. Use resolution checks to keep it
correct after the game state changes.
