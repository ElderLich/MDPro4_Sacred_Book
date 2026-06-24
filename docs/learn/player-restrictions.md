# Player Restrictions

Player restrictions are effects that say a player cannot do something: draw,
Summon, enter the Battle Phase, activate certain effects, add cards from the
Deck to the hand, discard as cost, and so on.

Most of these are field effects with `EFFECT_FLAG_PLAYER_TARGET`. Their
`SetTargetRange` values are player flags, not card locations.

## The Basic Player Lock Shape

Lava Golem (`c102380.lua`) prevents its owner from Normal Summoning or Setting
for the rest of the turn after using its Special Summon procedure:

```lua
local e1=Effect.CreateEffect(c)
e1:SetType(EFFECT_TYPE_FIELD)
e1:SetCode(EFFECT_CANNOT_SUMMON)
e1:SetProperty(EFFECT_FLAG_PLAYER_TARGET+EFFECT_FLAG_OATH)
e1:SetReset(RESET_PHASE+PHASE_END)
e1:SetTargetRange(1,0)
Duel.RegisterEffect(e1,tp)

local e2=e1:Clone()
e2:SetCode(EFFECT_CANNOT_MSET)
Duel.RegisterEffect(e2,tp)
```

The key pieces are:

| Piece | Meaning |
| --- | --- |
| `EFFECT_TYPE_FIELD` | The effect applies to the duel state, not only the handler. |
| `EFFECT_FLAG_PLAYER_TARGET` | `SetTargetRange` should be read as affected players. |
| `SetTargetRange(1,0)` | Affect the player who controls/registered the effect. |
| `Duel.RegisterEffect(e,tp)` | Register a temporary player effect for player `tp`. |
| `EFFECT_FLAG_OATH` | The restriction is an oath-style restriction that should not disappear just because the card leaves. |

For player-target field effects, `SetTargetRange(1,0)` means the registering
player, and `SetTargetRange(0,1)` means that player's opponent. This is
different from ordinary card-location field effects, where the values are
location masks such as `LOCATION_MZONE`.

## Temporary Cost Restrictions

Some effects apply a restriction as part of paying a cost. Truth Reinforce
(`c10118318.lua`) says you cannot conduct your Battle Phase the turn you
activate it:

```lua
function s.cost(e,tp,eg,ep,ev,re,r,rp,chk)
    if chk==0 then return Duel.GetActivityCount(tp,ACTIVITY_BATTLE_PHASE)==0 end
    local e1=Effect.CreateEffect(e:GetHandler())
    e1:SetType(EFFECT_TYPE_FIELD)
    e1:SetCode(EFFECT_CANNOT_BP)
    e1:SetProperty(EFFECT_FLAG_PLAYER_TARGET+EFFECT_FLAG_OATH)
    e1:SetTargetRange(1,0)
    e1:SetReset(RESET_PHASE+PHASE_END)
    Duel.RegisterEffect(e1,tp)
end
```

The `chk==0` branch checks whether the player has already performed the
forbidden action. The cost branch registers the restriction for the rest of the
turn.

Use this pattern for "you cannot X the turn you activate this card/effect" text:

1. Check the relevant activity counter in the cost or activation check.
2. Register a temporary oath restriction when the cost is paid.
3. Reset it at the End Phase.

## Continuous Player Restrictions

Some restrictions stay active while the handler remains in its range. Protector
of the Sanctuary (`c24221739.lua`) prevents the opponent from drawing outside
the Draw Phase:

```lua
local e1=Effect.CreateEffect(c)
e1:SetType(EFFECT_TYPE_FIELD)
e1:SetProperty(EFFECT_FLAG_PLAYER_TARGET)
e1:SetCode(EFFECT_CANNOT_DRAW)
e1:SetRange(LOCATION_MZONE)
e1:SetTargetRange(0,1)
e1:SetCondition(s.con)
c:RegisterEffect(e1)

function s.con(e)
    return Duel.GetCurrentPhase()~=PHASE_DRAW
end
```

Because this effect is registered on the monster, it only applies while the
monster is in its `SetRange`. It does not use `Duel.RegisterEffect`, and it
does not need an End Phase reset.

## Activation Restrictions

To stop a player from activating certain effects, use
`EFFECT_CANNOT_ACTIVATE` with a value function:

```lua
local e1=Effect.CreateEffect(c)
e1:SetType(EFFECT_TYPE_FIELD)
e1:SetProperty(EFFECT_FLAG_PLAYER_TARGET)
e1:SetCode(EFFECT_CANNOT_ACTIVATE)
e1:SetRange(LOCATION_MZONE)
e1:SetTargetRange(0,1)
e1:SetValue(s.aclimit)
e1:SetCondition(s.actcon)
c:RegisterEffect(e1)

function s.aclimit(e,re,tp)
    return re:IsHasType(EFFECT_TYPE_ACTIVATE)
end
```

