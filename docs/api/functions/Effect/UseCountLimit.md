# Effect.UseCountLimit

## Signature

```lua
Effect.UseCountLimit(Effect e, int p, [int count], [bool oath_only]) -> void
```

## Description

Manually consumes count uses of e's count limit for player p.
count defaults to 1. If oath_only is true, the count is consumed only when e's count code includes EFFECT_COUNT_CODE_OATH; otherwise the binding decrements the count limit directly.

## How To Use It

Use this to manually spend an Effect's count limit after a separate `Effect.CheckCountLimit` test.

```lua
if e:CheckCountLimit(tp) then
    e:UseCountLimit(tp,1)
end
```

The optional count defaults to 1. With `oath_only=true`, the local binding spends the count only when the effect's count code includes `EFFECT_COUNT_CODE_OATH`.

## Related Functions

- [Effect.SetCountLimit](/api/functions/Effect/SetCountLimit)
- [Effect.CheckCountLimit](/api/functions/Effect/CheckCountLimit)

## Parameters

- `e` `Effect` - Effect whose count is manually consumed.
- `p` `int` - Player whose local or shared count is consumed.
- `count` `int` optional - Number of uses to consume; default: 1.
- `oath_only` `bool` optional - If true, consume only when e's count code includes EFFECT_COUNT_CODE_OATH; default: false.

## Source

- `D:\Programs\GitHub\ygopro-core\libeffect.cpp:661`

## Guided Examples

Learn how to use this function in context:

- [Common Script Errors And Debugging](/learn/common-script-errors-and-debugging)
- [Count Limits And Once Per Turn](/learn/count-limits)
- [Field Spells](/learn/field-spells)
- [Pendulum Procedure Guide](/learn/pendulum-procedure)

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **86** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Effect.UseCountLimit) with `Effect.UseCountLimit`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Levia-Dragoon - Daedalus](/examples/cards/78579058) | `78579058` | [Scripts/c78579058.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c78579058.lua) | 1 |
| [Azure Ocean Dragon Lord - Neo-Daedalus Rage](/examples/cards/41570943) | `41570943` | [Scripts/c41570943.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c41570943.lua) | 1 |
| [Ghostrick Renovation](/examples/cards/61818176) | `61818176` | [Scripts/c61818176.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c61818176.lua) | 1 |
| [Ursarctic Polari](/examples/cards/27693363) | `27693363` | [Scripts/c27693363.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c27693363.lua) | 2 |
| [Prank-Kids Weather Washer](/examples/cards/44509529) | `44509529` | [Scripts/c44509529.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c44509529.lua) | 1 |
| [Junoldo the Shadespirit Power Patron](/examples/cards/10266279) | `10266279` | [Scripts/c10266279.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c10266279.lua) | 1 |
| [Ursarctic Polar Star](/examples/cards/62714453) | `62714453` | [Scripts/c62714453.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c62714453.lua) | 1 |
| Prank-Kids Rocket Ride | `18514525` | [Scripts/c18514525.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c18514525.lua) | 1 |
| Jupredo the Shademachine Power Patron | `43871165` | [Scripts/c43871165.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c43871165.lua) | 1 |
| Prank-Kids Bow-Wow-Bark | `43886072` | [Scripts/c43886072.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c43886072.lua) | 1 |
| Sea Stealth Attack | `19089195` | [Scripts/c19089195.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c19089195.lua) | 1 |
| Ursarctic Grand Chariot | `80086070` | [Scripts/c80086070.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c80086070.lua) | 1 |
| Lunalight Masquerade | `2344618` | [Scripts/c2344618.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c2344618.lua) | 1 |
| Amazoness Secret Arts | `86758746` | [Scripts/c86758746.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c86758746.lua) | 1 |
| Nervedo the Shadebeast Power Patron | `17473466` | [Scripts/c17473466.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c17473466.lua) | 1 |
| Witchcrafter Pittore | `95245544` | [Scripts/c95245544.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c95245544.lua) | 1 |
| Witchcrafter Genni | `64756282` | [Scripts/c64756282.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c64756282.lua) | 1 |
| Favorite Hero | `11881272` | [Scripts/c11881272.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c11881272.lua) | 1 |
| Malefic Paradigm Dragon | `16958382` | [Scripts/c16958382.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c16958382.lua) | 1 |
| Triamid Dancer | `69529337` | [Scripts/c69529337.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c69529337.lua) | 1 |
| Vernusylph of the Thawing Mountains | `9238125` | [Scripts/c9238125.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c9238125.lua) | 1 |
| Prank-Kids Dodo-Doodle-Doo | `17382973` | [Scripts/c17382973.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c17382973.lua) | 1 |
| Vernusylph of the Awakening Forests | `36745317` | [Scripts/c36745317.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c36745317.lua) | 1 |
| Witchcrafter Madame Verre | `21522601` | [Scripts/c21522601.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c21522601.lua) | 1 |
| ...and 62 more |  |  |  |

## Script Examples

### Levia-Dragoon - Daedalus (`78579058`)

Source: [Scripts/c78579058.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c78579058.lua)

```lua
			local related,valid=f(te,lc,sg,tc,tp)
			if related and valid then
				te:UseCountLimit(tp)
			end
		end
```

### Azure Ocean Dragon Lord - Neo-Daedalus Rage (`41570943`)

Source: [Scripts/c41570943.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c41570943.lua)

```lua
			local related,valid=f(te,lc,sg,tc,tp)
			if related and valid then
				te:UseCountLimit(tp)
			end
		end
```

### Ghostrick Renovation (`61818176`)

Source: [Scripts/c61818176.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c61818176.lua)

```lua
			Duel.MoveToField(sc,tp,tp,LOCATION_FZONE,POS_FACEUP,true)
			local te=sc:GetActivateEffect()
			te:UseCountLimit(tp,1,true)
			local tep=sc:GetControler()
			local cost=te:GetCost()
```
