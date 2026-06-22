# Effect.UseCountLimit

## Signature

```lua
Effect.UseCountLimit(Effect e, int p, [int count], [bool oath_only]) -> void
```

## Description

Manually consumes count uses of e's count limit for player p.
count defaults to 1. If oath_only is true, the count is consumed only when e's count code includes EFFECT_COUNT_CODE_OATH; otherwise the binding decrements the count limit directly.

## Parameters

- `e` `Effect`
- `p` `int`
- `count` `int` optional - default: 1
- `oath_only` `bool` optional - default: false

## Source

- `D:\Programs\GitHub\ygopro-core\libeffect.cpp:661`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **83** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Effect.UseCountLimit`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Ghostrick Renovation](/examples/cards/61818176) | `61818176` | [Scripts/c61818176.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c61818176.lua) | 65 |
| [Ursarctic Polari](/examples/cards/27693363) | `27693363` | [Scripts/c27693363.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c27693363.lua) | 65 |
| [Prank-Kids Weather Washer](/examples/cards/44509529) | `44509529` | [Scripts/c44509529.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44509529.lua) | 65 |
| [Junoldo the Shadespirit Power Patron](/examples/cards/10266279) | `10266279` | [Scripts/c10266279.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c10266279.lua) | 62 |
| [Ursarctic Polar Star](/examples/cards/62714453) | `62714453` | [Scripts/c62714453.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c62714453.lua) | 62 |
| [Prank-Kids Rocket Ride](/examples/cards/18514525) | `18514525` | [Scripts/c18514525.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c18514525.lua) | 61 |
| [Jupredo the Shademachine Power Patron](/examples/cards/43871165) | `43871165` | [Scripts/c43871165.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c43871165.lua) | 60 |
| Prank-Kids Bow-Wow-Bark | `43886072` | [Scripts/c43886072.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c43886072.lua) | 58 |
| Sea Stealth Attack | `19089195` | [Scripts/c19089195.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c19089195.lua) | 57 |
| Ursarctic Grand Chariot | `80086070` | [Scripts/c80086070.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c80086070.lua) | 57 |
| Lunalight Masquerade | `2344618` | [Scripts/c2344618.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c2344618.lua) | 57 |
| Amazoness Secret Arts | `86758746` | [Scripts/c86758746.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c86758746.lua) | 57 |
| Nervedo the Shadebeast Power Patron | `17473466` | [Scripts/c17473466.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c17473466.lua) | 56 |
| Favorite Hero | `11881272` | [Scripts/c11881272.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c11881272.lua) | 55 |
| Malefic Paradigm Dragon | `16958382` | [Scripts/c16958382.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c16958382.lua) | 55 |
| Triamid Dancer | `69529337` | [Scripts/c69529337.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c69529337.lua) | 55 |
| Vernusylph of the Thawing Mountains | `9238125` | [Scripts/c9238125.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c9238125.lua) | 55 |
| Prank-Kids Dodo-Doodle-Doo | `17382973` | [Scripts/c17382973.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c17382973.lua) | 55 |
| Vernusylph of the Awakening Forests | `36745317` | [Scripts/c36745317.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c36745317.lua) | 53 |
| Witchcrafter Pittore | `95245544` | [Scripts/c95245544.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c95245544.lua) | 52 |
| Witchcrafter Genni | `64756282` | [Scripts/c64756282.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c64756282.lua) | 52 |
| Numeron Wall | `42352091` | [Scripts/c42352091.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c42352091.lua) | 50 |
| Witchcrafter Madame Verre | `21522601` | [Scripts/c21522601.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c21522601.lua) | 49 |
| Cyberdark Chimera | `5370235` | [Scripts/c5370235.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c5370235.lua) | 49 |
| ...and 59 more |  |  |  |

## Script Examples

### Ghostrick Renovation (`61818176`)

Source: [Scripts/c61818176.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c61818176.lua)

```lua
			Duel.MoveToField(sc,tp,tp,LOCATION_FZONE,POS_FACEUP,true)
			local te=sc:GetActivateEffect()
			te:UseCountLimit(tp,1,true)
			local tep=sc:GetControler()
			local cost=te:GetCost()
```

### Ursarctic Polari (`27693363`)

Source: [Scripts/c27693363.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c27693363.lua)

```lua
		end
		Duel.MoveToField(tc,tp,tp,LOCATION_FZONE,POS_FACEUP,true)
		te:UseCountLimit(tp,1,true)
		local tep=tc:GetControler()
		local cost=te:GetCost()
```

### Prank-Kids Weather Washer (`44509529`)

Source: [Scripts/c44509529.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44509529.lua)

```lua
	local te=tc:IsHasEffect(25725326,tp)
	if te then
		te:UseCountLimit(tp)
		Duel.Remove(tc,POS_FACEUP,REASON_COST+REASON_REPLACE)
	else
```
