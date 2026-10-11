# RushDuel.AddHandToGraveSpecialSummonProcedure

Alias: `RD.AddHandToGraveSpecialSummonProcedure`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.AddHandToGraveSpecialSummonProcedure(any card, any desc, any filter, any count, any value, any position) -> any
```

## Description

Rush Duel helper declared in `RDSummon.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
添加手卡特殊召唤手续: 把手卡送去墓地
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `desc` `any`: Type and behavior are not yet reviewed; see the source.
- `filter` `any`: Type and behavior are not yet reviewed; see the source.
- `count` `any`: Type and behavior are not yet reviewed; see the source.
- `value` `any`: Type and behavior are not yet reviewed; see the source.
- `position` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

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

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **4** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.AddHandToGraveSpecialSummonProcedure) with `RushDuel.AddHandToGraveSpecialSummonProcedure`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Blaze Fiend Overlord Zebulth | `120287033` | [Rush/Scripts/c120287033.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120287033.lua) | 1 |
| Lana the Holy Wind of Healing | `120298044` | [Rush/Scripts/c120298044.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120298044.lua) | 1 |
| Dimension Riletta | `120309024` | [Rush/Scripts/c120309024.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120309024.lua) | 1 |
| The Tricky | `120272033` | [Rush/Scripts/c120272033.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120272033.lua) | 1 |

## Script Examples

### Blaze Fiend Overlord Zebulth (`120287033`)

Source: [Rush/Scripts/c120287033.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120287033.lua)

```lua
function cm.initial_effect(c)
	--Special Summon Procedure
	RD.AddHandToGraveSpecialSummonProcedure(c,aux.Stringid(m,0),cm.spconfilter,2)
	--Special Summon
	local e1=Effect.CreateEffect(c)
```

### Lana the Holy Wind of Healing (`120298044`)

Source: [Rush/Scripts/c120298044.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120298044.lua)

```lua
function cm.initial_effect(c)
	--Special Summon Procedure
	RD.AddHandToGraveSpecialSummonProcedure(c,aux.Stringid(m,0),cm.spconfilter,1,nil,POS_FACEUP_DEFENSE)
	--To Hand
	local e1=Effect.CreateEffect(c)
```

### Dimension Riletta (`120309024`)

Source: [Rush/Scripts/c120309024.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Rush/Scripts/c120309024.lua)

```lua
function cm.initial_effect(c)
	--Special Summon Procedure
	RD.AddHandToGraveSpecialSummonProcedure(c,aux.Stringid(m,0),cm.spconfilter,1,nil,POS_FACEUP_DEFENSE)
	--Position
	local e1=Effect.CreateEffect(c)
```
