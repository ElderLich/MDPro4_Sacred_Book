# Duel.IsPlayerCanSpecialSummonMonster

## Signature

```lua
Duel.IsPlayerCanSpecialSummonMonster(int player, int code, [int|nil setcode], [int|nil type], [int|nil atk], [int|nil def], [int|nil level], [int|nil race], [int|nil attribute], [int pos], [int target_player], [int sumtype]) -> bool
```

## Description

Checks whether player can Special Summon a virtual monster with the supplied card data.
Optional arguments override the loaded card data, then pos, target_player, and sumtype describe how and where the monster would be Summoned. This MDPro3 binding does not read a zone argument.

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
- `pos` `int` optional
- `target_player` `int` optional
- `sumtype` `int` optional

## Returns

- `bool` - true if the virtual monster can be Special Summoned.

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5052`

## Guided Examples

Learn how to use this function in context:

- [Archetypes and Set Codes](/learn/archetypes-and-setcodes)
- [Tokens And Summon Choices](/learn/tokens-and-summon-choices)

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **339** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Duel.IsPlayerCanSpecialSummonMonster) with `Duel.IsPlayerCanSpecialSummonMonster`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Surprise Fusion](/examples/cards/35167375) | `35167375` | [Scripts/c35167375.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c35167375.lua) | 2 |
| [Spirit Illusion](/examples/cards/71939275) | `71939275` | [Scripts/c71939275.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71939275.lua) | 2 |
| Chaos Magical Hats | `2372506` | [Scripts/c2372506.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c2372506.lua) | 1 |
| Duel Link Dragon, the Duel Dragon | `60025883` | [Scripts/c60025883.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c60025883.lua) | 2 |
| Magical Hats | `81210420` | [Scripts/c81210420.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c81210420.lua) | 1 |
| Plunder Patrollship Jord | `85969517` | [Scripts/c85969517.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c85969517.lua) | 3 |
| Mecha Phantom Beast Auroradon | `44097050` | [Scripts/c44097050.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44097050.lua) | 2 |
| Black Garden | `71645242` | [Scripts/c71645242.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71645242.lua) | 2 |
| Dual Avatar Invitation | `87669904` | [Scripts/c87669904.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c87669904.lua) | 2 |
| Sleipnir the Runick Mane | `74659582` | [Scripts/c74659582.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74659582.lua) | 2 |
| Sleepy Scapegoats | `3129527` | [Scripts/c3129527.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c3129527.lua) | 2 |
| Crystron Halqifibrax Prism | `65400671` | [Scripts/c65400671.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c65400671.lua) | 2 |
| Shinobaroness Peacock | `25415052` | [Scripts/c25415052.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c25415052.lua) | 2 |
| Sentence of Doom | `40771118` | [Scripts/c40771118.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c40771118.lua) | 2 |
| Lost World | `17228908` | [Scripts/c17228908.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c17228908.lua) | 2 |
| Token Support | `53545926` | [Scripts/c53545926.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c53545926.lua) | 2 |
| Dark Creator | `52768390` | [Scripts/c52768390.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c52768390.lua) | 2 |
| Blackwing - Gofu the Vague Shadow | `9929398` | [Scripts/c9929398.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c9929398.lua) | 2 |
| Dark Alligator | `34479658` | [Scripts/c34479658.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c34479658.lua) | 2 |
| Phantasmal Lord Ultimitl Bishbaalkin | `90884403` | [Scripts/c90884403.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c90884403.lua) | 4 |
| Shinobaron Peacock | `52900000` | [Scripts/c52900000.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c52900000.lua) | 2 |
| Ogdoadic Daybreak | `78789356` | [Scripts/c78789356.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c78789356.lua) | 2 |
| Generaider Boss Stage | `38053381` | [Scripts/c38053381.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c38053381.lua) | 2 |
| Blooming of the Darkest Rose | `99092624` | [Scripts/c99092624.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c99092624.lua) | 3 |
| ...and 315 more |  |  |  |

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

### Chaos Magical Hats (`2372506`)

Source: [Scripts/c2372506.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c2372506.lua)

```lua
function s.spfilter(c,e,tp)
	return c:IsType(TYPE_SPELL+TYPE_TRAP)
		and Duel.IsPlayerCanSpecialSummonMonster(tp,id,0xcf,TYPES_NORMAL_TRAP_MONSTER,0,0,8,RACE_SPELLCASTER,ATTRIBUTE_DARK)
		and c:IsCanBeSpecialSummoned(e,0,tp,true,true,POS_FACEDOWN_DEFENSE)
end
```
