# Chain Timing And Activation Windows

Chain timing is the part of a script that decides when an activated effect can
be offered to a player, when it can respond to another Chain Link, and which
checks still have to pass before the activation is legal.

The most important beginner habit is to separate the prompt from the legality.
`SetHintTiming` can help the client ask at useful moments, but it does not make
the effect legal by itself. The real permission still comes from the effect
type, event code, range, condition, cost, and target check.

## Three Layers

Read activated timing in layers:

| Layer | Script pieces | Job |
| --- | --- | --- |
| Broad window | `SetType`, `SetCode`, `SetRange`, `SetProperty` | Describes the kind of activation and the event or open window it belongs to. |
| Prompt timing | `SetHintTiming`, `TIMING_*`, `TIMINGS_CHECK_MONSTER` | Helps the client decide when to offer or highlight optional effects. |
| Legality | `condition`, `cost`, `target`, `chk==0` | Decides whether this activation is actually allowed right now. |

A script usually needs all three. A good prompt with no legal target still
should not activate. A legal Quick Effect with no useful hint timing may still
exist, but it may be less comfortable for the player to find at the right
window.

## Free Chain Windows

Many Spell/Trap activations use `EVENT_FREE_CHAIN`. This means the effect is
not waiting for a specific event such as a monster being destroyed. It can be
offered in open response windows if its type, card type, range, and legality
checks allow it.

Book of Moon (`c14087893.lua`) is the clean local pattern:

```lua
local e1=Effect.CreateEffect(c)
e1:SetCategory(CATEGORY_POSITION+CATEGORY_MSET)
e1:SetType(EFFECT_TYPE_ACTIVATE)
e1:SetProperty(EFFECT_FLAG_CARD_TARGET)
e1:SetCode(EVENT_FREE_CHAIN)
e1:SetHintTiming(TIMING_BATTLE_PHASE,TIMINGS_CHECK_MONSTER+TIMING_BATTLE_PHASE)
e1:SetTarget(c14087893.target)
e1:SetOperation(c14087893.activate)
c:RegisterEffect(e1)
```

The hint timing says when the prompt is useful. The target callback decides
whether there is a legal face-up monster to Set:

```lua
function c14087893.target(e,tp,eg,ep,ev,re,r,rp,chk,chkc)
    if chkc then
        return chkc:IsLocation(LOCATION_MZONE) and c14087893.filter(chkc)
    end
    if chk==0 then
        return Duel.IsExistingTarget(c14087893.filter,tp,LOCATION_MZONE,LOCATION_MZONE,1,nil)
    end
    Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_FACEUP)
    local g=Duel.SelectTarget(tp,c14087893.filter,tp,LOCATION_MZONE,LOCATION_MZONE,1,1,nil)
    Duel.SetOperationInfo(0,CATEGORY_POSITION,g,1,0,0)
end
```

If no matching monster exists, `chk==0` returns false. The client prompt did
not create permission by itself.

## Responding To A Chain Link

Effects that respond to an activated effect usually use `EVENT_CHAINING`.
Their condition receives the Chain Link being answered through the normal
callback arguments. In local scripts, `ev` is commonly passed to
[`Duel.IsChainNegatable`](/api/functions/Duel/IsChainNegatable),
[`Duel.NegateActivation`](/api/functions/Duel/NegateActivation), or other
Chain functions.

Cyber Dragon Infinity (`c10443957.lua`) shows the shape:

```lua
e3:SetCategory(CATEGORY_NEGATE+CATEGORY_DESTROY)
e3:SetType(EFFECT_TYPE_QUICK_O)
e3:SetCode(EVENT_CHAINING)
e3:SetCountLimit(1)
e3:SetProperty(EFFECT_FLAG_DAMAGE_STEP+EFFECT_FLAG_DAMAGE_CAL)
e3:SetRange(LOCATION_MZONE)
e3:SetCondition(c10443957.discon)
e3:SetCost(c10443957.discost)
e3:SetTarget(c10443957.distg)
e3:SetOperation(c10443957.disop)

function c10443957.discon(e,tp,eg,ep,ev,re,r,rp)
    return not e:GetHandler():IsStatus(STATUS_BATTLE_DESTROYED)
        and Duel.IsChainNegatable(ev)
end
```

This is a response effect, so `EVENT_CHAINING` is the event. The condition also
checks that the handler is not already marked as battle-destroyed.

