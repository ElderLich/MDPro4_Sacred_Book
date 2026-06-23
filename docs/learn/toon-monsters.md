# Toon Monsters

Toon Monsters are more script-pattern driven than Gemini, Union, or Spirit
Monsters. Local MDPro3/YGOPro sources define `TYPE_TOON`, but local helper files
do not provide a shared `aux.EnableToonAttribute` package. Each Toon card
scripts the pieces its own text needs.

That means a Toon guide should start from the recurring patterns, not from a
single magic helper.

## The Local Pieces

| Job | Common local pattern |
| --- | --- |
| Identify a Toon Monster | [`Card.IsType`](/api/functions/Card/IsType) with `TYPE_TOON`. |
| List Toon World | [`aux.AddCodeList`](/api/functions/Auxiliary/AddCodeList) with card code `15259703`. |
| Check Toon World-like cards | Face-up `IsCode(15259703)`, often helped by cards that change code to Toon World. |
| Built-in Special Summon | `EFFECT_SPSUMMON_PROC` from the hand. |
| Direct attack | `EFFECT_DIRECT_ATTACK` with a condition. |
| Cannot attack this turn | Temporary `EFFECT_CANNOT_ATTACK` reset at the End Phase. |
| Add Toon type by effect | `EFFECT_ADD_TYPE` with `TYPE_TOON`. |

`TYPE_TOON` is a card type bit, not an archetype set code. Toon support often
also uses set checks such as `IsSetCard(0x62)`, but that answers a different
question.

## Checking For Toon World

Many Toon monsters list Toon World in their text:

```lua
function s.initial_effect(c)
    aux.AddCodeList(c,15259703)
end
```

They then check whether a face-up Toon World is on the field:

```lua
function s.toonworld_filter(c)
    return c:IsFaceup() and c:IsCode(15259703)
end

function s.has_toonworld(tp)
    return Duel.IsExistingMatchingCard(s.toonworld_filter,tp,LOCATION_ONFIELD,0,1,nil)
end
```

Toon Kingdom (`c43175858.lua`) is important because it uses
[`aux.EnableChangeCode`](/api/functions/Auxiliary/EnableChangeCode) to become
code `15259703` in the Field Zone. Scripts that check `IsCode(15259703)` can
therefore see Toon Kingdom as Toon World while that code-change effect applies.

## Built-In Toon Special Summons

Older Toon monsters often use a hand Special Summon procedure that requires
Toon World and Tributes. Blue-Eyes Toon Dragon (`c53183600.lua`) and Toon
Dragon Egger (`c38369349.lua`) use this shape:

```lua
local e1=Effect.CreateEffect(c)
e1:SetType(EFFECT_TYPE_FIELD)
e1:SetCode(EFFECT_SPSUMMON_PROC)
e1:SetProperty(EFFECT_FLAG_CANNOT_DISABLE+EFFECT_FLAG_UNCOPYABLE)
e1:SetRange(LOCATION_HAND)
e1:SetCondition(s.spcon)
e1:SetTarget(s.sptg)
e1:SetOperation(s.spop)
c:RegisterEffect(e1)
```

The condition checks for a face-up Toon World and a legal release group:

```lua
function s.spcon(e,c)
    if c==nil then return true end
    local tp=c:GetControler()
    local rg=Duel.GetReleaseGroup(tp,false,REASON_SPSUMMON)
    return s.has_toonworld(tp)
        and rg:CheckSubGroup(aux.mzctcheckrel,2,2,tp,REASON_SPSUMMON)
end
```

The target selects the Tributes, keeps the group alive on the procedure effect,
and the operation releases it with `REASON_SPSUMMON`.

Modern Toon cards may use a different procedure. Toon Black Luster Soldier
(`c28711704.lua`) releases Toon Monsters whose Levels add up to at least 8:

```lua
function s.release_filter(c,tp)
    return (c:IsControler(tp) or c:IsFaceup())
        and c:IsType(TYPE_TOON)
        and c:IsLevelAbove(1)
end

function s.group_check(g,tp)
    Duel.SetSelectedCard(g)
    return g:CheckWithSumGreater(Card.GetLevel,8)
        and Duel.GetMZoneCount(tp,g)>0
        and Duel.CheckReleaseGroupEx(tp,aux.IsInGroup,#g,REASON_SPSUMMON,true,nil,g)
end
```

Use this as a lesson in shape, not as a universal Toon rule. Toon monsters do
not all share one Special Summon procedure.

## Direct Attacks And Opposing Toons

The classic direct attack pattern has two parts:

1. If Toon World exists and the opponent controls no Toon Monsters, this card
   can attack directly.
2. If the opponent does control a Toon Monster, this card cannot choose
   non-Toon monsters as battle targets and cannot attack directly.

Local scripts express that with `TYPE_TOON` filters:

