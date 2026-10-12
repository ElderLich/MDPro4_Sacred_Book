# Battle Participants And Timing

Battle scripts need to answer two questions separately: **which monster is
battling**, and **whether that same monster still belongs to this battle
when the effect resolves**. An attack target is also different from a card
target selected for an effect.

Read [chain timing and activation windows](/learn/chain-timing-and-activation-windows)
for effect registration, and [battle position effects](/learn/battle-position-effects)
for turning monsters face-up or face-down. This lesson focuses on combatants
and their identity through a resolving Chain.

## Choose The Getter That Answers Your Question

| Function | Result | Check before using it |
| --- | --- | --- |
| [`Duel.GetAttacker`](/api/functions/Duel/GetAttacker) | The current attacking Card, or `nil` | A battle context must exist; the attacker does not necessarily belong to `tp`. |
| [`Duel.GetAttackTarget`](/api/functions/Duel/GetAttackTarget) | The defending Card, or `nil` | Direct attacks have no defending monster. |
| [`Card.GetBattleTarget`](/api/functions/Card/GetBattleTarget) | That Card's opponent in the current battle | The Card must be a participant; a direct attacker has no opposing Card. |
| [`Duel.GetBattleMonster`](/api/functions/Duel/GetBattleMonster) | Two Cards ordered relative to the supplied player's current control | The first result is not always the attacker; either result can be `nil`. |

This fragment finds a battle opponent only when your effect's handler is the
attacker:

```lua
local c=e:GetHandler()
local attacker=Duel.GetAttacker()
local defender=Duel.GetAttackTarget()
if attacker~=c or not defender then return end
-- This is c attacking a monster, rather than a direct attack.
```

For "if this card battles a monster", use `c:GetBattleTarget()` instead:
the handler can be the attacker or defender. Always check the result before
calling a Card method on it.

`GetBattleTarget` does not return a target selected by `Duel.SelectTarget`.
Likewise, `Duel.GetFirstTarget` does not automatically return the opposing
battle monster. The `SetTarget` callback is the effect's activation-check
stage; merely having that callback does not make an effect target cards.
See [targeting flow](/learn/targeting-flow) for actual card-target registration.

## Pick The Correct Battle Event

The local core's `processor.cpp` raises these events at different stages:

| Event | Stage | Practical consequence |
| --- | --- | --- |
| `EVENT_ATTACK_ANNOUNCE` | Attack declaration in the Battle Step | A direct attack has no defender, and later effects may prevent the battle from proceeding. |
| `EVENT_BATTLE_START` | Start of the Damage Step | An attacked face-down monster has not yet been turned face-up by the battle process. |
| `EVENT_BATTLE_CONFIRM` | After the battle process turns a face-down defender face-up | The defender's revealed characteristics can now be used. |
| `EVENT_PRE_DAMAGE_CALCULATE` | Damage-calculation timing, before the final calculation proceeds | Used by the local scripts for effects applying during this damage calculation. |

An event code determines when a Trigger Effect is checked. `SetHintTiming`
does not substitute for the event code or make a Quick Effect legal in every
Damage Step window. Match the exact wording and the local implementation of
a comparable card.

## A Complete Battle Modifier

This teaching Effect Monster says:

> During damage calculation, if this card battles a face-up monster: You can
> make that monster lose 500 ATK during this damage calculation only.

Give the monster its own database row and script ID. Put a description such
as "Reduce the battling monster's ATK by 500?" in `str1`. This is a custom
example based on the event and reset used by Performapal Odd-Eyes Minotaur;
it does not copy that card's Pendulum or archetype conditions.

```lua
local s,id=GetID()

function s.initial_effect(c)
    local e1=Effect.CreateEffect(c)
    e1:SetDescription(aux.Stringid(id,0))
    e1:SetCategory(CATEGORY_ATKCHANGE)
    e1:SetType(EFFECT_TYPE_SINGLE+EFFECT_TYPE_TRIGGER_O)
    e1:SetCode(EVENT_PRE_DAMAGE_CALCULATE)
    e1:SetCondition(s.condition)
    e1:SetTarget(s.target)
    e1:SetOperation(s.operation)
    c:RegisterEffect(e1)
end

function s.condition(e,tp,eg,ep,ev,re,r,rp)
    local opponent=e:GetHandler():GetBattleTarget()
    return opponent and opponent:IsFaceup()
end

function s.target(e,tp,eg,ep,ev,re,r,rp,chk)
    local opponent=e:GetHandler():GetBattleTarget()
    if chk==0 then return opponent and opponent:IsFaceup() end
    e:SetLabelObject(opponent)
end

function s.operation(e,tp,eg,ep,ev,re,r,rp)
    local c=e:GetHandler()
    local opponent=e:GetLabelObject()
    if not opponent or not c:IsRelateToBattle()
        or not opponent:IsRelateToBattle() or not opponent:IsFaceup()
        or not opponent:IsLocation(LOCATION_MZONE) then return end
    local modifier=Effect.CreateEffect(c)
    modifier:SetType(EFFECT_TYPE_SINGLE)
    modifier:SetCode(EFFECT_UPDATE_ATTACK)
    modifier:SetValue(-500)
    modifier:SetReset(RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_DAMAGE_CAL)
    opponent:RegisterEffect(modifier)
end
```