MDPro4/YGOPro source note: the current local binding for
`Duel.IsChainNegatable` returns true for any chain count. Local scripts still
call it because it documents the intended pattern and keeps compatibility with
scripts that expect a chain-negatable check. Do not treat that one call as a
complete condition. Keep real card-specific checks around it.

## Spell Speed

The local core derives response speed from the effect type and the handler card
type:

| Script shape | Local speed |
| --- | ---: |
| Trigger effects and Ignition effects | 1 |
| Monster Quick Effects | 2 |
| Quick-Play Spell activation | 2 |
| Other Spell activation | 1 |
| Normal or Continuous Trap activation | 2 |
| Counter Trap activation | 3 |

Use the right shape for the card. A monster "(Quick Effect)" is normally an
`EFFECT_TYPE_QUICK_O` or `EFFECT_TYPE_QUICK_F` effect, not a Counter Trap. A
Counter Trap is still a Trap Card activation with `EFFECT_TYPE_ACTIVATE`; the
Trap card type gives it Spell Speed 3.

## Damage Step And Damage Calculation

Damage Step legality has two pieces:

| Need | Script piece |
| --- | --- |
| Open the broad Damage Step window | `EFFECT_FLAG_DAMAGE_STEP` |
| Open the damage calculation window | `EFFECT_FLAG_DAMAGE_CAL` |
| Decide whether this exact effect should activate there | `condition`, `cost`, `target` checks |

The local core filters most activations in the Damage Step unless the effect
has `EFFECT_FLAG_DAMAGE_STEP`. It filters most activations during damage
calculation unless the effect has `EFFECT_FLAG_DAMAGE_CAL`. These flags open
the broad window; they do not prove the card's text allows every point inside
that window.

Cyber Dragon Infinity uses both flags because its negation effect can be used
through those windows:

```lua
e3:SetProperty(EFFECT_FLAG_DAMAGE_STEP+EFFECT_FLAG_DAMAGE_CAL)
e3:SetCondition(c10443957.discon)
```

For effects that are only safe before damage calculation, local scripts often
pair a Damage Step property with a condition such as
[`aux.dscon`](/api/functions/Auxiliary/dscon). Keep the condition close to the
card text.

## Hint Timing Masks

[`Effect.SetHintTiming`](/api/functions/Effect/SetHintTiming) stores two timing
masks:

```lua
e1:SetHintTiming(s_time)
e1:SetHintTiming(s_time,o_time)
```

The first mask is for the handler controller. The second mask is for the
opponent side. If the second argument is omitted, the local core copies the
first mask to both sides. When prompts are checked, those two masks are
interpreted relative to the handler's current controller.

Common masks include:

| Timing | Typical use |
| --- | --- |
| `TIMING_MAIN_END` | Prompt near the end of a Main Phase. |
| `TIMING_BATTLE_PHASE` | Prompt during Battle Phase windows. |
| `TIMING_DAMAGE_STEP` | Prompt in the Damage Step. |
| `TIMING_DAMAGE_CAL` | Prompt during damage calculation. |
| `TIMING_CHAIN_END` | Prompt after a Chain finishes resolving. |
| `TIMING_END_PHASE` | Prompt near the End Phase. |
| `TIMINGS_CHECK_MONSTER` | Prompt around visible monster checks, defined locally as `0x1c0`. |

[`Duel.CheckTiming`](/api/functions/Duel/CheckTiming) checks whether a timing
mask appears in either player's current core hint timing. It is a low-level
prompt-window helper, not a replacement for activation legality. No indexed
local card script currently calls it directly, so prefer ordinary phase, event,
target, and cost checks unless you are writing a helper that really needs the
current hint mask.

## Opponent-Side Prompts

The two-argument form is useful when a card should mostly prompt the opponent
after they do something. Infinite Impermanence (`c10045474.lua`) uses this:

```lua
local e1=Effect.CreateEffect(c)
e1:SetCategory(CATEGORY_DISABLE)
e1:SetType(EFFECT_TYPE_ACTIVATE)
e1:SetProperty(EFFECT_FLAG_CARD_TARGET)
e1:SetCode(EVENT_FREE_CHAIN)
e1:SetHintTiming(0,TIMINGS_CHECK_MONSTER)
e1:SetTarget(c10045474.target)
e1:SetOperation(c10045474.activate)
c:RegisterEffect(e1)
```

The target callback still checks for a legal opponent monster:

```lua
if chk==0 then
    return Duel.IsExistingTarget(aux.NegateMonsterFilter,tp,0,LOCATION_MZONE,1,nil)
end
```

