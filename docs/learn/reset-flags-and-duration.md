# Reset Flags And Effect Duration

Reset flags answer a simple but dangerous question: when should this temporary
thing stop existing?

That "thing" might be a lingering disable effect, a player restriction, a
once-this-turn marker, a client hint, or a card flag. The action itself is
handled by the effect code, operation, or flag function. The reset only controls
how long the created effect or marker remains registered.

Most beginner bugs with temporary effects come from using the right effect code
with the wrong lifetime. A monster gets disabled correctly, but stays disabled
after it leaves the field. A player restriction works, but survives past the End
Phase. A flag marker is set, but never disappears. Reset flags are where those
lifetimes are written.

## The Three Questions

When you write a reset, answer these in order.

| Question | Common answer |
| --- | --- |
| What kind of reset can remove this? | `RESET_EVENT`, `RESET_PHASE`, `RESET_CHAIN`, or a manual reset. |
| Which event or phase matters? | `RESETS_STANDARD`, `PHASE_END`, `PHASE_DRAW`, `RESET_TURN_SET`, and similar constants. |
| How many matching reset checks should it survive? | The optional reset count in `Effect.SetReset`, `Card.RegisterFlagEffect`, or `Duel.RegisterFlagEffect`. |

The local core treats a missing or `0` reset count as `1`. For phase resets, if
the reset mask includes `RESET_PHASE` but does not include either
`RESET_SELF_TURN` or `RESET_OPPO_TURN`, the core adds both turn sides. That
means `RESET_PHASE+PHASE_END` means an End Phase for either player, not only the
handler's controller.

## Quick Patterns

| Need | Common reset shape |
| --- | --- |
| Temporary effect attached to a card until the End Phase | `RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END` |
| Temporary player or Duel restriction until the End Phase | `RESET_PHASE+PHASE_END` |
| Marker that should stay only while a card remains the same field object | `RESET_EVENT+RESETS_STANDARD` |
| Player marker for an option used this turn | `RESET_PHASE+PHASE_END` |
| Restriction for the next own Draw Phase | `RESET_PHASE+PHASE_DRAW+RESET_SELF_TURN` |
| Effect that exists only during the current Chain | `RESET_CHAIN` |

These are patterns, not magic phrases. Start from the card text, then decide
whether the temporary effect belongs to a card object, a player, the whole Duel,
or the current Chain.

## Card-Bound Temporary Effects

When a temporary effect changes a specific card, it usually needs both an event
reset and a time reset.

Infinite Impermanence (`c10045474.lua`) and Effect Veiler (`c97268402.lua`) use
this shape for temporary monster negation:

```lua
local e1=Effect.CreateEffect(c)
e1:SetType(EFFECT_TYPE_SINGLE)
e1:SetCode(EFFECT_DISABLE)
e1:SetReset(RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END)
tc:RegisterEffect(e1)
local e2=e1:Clone()
e2:SetCode(EFFECT_DISABLE_EFFECT)
e2:SetValue(RESET_TURN_SET)
tc:RegisterEffect(e2)
```

The phase part says "until the End Phase." The event part says "also remove this
if the target stops being the same card object on the field." If the monster is
Set face-down, leaves the field, returns to the hand or Deck, goes to the GY, is
banished, or is temporarily banished, the standard event reset clears the
temporary disable.

That distinction matters. A card-bound disable, ATK change, type change, or
flag should not follow the physical card through every possible state unless
the card text specifically says it should.

## What RESETS_STANDARD Covers

In the local constants, `RESETS_STANDARD` is the usual "this card is no longer
the same field object" package. It includes these reset events:

| Reset event | Beginner meaning |
| --- | --- |
| `RESET_TOFIELD` | The card returns or is placed onto the field as a new field object. |
| `RESET_LEAVE` | The card leaves the field. |
| `RESET_TODECK` | The card goes to the Deck or Extra Deck. |
| `RESET_TOHAND` | The card goes to the hand. |
| `RESET_TEMP_REMOVE` | The card is temporarily banished. |
| `RESET_REMOVE` | The card is banished. |
| `RESET_TOGRAVE` | The card goes to the GY. |
| `RESET_TURN_SET` | The card is Set face-down. |

