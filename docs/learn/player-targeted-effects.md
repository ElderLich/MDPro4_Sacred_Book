# Player-Targeted Effects

Some effects do not target a card. They target a player, store an amount, then
use that stored player and amount during resolution. Draw, damage, recovery,
discard, and many "your opponent" effects use this shape.

This is different from selecting card targets with `Duel.SelectTarget`. A
player target is Chain data, not a `Card` or `Group`.

## The Basic Shape

Pot of Greed (`c55144522.lua`) is the cleanest local example:

```lua
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

The target branch stores two values:

| Function | Stored value |
| --- | --- |
| [`Duel.SetTargetPlayer`](/api/functions/Duel/SetTargetPlayer) | The player that the operation will affect. |
| [`Duel.SetTargetParam`](/api/functions/Duel/SetTargetParam) | A single integer parameter, commonly an amount or count. |

The operation reads them with
[`Duel.GetChainInfo`](/api/functions/Duel/GetChainInfo). Request the
`CHAININFO_*` fields in the same order you want them returned.

## Why Store The Values?

Store player and amount data when the operation should resolve with the values
chosen or calculated at activation. That keeps the operation from silently
changing its mind later.

Mask of Darkness's old-style draw cousin, Masked Sorcerer (`c10189126.lua`),
sets the player and draw count when battle damage is inflicted:

```lua
function s.target(e,tp,eg,ep,ev,re,r,rp,chk)
    if chk==0 then return true end
    Duel.SetTargetPlayer(tp)
    Duel.SetTargetParam(1)
    Duel.SetOperationInfo(0,CATEGORY_DRAW,nil,0,tp,1)
end

function s.operation(e,tp,eg,ep,ev,re,r,rp)
    local p,d=Duel.GetChainInfo(0,CHAININFO_TARGET_PLAYER,CHAININFO_TARGET_PARAM)
    Duel.Draw(p,d,REASON_EFFECT)
end
```

The operation does not need to recompute who inflicted damage. It uses the
Chain data that was stored when the trigger was placed on the Chain.

## Player Target Property

Effects that target a player usually set
`EFFECT_FLAG_PLAYER_TARGET`:

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

This is a property flag on the effect. It tells the engine and client that the
effect's target is a player rather than only cards.

Do not use `EFFECT_FLAG_CARD_TARGET` for this unless the effect also selects
card targets. A player target is not a card target.

## Operation Info Still Matters

[`Duel.SetOperationInfo`](/api/functions/Duel/SetOperationInfo) informs the
engine and client what the effect intends to do. For player-targeted draw,
damage, and recovery, the last two fields are usually the target player and
the amount:

```lua
Duel.SetOperationInfo(0,CATEGORY_DRAW,nil,0,tp,2)
Duel.SetOperationInfo(0,CATEGORY_DAMAGE,nil,0,1-tp,1000)
Duel.SetOperationInfo(0,CATEGORY_RECOVER,nil,0,tp,500)
```

The operation info does not store the values for your Lua operation. Use
`SetTargetPlayer` and `SetTargetParam` for that. Operation info is metadata;
Chain target player/parameter are the values your script reads back.

## Damage And Recovery Use The Same Shape

Lava Golem (`c102380.lua`) deals damage to its controller during that player's
Standby Phase:

```lua
function s.damtg(e,tp,eg,ep,ev,re,r,rp,chk)
    if chk==0 then return true end
    Duel.SetTargetPlayer(tp)
    Duel.SetTargetParam(1000)
    Duel.SetOperationInfo(0,CATEGORY_DAMAGE,0,0,tp,1000)
end

function s.damop(e,tp,eg,ep,ev,re,r,rp)
    local p,d=Duel.GetChainInfo(0,CHAININFO_TARGET_PLAYER,CHAININFO_TARGET_PARAM)
    Duel.Damage(p,d,REASON_EFFECT)
end
```

The same pattern appears in recovery effects, except the operation calls
[`Duel.Recover`](/api/functions/Duel/Recover).

## When The Amount Is Dynamic

Sometimes the amount is calculated in the target branch:

```lua
local ct=Duel.GetMatchingGroupCount(s.filter,tp,LOCATION_GRAVE,0,nil)
if chk==0 then return ct>0 and Duel.IsPlayerCanDraw(tp,ct) end
Duel.SetTargetPlayer(tp)
Duel.SetTargetParam(ct)
Duel.SetOperationInfo(0,CATEGORY_DRAW,nil,0,tp,ct)
```

That pattern means "draw the number that was legal and announced at
activation." If the text says to count again at resolution, do not store the
count as the final amount. Store only the player, then recompute the amount in
the operation.

## Changing Stored Player Data

The local core also exposes
[`Duel.ChangeTargetPlayer`](/api/functions/Duel/ChangeTargetPlayer) and
[`Duel.ChangeTargetParam`](/api/functions/Duel/ChangeTargetParam). They edit
already-stored Chain data. Use them only for effects that explicitly change an
existing Chain's target player or parameter.

For a normal new effect, use `SetTargetPlayer` and `SetTargetParam` in that
effect's own target function.

## Common Mistakes

| Mistake | Better pattern |
| --- | --- |
| Selecting no card target but forgetting `EFFECT_FLAG_PLAYER_TARGET`. | Add the player-target property when the effect targets a player. |
| Reading `tp` in the operation instead of stored Chain data. | Use `Duel.GetChainInfo(0,CHAININFO_TARGET_PLAYER,CHAININFO_TARGET_PARAM)`. |
| Assuming `SetOperationInfo` stores Lua operation data. | Use `SetTargetPlayer` and `SetTargetParam` for values you read later. |
| Recomputing an announced amount at resolution by accident. | Store the count with `SetTargetParam` when the amount should be fixed at activation. |
| Using `EFFECT_FLAG_CARD_TARGET` for a player-only effect. | Reserve card-target flags for real card targets selected through targeting APIs. |

The reliable mental model is: target function checks legality, stores player
data, announces operation info; operation reads the stored Chain data and
applies the effect.
