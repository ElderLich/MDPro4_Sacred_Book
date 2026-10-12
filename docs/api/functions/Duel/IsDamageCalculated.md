# Duel.IsDamageCalculated

## Signature

```lua
Duel.IsDamageCalculated() -> bool
```

## Description

Returns whether damage calculation has been performed in the current battle/damage-step state.
Use it with Duel.GetCurrentPhase in Damage Step conditions, especially for ATK/DEF-changing effects that stop being legal after damage calculation.

## Returns

- `bool` - true after damage calculation has been performed in the current battle timing.

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4956`

## Guided Examples

Learn how to use this function in context:

- [Activation Legality](/learn/activation-legality)
- [Chain Timing And Activation Windows](/learn/chain-timing-and-activation-windows)

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **42** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Duel.IsDamageCalculated) with `Duel.IsDamageCalculated`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Assault Spirits | `87043568` | [Scripts/c87043568.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c87043568.lua) | 1 |
| Flower Cardian Cherry Blossom with Curtain | `5489987` | [Scripts/c5489987.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c5489987.lua) | 1 |
| At One With the Sword | `6112401` | [Scripts/c6112401.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c6112401.lua) | 1 |
| Guilt of the Sinful Spoils | `88695895` | [Scripts/c88695895.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c88695895.lua) | 1 |
| Psychic Commander | `21454943` | [Scripts/c21454943.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c21454943.lua) | 1 |
| Ocean Dragon Lord - Kairyu-Shin | `23931679` | [Scripts/c23931679.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c23931679.lua) | 1 |
| Gouki Iron Claw | `71555408` | [Scripts/c71555408.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c71555408.lua) | 1 |
| Attack of the Cornered Rat | `84389640` | [Scripts/c84389640.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c84389640.lua) | 1 |
| Superheavy Samurai Soulbuster Gauntlet | `35800511` | [Scripts/c35800511.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c35800511.lua) | 1 |
| Bark of Dark Ruler | `41925941` | [Scripts/c41925941.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c41925941.lua) | 1 |
| Shinobird Crow | `39817919` | [Scripts/c39817919.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c39817919.lua) | 1 |
| Trickstar Corobane | `98169343` | [Scripts/c98169343.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c98169343.lua) | 1 |
| Mecha Phantom Beast Tetherwolf | `67922702` | [Scripts/c67922702.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c67922702.lua) | 1 |
| Yosenju Tsujik | `25244515` | [Scripts/c25244515.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c25244515.lua) | 1 |
| Dark Honest | `26914168` | [Scripts/c26914168.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c26914168.lua) | 1 |
| Scrap Shark | `69155991` | [Scripts/c69155991.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c69155991.lua) | 1 |
| Dragunity Knight - Gae Bulg | `900787` | [Scripts/c900787.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c900787.lua) | 1 |
| Indomitable Gladiator Beast | `55136228` | [Scripts/c55136228.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c55136228.lua) | 1 |
| Bujingi Sinyou | `56574543` | [Scripts/c56574543.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c56574543.lua) | 1 |
| Reaper on the Nightmare | `85684223` | [Scripts/c85684223.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c85684223.lua) | 1 |
| There Can Be Only One | `24207889` | [Scripts/c24207889.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c24207889.lua) | 1 |
| Honest | `37742478` | [Scripts/c37742478.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c37742478.lua) | 1 |
| Constellar Praesepe | `2091298` | [Scripts/c2091298.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c2091298.lua) | 1 |
| Spirit Reaper | `23205979` | [Scripts/c23205979.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c23205979.lua) | 1 |
| ...and 18 more |  |  |  |

## Script Examples

### Assault Spirits (`87043568`)

Source: [Scripts/c87043568.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c87043568.lua)

```lua
	local ph=Duel.GetCurrentPhase()
	return a==e:GetHandler():GetEquipTarget()
		and ph==PHASE_DAMAGE and not Duel.IsDamageCalculated()
end
function c87043568.cfilter(c)
```

### Flower Cardian Cherry Blossom with Curtain (`5489987`)

Source: [Scripts/c5489987.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c5489987.lua)

```lua
function c5489987.atkcon(e,tp,eg,ep,ev,re,r,rp)
	local phase=Duel.GetCurrentPhase()
	if phase~=PHASE_DAMAGE or Duel.IsDamageCalculated() then return false end
	local tc=Duel.GetAttackTarget()
	if not tc then return false end
```

### At One With the Sword (`6112401`)

Source: [Scripts/c6112401.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c6112401.lua)

```lua
end
function c6112401.condition(e,tp,eg,ep,ev,re,r,rp)
	if Duel.GetCurrentPhase()==PHASE_DAMAGE and Duel.IsDamageCalculated() then return false end
	local g=Duel.GetFieldGroup(tp,LOCATION_MZONE,0)
	local tc=g:GetFirst()
```
