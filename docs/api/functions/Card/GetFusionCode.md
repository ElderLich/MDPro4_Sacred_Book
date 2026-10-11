# Card.GetFusionCode

## Signature

```lua
Card.GetFusionCode(Card c) -> int,...?
```

## Description

Returns c's Fusion Material codes: current code, second code when present, then EFFECT_ADD_FUSION_CODE values.
When the core is checking with not_material set, only the current and second codes are returned.

## Parameters

- `c` `Card`

## Returns

- `int` - Current code.
- `...?` - Additional Fusion Material code values, if any.

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3439`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **13** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Card.GetFusionCode) with `Card.GetFusionCode`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Alba System Dogmatikalamity | `93053159` | [Scripts/c93053159.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93053159.lua) | 1 |
| Thunder Dragon Titan | `41685633` | [Scripts/c41685633.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c41685633.lua) | 1 |
| Guardian Chimera | `11321089` | [Scripts/c11321089.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c11321089.lua) | 1 |
| Arcana Force EX - The Chaos Ruler | `12686296` | [Scripts/c12686296.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c12686296.lua) | 1 |
| Dinomorphia Kentregina | `48832775` | [Scripts/c48832775.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c48832775.lua) | 1 |
| Lunalight Kaleido Chick | `35618217` | [Scripts/c35618217.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c35618217.lua) | 1 |
| Trishula, the Dragon of Icy Imprisonment | `15661378` | [Scripts/c15661378.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c15661378.lua) | 1 |
| Dante, Pilgrim of the Burning Abyss | `18386170` | [Scripts/c18386170.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c18386170.lua) | 1 |
| Over Fusion | `52553471` | [Scripts/c52553471.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c52553471.lua) | 1 |
| Dinomorphia Stealthbergia | `74936480` | [Scripts/c74936480.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74936480.lua) | 1 |
| Fusion Tag | `59432181` | [Scripts/c59432181.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59432181.lua) | 1 |
| Garura, Wings of Resonant Life | `11765832` | [Scripts/c11765832.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c11765832.lua) | 1 |
| Pair Cycroid | `16114248` | [Scripts/c16114248.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c16114248.lua) | 1 |

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
