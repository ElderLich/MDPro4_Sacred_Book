# RushDuel.AddHandSpecialSummonProcedure

Alias: `RD.AddHandSpecialSummonProcedure`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.AddHandSpecialSummonProcedure(any card, any desc, any condition, any target, any operation, any value, any position) -> any
```

## Description

Rush Duel helper declared in `RDSummon.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
添加手卡特殊召唤手续
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `desc` `any`: Type and behavior are not yet reviewed; see the source.
- `condition` `any`: Type and behavior are not yet reviewed; see the source.
- `target` `any`: Type and behavior are not yet reviewed; see the source.
- `operation` `any`: Type and behavior are not yet reviewed; see the source.
- `value` `any`: Type and behavior are not yet reviewed; see the source.
- `position` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDSummon.lua:382`

```lua
function RushDuel.AddHandSpecialSummonProcedure(card, desc, condition, target, operation, value, position)
    local e1 = Effect.CreateEffect(card)
    e1:SetDescription(desc)
    e1:SetType(EFFECT_TYPE_FIELD)
    e1:SetCode(EFFECT_SPSUMMON_PROC)
    if position == nil then
        e1:SetProperty(EFFECT_FLAG_CANNOT_DISABLE + EFFECT_FLAG_UNCOPYABLE)
    else
        e1:SetProperty(EFFECT_FLAG_CANNOT_DISABLE + EFFECT_FLAG_UNCOPYABLE + EFFECT_FLAG_SPSUM_PARAM)
        e1:SetTargetRange(position, 0)
    end
    e1:SetRange(LOCATION_HAND)
    if condition ~= nil then
        e1:SetCondition(condition)
    end
    if target ~= nil then
        e1:SetTarget(target)
    end
    if operation ~= nil then
        e1:SetOperation(operation)
    end
    if value ~= nil then
        e1:SetValue(value)
    end
    card:RegisterEffect(e1)
    return e1
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **38** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.AddHandSpecialSummonProcedure) with `RushDuel.AddHandSpecialSummonProcedure`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Chaos Emperor Dragon - Envoy of the End](/examples/rush-cards/120305001) | `120305001` | [Rush/Scripts/c120305001.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120305001.lua) | 1 |
| [Brassdes of the Wicked Wheels](/examples/rush-cards/120304033) | `120304033` | [Rush/Scripts/c120304033.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120304033.lua) | 1 |
| [Player #C39: Home Run Smasher V](/examples/rush-cards/120305028) | `120305028` | [Rush/Scripts/c120305028.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120305028.lua) | 1 |
| [The Black Witch Facing the Temple](/examples/rush-cards/120309048) | `120309048` | [Rush/Scripts/c120309048.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120309048.lua) | 1 |
| [Jinzo the Machine Menace](/examples/rush-cards/120257028) | `120257028` | [Rush/Scripts/c120257028.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120257028.lua) | 1 |
| Qadi of the Monumenthes | `120300009` | [Rush/Scripts/c120300009.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120300009.lua) | 1 |
| Sparkhearts Anesh | `120298022` | [Rush/Scripts/c120298022.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120298022.lua) | 1 |
| The Flame Dragon Haunting the Temple | `120309047` | [Rush/Scripts/c120309047.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120309047.lua) | 1 |
| Excutie Lumière | `120231031` | [Rush/Scripts/c120231031.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120231031.lua) | 1 |
| Guardian Eatos | `120290065` | [Rush/Scripts/c120290065.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120290065.lua) | 1 |
| Battletested Curse of Dragon | `120249031` | [Rush/Scripts/c120249031.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120249031.lua) | 1 |
| Red-Eyes Darkness Metal Dragon | `120294000` | [Rush/Scripts/c120294000.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120294000.lua) | 1 |
| Blue-Eyes Vision Dragon | `120252004` | [Rush/Scripts/c120252004.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120252004.lua) | 1 |
| Launcher Catapult Turtle | `120249030` | [Rush/Scripts/c120249030.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120249030.lua) | 1 |
| Cyber Processor | `120244021` | [Rush/Scripts/c120244021.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120244021.lua) | 1 |
| Coredrasil the Spirit Tree Bunrei | `120306018` | [Rush/Scripts/c120306018.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120306018.lua) | 1 |
| Wroughtwyvern | `120263011` | [Rush/Scripts/c120263011.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120263011.lua) | 1 |
| Pitch-Dark Eradicator Sorcerer | `120309008` | [Rush/Scripts/c120309008.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120309008.lua) | 1 |
| Lightning Volteagle | `120246001` | [Rush/Scripts/c120246001.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120246001.lua) | 1 |
| Lightning Voltkite | `120246003` | [Rush/Scripts/c120246003.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120246003.lua) | 1 |
| Cross Lostream Melutine | `120309036` | [Rush/Scripts/c120309036.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120309036.lua) | 1 |
| Executie Flame | `120235019` | [Rush/Scripts/c120235019.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120235019.lua) | 1 |
| Deity of Seven Treasures - Beidai | `120261042` | [Rush/Scripts/c120261042.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120261042.lua) | 1 |
| Deity of Seven Treasures - Bika | `120283037` | [Rush/Scripts/c120283037.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120283037.lua) | 1 |
| ...and 14 more |  |  |  |

## Script Examples

### Chaos Emperor Dragon - Envoy of the End (`120305001`)

Source: [Rush/Scripts/c120305001.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120305001.lua)

```lua
function cm.initial_effect(c)
	--Special Summon Procedure
	RD.AddHandSpecialSummonProcedure(c,aux.Stringid(m,0),cm.spcon,cm.sptg,cm.spop,SUMMON_VALUE_SELF)
	--Counter
	Duel.AddCustomActivityCounter(m,ACTIVITY_CHAIN,aux.FALSE)
```

### Brassdes of the Wicked Wheels (`120304033`)

Source: [Rush/Scripts/c120304033.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120304033.lua)

```lua
	RD.AddCodeList(c,list)
	--Special Summon Procedure
	RD.AddHandSpecialSummonProcedure(c,aux.Stringid(m,0),cm.spcon,cm.sptg,cm.spop)
	--Atk Up
	local e1=Effect.CreateEffect(c)
```

### Player #C39: Home Run Smasher V (`120305028`)

Source: [Rush/Scripts/c120305028.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120305028.lua)

```lua
function cm.initial_effect(c)
	--Special Summon Procedure
	RD.AddHandSpecialSummonProcedure(c,aux.Stringid(m,0),cm.spcon,cm.sptg,cm.spop)
	--Destroy
	local e1=Effect.CreateEffect(c)
```
