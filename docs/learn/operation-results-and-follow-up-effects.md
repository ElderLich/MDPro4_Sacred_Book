# Operation Results And Follow-Up Effects

A selected card is a request. The movement function's return value and the
cards' resulting state tell you what happened. This difference matters when
an effect says "then", requires all selected cards to arrive, or offers a
choice only after its first action succeeds.

Start with [moving cards](/learn/moving-cards) and
[targeting flow](/learn/targeting-flow). This lesson adds the result checks
that decide whether a later action is allowed.

## Three Questions After An Operation

| Question | Tool | What it does not establish |
| --- | --- | --- |
| Did the operation report success, and how many cards? | The documented return value, such as `Duel.SendtoDeck(...)>0` | That every requested card reached the destination your text requires. |
| Which cards did it actually process? | [`Duel.GetOperatedGroup`](/api/functions/Duel/GetOperatedGroup), immediately afterward | That those cards are still in the desired location. |
| Did enough of them reach the required place? | `IsLocation`, `FilterCount`, or another result-specific test | That a later action is currently legal. Check that action too. |

For example, returning an Extra Deck monster "to the Deck" normally sends it
to the Extra Deck. A follow-up that specifically requires a card to enter
the **Main Deck** must distinguish `LOCATION_DECK` from `LOCATION_EXTRA`.

Use the return type from the API page. Most card-moving operations return a
count, while `SpecialSummonStep` returns a boolean. In Lua, **zero is true**:
`if Duel.SendtoDeck(...) then` does not test whether any cards moved.

## A Complete Example With An Optional Follow-Up

This teaching Normal Spell has deliberately explicit conditions:

> Shuffle 1 monster from your GY into the Deck, then, if it entered the Main
> Deck, you can draw 1 card.

It does not target. The player chooses the monster during resolution. The
optional draw is offered only after the return succeeds, the card reaches
the Main Deck, and drawing is currently permitted. Put "Draw 1 card?" in
this Spell's database `str1`, used by `aux.Stringid(id,0)`.

```lua
local s,id=GetID()

function s.initial_effect(c)
    local e1=Effect.CreateEffect(c)
    e1:SetCategory(CATEGORY_TODECK+CATEGORY_DRAW)
    e1:SetType(EFFECT_TYPE_ACTIVATE)
    e1:SetCode(EVENT_FREE_CHAIN)
    e1:SetTarget(s.target)
    e1:SetOperation(s.activate)
    c:RegisterEffect(e1)
end

function s.filter(c)
    return c:IsType(TYPE_MONSTER) and c:IsAbleToDeck()
end

function s.target(e,tp,eg,ep,ev,re,r,rp,chk)
    if chk==0 then
        return Duel.IsExistingMatchingCard(s.filter,tp,LOCATION_GRAVE,0,1,nil)
    end
    Duel.SetOperationInfo(0,CATEGORY_TODECK,nil,1,tp,LOCATION_GRAVE)
    Duel.SetOperationInfo(0,CATEGORY_DRAW,nil,0,tp,1)
end

function s.activate(e,tp,eg,ep,ev,re,r,rp)
    Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_TODECK)
    local g=Duel.SelectMatchingCard(tp,aux.NecroValleyFilter(s.filter),
        tp,LOCATION_GRAVE,0,1,1,nil)
    if #g==0 then return end
    if Duel.SendtoDeck(g,nil,SEQ_DECKSHUFFLE,REASON_EFFECT)==0 then return end
    local returned=Duel.GetOperatedGroup()
    local entered_main_deck=returned:IsExists(Card.IsLocation,1,nil,LOCATION_DECK)
    if not entered_main_deck then return end
    Duel.ShuffleDeck(tp)
    if not Duel.IsPlayerCanDraw(tp,1) then return end
    if Duel.SelectYesNo(tp,aux.Stringid(id,0)) then
        Duel.BreakEffect()
        Duel.Draw(tp,1,REASON_EFFECT)
    end
end
```

`SetOperationInfo` describes the effect's possible actions; it neither
performs the draw nor makes the optional part mandatory. This custom effect
does not require drawing to be legal at activation because returning the
monster is its mandatory action and drawing is optional. Compare with
effects that require both actions in [draw, hand, and Deck effects](/learn/draw-hand-and-deck-effects).

The operation filters the current GY again with the local
`aux.NecroValleyFilter` helper. If no selectable monster remains, it stops.
If the chosen monster returns to the Extra Deck, the first action succeeds
but the specifically worded Main Deck condition fails. If drawing becomes
forbidden, the first action stays completed and there is no draw prompt.

This example teaches an explicit condition; it is not a replacement for the
rulings of an existing card. Whether partial completion is enough depends on
that card's text and local script precedent.

## Requiring Two Actual Results

