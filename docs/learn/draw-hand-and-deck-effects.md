# Draw, Hand, And Deck Effects

Draw, hand, and Deck effects affect players, but they often move cards too.
They need two layers of care:

1. Check whether the player is allowed to perform the action.
2. Move, reveal, sort, discard, or shuffle cards with the API that matches the
   card text.

This page covers draw effects, hand reveal/shuffle patterns, sending cards from
the top of the Deck to the GY, and Deck-top inspection.

## Drawing Cards

Pot of Greed (`c55144522.lua`) is the standard draw template:

```lua
function s.target(e,tp,eg,ep,ev,re,r,rp,chk)
    if chk==0 then return Duel.IsPlayerCanDraw(tp,2) end
    Duel.SetTargetPlayer(tp)
    Duel.SetTargetParam(2)
    Duel.SetOperationInfo(0,CATEGORY_DRAW,nil,0,tp,2)
end

function s.activate(e,tp,eg,ep,ev,re,r,rp)
    local p,d=Duel.GetChainInfo(0,CHAININFO_TARGET_PLAYER,CHAININFO_TARGET_PARAM)
    Duel.Draw(p,d,REASON_EFFECT)
end
```

Use [`Duel.IsPlayerCanDraw`](/api/functions/Duel/IsPlayerCanDraw) in the
activation check. Use [`Duel.Draw`](/api/functions/Duel/Draw) in the operation.
`Duel.Draw` returns the number of cards actually drawn, so scripts that do
something afterward often test the return value.

```lua
if Duel.Draw(p,2,REASON_EFFECT)==2 then
    -- continue with the "then discard 1 card" part
end
```

Junoldo the Shadespirit Power Patron (`c10266279.lua`) draws 2 and then
discards only if the full draw happened.

## Drawing Then Discarding

When an effect says to draw and then discard, do not discard unless the draw
success condition matches the card text.

```lua
local p=Duel.GetChainInfo(0,CHAININFO_TARGET_PLAYER)
if Duel.Draw(p,2,REASON_EFFECT)==2 then
    Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_DISCARD)
    local dg=Duel.SelectMatchingCard(tp,Card.IsDiscardable,tp,LOCATION_HAND,0,1,1,nil,REASON_EFFECT)
    Duel.ShuffleHand(tp)
    if dg:GetCount()>0 then
        Duel.BreakEffect()
        Duel.SendtoGrave(dg,REASON_EFFECT+REASON_DISCARD)
    end
end
```

The local script shuffles the hand after selecting the discard because the hand
was just changed by drawing. Use [`Duel.ShuffleHand`](/api/functions/Duel/ShuffleHand)
when a reveal, draw, or selection would otherwise leave private hand order
trackable.

## Discarding From The Hand

For costs, local scripts usually use
[`Duel.DiscardHand`](/api/functions/Duel/DiscardHand) with a cost reason:

```lua
function s.cost(e,tp,eg,ep,ev,re,r,rp,chk)
    if chk==0 then return Duel.IsExistingMatchingCard(Card.IsDiscardable,tp,LOCATION_HAND,0,1,nil) end
    Duel.DiscardHand(tp,Card.IsDiscardable,1,1,REASON_COST+REASON_DISCARD)
end
```

For effect discards, use `REASON_EFFECT+REASON_DISCARD`. If the card text
selects the discarded card, choose it first, then send it with the correct
reason. If the text says the opponent chooses, pass the opponent as the
selecting player.

Do not use hand discard APIs for sending from the Deck to the GY. That has its
own functions.

## Sending From The Top Of The Deck To The GY

Local scripts use [`Duel.DiscardDeck`](/api/functions/Duel/DiscardDeck) for
"send cards from the top of the Deck to the GY" effects.

That Grass Looks Greener (`c11110587.lua`) calculates the Deck size difference:

```lua
function s.target(e,tp,eg,ep,ev,re,r,rp,chk)
    local ct=Duel.GetFieldGroupCount(tp,LOCATION_DECK,0)
        -Duel.GetFieldGroupCount(tp,0,LOCATION_DECK)
    if chk==0 then return ct>0 and Duel.IsPlayerCanDiscardDeck(tp,ct) end
    Duel.SetOperationInfo(0,CATEGORY_DECKDES,nil,0,tp,ct)
end

function s.activate(e,tp,eg,ep,ev,re,r,rp)
    local ct=Duel.GetFieldGroupCount(tp,LOCATION_DECK,0)
        -Duel.GetFieldGroupCount(tp,0,LOCATION_DECK)
    if ct>0 then
        Duel.DiscardDeck(tp,ct,REASON_EFFECT)
    end
end
```

Use [`Duel.IsPlayerCanDiscardDeck`](/api/functions/Duel/IsPlayerCanDiscardDeck)
for effect movement. Use
[`Duel.IsPlayerCanDiscardDeckAsCost`](/api/functions/Duel/IsPlayerCanDiscardDeckAsCost)
when the Deck send is a cost.

