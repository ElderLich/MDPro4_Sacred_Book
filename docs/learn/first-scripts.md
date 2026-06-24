# First Scripts To Study

This page gives new scripters a concrete path through real local scripts. Read
them in order. Each one adds one new idea without asking you to understand the
whole scripting ecosystem at once.

The examples are from the local `Scripts/` set, then rewritten here as teaching
patterns. When a line feels mysterious, follow its API link instead of guessing.

## 1. A Normal Spell That Draws

Pot of Greed (`c55144522.lua`) is a clean first activated effect:

```lua
local e1=Effect.CreateEffect(c)
e1:SetCategory(CATEGORY_DRAW)
e1:SetType(EFFECT_TYPE_ACTIVATE)
e1:SetProperty(EFFECT_FLAG_PLAYER_TARGET)
e1:SetCode(EVENT_FREE_CHAIN)
e1:SetTarget(s.target)
e1:SetOperation(s.activate)
c:RegisterEffect(e1)
```

The target function checks whether the player can draw, then stores the target
player and the draw amount on the Chain Link:

```lua
function s.target(e,tp,eg,ep,ev,re,r,rp,chk)
    if chk==0 then return Duel.IsPlayerCanDraw(tp,2) end
    Duel.SetTargetPlayer(tp)
    Duel.SetTargetParam(2)
    Duel.SetOperationInfo(0,CATEGORY_DRAW,nil,0,tp,2)
end
```

The operation reads that Chain data back and performs the draw:

```lua
function s.activate(e,tp,eg,ep,ev,re,r,rp)
    local p,d=Duel.GetChainInfo(0,CHAININFO_TARGET_PLAYER,CHAININFO_TARGET_PARAM)
    Duel.Draw(p,d,REASON_EFFECT)
end
```

Learn from this script:

| Line | Why it matters |
| --- | --- |
| `SetType(EFFECT_TYPE_ACTIVATE)` | This is a Spell/Trap Card activation. |
| `SetProperty(EFFECT_FLAG_PLAYER_TARGET)` | The effect stores player target data, not card targets. |
| `chk==0` | Activation is legal only if the draw can happen. |
| `SetOperationInfo` | Other effects can see that this Chain Link expects to draw. |

Related API:
[`Effect.CreateEffect`](/api/functions/Effect/CreateEffect),
[`Effect.SetType`](/api/functions/Effect/SetType),
[`Effect.SetTarget`](/api/functions/Effect/SetTarget),
[`Duel.SetTargetPlayer`](/api/functions/Duel/SetTargetPlayer),
[`Duel.SetTargetParam`](/api/functions/Duel/SetTargetParam),
[`Duel.GetChainInfo`](/api/functions/Duel/GetChainInfo),
[`Duel.Draw`](/api/functions/Duel/Draw).

## 2. A Spell That Targets And Destroys

Mystical Space Typhoon (`c5318639.lua`) adds official card targeting. The
effect must mark itself with `EFFECT_FLAG_CARD_TARGET`:

```lua
e1:SetCategory(CATEGORY_DESTROY)
e1:SetType(EFFECT_TYPE_ACTIVATE)
e1:SetCode(EVENT_FREE_CHAIN)
e1:SetHintTiming(0,TIMING_END_PHASE+TIMING_EQUIP)
e1:SetProperty(EFFECT_FLAG_CARD_TARGET)
e1:SetTarget(s.target)
e1:SetOperation(s.activate)
```

The `chkc` branch answers "can this manually chosen card become the target?"
Keep it consistent with the selection call:

```lua
function s.filter(c)
    return c:IsType(TYPE_SPELL+TYPE_TRAP)
end

function s.target(e,tp,eg,ep,ev,re,r,rp,chk,chkc)
    if chkc then
        return chkc:IsOnField() and s.filter(chkc) and chkc~=e:GetHandler()
    end
    if chk==0 then
        return Duel.IsExistingTarget(s.filter,tp,LOCATION_ONFIELD,LOCATION_ONFIELD,1,e:GetHandler())
    end
    Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_DESTROY)
    local g=Duel.SelectTarget(tp,s.filter,tp,LOCATION_ONFIELD,LOCATION_ONFIELD,1,1,e:GetHandler())
    Duel.SetOperationInfo(0,CATEGORY_DESTROY,g,1,0,0)
end
```

