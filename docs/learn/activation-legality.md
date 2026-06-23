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

## Explicit vs Implicit Requirements

Card text usually gives explicit requirements before the colon. Those are good
condition/cost/target checks. Some legality requirements are implicit in the
action instead:

| Intended action | Implicit legality check |
| --- | --- |
| Draw cards. | `Duel.IsPlayerCanDraw(...)` |
| Special Summon. | `Duel.GetLocationCount(...)` and `Card.IsCanBeSpecialSummoned(...)` |
| Add to hand. | a filter with `Card.IsAbleToHand` or the relevant able-to helper |
| Banish. | a filter with `Card.IsAbleToRemove` or `Card.IsAbleToRemoveAsCost` |
| Equip. | an available target plus legal equip state/checks |
| Inflict damage or recover LP. | target player/amount can be announced, and any card-dependent amount has a legal source |

Do not put every implicit action check into `condition`. Conditions should
answer timing and event questions. Action availability usually belongs in
`target` or `cost`, because those callbacks already have the `chk==0` check
branch.

## Optional Effects Should Have A Legal Outcome

Optional activated effects should normally be unavailable if they cannot make a
legal attempt. For example, a search effect should check that a matching card
exists and can be added to the hand.

```lua
function s.thfilter(c)
    return c:IsSetCard(0x123) and c:IsAbleToHand()
end

function s.thtg(e,tp,eg,ep,ev,re,r,rp,chk)
    if chk==0 then
        return Duel.IsExistingMatchingCard(s.thfilter,tp,LOCATION_DECK,0,1,nil)
    end
    Duel.SetOperationInfo(0,CATEGORY_TOHAND,nil,1,tp,LOCATION_DECK)
end
```

The operation may still fail if the Deck changes before resolution. Legality
only proves that the activation was valid when chosen.

## Mandatory Effects Still Resolve Carefully

Mandatory trigger effects normally activate when their event happens, even if
some later action may no longer be possible. Their check branch is often broad:

```lua
function s.mandtarg(e,tp,eg,ep,ev,re,r,rp,chk)
    if chk==0 then return true end
    Duel.SetOperationInfo(0,CATEGORY_DAMAGE,nil,0,1-tp,500)
end
```

The operation still checks the current state before applying an action. A
mandatory trigger is not permission to skip resolution checks.

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
