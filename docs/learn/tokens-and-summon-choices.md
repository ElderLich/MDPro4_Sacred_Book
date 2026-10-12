# Tokens And Summon Choices

Creating a Token has three separate parts: a database record supplies its
identity and printed stats, the script checks whether the Summon is legal,
and a Summon operation puts the new card on the field. Player choices belong
inside those legal limits.

Before this lesson, read [card data and script wiring](/learn/card-data-and-script-wiring)
and [activation legality](/learn/activation-legality). For monsters with their
own Summon procedures, continue to [Special Summon-only monsters](/learn/special-summon-only-monsters).

## One Token: A Complete Effect

This teaching Normal Spell says: **Special Summon 1 "Phantom Token"
(Fiend/DARK/Level 1/ATK 500/DEF 500).** It borrows the existing Token record
`1426715` used by Number 48: Shadow Lich; it does not recreate that Xyz
Monster's other effects or costs. Give the teaching Spell its own unused ID
and matching `c<ID>.lua` file. The Token's record must also be in the loaded
database.

```lua
local s,id=GetID()
local TOKEN_CODE=1426715

function s.initial_effect(c)
    local e1=Effect.CreateEffect(c)
    e1:SetCategory(CATEGORY_SPECIAL_SUMMON+CATEGORY_TOKEN)
    e1:SetType(EFFECT_TYPE_ACTIVATE)
    e1:SetCode(EVENT_FREE_CHAIN)
    e1:SetTarget(s.target)
    e1:SetOperation(s.activate)
    c:RegisterEffect(e1)
end

function s.cansummon(tp,pos)
    return Duel.GetLocationCount(tp,LOCATION_MZONE)>0
        and Duel.IsPlayerCanSpecialSummonMonster(tp,TOKEN_CODE,0,
            TYPES_TOKEN_MONSTER,500,500,1,RACE_FIEND,ATTRIBUTE_DARK,pos)
end

function s.target(e,tp,eg,ep,ev,re,r,rp,chk)
    if chk==0 then return s.cansummon(tp,POS_FACEUP) end
    Duel.SetOperationInfo(0,CATEGORY_TOKEN,nil,1,0,0)
    Duel.SetOperationInfo(0,CATEGORY_SPECIAL_SUMMON,nil,1,tp,0)
end

function s.activate(e,tp,eg,ep,ev,re,r,rp)
    if not s.cansummon(tp,POS_FACEUP) then return end
    local token=Duel.CreateToken(tp,TOKEN_CODE)
    Duel.SpecialSummon(token,0,tp,tp,false,false,POS_FACEUP)
end
```

The same space and permission checks run at activation and resolution. A
chained effect may fill the available zone or impose a Summon restriction.
Neither `SetOperationInfo` nor a successful activation check reserves space.

[`Duel.CreateToken`](/api/functions/Duel/CreateToken) returns a Card with no
field location yet. It reads the database entry for `TOKEN_CODE`; it does not
use the stat arguments from the earlier permission check. In
[`Duel.IsPlayerCanSpecialSummonMonster`](/api/functions/Duel/IsPlayerCanSpecialSummonMonster),
those arguments describe the prospective monster for the check. Keep them
consistent with the database, and use `TYPES_TOKEN_MONSTER` for the complete
Monster/Normal/Token type combination.

The two `tp` arguments in `SpecialSummon` mean **the summoning player** and
**the player receiving the monster**. They happen to be the same here. The
two `false` arguments retain the normal Summon checks. Do not turn them on
to bypass a failed legality test.

## Let The Player Choose A Legal Position

`POS_FACEUP` permits both face-up Attack and Defense Position. The normal
Summon processor handles the position choice when there is a choice. Use
`POS_FACEUP_DEFENSE` instead if the card text requires Defense Position.

When an effect needs an explicit position choice before a later action,
[`Duel.SelectPosition`](/api/functions/Duel/SelectPosition) takes a **Card**
in this core, not its numeric code. This replacement for `s.activate` shows
how to build a legal mask before asking:

```lua
function s.activate(e,tp,eg,ep,ev,re,r,rp)
    local positions=0
    if s.cansummon(tp,POS_FACEUP_ATTACK) then
        positions=positions+POS_FACEUP_ATTACK
    end
    if s.cansummon(tp,POS_FACEUP_DEFENSE) then
        positions=positions+POS_FACEUP_DEFENSE
    end
    if positions==0 then return end
    local token=Duel.CreateToken(tp,TOKEN_CODE)
    local position=Duel.SelectPosition(tp,token,positions)
    Duel.SpecialSummon(token,0,tp,tp,false,false,position)
end
```

