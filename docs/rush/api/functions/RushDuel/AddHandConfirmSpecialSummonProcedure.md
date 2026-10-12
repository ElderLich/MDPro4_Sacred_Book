# RushDuel.AddHandConfirmSpecialSummonProcedure

Alias: `RD.AddHandConfirmSpecialSummonProcedure`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.AddHandConfirmSpecialSummonProcedure(any card, any desc, any filter, any value, any position) -> any
```

## Description

Rush Duel helper declared in `RDSummon.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
添加手卡特殊召唤手续: 把手卡1张卡给对方观看
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `desc` `any`: Type and behavior are not yet reviewed; see the source.
- `filter` `any`: Type and behavior are not yet reviewed; see the source.
- `value` `any`: Type and behavior are not yet reviewed; see the source.
- `position` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDSummon.lua:411`

```lua
function RushDuel.AddHandConfirmSpecialSummonProcedure(card, desc, filter, value, position)
    local con = RushDuel.HandConfirmSpecialSummonCondition(filter)
    local tg = RushDuel.HandConfirmSpecialSummonTarget(filter)
    local op = RushDuel.HandConfirmSpecialSummonOperation
    local e1 = RD.AddHandSpecialSummonProcedure(card, desc, con, tg, op, value, position)
    return e1
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **13** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.AddHandConfirmSpecialSummonProcedure) with `RushDuel.AddHandConfirmSpecialSummonProcedure`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Uranulycoris the Planetairy | `120293047` | [Rush/Scripts/c120293047.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120293047.lua) | 1 |
| Kaien the Molten Martial Machine | `120294032` | [Rush/Scripts/c120294032.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120294032.lua) | 1 |
| Grace Princess Mari | `120287019` | [Rush/Scripts/c120287019.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120287019.lua) | 1 |
| Prey Archfiend | `120304034` | [Rush/Scripts/c120304034.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120304034.lua) | 1 |
| Grace Princess Kaori | `120287018` | [Rush/Scripts/c120287018.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120287018.lua) | 1 |
| Arthenée the Defender of Sacred Silence | `120306033` | [Rush/Scripts/c120306033.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120306033.lua) | 1 |
| Soen the Molten Martial Machine | `120304036` | [Rush/Scripts/c120304036.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120304036.lua) | 1 |
| Manifestriction Dragon Maxseal | `120239036` | [Rush/Scripts/c120239036.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120239036.lua) | 1 |
| Prey Dullahan | `120304035` | [Rush/Scripts/c120304035.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120304035.lua) | 1 |
| Excutie Plawtie | `120231037` | [Rush/Scripts/c120231037.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120231037.lua) | 1 |
| Saturnchamomile the Planetairy | `120293048` | [Rush/Scripts/c120293048.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120293048.lua) | 1 |
| Rikuen the Molten Martial Machine | `120294033` | [Rush/Scripts/c120294033.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120294033.lua) | 1 |
| Faceless Culdesac | `120109034` | [Rush/Scripts/c120109034.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120109034.lua) | 1 |

## Script Examples

### Uranulycoris the Planetairy (`120293047`)

Source: [Rush/Scripts/c120293047.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120293047.lua)

```lua
	RD.AddCodeList(c,list)
	--Special Summon Procedure
	RD.AddHandConfirmSpecialSummonProcedure(c,aux.Stringid(m,0),cm.spconfilter)
	--Destroy
	local e1=Effect.CreateEffect(c)
```

### Kaien the Molten Martial Machine (`120294032`)

Source: [Rush/Scripts/c120294032.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120294032.lua)

```lua
function cm.initial_effect(c)
	--Special Summon Procedure
	RD.AddHandConfirmSpecialSummonProcedure(c,aux.Stringid(m,0),cm.spconfilter)
	--Special Summon
	local e1=Effect.CreateEffect(c)
```

### Grace Princess Mari (`120287019`)

Source: [Rush/Scripts/c120287019.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120287019.lua)

```lua
	RD.AddCodeList(c,list)
	--Special Summon Procedure
	RD.AddHandConfirmSpecialSummonProcedure(c,aux.Stringid(m,0),cm.spconfilter)
	--Atk Up
	local e1=Effect.CreateEffect(c)
```
