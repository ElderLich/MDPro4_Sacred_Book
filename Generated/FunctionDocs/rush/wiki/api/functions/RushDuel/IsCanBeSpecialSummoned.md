# RushDuel.IsCanBeSpecialSummoned

Alias: `RD.IsCanBeSpecialSummoned`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.IsCanBeSpecialSummoned(Card card, Effect effect, int player, int position) -> bool
```

## Description

Calls card:IsCanBeSpecialSummoned(effect,0,player,false,false,position). This is a legality predicate for an ordinary effect Special Summon to that player, with neither summoning conditions nor revive limits bypassed.
It does not check or reserve a free zone. If the destination player differs from the summoning player, use the native Card.IsCanBeSpecialSummoned arguments that match the later operation.

## Parameters

- `card` `Card`: Monster to check.
- `effect` `Effect`: Summoning effect.
- `player` `int`: Summoning player and default destination player.
- `position` `int`: Position mask to match the later summon.

## Returns

- `bool`: Whether the native per-card summon check passes.

## Source

`Rush/Utilities/RDCondition.lua:126`

```lua
function RushDuel.IsCanBeSpecialSummoned(card, effect, player, position)
    return card:IsCanBeSpecialSummoned(effect, 0, player, false, false, position)
end
```