Its hand activation is not hidden inside hint timing. The script registers a
separate effect with `EFFECT_TRAP_ACT_IN_HAND` and a field-empty condition.
That is a good rule of thumb: use hint timing for prompts, and use separate
effects or conditions for real exceptions.

## Watching Chain Solving

Responding to a Chain Link and watching a Chain Link resolve are different
patterns.

`EVENT_CHAINING` is used before the Chain Link resolves, usually for effects
that negate activations. `EVENT_CHAIN_SOLVING` is used by continuous watcher
effects during Chain resolution.

Infinite Impermanence uses `EVENT_CHAIN_SOLVING` for the temporary column
negation it creates after it resolves:

```lua
local e5=Effect.CreateEffect(c)
e5:SetType(EFFECT_TYPE_FIELD+EFFECT_TYPE_CONTINUOUS)
e5:SetCode(EVENT_CHAIN_SOLVING)
e5:SetOperation(c10045474.disop)
e5:SetReset(RESET_PHASE+PHASE_END)
e5:SetLabel(c:GetSequence())
Duel.RegisterEffect(e5,tp)
```

The operation reads Chain information for the resolving Chain Link:

```lua
local controller,loc,seq=Duel.GetChainInfo(ev,
    CHAININFO_TRIGGERING_CONTROLER,
    CHAININFO_TRIGGERING_LOCATION,
    CHAININFO_TRIGGERING_SEQUENCE)
```

Use [`Duel.GetChainInfo`](/api/functions/Duel/GetChainInfo) when the script
needs data about the specific Chain Link. Do not use a continuous watcher when
the card text is supposed to activate as a response.

## Common Mistakes

| Mistake | Better pattern |
| --- | --- |
| Treating `SetHintTiming` as permission to activate. | Keep legality in type/code/range, condition, cost, and `chk==0` target checks. |
| Using `EVENT_FREE_CHAIN` for an effect that should answer a Chain Link. | Use `EVENT_CHAINING` and inspect `ev`, `re`, `rp`, and related Chain data. |
| Adding Damage Step flags and no Damage Step condition. | Add flags only when needed, then keep the exact timing check in the condition. |
| Forgetting `EFFECT_FLAG_DAMAGE_CAL` for damage calculation text. | Use `EFFECT_FLAG_DAMAGE_STEP+EFFECT_FLAG_DAMAGE_CAL` only when the card is legal there. |
| Treating `Duel.IsChainNegatable` as the whole condition in MDPro4. | Add real checks for handler state, card text, player, type, cost, and target rules. |
| Making a hand-activation exception with hint timing only. | Register the proper exception effect, such as `EFFECT_TRAP_ACT_IN_HAND`, with its own condition. |
| Using `Duel.CheckTiming` instead of a legality check. | Use it only for current hint-mask tests; still check phase, event, action availability, and targets. |

## Useful API Pages

- [`Effect.SetType`](/api/functions/Effect/SetType)
- [`Effect.SetCode`](/api/functions/Effect/SetCode)
- [`Effect.SetRange`](/api/functions/Effect/SetRange)
- [`Effect.SetProperty`](/api/functions/Effect/SetProperty)
- [`Effect.SetHintTiming`](/api/functions/Effect/SetHintTiming)
- [`Duel.CheckTiming`](/api/functions/Duel/CheckTiming)
- [`Duel.GetCurrentPhase`](/api/functions/Duel/GetCurrentPhase)
- [`Duel.IsDamageCalculated`](/api/functions/Duel/IsDamageCalculated)
- [`Duel.IsChainNegatable`](/api/functions/Duel/IsChainNegatable)
- [`Duel.GetChainInfo`](/api/functions/Duel/GetChainInfo)
- [`Duel.NegateActivation`](/api/functions/Duel/NegateActivation)
- [`Duel.NegateEffect`](/api/functions/Duel/NegateEffect)
- [`Duel.SetOperationInfo`](/api/functions/Duel/SetOperationInfo)

Related lessons:

- [Activated Effects](activated-effects)
- [Activation Legality](activation-legality)
- [Categories, Properties, And Hint Timing](categories-properties-and-hints)
- [Client UI And Prompt Behavior](client-ui-and-prompt-behavior)
- [Cost, Target, And Operation Lifecycle](cost-target-operation-lifecycle)
- [Negation and Immunity](negation-and-immunity)
