# Beginner Script Ladder

This ladder turns the first lessons into small complete scripts. Read the rungs
in order. Each one adds one new scripting idea and is backed by a local script
from `ygopro-scripts`.

The snippets use modern `local s,id=GetID()` style even when the source script
uses the older `c12345678` table style. The behavior pattern is the same.

| Rung | Local source | New idea |
| --- | --- | --- |
| 1. Draw Spell | `c55144522.lua` | A basic activated effect with player target data. |
| 2. Target and destroy | `c5318639.lua` | Official Chain targets and relation checks. |
| 3. Destroy a current Group | `c53129443.lua` | Non-targeting Group action rebuilt at resolution. |
| 4. Choose by highest stat | `c97169186.lua` | Min/max selection and tied Groups. |
| 5. Continuous stat modifier | `c10012614.lua` | A card activation plus a separate face-up field effect. |
| 6. Mandatory trigger | `c11548522.lua` | `EVENT_*` trigger flow and handler relation checks. |
| 7. Quick-Play prompt | `c14087893.lua` | Hint timing and stronger target-state rechecks. |
| 8. Trap response | `c44095762.lua` | Event-specific Trap activation and opponent-turn condition. |

## 1. Draw Spell

Start with one activated Spell that draws 2 cards.

```lua
local s,id=GetID()

function s.initial_effect(c)
    local e1=Effect.CreateEffect(c)
    e1:SetCategory(CATEGORY_DRAW)
    e1:SetType(EFFECT_TYPE_ACTIVATE)
    e1:SetProperty(EFFECT_FLAG_PLAYER_TARGET)
    e1:SetCode(EVENT_FREE_CHAIN)
    e1:SetTarget(s.target)
    e1:SetOperation(s.activate)
    c:RegisterEffect(e1)
end

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

What this teaches:

| Line | Purpose |
| --- | --- |
| `SetType(EFFECT_TYPE_ACTIVATE)` | This is a Spell/Trap Card activation. |
| `chk==0` | The activation is legal only if the draw can happen. |
| `SetTargetPlayer` and `SetTargetParam` | Store player data on the Chain Link. |
| `GetChainInfo` | Read that data back at resolution. |

## 2. Target And Destroy

Next, target one Spell/Trap on the field and destroy it.

```lua
local s,id=GetID()

function s.initial_effect(c)
    local e1=Effect.CreateEffect(c)
    e1:SetCategory(CATEGORY_DESTROY)
    e1:SetType(EFFECT_TYPE_ACTIVATE)
    e1:SetCode(EVENT_FREE_CHAIN)
    e1:SetHintTiming(0,TIMING_END_PHASE+TIMING_EQUIP)
    e1:SetProperty(EFFECT_FLAG_CARD_TARGET)
    e1:SetTarget(s.target)
    e1:SetOperation(s.activate)
    c:RegisterEffect(e1)
end

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

function s.activate(e,tp,eg,ep,ev,re,r,rp)
    local tc=Duel.GetFirstTarget()
    if tc:IsRelateToEffect(e) then
        Duel.Destroy(tc,REASON_EFFECT)
    end
end
```

What this teaches:

| Line | Purpose |
| --- | --- |
| `EFFECT_FLAG_CARD_TARGET` | The selected card becomes an official Chain target. |
| `chkc` | Manual target rechecks must match the filter. |
| `Duel.SelectTarget` | Records the target on the Chain Link. |
| `IsRelateToEffect` | The target may move before resolution. |

## 3. Destroy A Current Group

Now remove targeting. This effect destroys all monsters currently on the field.

```lua
local s,id=GetID()

function s.initial_effect(c)
    local e1=Effect.CreateEffect(c)
    e1:SetCategory(CATEGORY_DESTROY)
    e1:SetType(EFFECT_TYPE_ACTIVATE)
    e1:SetCode(EVENT_FREE_CHAIN)
    e1:SetTarget(s.target)
    e1:SetOperation(s.activate)
    c:RegisterEffect(e1)
