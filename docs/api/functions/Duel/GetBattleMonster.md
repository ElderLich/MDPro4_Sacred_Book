# Duel.GetBattleMonster

## Signature

```lua
Duel.GetBattleMonster(int player) -> Card|nil,Card|nil
```

## Description

Returns the monster controlled by player that is currently in battle, followed by the monster controlled by the opponent that is currently in battle.
Each return can be nil if there is no attacker or attack target for that controller.

## Parameters

- `player` `int`

## Returns

- `Card|nil` - Monster controlled by player.
- `Card|nil` - Monster controlled by the opponent.

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4959`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **56** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Duel.GetBattleMonster`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Sea Stealth Attack | `19089195` | [Scripts/c19089195.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c19089195.lua) | 57 |
| Dual Avatar - Manifested A-Un | `28798938` | [Scripts/c28798938.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c28798938.lua) | 55 |
| Sangen Furo | `55484152` | [Scripts/c55484152.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c55484152.lua) | 49 |
| Abyss Shark | `61496006` | [Scripts/c61496006.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c61496006.lua) | 46 |
| Prohibited Power Patron Portal - Terminus | `25661743` | [Scripts/c25661743.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c25661743.lua) | 46 |
| Performapal Duelist Extraordinaire | `92644052` | [Scripts/c92644052.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92644052.lua) | 45 |
| Number C79: Battlin' Boxer General Kaiser | `10300821` | [Scripts/c10300821.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c10300821.lua) | 45 |
| War Rock Meteoragon | `10497636` | [Scripts/c10497636.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c10497636.lua) | 45 |
| Infinite Antlion | `39078434` | [Scripts/c39078434.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c39078434.lua) | 45 |
| Exosister Carpedivem | `30802207` | [Scripts/c30802207.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30802207.lua) | 44 |
| War Rock Skyler | `72554862` | [Scripts/c72554862.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c72554862.lua) | 44 |
| Pennant of Revolution | `73193552` | [Scripts/c73193552.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c73193552.lua) | 44 |
| Heroic Champion - Claivesolish | `97453744` | [Scripts/c97453744.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c97453744.lua) | 43 |
| Ice Barrier | `34293667` | [Scripts/c34293667.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c34293667.lua) | 43 |
| Heroic Champion - Jarngreipr | `23848752` | [Scripts/c23848752.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c23848752.lua) | 42 |
| Fighting Flame Sword | `35697544` | [Scripts/c35697544.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c35697544.lua) | 42 |
| Tilting Entrainment | `77855162` | [Scripts/c77855162.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c77855162.lua) | 42 |
| Mementotlan Fracture Dance | `43215738` | [Scripts/c43215738.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c43215738.lua) | 41 |
| Performapal Ladyange | `58938528` | [Scripts/c58938528.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c58938528.lua) | 40 |
| Sunvine Gardna | `28168762` | [Scripts/c28168762.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c28168762.lua) | 40 |
| Swordsoul Auspice Chunjun | `29884951` | [Scripts/c29884951.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c29884951.lua) | 39 |
| Lyrilusc - Phantom Feathers | `8243121` | [Scripts/c8243121.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c8243121.lua) | 39 |
| Piercing the Darkness | `21862633` | [Scripts/c21862633.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c21862633.lua) | 38 |
| Lyrilusc - Promenade Thrush | `19369609` | [Scripts/c19369609.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c19369609.lua) | 38 |
| ...and 32 more |  |  |  |

## Script Examples

### Sea Stealth Attack (`19089195`)

Source: [Scripts/c19089195.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c19089195.lua)

```lua
function c19089195.descon(e,tp,eg,ep,ev,re,r,rp)
	if not Duel.IsEnvironment(22702055) then return false end
	local tc,bc=Duel.GetBattleMonster(tp)
	if not tc or not bc then return false end
	if tc:IsFaceup() and tc:GetOriginalLevel()>=5 and tc:IsAttribute(ATTRIBUTE_WATER) then
```

### Dual Avatar - Manifested A-Un (`28798938`)

Source: [Scripts/c28798938.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c28798938.lua)

```lua
function c28798938.atkcon(e)
	local tp=e:GetHandlerPlayer()
	local a=Duel.GetBattleMonster(tp)
	return Duel.GetCurrentPhase()==PHASE_DAMAGE_CAL and a and a:IsSetCard(0x14f)
end
```

### Sangen Furo (`55484152`)

Source: [Scripts/c55484152.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c55484152.lua)

```lua
end
function s.spcon(e,tp,eg,ep,ev,re,r,rp)
	local a=Duel.GetBattleMonster(tp)
	return a and (a:IsLocation(LOCATION_MZONE) and a:IsRace(RACE_DRAGON) and a:IsAttribute(ATTRIBUTE_FIRE)
		or not a:IsLocation(LOCATION_MZONE) and a:IsPreviousControler(tp)
```