The category for this action is usually `CATEGORY_DECKDES`.

## Revealing The Top Of The Deck

Deck-top effects usually combine three steps:

1. Confirm the top cards.
2. Get a `Group` containing those cards.
3. Move or reorder them.

Sunlight Unicorn (`c10321588.lua`) reveals the top card:

```lua
if Duel.GetFieldGroupCount(tp,LOCATION_DECK,0)==0 then return end
Duel.ConfirmDecktop(tp,1)
local g=Duel.GetDecktopGroup(tp,1)
local tc=g:GetFirst()
if tc:IsType(TYPE_EQUIP) and tc:IsAbleToHand() then
    Duel.DisableShuffleCheck()
    Duel.SendtoHand(g,nil,REASON_EFFECT)
    Duel.ShuffleHand(tp)
else
    Duel.MoveSequence(tc,SEQ_DECKBOTTOM)
end
```

Use [`Duel.ConfirmDecktop`](/api/functions/Duel/ConfirmDecktop) before reading
cards that are being revealed. Use
[`Duel.GetDecktopGroup`](/api/functions/Duel/GetDecktopGroup) to work with
those cards.

The `DisableShuffleCheck` call is used before moving known Deck cards in ways
that should not force an automatic shuffle check.

## Sorting And Returning Cards

Sylvan Sprout (`c10753491.lua`) reveals one or two cards, sends Plant monsters
to the GY, then lets the player order the rest before moving them to the bottom
of the Deck:

```lua
Duel.ConfirmDecktop(tp,ac)
local g=Duel.GetDecktopGroup(tp,ac)
local sg=g:Filter(Card.IsRace,nil,RACE_PLANT)
if sg:GetCount()>0 then
    Duel.DisableShuffleCheck()
    Duel.SendtoGrave(sg,REASON_EFFECT+REASON_REVEAL)
end
ac=ac-sg:GetCount()
if ac>0 then
    Duel.SortDecktop(tp,tp,ac)
    for i=1,ac do
        local mg=Duel.GetDecktopGroup(tp,1)
        Duel.MoveSequence(mg:GetFirst(),SEQ_DECKBOTTOM)
    end
end
```

[`Duel.SortDecktop`](/api/functions/Duel/SortDecktop) takes the sorting player,
the target player's Deck, and the number of cards being sorted. After sorting,
the script repeatedly moves the current top card to the bottom.

## Searching And Revealing Cards

When a card moves from a private location such as the Deck or hand to a public
location, scripts often confirm the card:

```lua
Duel.SendtoHand(g,nil,REASON_EFFECT)
Duel.ConfirmCards(1-tp,g)
```

Use [`Duel.ConfirmCards`](/api/functions/Duel/ConfirmCards) so the opponent can
see which private card was added or chosen. If a card was revealed from the
hand and remains in the hand, use `Duel.ShuffleHand` afterward when local
examples do, so the opponent cannot track the exact hand position.

## Common Checks

| Question | Function |
| --- | --- |
| Can this player draw this many cards? | [`Duel.IsPlayerCanDraw`](/api/functions/Duel/IsPlayerCanDraw) |
| Can this player send cards from the top of the Deck to the GY by effect? | [`Duel.IsPlayerCanDiscardDeck`](/api/functions/Duel/IsPlayerCanDiscardDeck) |
| Can this player send cards from the top of the Deck to the GY as cost? | [`Duel.IsPlayerCanDiscardDeckAsCost`](/api/functions/Duel/IsPlayerCanDiscardDeckAsCost) |
| How many cards are in a location? | [`Duel.GetFieldGroupCount`](/api/functions/Duel/GetFieldGroupCount) |
| Which cards are currently on top of the Deck? | [`Duel.GetDecktopGroup`](/api/functions/Duel/GetDecktopGroup) |

For exact card movement from hand, Deck, GY, or banishment, also check the
card-level `IsAbleTo...` function that matches the destination.

## Common Mistakes

| Mistake | Better pattern |
| --- | --- |
| Calling `Duel.Draw` without checking draw legality. | Use `Duel.IsPlayerCanDraw` in the target branch. |
| Treating `DiscardDeck` as a hand discard. | `DiscardDeck` sends from the top of the Deck to the GY. |
| Using effect legality checks for costs. | Use `IsPlayerCanDiscardDeckAsCost` when the Deck send is a cost. |
| Revealing private cards without confirmation. | Use `Duel.ConfirmCards` or `Duel.ConfirmDecktop` as appropriate. |
| Forgetting to shuffle the hand after reveal/search patterns. | Follow local examples with `Duel.ShuffleHand` when a private hand position was exposed. |
| Sorting Deck-top cards before confirming them. | Reveal first, get the Deck-top group, then sort or move cards. |

Draw, hand, and Deck scripts are mostly about respecting hidden information.
Check legality first, reveal what the opponent is allowed to know, then move or
shuffle cards with the exact reason flags the text needs.
