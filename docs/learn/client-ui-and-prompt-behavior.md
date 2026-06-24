# Client UI And Prompt Behavior

Good scripts do two jobs at once: they enforce the card's rules, and they tell
the client enough for the player to understand what is happening. Prompt code
does not make an effect legal, but missing or vague prompt code can make a
legal effect feel hidden, confusing, or broken.

Read UI-facing script code in four layers:

| Layer | Common API | What the player sees |
| --- | --- | --- |
| Activation offer | `Effect.SetHintTiming` | When the client should offer or highlight an optional effect. |
| Selection prompt | `Duel.Hint(HINT_SELECTMSG,...)` | What the next card/group selection is asking for. |
| Opponent notice | `Duel.Hint(HINT_OPSELECTED,...)` | Which option or effect line the opponent is told was chosen. |
| Operation announcement | `Duel.SetOperationInfo` | What the Chain Link is expected to do. |

None of these replaces `SetType`, `SetCode`, `SetRange`, conditions, costs, or
the `chk==0` legality branch.

## Activation Offers

`Effect.SetHintTiming` tells the client when an optional effect is worth
offering. The first mask is for the handler's controller. The second mask is
for the opponent side. If the second mask is omitted, the local core copies the
first mask to both sides.

Book of Moon (`c14087893.lua`) asks to be offered around Battle Phase and
monster-check windows:

```lua
e1:SetType(EFFECT_TYPE_ACTIVATE)
e1:SetProperty(EFFECT_FLAG_CARD_TARGET)
e1:SetCode(EVENT_FREE_CHAIN)
e1:SetHintTiming(TIMING_BATTLE_PHASE,TIMINGS_CHECK_MONSTER+TIMING_BATTLE_PHASE)
```

That line only affects prompting. The target branch still decides whether the
activation is legal:

```lua
if chk==0 then
    return Duel.IsExistingTarget(c14087893.filter,tp,LOCATION_MZONE,LOCATION_MZONE,1,nil)
end
```

If the client never offers an effect, check the legality first: effect type,
event code, range, condition, cost, target legality, count limit, and card-type
activation rules. Hint timing is the final polish layer, not the permission
system.

## Opponent-Side Timing

The two-argument form is useful when the effect should mostly prompt after the
opponent does something.

Infinite Impermanence (`c10045474.lua`) uses a zero controller-side mask and an
opponent-side monster-check mask:

```lua
e1:SetCode(EVENT_FREE_CHAIN)
e1:SetHintTiming(0,TIMINGS_CHECK_MONSTER)
```

That makes sense for a Trap that often responds to an opponent's monster. Its
hand activation is still handled by a separate permission effect:

```lua
local e2=Effect.CreateEffect(c)
e2:SetType(EFFECT_TYPE_SINGLE)
e2:SetCode(EFFECT_TRAP_ACT_IN_HAND)
e2:SetCondition(c10045474.handcon)
c:RegisterEffect(e2)
```

Use hint timing to make a legal effect discoverable. Use real effect codes and
conditions to create activation exceptions.

## Selection Prompts

`Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_*)` sets the text for the next selection
made by that player. It does not filter the selection.

Mystical Space Typhoon (`c5318639.lua`) uses a destroy prompt before selecting
the official target:

```lua
Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_DESTROY)
local g=Duel.SelectTarget(tp,c5318639.filter,tp,LOCATION_ONFIELD,LOCATION_ONFIELD,1,1,e:GetHandler())
Duel.SetOperationInfo(0,CATEGORY_DESTROY,g,1,0,0)
```

The hint says "choose something to destroy." The filter and `SelectTarget`
decide which cards are legal and record the chosen card as the Chain target.

Common prompt choices:

| Hint | Typical follow-up |
| --- | --- |
| `HINTMSG_FACEUP` | Select a visible face-up card. |
| `HINTMSG_DESTROY` | Select a card that will be destroyed. |
| `HINTMSG_REMOVE` | Select a card that will be banished. |
| `HINTMSG_TOGRAVE` | Select a card to send to the GY. |
| `HINTMSG_ATOHAND` | Select a card to add to the hand. |
| `HINTMSG_SPSUMMON` | Select a monster to Special Summon. |
| `HINTMSG_EQUIP` | Select a card to equip or an equip target. |
| `HINTMSG_DISABLE` | Select a card whose effect will be disabled or negated. |
| `HINTMSG_SET` | Select a card to Set. |
| `HINTMSG_CODE` | Announce or choose a card name/code. |