`RESETS_STANDARD` does not include every possible reset flag. For example,
`RESET_DISABLE`, `RESET_CONTROL`, `RESET_OVERLAY`, and `RESET_MSCHANGE` are
separate. Add those only when the local pattern or card text needs that extra
lifetime rule.

## Duel-Wide And Player Effects

Temporary restrictions registered with `Duel.RegisterEffect` are often not tied
to one card's location. They usually reset by phase only.

Lava Golem (`c102380.lua`) applies a Summon restriction for the rest of the
turn after its Special Summon procedure:

```lua
local e1=Effect.CreateEffect(c)
e1:SetType(EFFECT_TYPE_FIELD)
e1:SetCode(EFFECT_CANNOT_SUMMON)
e1:SetProperty(EFFECT_FLAG_PLAYER_TARGET+EFFECT_FLAG_OATH)
e1:SetTargetRange(1,0)
e1:SetReset(RESET_PHASE+PHASE_END)
Duel.RegisterEffect(e1,tp)
local e2=e1:Clone()
e2:SetCode(EFFECT_CANNOT_MSET)
Duel.RegisterEffect(e2,tp)
```

There is no `RESET_EVENT+RESETS_STANDARD` here because the restriction belongs
to the player for the turn. It should not disappear just because the handler
moved somewhere else after creating the restriction.

Truth Reinforce (`c10118318.lua`) uses the same idea for a Battle Phase lock:

```lua
local e1=Effect.CreateEffect(e:GetHandler())
e1:SetType(EFFECT_TYPE_FIELD)
e1:SetProperty(EFFECT_FLAG_PLAYER_TARGET+EFFECT_FLAG_OATH)
e1:SetCode(EFFECT_CANNOT_BP)
e1:SetTargetRange(1,0)
e1:SetReset(RESET_PHASE+PHASE_END)
Duel.RegisterEffect(e1,tp)
```

When the text says "also, you cannot..." or "for the rest of this turn, you
cannot...", ask whether that restriction follows a card or follows a player. In
many local scripts, it follows the player.

## Phase Resets And Turn Sides

Use `RESET_SELF_TURN` or `RESET_OPPO_TURN` when the timing only cares about one
player's turns.

The local core helps with the broad case: `RESET_PHASE+PHASE_END` receives both
turn sides automatically. That is perfect for "until the End Phase" or "until
the end of this turn."

For "during your next Draw Phase" or "until your next Standby Phase", be
explicit:

```lua
e1:SetReset(RESET_PHASE+PHASE_DRAW+RESET_SELF_TURN)
```

The draw-skip option in `c967928.lua` has one extra wrinkle. If the skip effect
is created while that player is already in their own Draw Phase, the script uses
a reset count of `2` and stores the current turn count:

```lua
if Duel.GetTurnPlayer()==1-tp and Duel.GetCurrentPhase()==PHASE_DRAW then
    e1:SetLabel(Duel.GetTurnCount())
    e1:SetReset(RESET_PHASE+PHASE_DRAW+RESET_SELF_TURN,2)
else
    e1:SetReset(RESET_PHASE+PHASE_DRAW+RESET_SELF_TURN)
end
```

That prevents the current Draw Phase from consuming the only reset count before
the future skip can matter. The operation's condition then checks the stored
turn count so the current Draw Phase is not skipped by accident.

## Flag Effects Use The Same Lifetime Rules

[`Card.RegisterFlagEffect`](/api/functions/Card/RegisterFlagEffect) and
[`Duel.RegisterFlagEffect`](/api/functions/Duel/RegisterFlagEffect) create real
effects used as script markers. Their `reset_flag` and `reset_count` follow the
same reset-count rules as [`Effect.SetReset`](/api/functions/Effect/SetReset):
count `0` becomes `1`, and a phase reset without a turn side is treated as both
turn sides by the core.

