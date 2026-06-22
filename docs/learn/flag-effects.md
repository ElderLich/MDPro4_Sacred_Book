# Flag Effects

Flag effects are temporary markers that scripts attach to a player or a card.
They are useful when the script needs to remember something that is not already
stored by the card object: "this player already used this option this turn",
"this card was marked by this effect", or "this target belongs to this
operation."

The core creates a real `Effect` for each flag. The public `code` is masked with
`MAX_CARD_ID` and stored with `EFFECT_FLAG_EFFECT`, so a flag code does not
collide with a normal effect code. Flag effects cannot be disabled. If
`reset_count` is `0`, the core treats it as `1`.

## Player Flags

Use `Duel.RegisterFlagEffect` when the marker belongs to a player rather than a
specific card. Then use `Duel.GetFlagEffect` to check whether that marker is
already present.

Dragon Master Magia (`12381100`) uses this pattern for its once-per-turn
negations by card type. The Monster, Spell, and Trap negations each get a
different flag code, all resetting in the End Phase.

```lua
function s.discon(e,tp,eg,ep,ev,re,r,rp)
    return rp==1-tp and not e:GetHandler():IsStatus(STATUS_BATTLE_DESTROYED)
        and Duel.IsChainNegatable(ev)
        and ((re:IsActiveType(TYPE_MONSTER) and Duel.GetFlagEffect(tp,id)==0)
        or (re:IsActiveType(TYPE_SPELL) and Duel.GetFlagEffect(tp,id+o)==0)
        or (re:IsActiveType(TYPE_TRAP) and Duel.GetFlagEffect(tp,id+o*2)==0))
end

function s.distg(e,tp,eg,ep,ev,re,r,rp,chk)
    if chk==0 then return true end
    if re:IsActiveType(TYPE_MONSTER) then
        Duel.RegisterFlagEffect(tp,id,RESET_PHASE+PHASE_END,0,1)
    elseif re:IsActiveType(TYPE_SPELL) then
        Duel.RegisterFlagEffect(tp,id+o,RESET_PHASE+PHASE_END,0,1)
    elseif re:IsActiveType(TYPE_TRAP) then
        Duel.RegisterFlagEffect(tp,id+o*2,RESET_PHASE+PHASE_END,0,1)
    end
end
```

That reads as: if the matching marker is absent, the effect can be used; once
that option is chosen, register the marker until the End Phase.

## Card Flags

Use `Card.RegisterFlagEffect` when the marker belongs to one card. This is
common for cards that were affected by an operation, cards that should gain a
temporary status, or cards that need to be recognized later after an event.

```lua
function s.operation(e,tp,eg,ep,ev,re,r,rp)
    local c=e:GetHandler()
    if c:IsRelateToEffect(e) and c:GetFlagEffect(id)==0 then
        c:RegisterFlagEffect(id,RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END,0,1)
    end
end
```

Use `RESET_EVENT+RESETS_STANDARD` for a marker that should disappear when the
card stops being the same object on the field. Add a phase reset such as
`RESET_PHASE+PHASE_END` when the marker should also expire by time.

## Labels

A flag can also store one integer label. Use it when the marker needs a small
piece of data, such as a field ID, a turn count, or a bit mask.

```lua
local fid=tc:GetFieldID()
tc:RegisterFlagEffect(id,RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END,0,1,fid)

if tc:GetFlagEffectLabel(id)==fid then
    -- tc is still the same marked card for this effect.
end
```

`GetFlagEffectLabel` returns `nil` when no matching flag exists. If multiple
flags with the same code exist, it returns multiple Lua values, one label per
flag. A matching flag with no label contributes `0`.

`SetFlagEffectLabel` updates the first matching flag and returns whether one was
found.

## Choosing The Function

| Need | Use |
| --- | --- |
| Mark that a player used an option this turn | [`Duel.RegisterFlagEffect`](/api/functions/Duel/RegisterFlagEffect) |
| Check whether a player marker exists | [`Duel.GetFlagEffect`](/api/functions/Duel/GetFlagEffect) |
| Clear a player marker manually | [`Duel.ResetFlagEffect`](/api/functions/Duel/ResetFlagEffect) |
| Mark one specific card | [`Card.RegisterFlagEffect`](/api/functions/Card/RegisterFlagEffect) |
| Check whether one card has a marker | [`Card.GetFlagEffect`](/api/functions/Card/GetFlagEffect) |
| Store a field ID, turn count, or bit mask | `RegisterFlagEffect(..., label)` plus [`GetFlagEffectLabel`](/api/functions/Card/GetFlagEffectLabel) |
| Update an existing marker's data | [`Card.SetFlagEffectLabel`](/api/functions/Card/SetFlagEffectLabel) or [`Duel.SetFlagEffectLabel`](/api/functions/Duel/SetFlagEffectLabel) |

## Common Mistakes

Do not use a card flag when the marker belongs to the player. Dragon Master
Magia spends a player option, so it uses `Duel.GetFlagEffect(tp, code)`, not
`c:GetFlagEffect(code)`.

Do not forget the reset. A missing or too-broad reset can leave the marker
longer than the card text intends. For "until the end of this turn", use
`RESET_PHASE+PHASE_END`. For a card-attached marker, include the event reset when
the marker should disappear if the card leaves or changes state.

Do not confuse flag effects with `Effect.SetCountLimit`. Count limits are the
normal way to limit an effect's activation/use count. Flag effects are for
custom memory that the built-in count-limit system does not directly express,
such as separate once-per-turn choices for Monster, Spell, and Trap effects.