Ancient Gear Beast (`c10509340.lua`) uses this shape while it is attacking. The
value function receives the effect being checked, so it can inspect the
activation type, card type, category, owner, or other effect data.

## Hand And Deck Access Restrictions

Several restrictions use a target function to decide which attempted card
movement is forbidden.

Deck Lockdown (`c1149109.lua`) prevents both players from adding cards from the
Deck to the hand:

```lua
local e1=Effect.CreateEffect(c)
e1:SetType(EFFECT_TYPE_FIELD)
e1:SetCode(EFFECT_CANNOT_TO_HAND)
e1:SetRange(LOCATION_SZONE)
e1:SetProperty(EFFECT_FLAG_PLAYER_TARGET)
e1:SetTargetRange(1,1)
e1:SetTarget(aux.TargetBoolFunction(Card.IsLocation,LOCATION_DECK))
c:RegisterEffect(e1)
```

Greed Goblin (`c425934.lua`) prevents discarding as cost:

```lua
local e1=Effect.CreateEffect(c)
e1:SetType(EFFECT_TYPE_FIELD)
e1:SetProperty(EFFECT_FLAG_PLAYER_TARGET)
e1:SetRange(LOCATION_MZONE)
e1:SetTargetRange(1,1)
e1:SetCode(EFFECT_CANNOT_DISCARD_HAND)
e1:SetTarget(s.target)
e1:SetValue(1)
c:RegisterEffect(e1)

function s.target(e,dc,re,r)
    return r&REASON_COST==REASON_COST
end
```

These target callbacks are not Chain target functions. They are restriction
filters called by the engine while it checks whether an attempted action is
allowed.

## Phase Skips

Skipping a future phase is also a player-targeted field effect. Offerings to
the Doomed (`c19230407.lua`) destroys a monster, then skips your next Draw
Phase:

```lua
local e1=Effect.CreateEffect(e:GetHandler())
e1:SetType(EFFECT_TYPE_FIELD)
e1:SetProperty(EFFECT_FLAG_PLAYER_TARGET)
e1:SetCode(EFFECT_SKIP_DP)
e1:SetTargetRange(1,0)
if Duel.GetTurnPlayer()==tp and Duel.GetCurrentPhase()==PHASE_DRAW then
    e1:SetReset(RESET_PHASE+PHASE_DRAW+RESET_SELF_TURN,2)
else
    e1:SetReset(RESET_PHASE+PHASE_DRAW+RESET_SELF_TURN)
end
Duel.RegisterEffect(e1,tp)
```

The reset is subtle. If the effect is activated during your own Draw Phase, the
script uses a count of `2` so the current Draw Phase does not consume the skip
immediately.

## Common Restriction Codes

| Effect code | Common use |
| --- | --- |
| `EFFECT_CANNOT_DRAW` | A player cannot draw by effect or outside allowed timing. |
| `EFFECT_CANNOT_SUMMON` | A player cannot Normal Summon. |
| `EFFECT_CANNOT_MSET` | A player cannot Set a monster. |
| `EFFECT_CANNOT_SPECIAL_SUMMON` | A player cannot Special Summon matching monsters. |
| `EFFECT_CANNOT_ACTIVATE` | A player cannot activate effects matching the value function. |
| `EFFECT_CANNOT_BP` | A player cannot enter the Battle Phase. |
| `EFFECT_SKIP_DP` | A player's Draw Phase is skipped. |
| `EFFECT_CANNOT_TO_HAND` | Cards matching the target callback cannot be added to the hand. |
| `EFFECT_CANNOT_DISCARD_HAND` | Cards cannot be discarded from the hand under matching reasons. |

Check [Constants](/api/constants) for the local numeric values. The important
scripting question is not the number; it is whether the restriction targets
players, cards, or a specific attempted action.

## Common Mistakes

| Mistake | Better pattern |
| --- | --- |
| Using `SetTargetRange(LOCATION_MZONE,0)` on a player-target restriction. | With `EFFECT_FLAG_PLAYER_TARGET`, use `1,0`, `0,1`, or `1,1`. |
| Registering an oath restriction on the card instead of the player. | Use `Duel.RegisterEffect(e,tp)` for temporary player locks. |
| Forgetting to check past activity before applying a "for the rest of this turn" lock. | Use `Duel.GetActivityCount` in the `chk==0` branch where local scripts do. |
| Treating a restriction `SetTarget` as a Chain target. | Restriction targets are engine filters, not selected Chain targets. |
| Resetting a phase skip too early. | Follow local phase-skip reset patterns when the current phase might match the skipped phase. |

Player restrictions are powerful because they change what the engine allows.
Keep the affected player, duration, and attempted-action filter explicit.