end

function s.target(e,tp,eg,ep,ev,re,r,rp,chk)
    if chk==0 then
        return Duel.IsExistingMatchingCard(aux.TRUE,tp,LOCATION_MZONE,LOCATION_MZONE,1,nil)
    end
    local g=Duel.GetMatchingGroup(aux.TRUE,tp,LOCATION_MZONE,LOCATION_MZONE,nil)
    Duel.SetOperationInfo(0,CATEGORY_DESTROY,g,#g,0,0)
end

function s.activate(e,tp,eg,ep,ev,re,r,rp)
    local g=Duel.GetMatchingGroup(aux.TRUE,tp,LOCATION_MZONE,LOCATION_MZONE,nil)
    Duel.Destroy(g,REASON_EFFECT)
end
```

What this teaches:

| Line | Purpose |
| --- | --- |
| `IsExistingMatchingCard` | Legality checks that there is something to do. |
| `GetMatchingGroup` in target | Announces the current expected Group. |
| `GetMatchingGroup` in operation | Rebuilds the Group from the current field at resolution. |

## 4. Choose By Highest Stat

This effect destroys the opponent's face-up monster with the highest DEF. If
several tie, the player chooses one from the tied Group.

```lua
local s,id=GetID()

function s.initial_effect(c)
    local e1=Effect.CreateEffect(c)
    e1:SetCategory(CATEGORY_DESTROY)
    e1:SetType(EFFECT_TYPE_ACTIVATE)
    e1:SetCode(EVENT_FREE_CHAIN)
    e1:SetTarget(s.target)
    e1:SetOperation(s.activate)
    c:RegisterEffect(e1)
end

function s.filter(c)
    return c:IsFaceup() and c:IsDefenseAbove(0)
end

function s.target(e,tp,eg,ep,ev,re,r,rp,chk)
    if chk==0 then
        return Duel.IsExistingMatchingCard(s.filter,tp,0,LOCATION_MZONE,1,nil)
    end
    local g=Duel.GetMatchingGroup(s.filter,tp,0,LOCATION_MZONE,nil)
    local tg=g:GetMaxGroup(Card.GetDefense)
    Duel.SetOperationInfo(0,CATEGORY_DESTROY,tg,1,0,0)
end

function s.activate(e,tp,eg,ep,ev,re,r,rp)
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
end
```

What this teaches:

| Line | Purpose |
| --- | --- |
| `IsDefenseAbove(0)` | Filters out candidates without usable DEF. |
| `GetMaxGroup(Card.GetDefense)` | Gets every card tied for highest DEF. |
| `Group.Select` | Chooses from the tied Group only when needed. |

Read [Min/Max Stat Card Selection](min-max-stat-selection) after this rung.

## 5. Continuous Stat Modifier

A Continuous Spell often has one effect to activate the card and another effect
for the rule it applies while face-up.

```lua
local s,id=GetID()

function s.initial_effect(c)
    local e1=Effect.CreateEffect(c)
    e1:SetType(EFFECT_TYPE_ACTIVATE)
    e1:SetCode(EVENT_FREE_CHAIN)
    c:RegisterEffect(e1)

    local e2=Effect.CreateEffect(c)
    e2:SetType(EFFECT_TYPE_FIELD)
    e2:SetRange(LOCATION_SZONE)
    e2:SetTargetRange(LOCATION_MZONE,0)
    e2:SetCode(EFFECT_UPDATE_ATTACK)
    e2:SetCondition(s.con)
    e2:SetValue(200)
    c:RegisterEffect(e2)
end

function s.con(e)
    local ph=Duel.GetCurrentPhase()
    local tp=Duel.GetTurnPlayer()
    return tp==e:GetHandlerPlayer() and ph>=PHASE_BATTLE_START and ph<=PHASE_BATTLE
end
```

What this teaches:

| Line | Purpose |
| --- | --- |
| First effect | Activates the card. |
| Second effect | Applies the continuous ATK update. |
| `SetRange(LOCATION_SZONE)` | The modifier exists while this card is face-up in the Spell & Trap Zone. |
| `SetTargetRange(LOCATION_MZONE,0)` | The modifier applies to the controller's monsters. |

## 6. Mandatory Trigger

This trigger activates when the handler is sent to the GY and returns the
handler to the Deck.

```lua
local s,id=GetID()

function s.initial_effect(c)
    local e1=Effect.CreateEffect(c)
    e1:SetDescription(aux.Stringid(id,0))
    e1:SetCategory(CATEGORY_TODECK)
    e1:SetType(EFFECT_TYPE_SINGLE+EFFECT_TYPE_TRIGGER_F)
    e1:SetCode(EVENT_TO_GRAVE)
    e1:SetTarget(s.tdtg)
    e1:SetOperation(s.tdop)
    c:RegisterEffect(e1)
end

function s.tdtg(e,tp,eg,ep,ev,re,r,rp,chk)
    if chk==0 then return true end
    Duel.SetOperationInfo(0,CATEGORY_TODECK,e:GetHandler(),1,0,0)
end

function s.tdop(e,tp,eg,ep,ev,re,r,rp)
    local c=e:GetHandler()
    if c:IsRelateToEffect(e) then
        Duel.SendtoDeck(c,nil,SEQ_DECKSHUFFLE,REASON_EFFECT)
    end
end
```

What this teaches:

| Line | Purpose |
| --- | --- |
| `EFFECT_TYPE_SINGLE+EFFECT_TYPE_TRIGGER_F` | The handler has a mandatory trigger. |
| `EVENT_TO_GRAVE` | The event watched by the trigger. |
| `e:GetHandler()` | The card whose script owns the effect. |
| `IsRelateToEffect` | The handler must still be related to its resolving trigger. |

## 7. Quick-Play Prompt And Recheck

Quick-Play Spells still use `EFFECT_TYPE_ACTIVATE`. The card type and core speed
handling make the activation fast; the script gives the client better prompt
timing and rechecks the target state at resolution.

```lua
local s,id=GetID()

function s.initial_effect(c)
    local e1=Effect.CreateEffect(c)
    e1:SetCategory(CATEGORY_POSITION+CATEGORY_MSET)
    e1:SetType(EFFECT_TYPE_ACTIVATE)
    e1:SetProperty(EFFECT_FLAG_CARD_TARGET)
    e1:SetCode(EVENT_FREE_CHAIN)
    e1:SetHintTiming(TIMING_BATTLE_PHASE,TIMINGS_CHECK_MONSTER+TIMING_BATTLE_PHASE)
    e1:SetTarget(s.target)
    e1:SetOperation(s.activate)
    c:RegisterEffect(e1)
end

function s.filter(c)
    return c:IsFaceup() and c:IsCanTurnSet()
end

function s.target(e,tp,eg,ep,ev,re,r,rp,chk,chkc)
    if chkc then return chkc:IsLocation(LOCATION_MZONE) and s.filter(chkc) end
    if chk==0 then
        return Duel.IsExistingTarget(s.filter,tp,LOCATION_MZONE,LOCATION_MZONE,1,nil)
    end
    Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_FACEUP)
    local g=Duel.SelectTarget(tp,s.filter,tp,LOCATION_MZONE,LOCATION_MZONE,1,1,nil)
    Duel.SetOperationInfo(0,CATEGORY_POSITION,g,1,0,0)