Use the hint that matches what the next click means. A generic prompt might be
legal, but it makes the script feel worse to play.

## Target Prompts Versus Resolution Choices

Target prompts happen during activation and should use targeting APIs when the
card text targets. Resolution choices happen later and usually use matching or
Group selection APIs.

Book of Moon targets at activation:

```lua
Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_FACEUP)
local g=Duel.SelectTarget(tp,c14087893.filter,tp,LOCATION_MZONE,LOCATION_MZONE,1,1,nil)
Duel.SetOperationInfo(0,CATEGORY_POSITION,g,1,0,0)
```

Cyberdark Invasion (`c1157683.lua`) targets a monster at activation, then
chooses an Equip Card during resolution:

```lua
Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_FACEUP)
Duel.SelectTarget(tp,c1157683.eqfilter,tp,LOCATION_MZONE,0,1,1,nil,tp)
```

```lua
local tc=Duel.GetFirstTarget()
if tc:IsRelateToEffect(e) then
    Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_EQUIP)
    local g=Duel.SelectMatchingCard(tp,aux.NecroValleyFilter(c1157683.eqfilter2),tp,LOCATION_GRAVE,LOCATION_GRAVE,1,1,nil)
    local ec=g:GetFirst()
    if not ec or not Duel.Equip(tp,ec,tc) then return end
end
```

That split is important:

- `SelectTarget` records official Chain targets.
- `SelectMatchingCard` chooses cards at resolution.
- `Duel.GetFirstTarget()` plus `IsRelateToEffect` rechecks an official target.
- A resolution choice often needs `Duel.HintSelection(g)` if the script wants
  to highlight a group it found without a normal selection prompt.

## Sequential Prompts

When an effect performs several choices, set a fresh prompt before each choice.

Trap Trick (`c80101899.lua`) first asks which Trap to banish from the Deck,
then asks which matching Trap to Set:

```lua
Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_REMOVE)
local g1=Duel.SelectMatchingCard(tp,c80101899.rmfilter,tp,LOCATION_DECK,0,1,1,nil,tp)
local tc1=g1:GetFirst()
if tc1 and Duel.Remove(tc1,POS_FACEUP,REASON_EFFECT)~=0 and tc1:IsLocation(LOCATION_REMOVED) then
    Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_SET)
    local g2=Duel.SelectMatchingCard(tp,c80101899.setfilter,tp,LOCATION_DECK,0,1,1,nil,tc1:GetCode())
    -- Set the selected Trap.
end
```

Without the second `Duel.Hint`, the player can still be asked to choose a card,
but the prompt may describe the previous action. That kind of mismatch makes a
script feel sloppy even when the effect resolves correctly.

## Opponent Notices

`Duel.Hint(HINT_OPSELECTED,1-tp,e:GetDescription())` tells the opponent which
described option or effect line was chosen.

Cyberdark Invasion uses it before each face-up Trap Quick Effect:

```lua
Duel.Hint(HINT_OPSELECTED,1-tp,e:GetDescription())
Duel.RegisterFlagEffect(tp,1157683,RESET_PHASE+PHASE_END,0,1)
Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_FACEUP)
Duel.SelectTarget(tp,c1157683.eqfilter,tp,LOCATION_MZONE,0,1,1,nil,tp)
```

Use this for optional effects with descriptions, especially when a face-up card
has multiple effects. It helps the opponent understand which line of text is
being used before the controller selects cards.

## Operation Info

`Duel.SetOperationInfo` records what the current Chain Link expects to do. It
helps the client, replay/response logic, and other scripts that inspect Chain
operation categories.

Pot of Greed (`c55144522.lua`) is player-targeted, so it stores target player
and amount, then announces a draw:

```lua
Duel.SetTargetPlayer(tp)
Duel.SetTargetParam(2)
Duel.SetOperationInfo(0,CATEGORY_DRAW,nil,0,tp,2)
```

