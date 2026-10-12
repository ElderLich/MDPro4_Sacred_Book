# Duel.SkipPhase

## Signature

```lua
Duel.SkipPhase(int player, int phase, int reset_flag, int reset_count, [int value]) -> void
```

## Description

Applies a temporary field effect that makes player skip phase.
The phase must be one of PHASE_DRAW, PHASE_STANDBY, PHASE_MAIN1, PHASE_BATTLE, PHASE_MAIN2, or PHASE_END. reset_count values of 0 or less are treated as 1, and value is stored on the generated skip effect.

## Parameters

- `player` `int`
- `phase` `int`
- `reset_flag` `int`
- `reset_count` `int`
- `value` `int` optional - default: 0

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4955`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **56** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Duel.SkipPhase) with `Duel.SkipPhase`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Veda Kalarcanum | `40785230` | [Scripts/c40785230.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c40785230.lua) | 5 |
| PSY-Framegear Beta | `2810642` | [Scripts/c2810642.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c2810642.lua) | 1 |
| Doll House | `67331360` | [Scripts/c67331360.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c67331360.lua) | 1 |
| Numeron Wall | `42352091` | [Scripts/c42352091.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c42352091.lua) | 1 |
| Red Nova Dragon/Assault Mode | `82323997` | [Scripts/c82323997.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c82323997.lua) | 1 |
| Melffy Footsteps | `25687946` | [Scripts/c25687946.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c25687946.lua) | 3 |
| Cosmic Blazar Dragon | `21123811` | [Scripts/c21123811.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c21123811.lua) | 1 |
| Sangen Kaiho | `25388971` | [Scripts/c25388971.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c25388971.lua) | 1 |
| Champion's Pulse | `46001505` | [Scripts/c46001505.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c46001505.lua) | 1 |
| Gatling Ogre | `88931417` | [Scripts/c88931417.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c88931417.lua) | 1 |
| Sunvine Gardna | `28168762` | [Scripts/c28168762.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c28168762.lua) | 1 |
| Nekroz of Valkyrus | `25857246` | [Scripts/c25857246.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c25857246.lua) | 1 |
| Hidden Fangs of Revenge | `47128571` | [Scripts/c47128571.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c47128571.lua) | 3 |
| Dinowrestler Martial Anga | `11755663` | [Scripts/c11755663.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c11755663.lua) | 1 |
| Photon Timestop | `8653757` | [Scripts/c8653757.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c8653757.lua) | 5 |
| Light Wing Shield | `83880087` | [Scripts/c83880087.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c83880087.lua) | 3 |
| A.I.'s Show | `54374642` | [Scripts/c54374642.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c54374642.lua) | 1 |
| Performapal Classikuriboh | `55554175` | [Scripts/c55554175.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c55554175.lua) | 1 |
| Shinobird Salvation | `276357` | [Scripts/c276357.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c276357.lua) | 1 |
| Cyber Valley | `3657444` | [Scripts/c3657444.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c3657444.lua) | 1 |
| Photon Jumper | `97639441` | [Scripts/c97639441.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c97639441.lua) | 1 |
| Smoke Mosquito | `28427869` | [Scripts/c28427869.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c28427869.lua) | 1 |
| Dragonox, the Empowered Warrior | `92870717` | [Scripts/c92870717.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c92870717.lua) | 1 |
| Battle Break | `22047978` | [Scripts/c22047978.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c22047978.lua) | 1 |
| ...and 32 more |  |  |  |

## Script Examples

### Veda Kalarcanum (`40785230`)

Source: [Scripts/c40785230.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c40785230.lua)

```lua
function c40785230.etop(e,tp,eg,ep,ev,re,r,rp)
	local turnp=Duel.GetTurnPlayer()
	Duel.SkipPhase(turnp,PHASE_DRAW,RESET_PHASE+PHASE_END,1)
	Duel.SkipPhase(turnp,PHASE_STANDBY,RESET_PHASE+PHASE_END,1)
	Duel.SkipPhase(turnp,PHASE_MAIN1,RESET_PHASE+PHASE_END,1)
```

### PSY-Framegear Beta (`2810642`)

Source: [Scripts/c2810642.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c2810642.lua)

```lua
	if dc:IsRelateToEffect(e) and Duel.Destroy(dc,REASON_EFFECT)~=0 then
		Duel.BreakEffect()
		Duel.SkipPhase(1-tp,PHASE_BATTLE,RESET_PHASE+PHASE_BATTLE_STEP,1)
	end
end
```

### Doll House (`67331360`)

Source: [Scripts/c67331360.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c67331360.lua)

```lua
		if tc and not tc:IsImmuneToEffect(e) and Duel.Overlay(tc,g1)~=0 then
			Duel.BreakEffect()
			Duel.SkipPhase(1-tp,PHASE_BATTLE,RESET_PHASE+PHASE_BATTLE_STEP,1)
		end
	end
```