end

function s.activate(e,tp,eg,ep,ev,re,r,rp)
    local tc=Duel.GetFirstTarget()
    if tc:IsRelateToEffect(e) and tc:IsLocation(LOCATION_MZONE) and tc:IsFaceup() then
        Duel.ChangePosition(tc,POS_FACEDOWN_DEFENSE)
    end
end
```

What this teaches:

| Line | Purpose |
| --- | --- |
| `SetHintTiming` | Tells the client when prompts are useful. |
| `IsCanTurnSet` | The target must be able to perform the action. |
| Resolution rechecks | The target must still be related, in the right location, and face-up. |

## 8. Trap Response

This Trap responds to an attack announcement and destroys the opponent's Attack
Position monsters.

```lua
local s,id=GetID()

function s.initial_effect(c)
    local e1=Effect.CreateEffect(c)
    e1:SetCategory(CATEGORY_DESTROY)
    e1:SetType(EFFECT_TYPE_ACTIVATE)
    e1:SetCode(EVENT_ATTACK_ANNOUNCE)
    e1:SetCondition(s.condition)
    e1:SetTarget(s.target)
    e1:SetOperation(s.activate)
    c:RegisterEffect(e1)
end

function s.condition(e,tp,eg,ep,ev,re,r,rp)
    return tp~=Duel.GetTurnPlayer()
