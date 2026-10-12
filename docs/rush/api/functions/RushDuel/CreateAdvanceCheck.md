# RushDuel.CreateAdvanceCheck

Alias: `RD.CreateAdvanceCheck`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.CreateAdvanceCheck(any card, any filter, any count, any flag) -> any
```

## Description

Rush Duel helper declared in `RDSummon.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
上级召唤时的解放怪兽检测
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `filter` `any`: Type and behavior are not yet reviewed; see the source.
- `count` `any`: Type and behavior are not yet reviewed; see the source.
- `flag` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDSummon.lua:180`

```lua
function RushDuel.CreateAdvanceCheck(card, filter, count, flag)
    local e1 = Effect.CreateEffect(card)
    e1:SetType(EFFECT_TYPE_SINGLE)
    e1:SetCode(EFFECT_MATERIAL_CHECK)
    e1:SetValue(function(e, c)
        local mg = c:GetMaterial()
        local ct = math.min(count, #mg)
        local label = 0
        if c:IsLevelBelow(6) and count == 2 then
            -- 当前等级小于解放要求
        elseif ct > 0 and mg:IsExists(filter, ct, nil, e) then
            label = flag
        end
        e:SetLabel(label)
    end)
    card:RegisterEffect(e1)
    local e2 = Effect.CreateEffect(card)
    e2:SetType(EFFECT_TYPE_SINGLE + EFFECT_TYPE_CONTINUOUS)
    e2:SetCode(EVENT_SUMMON_SUCCESS)
    e2:SetProperty(EFFECT_FLAG_CANNOT_DISABLE + EFFECT_FLAG_UNCOPYABLE)
    e2:SetLabelObject(e1)
    e2:SetCondition(RushDuel.AdvanceCheckCondition)
    e2:SetOperation(RushDuel.AdvanceCheckOperation)
    card:RegisterEffect(e2)
    return e1, e2
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **11** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.CreateAdvanceCheck) with `RushDuel.CreateAdvanceCheck`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Royal Rebel's Heavy Metal | `120130031` | [Rush/Scripts/c120130031.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120130031.lua) | 1 |
| Royal Rebel's Extreme | `120306006` | [Rush/Scripts/c120306006.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120306006.lua) | 1 |
| Super Galaxy King Lord of Galactica | `120254038` | [Rush/Scripts/c120254038.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120254038.lua) | 1 |
| Royal Rebel's Doom Metal | `120170024` | [Rush/Scripts/c120170024.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120170024.lua) | 1 |
| Jointech Hero | `120249008` | [Rush/Scripts/c120249008.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120249008.lua) | 1 |
| Secret Guardian Miscalculate | `120257023` | [Rush/Scripts/c120257023.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120257023.lua) | 1 |
| Royal Rebel's Progrock | `120254017` | [Rush/Scripts/c120254017.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120254017.lua) | 1 |
| Contact Dark Matter Wyvern | `120264003` | [Rush/Scripts/c120264003.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120264003.lua) | 1 |
| Royal Rebel's Hard Rock | `120203012` | [Rush/Scripts/c120203012.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120203012.lua) | 1 |
| Royal Rebel's Growl | `120140016` | [Rush/Scripts/c120140016.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120140016.lua) | 1 |
| Royal Rebel's Invasion | `120140015` | [Rush/Scripts/c120140015.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120140015.lua) | 1 |

## Script Examples

### Royal Rebel's Heavy Metal (`120130031`)

Source: [Rush/Scripts/c120130031.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120130031.lua)

```lua
function cm.initial_effect(c)
	--Tribute
	RD.CreateAdvanceCheck(c,cm.tricheck,1,20130031)
	--Destroy
	local e1=Effect.CreateEffect(c)
```

### Royal Rebel's Extreme (`120306006`)

Source: [Rush/Scripts/c120306006.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120306006.lua)

```lua
function cm.initial_effect(c)
	--Tribute
	RD.CreateAdvanceCheck(c,cm.tricheck,1,20309006)
	--Release
	local e1=Effect.CreateEffect(c)
```

### Super Galaxy King Lord of Galactica (`120254038`)

Source: [Rush/Scripts/c120254038.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120254038.lua)

```lua
	RD.AddMaximumProcedure(c,4000,list[1],list[2])
	--Tribute
	RD.CreateAdvanceCheck(c,cm.tricheck,1,20254038)
	--To Hand
	local e1=Effect.CreateEffect(c)
```
