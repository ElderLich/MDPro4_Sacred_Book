# Applying The Latest Engine And Script Changes

This lesson turns the imported changes into rules you can apply to your own
cards. The source snapshot advances main scripts from `b605741` to
`14745a5a`, core from `8b020270` to `c4ccbab4`, and adds the Rush library at
`6916047c`. The define repository has no new commits in this update.

## Card Type And Current Type

The core now separates a card's **card type** from its effective **current
type**. `get_card_type()` starts from database type and applies
`EFFECT_ADD_CARD_TYPE`, `EFFECT_REMOVE_CARD_TYPE`, and `EFFECT_CHANGE_CARD_TYPE`.
`get_type()` then handles current-state rules, including Pendulum Zone behavior
and ordinary `EFFECT_ADD_TYPE`/`REMOVE_TYPE`/`CHANGE_TYPE` effects.

| Question | API |
| --- | --- |
| What is its current effective type? | [`GetType`](/api/functions/Card/GetType), [`IsType`](/api/functions/Card/IsType), [`IsAllTypes`](/api/functions/Card/IsAllTypes) |
| What type of card is it, including the new card-type changes? | [`GetCardType`](/api/functions/Card/GetCardType), [`IsCardType`](/api/functions/Card/IsCardType), [`IsAllCardTypes`](/api/functions/Card/IsAllCardTypes) |
| What was that card type on the field before it moved? | [`GetPreviousCardTypeOnField`](/api/functions/Card/GetPreviousCardTypeOnField), [`IsPreviousCardTypeOnField`](/api/functions/Card/IsPreviousCardTypeOnField) |
| What type was printed in its data? | [`GetOriginalType`](/api/functions/Card/GetOriginalType) |

`IsCardType(mask)` accepts **any** matching bit. `IsAllCardTypes(mask)` requires
**all** of them. A filter for a “Normal Monster card” therefore uses:

```lua
function s.filter(c)
    return c:IsAllCardTypes(TYPE_NORMAL+TYPE_MONSTER)
end
```

Imported scripts such as `c10007434.lua`, `c30752324.lua`, and `c45151304.lua`
use this distinction. Add a face-up, location, cost, or movement check when the
particular card requires it; type alone does not prove the card is eligible.

The new effect codes are 377, 378, and 379 respectively. Use their symbolic
names in scripts. Do not globally replace `IsType`: ordinary checks for the
current monster/Spell/Trap state still need its existing behavior.

::: warning The running core must expose the API
Updating editor completion and documentation does not update the game's
native core binary. A missing `IsAllCardTypes` method means the runtime and
script snapshot differ. Replacing it with `IsAllTypes` changes the question
being asked and can conceal the compatibility problem.
:::

## A Counter Mention Is Metadata

`aux.HasMentionedCounter(c,counter)` reads the script's `mentioned_counter`
metadata. It does not check how many counters are currently on the card.

```lua
-- On a script whose text names this counter type:
s.mentioned_counter={[0x1]=true}

-- In a filter for cards whose text mentions that counter:
function s.filter(c)
    return aux.HasMentionedCounter(c,0x1)
end
```

Use [`Card.GetCounter`](/api/functions/Card/GetCounter) for a live counter count
and the [Counters lesson](counters) for counter placement and removal.
Metadata, permissions, and counters currently present are separate concerns.

## Three Small Fixes With Large Effects

### Check Numeric Action Results

Upstream `0200c677d` corrected `c43419178.lua`:

```lua
if tc and Duel.SendtoGrave(tc,REASON_EFFECT)>0
    and tc:IsLocation(LOCATION_GRAVE) then
    -- Continue with the dependent action.
end
```

Lua treats zero as true. A bare `if Duel.SendtoGrave(...) then` cannot tell
success from a zero result. The location check also verifies that this card
reached the destination required by the next action.

### Guard Subgroup Results

Upstream `78175e702` corrected many subgroup selections:

```lua
local selected=g:SelectSubGroup(tp,s.groupcheck,false,2,2)
if not selected then return end
-- Use selected only after the nil guard.
```

This is a callback fragment: `g` is your candidate Group and `s.groupcheck` is
the card's group predicate. Keep `CheckSubGroup` legality checks where needed,
but still guard the returned selection before dereferencing it.

### Use Inequality For Numeric Tests

Upstream `e74a16853` fixed `not c:GetAttack()==0` to `c:GetAttack()~=0` in
`c2606417.lua`. `not` binds before `==`; the original expression compared a
Boolean with zero. See [Lua Essentials](lua-essentials) for a short exercise.

## Updated Hint Names

New code should use `HINTMSG_NUMBER` and `HINTMSG_LVRANK`. The misspelled
`HINGMSG_NUMBER` and `HINGMSG_LVRANK` remain compatibility aliases in this
snapshot. The correctly spelled names make completion and source searches
consistent; there is no need to rewrite unrelated logic around them.

## Review An Existing Card

1. Read the changed card text and its new script together.
2. Determine whether a changed predicate asks about current type, card type,
   printed type, or previous state.
3. Check action return values and possible `nil` selections.
4. Test a legal state, an illegal state, and a state that changes before
   resolution. Add a second-copy test for name-based count limits.
5. For Rush, follow the [Rush track](rush-duel-scripting) and verify the shared
   helper implementation as well as the card script.

The source trail is the companion `ygopro-core` repository's `card.cpp` and
`libcard.cpp`, this repository's `Utilities/utility.lua` and
`Utilities/constant.lua`, and the card scripts named above. The
[function reference](/api/functions/) links individual calls to the source
snapshot.
