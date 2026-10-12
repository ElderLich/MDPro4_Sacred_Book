# RushDuel.AddHealthySummonProcedure

Alias: `RD.AddHealthySummonProcedure`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.AddHealthySummonProcedure(any card, any desc, any attack) -> any
```

## Description

Rush Duel helper declared in `RDSummon.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
添加不用解放的妥协召唤手续 (改变原本攻击力)
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `desc` `any`: Type and behavior are not yet reviewed; see the source.
- `attack` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDSummon.lua:170`

```lua
function RushDuel.AddHealthySummonProcedure(card, desc, attack)
    return RushDuel.AddSummonProcedureZero(card, desc, nil, RushDuel.SummonAttackChangeOperation(attack))
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **6** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.AddHealthySummonProcedure) with `RushDuel.AddHealthySummonProcedure`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Healthie Shanlong | `120306020` | [Rush/Scripts/c120306020.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120306020.lua) | 1 |
| Healthie Sati | `120306024` | [Rush/Scripts/c120306024.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120306024.lua) | 1 |
| Beast King Barbaros | `120300000` | [Rush/Scripts/c120300000.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120300000.lua) | 1 |
| Healthie Rem | `120306022` | [Rush/Scripts/c120306022.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120306022.lua) | 1 |
| Healthie Cafferin | `120306019` | [Rush/Scripts/c120306019.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120306019.lua) | 1 |
| Healthie Lamilla | `120306021` | [Rush/Scripts/c120306021.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120306021.lua) | 1 |

## Script Examples

### Healthie Shanlong (`120306020`)

Source: [Rush/Scripts/c120306020.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120306020.lua)

```lua
	RD.AddCodeList(c,list)
	--Summon Procedure
	RD.AddHealthySummonProcedure(c,aux.Stringid(m,0),1000)
	--To Grave
	local e1=Effect.CreateEffect(c)
```

### Healthie Sati (`120306024`)

Source: [Rush/Scripts/c120306024.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120306024.lua)

```lua
function cm.initial_effect(c)
	--Summon Procedure
	RD.AddHealthySummonProcedure(c,aux.Stringid(m,0),1000)
	--Special Summon
	local e1=Effect.CreateEffect(c)
```

### Beast King Barbaros (`120300000`)

Source: [Rush/Scripts/c120300000.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120300000.lua)

```lua
function cm.initial_effect(c)
	--Summon Procedure
	RD.AddHealthySummonProcedure(c,aux.Stringid(m,0),1900)
	RD.AddSummonProcedureThree(c,aux.Stringid(m,1),nil,cm.sumfilter)
	--Destroy
```