```lua
function s.opponent_toon(c)
    return c:IsFaceup() and c:IsType(TYPE_TOON)
end

function s.dircon(e)
    local tp=e:GetHandlerPlayer()
    return s.has_toonworld(tp)
        and not Duel.IsExistingMatchingCard(s.opponent_toon,tp,0,LOCATION_MZONE,1,nil)
end

function s.atcon(e)
    local tp=e:GetHandlerPlayer()
    return Duel.IsExistingMatchingCard(s.opponent_toon,tp,0,LOCATION_MZONE,1,nil)
end

function s.atlimit(e,c)
    return not c:IsType(TYPE_TOON) or c:IsFacedown()
end
```

Blue-Eyes Toon Dragon and Toon Dragon Egger both use this structure. Toon Black
Luster Soldier uses the direct-attack half, but its other effects have their
own conditions and costs.

## Cannot Attack This Turn

Several Toon monsters cannot attack the turn they are Summoned. The local
pattern is a continuous event watcher that registers a temporary single-card
restriction:

```lua
function s.atklimit(e,tp,eg,ep,ev,re,r,rp)
    local c=e:GetHandler()
    local e1=Effect.CreateEffect(c)
    e1:SetType(EFFECT_TYPE_SINGLE)
    e1:SetCode(EFFECT_CANNOT_ATTACK)
    e1:SetReset(RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END)
    c:RegisterEffect(e1)
end
```

Register it for every Summon event that the card text mentions:

```lua
e1:SetCode(EVENT_SUMMON_SUCCESS)
local e2=e1:Clone()
e2:SetCode(EVENT_FLIP_SUMMON_SUCCESS)
local e3=e1:Clone()
e3:SetCode(EVENT_SPSUMMON_SUCCESS)
```

Toon Dark Magician (`c21296502.lua`) uses all three events.

## Effects That Depend On Toon World

Do not only check Toon World when activating an effect if the effect also needs
it at resolution or for a continuous bonus. Put the check in the same place as
the text demands.

Toon Black Luster Soldier requires a face-up Toon World for its banish effect
and then prevents itself from attacking for the rest of the turn as the cost:

```lua
function s.rmcon(e,tp,eg,ep,ev,re,r,rp)
    return s.has_toonworld(tp)
end

function s.rmcost(e,tp,eg,ep,ev,re,r,rp,chk)
    local c=e:GetHandler()
    if chk==0 then return c:GetAttackAnnouncedCount()==0 end
    local e1=Effect.CreateEffect(c)
    e1:SetType(EFFECT_TYPE_SINGLE)
    e1:SetProperty(EFFECT_FLAG_CANNOT_DISABLE+EFFECT_FLAG_OATH)
    e1:SetCode(EFFECT_CANNOT_ATTACK)
    e1:SetReset(RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END)
    c:RegisterEffect(e1,true)
end
```

This is a good model for "you cannot attack the turn you activate this effect"
text. It checks attack history with
[`Card.GetAttackAnnouncedCount`](/api/functions/Card/GetAttackAnnouncedCount),
then registers the restriction as cost.

## Toon Support Cards

Toon support often reads or grants `TYPE_TOON`:

```lua
local e1=Effect.CreateEffect(c)
e1:SetType(EFFECT_TYPE_FIELD)
e1:SetCode(EFFECT_CANNOT_BE_EFFECT_TARGET)
e1:SetRange(LOCATION_FZONE)
e1:SetTargetRange(LOCATION_MZONE,0)
e1:SetTarget(aux.TargetBoolFunction(Card.IsType,TYPE_TOON))
e1:SetValue(aux.tgoval)
c:RegisterEffect(e1)
```

Toon Kingdom uses that kind of target filter to protect your Toon Monsters.

Comic Hand (`c33453260.lua`) goes the other direction: while equipped, it grants
the equipped monster Toon type:

```lua
local e1=Effect.CreateEffect(c)
e1:SetType(EFFECT_TYPE_EQUIP)
e1:SetCode(EFFECT_ADD_TYPE)
e1:SetValue(TYPE_TOON)
c:RegisterEffect(e1)
```

If your support card needs to search "Toon" Spell/Trap Cards, prefer the local
set-code patterns used by the actual scripts when the card text names the Toon
archetype. Use `TYPE_TOON` when the text really asks for Toon Monsters.

## Common Mistakes

| Mistake | Better pattern |
| --- | --- |
| Looking for a shared `EnableToonAttribute` helper. | Script the exact Toon World, attack, Special Summon, and support pieces the card text needs. |
| Treating `TYPE_TOON` as a set code. | Use `c:IsType(TYPE_TOON)` for Toon Monsters and `c:IsSetCard(0x62)` for Toon archetype checks when local examples do that. |
| Forgetting Toon Kingdom's code change. | Check for face-up code `15259703`, not only the original card named Toon World. |
| Copying an old Toon attack pattern onto every Toon card. | Match the individual card text; modern Toons often differ. |
| Checking Toon World only once. | Continuous effects and resolution-sensitive effects should check it where the behavior applies. |

The safe Toon workflow is: identify the exact text hooks, find a local Toon
script with the same shape, then combine only the pieces that card actually
needs.
