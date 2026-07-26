# Duel.CreateToken

## Signature

```lua
Duel.CreateToken(int player, int code) -> Card|false
```

## Description

Creates a Token card with card code code for player and returns it.
The returned Token is not placed on the field automatically; scripts normally pass it to Duel.SpecialSummon or another operation afterwards.

## Parameters

- `player` `int`
- `code` `int`

## Returns

- `Card|false`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4872`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **239** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Duel.CreateToken`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Surprise Fusion](/examples/cards/35167375) | `35167375` | [Scripts/c35167375.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c35167375.lua) | 1 |
| [Spirit Illusion](/examples/cards/71939275) | `71939275` | [Scripts/c71939275.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71939275.lua) | 1 |
| Duel Link Dragon, the Duel Dragon | `60025883` | [Scripts/c60025883.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c60025883.lua) | 1 |
| Plunder Patrollship Jord | `85969517` | [Scripts/c85969517.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c85969517.lua) | 1 |
| Mecha Phantom Beast Auroradon | `44097050` | [Scripts/c44097050.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44097050.lua) | 1 |
| Black Garden | `71645242` | [Scripts/c71645242.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71645242.lua) | 2 |
| Dual Avatar Invitation | `87669904` | [Scripts/c87669904.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c87669904.lua) | 1 |
| Sleipnir the Runick Mane | `74659582` | [Scripts/c74659582.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74659582.lua) | 1 |
| Crystron Halqifibrax Prism | `65400671` | [Scripts/c65400671.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c65400671.lua) | 1 |
| Shinobaroness Peacock | `25415052` | [Scripts/c25415052.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c25415052.lua) | 1 |
| Lost World | `17228908` | [Scripts/c17228908.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c17228908.lua) | 1 |
| Token Support | `53545926` | [Scripts/c53545926.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c53545926.lua) | 1 |
| Dark Creator | `52768390` | [Scripts/c52768390.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c52768390.lua) | 1 |
| Blackwing - Gofu the Vague Shadow | `9929398` | [Scripts/c9929398.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c9929398.lua) | 1 |
| Dark Alligator | `34479658` | [Scripts/c34479658.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c34479658.lua) | 1 |
| Phantasmal Lord Ultimitl Bishbaalkin | `90884403` | [Scripts/c90884403.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c90884403.lua) | 2 |
| Shinobaron Peacock | `52900000` | [Scripts/c52900000.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c52900000.lua) | 1 |
| Ogdoadic Daybreak | `78789356` | [Scripts/c78789356.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c78789356.lua) | 1 |
| Generaider Boss Stage | `38053381` | [Scripts/c38053381.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c38053381.lua) | 1 |
| Blooming of the Darkest Rose | `99092624` | [Scripts/c99092624.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c99092624.lua) | 1 |
| V-LAN Hydra | `13536606` | [Scripts/c13536606.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c13536606.lua) | 1 |
| Prank-Kids Pranks | `43664494` | [Scripts/c43664494.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c43664494.lua) | 1 |
| Garden Rose Flora | `76524506` | [Scripts/c76524506.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c76524506.lua) | 1 |
| Nibiru, the Primal Being | `27204311` | [Scripts/c27204311.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c27204311.lua) | 1 |
| ...and 215 more |  |  |  |

## Script Examples

### Surprise Fusion (`35167375`)

Source: [Scripts/c35167375.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c35167375.lua)

```lua
			and Duel.IsPlayerCanSpecialSummonMonster(tp,id+o,0,TYPES_TOKEN_MONSTER,0,0,level,RACE_SPELLCASTER,ATTRIBUTE_DARK) then
			for i=1,2 do
				local token=Duel.CreateToken(tp,id+o)
				local e1=Effect.CreateEffect(e:GetHandler())
				e1:SetType(EFFECT_TYPE_SINGLE)
```

### Spirit Illusion (`71939275`)

Source: [Scripts/c71939275.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71939275.lua)

```lua
	if Duel.GetLocationCount(tp,LOCATION_MZONE)>0
		and Duel.IsPlayerCanSpecialSummonMonster(tp,id+o,0,TYPES_TOKEN_MONSTER,tc:GetAttack(),0,5,tc:GetRace(),tc:GetAttribute()) then
		local token=Duel.CreateToken(tp,id+o)
		local e1=Effect.CreateEffect(c)
		e1:SetType(EFFECT_TYPE_SINGLE)
```

### Duel Link Dragon, the Duel Dragon (`60025883`)

Source: [Scripts/c60025883.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c60025883.lua)

```lua
	if Duel.GetLocationCount(tp,LOCATION_MZONE,tp,LOCATION_REASON_TOFIELD,zone)<=0
		or not Duel.IsPlayerCanSpecialSummonMonster(tp,60025884,0,TYPES_TOKEN_MONSTER,atk,def,lv,race,att) then return end
	local token=Duel.CreateToken(tp,60025884)
	Duel.SpecialSummonStep(token,0,tp,tp,false,false,POS_FACEUP,zone)
	local e1=Effect.CreateEffect(c)
```
