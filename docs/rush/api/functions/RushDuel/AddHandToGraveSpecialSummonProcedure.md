# RushDuel.AddHandToGraveSpecialSummonProcedure

Alias: `RD.AddHandToGraveSpecialSummonProcedure`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.AddHandToGraveSpecialSummonProcedure(Card card, int desc, function filter, int count, [int|function value], [int position]) -> Effect
```

## Description

Registers a hand Special Summon procedure requiring count matching other cards from hand. The condition checks capacity and candidates; the target step uses cancelable exact-count selection and retains the Group; the operation sends that Group with REASON_SPSUMMON and deletes the retained Group.
The filter must include the intended payment legality. This registers a procedure and returns its Effect; it does not perform an effect Special Summon immediately.

## Parameters

- `card` `Card`: Monster receiving the procedure.
- `desc` `int`: Summon option description identifier.
- `filter` `function`: Hand-card predicate; receives candidate, effect, player. The summoning card is excluded.
- `count` `int`: Exact number of other hand cards to send.
- `value` `int|function` (optional): Optional summon-procedure value.
- `position` `int` (optional): Optional summon position; supplied through EFFECT_FLAG_SPSUM_PARAM.

## Returns

- `Effect`: Registered hand Special Summon procedure.

## Source

`Rush/Utilities/RDSummon.lua:448`

```lua
function RushDuel.AddHandToGraveSpecialSummonProcedure(card, desc, filter, count, value, position)
    local con = RushDuel.HandToGraveSpecialSummonCondition(filter, count)
    local tg = RushDuel.HandToGraveSpecialSummonTarget(filter, count)
    local op = RushDuel.HandToGraveSpecialSummonOperation
    local e1 = RD.AddHandSpecialSummonProcedure(card, desc, con, tg, op, value, position)
    return e1
end
```

## Guided Examples

Learn how to use this function in context:

- [Rush Special Summons And Result Types](/learn/rush-special-summon-results)

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **4** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.AddHandToGraveSpecialSummonProcedure) with `RushDuel.AddHandToGraveSpecialSummonProcedure`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Blaze Fiend Overlord Zebulth | `120287033` | [Rush/Scripts/c120287033.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120287033.lua) | 1 |
| Lana the Holy Wind of Healing | `120298044` | [Rush/Scripts/c120298044.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120298044.lua) | 1 |
| Dimension Riletta | `120309024` | [Rush/Scripts/c120309024.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120309024.lua) | 1 |
| The Tricky | `120272033` | [Rush/Scripts/c120272033.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120272033.lua) | 1 |

## Script Examples

### Blaze Fiend Overlord Zebulth (`120287033`)

Source: [Rush/Scripts/c120287033.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120287033.lua)

```lua
function cm.initial_effect(c)
	--Special Summon Procedure
	RD.AddHandToGraveSpecialSummonProcedure(c,aux.Stringid(m,0),cm.spconfilter,2)
	--Special Summon
	local e1=Effect.CreateEffect(c)
```

### Lana the Holy Wind of Healing (`120298044`)

Source: [Rush/Scripts/c120298044.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120298044.lua)

```lua
function cm.initial_effect(c)
	--Special Summon Procedure
	RD.AddHandToGraveSpecialSummonProcedure(c,aux.Stringid(m,0),cm.spconfilter,1,nil,POS_FACEUP_DEFENSE)
	--To Hand
	local e1=Effect.CreateEffect(c)
```

### Dimension Riletta (`120309024`)

Source: [Rush/Scripts/c120309024.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120309024.lua)

```lua
function cm.initial_effect(c)
	--Special Summon Procedure
	RD.AddHandToGraveSpecialSummonProcedure(c,aux.Stringid(m,0),cm.spconfilter,1,nil,POS_FACEUP_DEFENSE)
	--Position
	local e1=Effect.CreateEffect(c)
```
