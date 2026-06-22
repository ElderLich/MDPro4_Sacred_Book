# Effect.CheckCountLimit

## Signature

```lua
Effect.CheckCountLimit(Effect e, int p) -> bool
```

## Description

Checks whether e's count limit is still available for player p.

## Parameters

- `e` `Effect`
- `p` `int`

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libeffect.cpp:660`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **1** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Effect.CheckCountLimit`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Xyz Block | `44487250` | [Scripts/c44487250.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44487250.lua) | 23 |

## Script Examples

### Xyz Block (`44487250`)

Source: [Scripts/c44487250.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44487250.lua)

```lua
			for _,te in ipairs(fromhand_effects) do
				local cost=te:GetCost()
				if te:CheckCountLimit(tp) and (not cost or cost(te,tp,eg,ep,ev,re,r,rp,0,e)) then
					table.insert(available_fromhand_effects,te)
				end
```
