# RushDuel.AddPrimeSummonProcedure

Alias: `RD.AddPrimeSummonProcedure`. Requires the matching Rush Duel Lua bootstrap.

## Signature

```lua
RushDuel.AddPrimeSummonProcedure(any card, any desc, any attack, any filter) -> any
```

## Description

Rush Duel helper declared in `RDSummon.lua`. Its argument names are extracted from the pinned source; parameter and return types have not yet been reviewed.

### Upstream source comment

```text
添加解放1只的妥协召唤手续 (改变原本攻击力)
```

## Parameters

- `card` `any`: Type and behavior are not yet reviewed; see the source.
- `desc` `any`: Type and behavior are not yet reviewed; see the source.
- `attack` `any`: Type and behavior are not yet reviewed; see the source.
- `filter` `any`: Type and behavior are not yet reviewed; see the source.

## Returns

- `any`: Return contract has not been reviewed; inspect the source below.

## Source

`Rush/Utilities/RDSummon.lua:175`

```lua
function RushDuel.AddPrimeSummonProcedure(card, desc, attack, filter)
    return RushDuel.AddSummonProcedureOne(card, desc, nil, filter, RushDuel.SummonAttackChangeOperation(attack))
end
```

## Used By

Generated from the local `Rush/Scripts/` folder and `rush_cards.cdb`.

- Detected in **10** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=rush&mode=code&q=RushDuel.AddPrimeSummonProcedure) with `RushDuel.AddPrimeSummonProcedure`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Prime Dian Keto | `120257007` | [Rush/Scripts/c120257007.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120257007.lua) | 1 |
| Prime Claw Girl | `120257004` | [Rush/Scripts/c120257004.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120257004.lua) | 1 |
| Prime Bandijo | `120257006` | [Rush/Scripts/c120257006.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120257006.lua) | 1 |
| Prime Bandijo | `120273003` | [Rush/Scripts/c120273003.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120273003.lua) | 1 |
| Healthie Olivia | `120306023` | [Rush/Scripts/c120306023.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120306023.lua) | 1 |
| Jointech Prime Rex | `120109041` | [Rush/Scripts/c120109041.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120109041.lua) | 1 |
| Transam Prime Armor Nova | `120257008` | [Rush/Scripts/c120257008.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120257008.lua) | 1 |
| Behemoth the King of All Animals | `120238002` | [Rush/Scripts/c120238002.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120238002.lua) | 1 |
| Mean Mutt Sacred Prime Shiba | `120264011` | [Rush/Scripts/c120264011.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120264011.lua) | 1 |
| Prime Tractiger | `120257005` | [Rush/Scripts/c120257005.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120257005.lua) | 1 |

## Script Examples

### Prime Dian Keto (`120257007`)

Source: [Rush/Scripts/c120257007.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120257007.lua)

```lua
	RD.AddCodeList(c,list)
	--Summon Procedure
	RD.AddPrimeSummonProcedure(c,aux.Stringid(m,0),1000)
	--Recover
	local e1=Effect.CreateEffect(c)
```

### Prime Claw Girl (`120257004`)

Source: [Rush/Scripts/c120257004.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120257004.lua)

```lua
	RD.AddCodeList(c,list)
	--Summon Procedure
	RD.AddPrimeSummonProcedure(c,aux.Stringid(m,0),200)
	--Special Summon
	local e1=Effect.CreateEffect(c)
```

### Prime Bandijo (`120257006`)

Source: [Rush/Scripts/c120257006.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Rush/Scripts/c120257006.lua)

```lua
	RD.AddCodeList(c,list)
	--Summon Procedure
	RD.AddPrimeSummonProcedure(c,aux.Stringid(m,0),1800)
	--To Hand
	local e1=Effect.CreateEffect(c)
```