The optional Trigger Effect supplies the activation choice. A second
`SelectYesNo` inside the operation would ask for the same decision again.
The operation applies the accepted effect if its requirements still hold.

`SetLabelObject` remembers which opposing monster the effect refers to.
It does not register that monster as an effect target, and this example has
no `EFFECT_FLAG_CARD_TARGET`. The Card is an existing engine object, so the
Group `KeepAlive`/`DeleteGroup` pattern does not apply to this stored Card.

The modifier resets at the end of `PHASE_DAMAGE_CAL`, as well as on its
standard reset events. That is shorter than "until the end of the Damage
Step" or "until the end of the turn". Changing the duration in the text
requires changing the reset too; see [reset flags and duration](/learn/reset-flags-and-duration).

## Identity Checks Are Different From State Checks

[`Card.IsRelateToBattle`](/api/functions/Card/IsRelateToBattle) compares the
Card's field identity with the battle participants recorded by the core.
A stored Card reference alone is insufficient: if a monster leaves the
field and returns, the Card object can still exist but no longer represent
the participant from this battle.

Keep three kinds of checks distinct:

- **Battle identity:** `IsRelateToBattle` is appropriate for this example's
  Damage Step resolution. It is not a general test for any remembered Card
  at any event or during a later turn.
- **Effect identity:** `IsRelateToEffect(e)` checks a relationship to the
  resolving effect. Use it where that effect's target/handler semantics
  require it; it does not replace battle identity.
- **Current state:** location, face-up status, controller, race, and other
  conditions must be checked when the resolving effect requires them.
  Battle identity does not establish all those properties.

The core refreshes the defender's recorded identity after the normal battle
flip. That flip is part of the ongoing battle, rather than leaving and
re-entering the field. This is one reason to use the battle API instead of
inventing a comparison based only on code or position.

War Rock Meteoragon (`10497636`) stores its opponent with `SetLabelObject`
and later checks battle relation, face-up status, and opposing control before
disabling it. Performapal Odd-Eyes Minotaur (`10731333`) obtains the current
battle opponent at its damage-calculation event and checks relation before
applying its ATK modifier. Which details must be saved depends on what the
effect refers to and when it resolves.

## Battle Destruction Is A Different Case

Do not add `IsRelateToBattle` to every card mentioned by a battle-related
effect. A monster destroyed by battle may already be in the GY when the
follow-up is meant to use it.

Digital Bug Scaradiator (`12615446`) illustrates the distinction at
`EVENT_BATTLE_DESTROYING`: its handler checks its battle relation, while the
destroyed monster is checked for its GY location and battle reason before
being used as Xyz Material. The operation also checks its relationship to
the resolving effect. A blanket "both Cards must still be on the field"
guard would prevent the intended effect.

## Try These Cases

| Situation | Expected behavior for the complete example |
| --- | --- |
| The handler attacks a monster | Its opposing monster can receive the modifier. |
| The handler is attacked | Its attacker can receive the modifier. |
| The handler attacks directly | No opposing monster means no activation for this effect. |
| The defender started face-down | It is checked after the normal battle flip, at this effect's damage-calculation event. |
| A participant leaves and returns before resolution | The old battle relationship fails; do not modify the returned Card. |
| The opponent is no longer face-up in a Monster Zone | Do not apply this example's modifier. |
| Damage calculation ends | The temporary modifier expires. |

When adapting the example, also test an opponent immune to the effect and
effects that change who controls a participant. Whether a control change
matters to your resolution depends on the wording; add an explicit
controller check when the text requires one.

## Sources And Next Steps

The participant getters are implemented in `libduel.cpp` and `libcard.cpp`;
`card_is_relate_to_battle` compares `fieldid_r` with `core.pre_field`. The
battle processor establishes and updates those identities around the Damage
Step events described above.

- [Performapal Odd-Eyes Minotaur source](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c10731333.lua): damage-calculation ATK change and duration.
- [War Rock Meteoragon source](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c10497636.lua): remember and recheck the battling opponent.
- [Salamangreat of Fire source](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c11962031.lua): find the player's combatant from either side of an attack.
- [Digital Bug Scaradiator source](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c12615446.lua): a battle-destroyed monster after it reaches the GY.
- [Continuous stat modifiers](/learn/continuous-stat-modifiers): other ways of applying ATK and DEF changes.