Trap Trick does not know the exact removed card until resolution, so it
announces only the expected category, count, player, and location:

```lua
Duel.SetOperationInfo(0,CATEGORY_REMOVE,nil,1,tp,LOCATION_DECK)
```

Use concrete targets when they are known. Use `nil` targets when the exact card
will be chosen later. Do not announce an operation that is only possible after
a random result or later branch unless the local pattern intentionally does so.

## Zone And Selection Feedback

Some UI helpers are not activation prompts. Infinite Impermanence highlights
the affected Spell & Trap Zone column after it resolves from the field:

```lua
Duel.Hint(HINT_ZONE,tp,0x1<<(c:GetSequence()+8))
```

`Duel.HintSelection(g)` highlights a known group. Use it when the script has
already determined the cards and wants the client to show them, not when the
player still has to choose.

## Why An Effect Feels Invisible

When a legal-looking effect never appears, check in this order:

1. Is the effect in the right place? Check `SetRange`, activation card type,
   hand/set-turn exception effects, and whether the handler is still related.
2. Is the window correct? Check `SetType`, `SetCode`, Spell Speed, Damage Step
   properties, and Chain response conditions.
3. Does the legality branch pass? Check condition, cost `chk==0`, target
   `chk==0`, count limit, available zones, and action legality.
4. Is hint timing too quiet? Add or adjust `SetHintTiming` only after the
   effect is actually legal.
5. Is the player being asked the wrong question? Check the last
   `Duel.Hint(HINT_SELECTMSG,...)` before the selection function.

## Why An Effect Feels Awkward

These scripts usually work, but feel rough:

| Symptom | Likely cause | Better pattern |
| --- | --- | --- |
| The prompt appears at odd times. | Missing or overly broad `SetHintTiming`. | Use timing masks that match the card's natural response window. |
| The prompt appears but activation fails. | Hint timing is present, but legality fails. | Fix condition, cost, target, range, or count-limit checks. |
| The player chooses a card but the wrong UI text is shown. | Stale or generic `HINT_SELECTMSG`. | Put a specific `Duel.Hint` directly before each selection. |
| The opponent cannot tell which face-up effect was chosen. | Missing `HINT_OPSELECTED`. | Use the effect description as the opponent notice. |
| Other response effects miss the action. | Missing or misleading `SetOperationInfo`. | Announce known categories, targets, count, player, and param. |
| A targeted card is chosen at resolution instead. | `SelectMatchingCard` used where `SelectTarget` was required. | Use `SelectTarget` during activation and recheck relation at resolution. |
| A resolution choice looks unconfirmed. | The group was found by script, not selected by the player. | Use `Duel.HintSelection(g)` when showing a known group helps. |

## Useful API Pages

- [`Duel.Hint`](/api/functions/Duel/Hint)
- [`Duel.HintSelection`](/api/functions/Duel/HintSelection)
- [`Effect.SetHintTiming`](/api/functions/Effect/SetHintTiming)
- [`Duel.SetOperationInfo`](/api/functions/Duel/SetOperationInfo)
- [`Duel.GetOperationInfo`](/api/functions/Duel/GetOperationInfo)
- [`Duel.SetTargetPlayer`](/api/functions/Duel/SetTargetPlayer)
- [`Duel.SetTargetParam`](/api/functions/Duel/SetTargetParam)
- [`Duel.GetChainInfo`](/api/functions/Duel/GetChainInfo)
- [`Duel.SelectTarget`](/api/functions/Duel/SelectTarget)
- [`Duel.SelectMatchingCard`](/api/functions/Duel/SelectMatchingCard)
- [`Duel.GetFirstTarget`](/api/functions/Duel/GetFirstTarget)
- [`Card.IsRelateToEffect`](/api/functions/Card/IsRelateToEffect)

Related lessons:

- [Categories, Properties, And Hint Timing](categories-properties-and-hints)
- [Chain Timing And Activation Windows](chain-timing-and-activation-windows)
- [Targeting flow](targeting-flow)
- [Selection And Group Handling](selection-and-group-handling)
- [Common Script Errors And Debugging](common-script-errors-and-debugging)