Xyz Universe (`11109820`) requires both targeted monsters to remain related
to its effect, sends them to the GY, then counts how many operated cards
actually reached the GY. The relevant source fragment is:

```lua
local g=Duel.GetChainInfo(0,CHAININFO_TARGET_CARDS)
local tc1=g:GetFirst()
local tc2=g:GetNext()
if not tc1:IsRelateToEffect(e) or not tc2:IsRelateToEffect(e) then return end
Duel.SendtoGrave(g,REASON_EFFECT)
local og=Duel.GetOperatedGroup()
if og:FilterCount(Card.IsLocation,nil,LOCATION_GRAVE)<2 then return end
```

The full source continues by selecting and Special Summoning a legal Xyz
Monster. A two-card input Group alone would not prove that both arrived in
the GY. A positive movement count alone would not prove it either. The
destination count expresses the required result.

Do not automatically copy its "both must still relate" early return to
every multi-target effect. Some effects apply to the remaining valid targets
and decide the follow-up from that partial result. Design the first action
and the follow-up condition separately, according to the card text.

EN Shuffle (`10186633`) uses a different threshold: after returning its
selected card(s), it asks whether **at least one** operated card is in
`LOCATION_DECK+LOCATION_EXTRA` before its later draw. The Extra Deck is
accepted there because that script's condition differs from our teaching
Spell's explicit Main Deck condition.

The complete example calls [`Duel.ShuffleDeck(tp)`](/api/functions/Duel/ShuffleDeck)
before offering the draw.
In this core, `SEQ_DECKSHUFFLE` can leave the shuffle pending until the
operation finishes; a draw inside that same operation must not use the old
Deck order. `BreakEffect` does not flush that pending shuffle. EN Shuffle
also explicitly shuffles before its follow-up draw.

## Capture The Result Before Another Action

`GetOperatedGroup` is not an event Group and not a history query. Read it
immediately after the relevant operation. Functions such as `SendtoDeck`,
`SendtoGrave`, `Destroy`, `Remove`, `Release`, and `SpecialSummon` use the
core's operated-card set; another operation can replace that set.

```lua
Duel.SendtoGrave(g,REASON_EFFECT)
local moved=Duel.GetOperatedGroup()
local arrived=moved:FilterCount(Card.IsLocation,nil,LOCATION_GRAVE)
-- Decide the next action using this result before performing another move.
if arrived>=2 then
    Duel.BreakEffect()
    Duel.Draw(tp,1,REASON_EFFECT)
end
```

This fragment assumes `g`, the required threshold, and draw legality were
established by the surrounding effect. It illustrates where to capture the
result, not a standalone card.

The local core constructs a **new Group** from its current operated set.
The saved Group's membership does not turn into the next operation's Group.
However, its Cards are live objects: after another action, their locations
or stats may differ. Save a number or boolean immediately if the next step
needs the result as it was at that moment, as `arrived` does above. If a Group
must survive between callbacks, also follow the lifetime rules in
[selection and Group handling](/learn/selection-and-group-handling).

## What BreakEffect Does

[`Duel.BreakEffect`](/api/functions/Duel/BreakEffect) marks a separation
between parts of a resolving effect so the engine can process their timing
correctly. It does not make a new Chain Link, offer the opponent an activation
inside the current resolution, or replace the condition for continuing.

Put the success test before the dependent action. Add `BreakEffect` when the
effect's sequence calls for that separation, using the actual card text and
matching scripts as your guide. Do not insert it between every line: an
effect whose actions happen simultaneously needs a different structure.

## Try These Cases

| Case for the complete example | Expected result |
| --- | --- |
| An ordinary monster enters the Main Deck; drawing is legal | Ask whether to draw, then draw only on Yes. |
| The chosen monster enters the Extra Deck | Finish the return; do not offer a draw. |
| The GY has no eligible monster at resolution | End without a return or draw. |
| The first action fails or does not produce a Main Deck arrival | Do not offer a draw. |
| A chained restriction prevents drawing | Complete a legal return, without offering the follow-up. |
| The player declines the draw | Keep the completed return; do not undo it. |

For a multi-card effect, additionally test one success out of two and a
destination replacement. Log both the reported count and the immediate
destination count when diagnosing a wrong follow-up.

## Sources And Next Steps

The local `libduel.cpp` binding `duel_get_operated_group` copies
`core.operated_set`; the operation bindings and the scripts below establish
the result-checking patterns.

- [Xyz Universe source](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c11109820.lua): require two actual GY arrivals.
- [EN Shuffle source](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c10186633.lua): accept a Deck or Extra Deck return before drawing.
- [Five-Headed Link Dragon source](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c10669138.lua): count five actually banished cards to decide an upkeep failure branch.
- [Tokens and Summon choices](/learn/tokens-and-summon-choices): boolean step results and batch completion.
- [Chain timing and activation windows](/learn/chain-timing-and-activation-windows): events and resolution timing.
