# Activation Legality

Activation legality is the part of a script that answers: "May this effect be
activated right now?"

Most of that work happens in `condition`, `cost`, and `target`. The important
habit is to separate legality checks from resolution. A legal activation can
still resolve without doing anything if its target disappears or a required
zone closes.

## The Legality Flow

For an activated effect, the engine checks roughly this shape:

1. Is the effect type/timing available?
2. Is the handler in the right place?
3. Does `condition` return true?
4. Can the `cost` be paid with `chk==0`?
5. Does `target` return true with `chk==0`?
6. If activated, pay cost and select targets.
7. Later, resolve the operation.

This is why target and cost callbacks must be careful: the check branch is not
the same as the real activation branch.

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

The non-check branch is where you select targets, announce operation info, or
store labels that the operation will read.

## Common Legality Questions

| Question | Typical check |
| --- | --- |
| Is the handler in the right place? | `SetRange`, `c:IsLocation(...)` |
| Is the phase right? | `Duel.IsMainPhase()`, `Duel.IsBattlePhase()`, `Duel.IsPhase(...)` |
| Is a card available? | `Duel.IsExistingMatchingCard(...)` |
| Can the card be targeted? | `Duel.IsExistingTarget(...)` and the `chkc` branch |
| Can the player perform the action? | `Duel.IsPlayerCanDraw(...)`, `Duel.GetLocationCount(...)` |
| Can the cost be paid? | `Duel.CheckLPCost(...)`, `Duel.CheckReleaseGroup(...)` |
| Can the monster be Special Summoned? | `c:IsCanBeSpecialSummoned(...)`, `Duel.GetLocationCount(...)` |
| Is the effect once per turn? | `SetCountLimit(...)` |

## Target Rechecks With `chkc`

Targeting effects often include a `chkc` branch. It tells the client whether a
manually chosen card is a legal target for this effect.

```lua
function s.target(e,tp,eg,ep,ev,re,r,rp,chk,chkc)
    if chkc then
        return chkc:IsControler(tp) and chkc:IsLocation(LOCATION_MZONE)
            and s.filter(chkc)
    end
    if chk==0 then
        return Duel.IsExistingTarget(s.filter,tp,LOCATION_MZONE,0,1,nil)
    end
    Duel.SelectTarget(tp,s.filter,tp,LOCATION_MZONE,0,1,1,nil)
end
```

The `chkc` branch should match the same target rules used by
`Duel.SelectTarget`.

## Resolution Is Separate

Legal activation does not guarantee successful resolution. Cards may move, be
flipped face-down, become unaffected, or stop being related to the effect.

```lua
local tc=Duel.GetFirstTarget()
if tc and tc:IsRelateToEffect(e) then
    Duel.Destroy(tc,REASON_EFFECT)
end
```

Use activation checks to make the effect legal. Use resolution checks to keep it
correct after the game state changes.

## Common Mistakes

| Mistake | Safer pattern |
| --- | --- |
| Paying cost during `chk==0`. | Only return whether the cost can be paid, then pay later. |
| Using `SelectMatchingCard` for an effect that targets. | Use `SelectTarget` and relation checks. |
| Forgetting zone checks for Special Summons or setting cards. | Check `Duel.GetLocationCount` or the relevant summon legality function. |
| Assuming a target is still valid at resolution. | Check `tc and tc:IsRelateToEffect(e)`. |
| Announcing a category that the operation does not perform. | Match `SetCategory` and `SetOperationInfo` to the real action. |
