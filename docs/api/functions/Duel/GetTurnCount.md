# Duel.GetTurnCount

## Signature

```lua
Duel.GetTurnCount([int player]) -> int
```

## Description

Returns the current turn count.
With no player argument, this returns the duel-wide turn number; with player 0 or 1, it returns that player's personal turn count.

## Parameters

- `player` `int` optional

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4850`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **232** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Duel.GetTurnCount`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Astrograph Sorcerer](/examples/cards/76794549) | `76794549` | [Scripts/c76794549.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c76794549.lua) | 71 |
| [D/D/D/D Super-Dimensional Sovereign Emperor Zero Paradox](/examples/cards/97417863) | `97417863` | [Scripts/c97417863.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c97417863.lua) | 62 |
| [PSY-Framelord Zeta](/examples/cards/37192109) | `37192109` | [Scripts/c37192109.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c37192109.lua) | 62 |
| [The Gaze of Timaeus](/examples/cards/22283204) | `22283204` | [Scripts/c22283204.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c22283204.lua) | 62 |
| Soul of the Supreme King | `92428405` | [Scripts/c92428405.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92428405.lua) | 59 |
| K9-EW Special Release Experiment | `26585784` | [Scripts/c26585784.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c26585784.lua) | 59 |
| Fusion Destiny | `52947044` | [Scripts/c52947044.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c52947044.lua) | 59 |
| Frightfur March | `74416026` | [Scripts/c74416026.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74416026.lua) | 58 |
| The Weather Painter Moonbow | `95515518` | [Scripts/c95515518.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c95515518.lua) | 57 |
| Ghoti Fury | `65898344` | [Scripts/c65898344.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c65898344.lua) | 56 |
| Purrelyeap!? | `82983267` | [Scripts/c82983267.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c82983267.lua) | 55 |
| Raider's Knight | `28781003` | [Scripts/c28781003.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c28781003.lua) | 54 |
| Bunny Ear Enthusiast | `39643167` | [Scripts/c39643167.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c39643167.lua) | 54 |
| CXyz N.As.Ch. Knight | `61374414` | [Scripts/c61374414.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c61374414.lua) | 53 |
| Mekk-Knight Purple Nightfall | `28692962` | [Scripts/c28692962.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c28692962.lua) | 53 |
| Dangers of the Divine | `22082432` | [Scripts/c22082432.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c22082432.lua) | 53 |
| Marincess Cascade | `27012990` | [Scripts/c27012990.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c27012990.lua) | 53 |
| Snake-Eyes Vengeance Dragon | `79415624` | [Scripts/c79415624.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c79415624.lua) | 52 |
| Bujincident | `11221418` | [Scripts/c11221418.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c11221418.lua) | 52 |
| Revendread Evolution | `7986397` | [Scripts/c7986397.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c7986397.lua) | 52 |
| Metaphys Executor | `45148985` | [Scripts/c45148985.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c45148985.lua) | 52 |
| Cynet Backdoor | `43839002` | [Scripts/c43839002.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c43839002.lua) | 52 |
| Sauravis, Dragon Sage of the Voiceless Voice | `88284599` | [Scripts/c88284599.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c88284599.lua) | 51 |
| Unchained Enma Lord Yama | `94014327` | [Scripts/c94014327.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c94014327.lua) | 51 |
| ...and 208 more |  |  |  |

## Script Examples

### Astrograph Sorcerer (`76794549`)

Source: [Scripts/c76794549.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c76794549.lua)

```lua
	if not c:IsRelateToEffect(e) then return end
	if Duel.SpecialSummon(c,0,tp,tp,false,false,POS_FACEUP)~=0 then
		local g=Duel.GetMatchingGroup(c76794549.thfilter1,tp,0x70,0x70,nil,tp,Duel.GetTurnCount())
		if g:GetCount()>0 and Duel.SelectYesNo(tp,aux.Stringid(76794549,4)) then
			Duel.BreakEffect()
```

### D/D/D/D Super-Dimensional Sovereign Emperor Zero Paradox (`97417863`)

Source: [Scripts/c97417863.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c97417863.lua)

```lua
		e1:SetReset(RESET_PHASE+PHASE_END,2)
		e1:SetCountLimit(1)
		e1:SetLabel(fid,Duel.GetTurnCount())
		e1:SetLabelObject(tc)
		e1:SetCondition(c97417863.descon)
```

### PSY-Framelord Zeta (`37192109`)

Source: [Scripts/c37192109.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c37192109.lua)

```lua
		if Duel.GetTurnPlayer()==tp and Duel.GetCurrentPhase()==PHASE_STANDBY then
			e1:SetReset(RESET_PHASE+PHASE_STANDBY+RESET_SELF_TURN,2)
			e1:SetValue(Duel.GetTurnCount())
		else
			e1:SetReset(RESET_PHASE+PHASE_STANDBY+RESET_SELF_TURN)
```