end

function s.filter(c)
    return c:IsAttackPos()
end

function s.target(e,tp,eg,ep,ev,re,r,rp,chk)
    if chk==0 then
        return Duel.IsExistingMatchingCard(s.filter,tp,0,LOCATION_MZONE,1,nil)
    end
    local g=Duel.GetMatchingGroup(s.filter,tp,0,LOCATION_MZONE,nil)
    Duel.SetOperationInfo(0,CATEGORY_DESTROY,g,#g,0,0)
end

function s.activate(e,tp,eg,ep,ev,re,r,rp)
    local g=Duel.GetMatchingGroup(s.filter,tp,0,LOCATION_MZONE,nil)
    if #g>0 then
        Duel.Destroy(g,REASON_EFFECT)
    end
end
```

What this teaches:

| Line | Purpose |
| --- | --- |
| `EVENT_ATTACK_ANNOUNCE` | The Trap is not free-chain; it responds to a specific event. |
| `tp~=Duel.GetTurnPlayer()` | The local script only lets the defending player activate it. |
| Rebuilt Group | The operation destroys the current matching monsters at resolution. |

## Move Forward

After the ladder, the main pieces are in your hands:

| If you want to script... | Read next |
| --- | --- |
| Better activation checks | [Activation Legality](activation-legality) |
| More target patterns | [Targeting Flow](targeting-flow) |
| Resolution choices and stored Groups | [Selection And Group Handling](selection-and-group-handling) |
| Client prompts | [Client UI And Prompt Behavior](client-ui-and-prompt-behavior) |
| Continuous rules | [Effects That Apply Continuously](continuous-effects) |
| Spell/Trap variants | [Spell Card Patterns](spell-card-patterns) and [Trap Card Patterns](trap-card-patterns) |
| Debugging mistakes | [Common Script Errors And Debugging](common-script-errors-and-debugging) |

Useful API pages:

- [`Effect.CreateEffect`](/api/functions/Effect/CreateEffect)
- [`Effect.SetType`](/api/functions/Effect/SetType)
- [`Effect.SetCode`](/api/functions/Effect/SetCode)
- [`Effect.SetTarget`](/api/functions/Effect/SetTarget)
- [`Effect.SetOperation`](/api/functions/Effect/SetOperation)
- [`Duel.SetOperationInfo`](/api/functions/Duel/SetOperationInfo)
- [`Duel.SelectTarget`](/api/functions/Duel/SelectTarget)
- [`Duel.SelectMatchingCard`](/api/functions/Duel/SelectMatchingCard)
- [`Duel.GetMatchingGroup`](/api/functions/Duel/GetMatchingGroup)
- [`Card.IsRelateToEffect`](/api/functions/Card/IsRelateToEffect)
- [`Group.GetMaxGroup`](/api/functions/Group/GetMaxGroup)