Resolution reads the official target and checks relation before acting:

```lua
function s.activate(e,tp,eg,ep,ev,re,r,rp)
    local tc=Duel.GetFirstTarget()
    if tc:IsRelateToEffect(e) then
        Duel.Destroy(tc,REASON_EFFECT)
    end
end
```

Learn from this script:

| Line | Why it matters |
| --- | --- |
| `EFFECT_FLAG_CARD_TARGET` | The selected card becomes an official Chain target. |
| `Duel.IsExistingTarget` | Legality checks that a target exists. |
| `Duel.SelectTarget` | The real activation records the chosen target. |
| `IsRelateToEffect` | The target may have moved before resolution. |

Related API:
[`Duel.IsExistingTarget`](/api/functions/Duel/IsExistingTarget),
[`Duel.SelectTarget`](/api/functions/Duel/SelectTarget),
[`Duel.GetFirstTarget`](/api/functions/Duel/GetFirstTarget),
[`Card.IsRelateToEffect`](/api/functions/Card/IsRelateToEffect),
[`Duel.Destroy`](/api/functions/Duel/Destroy).

## 3. A Quick-Play Spell With Better Prompts

Book of Moon (`c14087893.lua`) uses the same targeting shape, but adds stronger
client timing and an extra state recheck:

```lua
e1:SetCategory(CATEGORY_POSITION+CATEGORY_MSET)
e1:SetType(EFFECT_TYPE_ACTIVATE)
e1:SetProperty(EFFECT_FLAG_CARD_TARGET)
e1:SetCode(EVENT_FREE_CHAIN)
e1:SetHintTiming(TIMING_BATTLE_PHASE,TIMINGS_CHECK_MONSTER+TIMING_BATTLE_PHASE)
```

The target filter says exactly what the card can choose:

```lua
function s.filter(c)
    return c:IsFaceup() and c:IsCanTurnSet()
end
```

The operation checks that the target is still related, still in the Monster
Zone, and still face-up:

```lua
local tc=Duel.GetFirstTarget()
if tc:IsRelateToEffect(e) and tc:IsLocation(LOCATION_MZONE) and tc:IsFaceup() then
    Duel.ChangePosition(tc,POS_FACEDOWN_DEFENSE)
end
```

Learn from this script:

| Line | Why it matters |
| --- | --- |
| `SetHintTiming(...)` | The client should offer the effect at useful windows. |
| `IsCanTurnSet` | The legality branch checks the action, not only the card type. |
| `IsLocation` and `IsFaceup` | Some target wording needs state checks at resolution. |

Related API:
[`Effect.SetHintTiming`](/api/functions/Effect/SetHintTiming),
[`Card.IsCanTurnSet`](/api/functions/Card/IsCanTurnSet),
[`Duel.ChangePosition`](/api/functions/Duel/ChangePosition).

## 4. A Continuous Spell With A Field Effect

Banner of Courage (`c10012614.lua`) shows the difference between activating a
Continuous Spell and the continuous effect it applies while face-up:

```lua
local e1=Effect.CreateEffect(c)
e1:SetType(EFFECT_TYPE_ACTIVATE)
e1:SetCode(EVENT_FREE_CHAIN)
c:RegisterEffect(e1)
```

That first effect only activates the card. The ATK modifier is a second effect:

```lua
local e2=Effect.CreateEffect(c)
e2:SetType(EFFECT_TYPE_FIELD)
e2:SetRange(LOCATION_SZONE)
e2:SetTargetRange(LOCATION_MZONE,0)
e2:SetCode(EFFECT_UPDATE_ATTACK)
e2:SetCondition(s.con)
e2:SetValue(200)
c:RegisterEffect(e2)
```

The condition limits the modifier to the controller's Battle Phase:

