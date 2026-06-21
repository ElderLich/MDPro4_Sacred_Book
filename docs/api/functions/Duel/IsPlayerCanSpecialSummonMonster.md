# Duel.IsPlayerCanSpecialSummonMonster

## Signature

```lua
Duel.IsPlayerCanSpecialSummonMonster(int player, int code, [int|nil setcode], [int|nil type], [int|nil atk], [int|nil def], [int|nil level], [int|nil race], [int|nil attribute], [int pos], [int target_player], [int sumtype], [int zone]) -> bool
```

## Description

Check player player can be pos to the form of special summon the parameters of the monster to the target_player field
This function is usually used to determine whether it is possible to trick token and trap monsters

## Parameters

- `player` `int`
- `code` `int`
- `setcode` `int|nil` optional
- `type` `int|nil` optional
- `atk` `int|nil` optional
- `def` `int|nil` optional
- `level` `int|nil` optional
- `race` `int|nil` optional
- `attribute` `int|nil` optional
- `pos` `int` optional - default: POS_FACEUP
- `target_player` `int` optional - default: player
- `sumtype` `int` optional - default: 0
- `zone` `int` optional

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5052`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **330** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Duel.IsPlayerCanSpecialSummonMonster`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Surprise Fusion](/examples/cards/35167375) | `35167375` | [Scripts/c35167375.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c35167375.lua) | 73 |
| [Spirit Illusion](/examples/cards/71939275) | `71939275` | [Scripts/c71939275.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71939275.lua) | 65 |
| Duel Link Dragon, the Duel Dragon | `60025883` | [Scripts/c60025883.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c60025883.lua) | 59 |
| Chaos Hats | `2372506` | [Scripts/c2372506.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c2372506.lua) | 59 |
| Magical Hats | `81210420` | [Scripts/c81210420.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c81210420.lua) | 59 |
| Plunder Patrollship Jord | `85969517` | [Scripts/c85969517.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c85969517.lua) | 58 |
| Mecha Phantom Beast Auroradon | `44097050` | [Scripts/c44097050.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44097050.lua) | 58 |
| Black Garden | `71645242` | [Scripts/c71645242.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71645242.lua) | 56 |
| Dual Avatar Invitation | `87669904` | [Scripts/c87669904.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c87669904.lua) | 55 |
| Sleipnir the Runick Mane | `74659582` | [Scripts/c74659582.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74659582.lua) | 54 |
| Crystron Halqifibrax Prism | `65400671` | [Scripts/c65400671.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c65400671.lua) | 53 |
| Shinobaroness Peacock | `25415052` | [Scripts/c25415052.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c25415052.lua) | 52 |
| Sentence of Doom | `40771118` | [Scripts/c40771118.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c40771118.lua) | 52 |
| Lost World | `17228908` | [Scripts/c17228908.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c17228908.lua) | 51 |
| Token Support | `53545926` | [Scripts/c53545926.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c53545926.lua) | 51 |
| Dark Creator | `52768390` | [Scripts/c52768390.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c52768390.lua) | 51 |
| Blackwing - Gofu the Vague Shadow | `9929398` | [Scripts/c9929398.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c9929398.lua) | 50 |
| Dark Alligator | `34479658` | [Scripts/c34479658.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c34479658.lua) | 50 |
| Phantasmal Lord Ultimitl Bishbaalkin | `90884403` | [Scripts/c90884403.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c90884403.lua) | 49 |
| Shinobaron Peacock | `52900000` | [Scripts/c52900000.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c52900000.lua) | 49 |
| Ogdoadic Daybreak | `78789356` | [Scripts/c78789356.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c78789356.lua) | 49 |
| Generaider Boss Stage | `38053381` | [Scripts/c38053381.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c38053381.lua) | 48 |
| Blooming of the Darkest Rose | `99092624` | [Scripts/c99092624.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c99092624.lua) | 48 |
| V-LAN Hydra | `13536606` | [Scripts/c13536606.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c13536606.lua) | 48 |
| ...and 306 more |  |  |  |

## Script Examples

### Surprise Fusion (`35167375`)

Source: [Scripts/c35167375.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c35167375.lua)

```lua
	return c:IsType(TYPE_FUSION) and c:IsReleasableByEffect() and (not chk
		or (Duel.GetMZoneCount(tp,c)>1 and not Duel.IsPlayerAffectedByEffect(tp,59822133)
			and Duel.IsPlayerCanSpecialSummonMonster(tp,id+o,0,TYPES_TOKEN_MONSTER,0,0,c:GetLevel(),RACE_SPELLCASTER,ATTRIBUTE_DARK)))
end
function s.sptg(e,tp,eg,ep,ev,re,r,rp,chk)
```

### Spirit Illusion (`71939275`)

Source: [Scripts/c71939275.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71939275.lua)

```lua
	local tc=e:GetHandler():GetEquipTarget()
	if chk==0 then return Duel.GetLocationCount(tp,LOCATION_MZONE)>0
		and Duel.IsPlayerCanSpecialSummonMonster(tp,id+o,0,TYPES_TOKEN_MONSTER,tc:GetAttack(),0,5,tc:GetRace(),tc:GetAttribute()) end
	Duel.Hint(HINT_OPSELECTED,1-tp,e:GetDescription())
	Duel.SetOperationInfo(0,CATEGORY_TOKEN,nil,1,0,0)
```

### Duel Link Dragon, the Duel Dragon (`60025883`)

Source: [Scripts/c60025883.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c60025883.lua)

```lua
	return c:IsType(TYPE_SYNCHRO) and c:IsAbleToRemoveAsCost()
		and (c:IsSetCard(0xc2) or c:IsRace(RACE_DRAGON) and (c:IsLevel(7) or c:IsLevel(8)))
		and Duel.IsPlayerCanSpecialSummonMonster(tp,60025884,0,TYPES_TOKEN_MONSTER,c:GetAttack(),c:GetDefense(),c:GetLevel(),c:GetRace(),c:GetAttribute())
end
function c60025883.spcost(e,tp,eg,ep,ev,re,r,rp,chk)
```
