# Card.GetFusionCode

## Signature

```lua
Card.GetFusionCode(Card c) -> int,int|nil,...|nil
```

## Description

Return c as the fusion material when the card number (including the original c card number)

## Parameters

- `c` `Card`

## Returns

- `int`
- `int|nil`
- `...|nil`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3389`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **13** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.GetFusionCode`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Alba System Dogmatikalamity | `93053159` | [Scripts/c93053159.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93053159.lua) | 58 |
| Thunder Dragon Titan | `41685633` | [Scripts/c41685633.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c41685633.lua) | 52 |
| Guardian Chimera | `11321089` | [Scripts/c11321089.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c11321089.lua) | 49 |
| Arcana Force EX - The Chaos Ruler | `12686296` | [Scripts/c12686296.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c12686296.lua) | 49 |
| Dinomorphia Kentregina | `48832775` | [Scripts/c48832775.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c48832775.lua) | 49 |
| Lunalight Kaleido Chick | `35618217` | [Scripts/c35618217.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c35618217.lua) | 45 |
| Trishula, the Dragon of Icy Imprisonment | `15661378` | [Scripts/c15661378.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c15661378.lua) | 44 |
| Dante, Pilgrim of the Burning Abyss | `18386170` | [Scripts/c18386170.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c18386170.lua) | 40 |
| Over Fusion | `52553471` | [Scripts/c52553471.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c52553471.lua) | 39 |
| Dinomorphia Stealthbergia | `74936480` | [Scripts/c74936480.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74936480.lua) | 37 |
| Fusion Tag | `59432181` | [Scripts/c59432181.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59432181.lua) | 31 |
| Garura, Wings of Resonant Life | `11765832` | [Scripts/c11765832.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c11765832.lua) | 30 |
| Pair Cycroid | `16114248` | [Scripts/c16114248.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c16114248.lua) | 12 |

## Script Examples

### Alba System Dogmatikalamity (`93053159`)

Source: [Scripts/c93053159.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93053159.lua)

```lua
	if aux.FCheckAdditional and not aux.FCheckAdditional(tp,sg,fc)
		or aux.FGoalCheckAdditional and not aux.FGoalCheckAdditional(tp,sg,fc) then return false end
	return g:GetClassCount(Card.GetFusionCode)==g:GetCount()
		and (chkf==PLAYER_NONE or Duel.GetLocationCountFromEx(tp,tp,sg,fc)>0)
end
```

### Thunder Dragon Titan (`41685633`)

Source: [Scripts/c41685633.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c41685633.lua)

```lua
	if not (c:IsLocation(LOCATION_MZONE) and c:IsFusionType(TYPE_FUSION)) then return false end
	if not c:IsFusionCode(41685633) then return true end
	for i,code in ipairs({c:GetFusionCode()}) do
		if code~=41685633 then return true end
	end
```

### Guardian Chimera (`11321089`)

Source: [Scripts/c11321089.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c11321089.lua)

```lua
	local chkloc=LOCATION_HAND
	if c:IsOnField() then chkloc=LOCATION_ONFIELD end
	return not sg:IsExists(Card.IsFusionCode,1,c,c:GetFusionCode())
		and (not c:IsLocation(LOCATION_HAND+LOCATION_ONFIELD) or #sg<2 or sg:IsExists(aux.NOT(Card.IsLocation),1,c,chkloc))
end
```
