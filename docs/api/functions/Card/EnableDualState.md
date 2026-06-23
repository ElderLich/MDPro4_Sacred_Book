# Card.EnableDualState

## Signature

```lua
Card.EnableDualState(Card c) -> void
```

## Description

Registers EFFECT_DUAL_STATUS on c so local Gemini/Dual checks treat it as having gained its effects.
This does not perform a Normal Summon or spend a Normal Summon. Use it only for effects that explicitly make a Gemini Monster be treated as having been Normal Summoned again.
The registered status effect includes the local client hint and resets with the normal card event reset.

## Parameters

- `c` `Card` - Gemini Monster that should immediately gain Dual State.

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3511`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **8** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.EnableDualState`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Burnout | `25669282` | [Scripts/c25669282.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c25669282.lua) | 46 |
| Gemini Ablation | `80758812` | [Scripts/c80758812.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c80758812.lua) | 45 |
| Sublimation Knight | `54485355` | [Scripts/c54485355.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c54485355.lua) | 44 |
| Gemini Booster | `18096222` | [Scripts/c18096222.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c18096222.lua) | 43 |
| Black Brutdrago | `96029574` | [Scripts/c96029574.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c96029574.lua) | 39 |
| Unleash Your Power! | `73567374` | [Scripts/c73567374.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c73567374.lua) | 38 |
| Blazewing Butterfly | `16984449` | [Scripts/c16984449.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c16984449.lua) | 31 |
| Super Double Summon | `26120084` | [Scripts/c26120084.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c26120084.lua) | 23 |

## Script Examples

### Burnout (`25669282`)

Source: [Scripts/c25669282.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c25669282.lua)

```lua
	local tc=Duel.GetFirstTarget()
	if tc:IsRelateToEffect(e) and Duel.SpecialSummonStep(tc,0,tp,tp,false,false,POS_FACEUP) then
		tc:EnableDualState()
	end
	Duel.SpecialSummonComplete()
```

### Gemini Ablation (`80758812`)

Source: [Scripts/c80758812.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c80758812.lua)

```lua
	local tc=g:GetFirst()
	if tc and Duel.SpecialSummonStep(tc,0,tp,tp,false,false,POS_FACEUP) then
		tc:EnableDualState()
	end
	Duel.SpecialSummonComplete()
```

### Sublimation Knight (`54485355`)

Source: [Scripts/c54485355.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c54485355.lua)

```lua
		while tc do
			if Duel.SpecialSummonStep(tc,0,tp,tp,false,false,POS_FACEUP) then
				tc:EnableDualState()
			end
			tc=spg:GetNext()
```