```lua
function s.con(e)
    local ph=Duel.GetCurrentPhase()
    local tp=Duel.GetTurnPlayer()
    return tp==e:GetHandlerPlayer() and ph>=PHASE_BATTLE_START and ph<=PHASE_BATTLE
end
```

Learn from this script:

| Line | Why it matters |
| --- | --- |
| One activation effect | Continuous Spells still need a normal activation effect. |
| One field effect | The actual modifier is separate and always checked while face-up. |
| `SetRange(LOCATION_SZONE)` | The modifier exists only while the Spell remains in the Spell & Trap Zone. |
| `SetTargetRange(LOCATION_MZONE,0)` | The effect applies to the controller's monsters. |

Related API:
[`Effect.SetRange`](/api/functions/Effect/SetRange),
[`Effect.SetTargetRange`](/api/functions/Effect/SetTargetRange),
[`Effect.SetCondition`](/api/functions/Effect/SetCondition),
[`Effect.SetValue`](/api/functions/Effect/SetValue),
[`Duel.GetCurrentPhase`](/api/functions/Duel/GetCurrentPhase).

## 5. A Stat-Based Non-Targeting Choice

Fissure (`c97169186.lua`) does not target. It destroys the opponent's face-up
monster with the highest DEF. If there is a tie, the player chooses among the
tied cards.

```lua
function s.filter(c)
    return c:IsFaceup() and c:IsDefenseAbove(0)
end
```

The target function announces the likely destroy group without selecting an
official target:

```lua
function s.target(e,tp,eg,ep,ev,re,r,rp,chk)
    if chk==0 then
        return Duel.IsExistingMatchingCard(s.filter,tp,0,LOCATION_MZONE,1,nil)
    end
    local g=Duel.GetMatchingGroup(s.filter,tp,0,LOCATION_MZONE,nil)
    local tg=g:GetMaxGroup(Card.GetDefense)
    Duel.SetOperationInfo(0,CATEGORY_DESTROY,tg,1,0,0)
end
```

The operation recalculates the current highest DEF group at resolution:

```lua
local g=Duel.GetMatchingGroup(s.filter,tp,0,LOCATION_MZONE,nil)
if #g>0 then
    local tg=g:GetMaxGroup(Card.GetDefense)
    if #tg>1 then
        Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_DESTROY)
        local sg=tg:Select(tp,1,1,nil)
        Duel.HintSelection(sg)
        Duel.Destroy(sg,REASON_EFFECT)
    else
        Duel.Destroy(tg,REASON_EFFECT)
    end
end
```

Learn from this script:

| Line | Why it matters |
| --- | --- |
| `IsExistingMatchingCard` | No target is recorded at activation. |
| `GetMatchingGroup` | The script builds the current candidate pool. |
| `GetMaxGroup(Card.GetDefense)` | The local helper finds all cards tied for maximum DEF. |
| `Group.Select` | The player chooses only if several cards tie. |

Related API:
[`Duel.IsExistingMatchingCard`](/api/functions/Duel/IsExistingMatchingCard),
[`Duel.GetMatchingGroup`](/api/functions/Duel/GetMatchingGroup),
[`Group.GetMaxGroup`](/api/functions/Group/GetMaxGroup),
[`Group.GetMinGroup`](/api/functions/Group/GetMinGroup),
[`Group.Select`](/api/functions/Group/Select),
[`Duel.HintSelection`](/api/functions/Duel/HintSelection).

For the full tied-group pattern, custom scores, returned values, and targeting
variants, read [Min/Max Stat Card Selection](min-max-stat-selection).

## What To Read Next

After these five scripts, the core loop should feel familiar:

1. Build and register an effect.
2. Prove activation legality in `chk==0`.
3. Prompt or record what the player chooses.
4. Announce expected operations.
5. Recheck the current game state at resolution.

Continue with:

- [Creation, building, and registration of an effect object](effect-object)
- [Conditions, Costs, Activation Procedures, And Resolution](effect-callbacks)
- [Targeting flow](targeting-flow)
- [Selection And Group Handling](selection-and-group-handling)
- [Common Script Errors And Debugging](common-script-errors-and-debugging)