Dragon Master Magia (`c12381100.lua`) marks which once-per-turn option was used
by the player:

```lua
if re:IsActiveType(TYPE_MONSTER) then
    Duel.RegisterFlagEffect(tp,id,RESET_PHASE+PHASE_END,0,1)
elseif re:IsActiveType(TYPE_SPELL) then
    Duel.RegisterFlagEffect(tp,id+o,RESET_PHASE+PHASE_END,0,1)
elseif re:IsActiveType(TYPE_TRAP) then
    Duel.RegisterFlagEffect(tp,id+o*2,RESET_PHASE+PHASE_END,0,1)
end
```

A card marker usually needs card identity resets:

```lua
tc:RegisterFlagEffect(id,RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END,0,1)
```

Use a player flag when the memory belongs to the player. Use a card flag when
the memory belongs to one specific card. For more flag examples, see
[Flag Effects](flag-effects).

## Current Chain Only

`RESET_CHAIN` is for effects that should vanish after the current Chain
handling. It is much shorter than "until the End Phase."

Functions such as [`Duel.NegateRelatedChain`](/api/functions/Duel/NegateRelatedChain)
create related-chain cleanup behavior internally. If you are creating your own
temporary registered effect, only use `RESET_CHAIN` when the effect truly should
exist for this Chain and no longer.

## Manual Resets

Sometimes a script removes a temporary effect explicitly instead of waiting for
its reset mask. [`Effect.Reset`](/api/functions/Effect/Reset) can reset an
effect manually, and flag effects can be cleared with
[`Card.ResetFlagEffect`](/api/functions/Card/ResetFlagEffect) or
[`Duel.ResetFlagEffect`](/api/functions/Duel/ResetFlagEffect).

Manual resets are useful for delayed watchers, stored Groups, or effects that
must end when a custom condition is met. They do not replace normal reset flags;
they are an extra escape hatch.

## Common Mistakes

| Mistake | Fix |
| --- | --- |
| Temporary effect has no reset. | Add a reset that matches the card text. |
| Card-bound effect uses only `RESET_PHASE+PHASE_END`. | Add `RESET_EVENT+RESETS_STANDARD` if it should disappear when the card leaves, is Set, or changes state. |
| Player restriction uses `RESETS_STANDARD`. | Usually use a phase reset only; the restriction belongs to a player, not a card object. |
| "Next own phase" uses only `RESET_PHASE+PHASE_*`. | Add `RESET_SELF_TURN` or `RESET_OPPO_TURN` when only one player's phase matters. |
| Reset count is `1` while the effect is created during the same phase it watches. | Use a local script pattern like the draw-skip example: count `2` plus a turn-count guard. |
| A flag marker never disappears. | Give the flag a reset, or clear it manually with the matching reset function. |

## Useful API Pages

- [`Effect.SetReset`](/api/functions/Effect/SetReset)
- [`Effect.Reset`](/api/functions/Effect/Reset)
- [`Card.RegisterEffect`](/api/functions/Card/RegisterEffect)
- [`Duel.RegisterEffect`](/api/functions/Duel/RegisterEffect)
- [`Card.RegisterFlagEffect`](/api/functions/Card/RegisterFlagEffect)
- [`Duel.RegisterFlagEffect`](/api/functions/Duel/RegisterFlagEffect)
- [`Card.ResetFlagEffect`](/api/functions/Card/ResetFlagEffect)
- [`Duel.ResetFlagEffect`](/api/functions/Duel/ResetFlagEffect)
- [`Duel.GetCurrentPhase`](/api/functions/Duel/GetCurrentPhase)
- [`Duel.GetTurnPlayer`](/api/functions/Duel/GetTurnPlayer)
- [`Duel.NegateRelatedChain`](/api/functions/Duel/NegateRelatedChain)