This explicit prompt is usually unnecessary for the first example. It is
useful when the selected position itself affects the rest of the operation.
Keep choices out of the `chk==0` legality branch: that branch may run many
times while the engine is checking available actions.

## "Up To" A Number: Continue Or Stop

Phantom Skyblaster (`12958919`) shows a different player decision: after the
first Token, offer another while the effect still permits one. Its source
limits the count using available zones and the number of monsters controlled
at resolution. It also handles the local restriction on simultaneous
multi-monster Summons represented by effect code `59822133`.

The following is its operation structure with an added check of each
`SpecialSummonStep` result. In the original card's script, the continuation
question uses `aux.Stringid(12958919,2)` (database `str3`). When adapting this
for a custom card, supply the corresponding text under your own ID.

```lua
function s.skyblaster_example(e,tp,eg,ep,ev,re,r,rp)
    local limit=math.min(Duel.GetLocationCount(tp,LOCATION_MZONE),
        Duel.GetFieldGroupCount(tp,LOCATION_MZONE,0))
    if limit<=0 then return end
    if Duel.IsPlayerAffectedByEffect(tp,59822133) then limit=1 end
    if not Duel.IsPlayerCanSpecialSummonMonster(tp,12958920,0x49,
        TYPES_TOKEN_MONSTER,500,500,4,RACE_FIEND,ATTRIBUTE_DARK) then return end
    for i=1,limit do
        local token=Duel.CreateToken(tp,12958920)
        if not Duel.SpecialSummonStep(token,0,tp,tp,false,false,POS_FACEUP) then
            break
        end
        if i==limit or not Duel.SelectYesNo(tp,aux.Stringid(12958919,2)) then
            break
        end
    end
    Duel.SpecialSummonComplete()
end
```

This is an operation to study, not a second effect registered by the complete
Spell above. The optional activation already lets the player decline the
effect; after accepting, this pattern starts with one Token and asks whether
to continue. A different card text may permit zero or require an exact
number, so choose the minimum deliberately. The Skyblaster-specific monster
count and effect-code check are not a universal Summon-legality helper.

[`Duel.SpecialSummonStep`](/api/functions/Duel/SpecialSummonStep) returns a
**boolean**. Test it with `if not ...`; `false~=0` is true in Lua, so a numeric
comparison is wrong. [`Duel.SpecialSummonComplete`](/api/functions/Duel/SpecialSummonComplete)
finishes the batch and raises the final Summon events. Every path after a
successful step must reach it. `break` above exits the loop but still reaches
completion; a `return` there would leave an unfinished batch.

For a simultaneous group Summon, do not call `SpecialSummonComplete` after
every Token. Scapegoat (`73915051`) also demonstrates registering each
Token's Tribute restriction between its step and the single final completion.
Its four-Token requirement and turn-wide Summon restrictions are specific to
that card; copying only its loop would not recreate Scapegoat.

## Try These Cases

| Situation | Expected behavior in the one-Token example |
| --- | --- |
| No usable Monster Zone at activation | The Spell cannot be activated. |
| The last zone is filled by a chained effect | Resolution creates no Token. |
| A player restriction prevents this Token's Summon | Both legality checks reject it. |
| Both face-up positions are legal | The Summon allows the player to choose. |
| The Token database row has the wrong stats | Fix the database; changing the permission-check arguments does not change the created Card. |

For the batch example, also test stopping after one, accepting every offered
Token, one available zone, and a failed step. Check that the batch completes
once and that the script never asks for a Token beyond its legal count.

## Sources And Next Steps

The contracts above follow the local core's `duel_create_token`,
`duel_is_player_can_spsummon_monster`, `duel_select_position`, and the three
Special Summon bindings in `libduel.cpp`.

- [Number 48: Shadow Lich source](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c1426714.lua): one Token, checked at both stages.
- [Phantom Skyblaster source](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c12958919.lua): bounded continuation choices and a single completion.
- [Scapegoat source](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c73915051.lua): exact-count batch and per-Token restrictions.
- [Client UI and prompt behavior](/learn/client-ui-and-prompt-behavior): descriptions, hints, and choices.
- [Player restrictions](/learn/player-restrictions): restrictions beyond available zones.
