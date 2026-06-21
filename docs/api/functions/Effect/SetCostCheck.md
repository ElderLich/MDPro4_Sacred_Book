# Effect.SetCostCheck

## Signature

```lua
Effect.SetCostCheck(Effect e, bool b) -> void
```

## Description

Sets e's cost-check flag to b.

## Parameters

- `e` `Effect`
- `b` `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libeffect.cpp:657`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **4** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Effect.SetCostCheck`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Kewl Tune Playlist | `40847034` | [Scripts/c40847034.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c40847034.lua) | 41 |
| Kewl Tune Loudness War | `41069676` | [Scripts/c41069676.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c41069676.lua) | 38 |
| Destiny HERO - Diamond Dude | `13093792` | [Scripts/c13093792.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c13093792.lua) | 32 |
| Serial Spell | `49398568` | [Scripts/c49398568.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c49398568.lua) | 24 |

## Script Examples

### Kewl Tune Playlist (`40847034`)

Source: [Scripts/c40847034.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c40847034.lua)

```lua
		if tg then
			local cchk=e:IsCostChecked()
			e:SetCostCheck(false)
			tg(e,tp,eg,ep,ev,re,r,rp,1)
			e:SetCostCheck(cchk)
```

### Kewl Tune Loudness War (`41069676`)

Source: [Scripts/c41069676.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c41069676.lua)

```lua
	if tg then
		local cchk=e:IsCostChecked()
		e:SetCostCheck(false)
		tg(e,tp,eg,ep,ev,re,r,rp,1)
		e:SetCostCheck(cchk)
```

### Destiny HERO - Diamond Dude (`13093792`)

Source: [Scripts/c13093792.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c13093792.lua)

```lua
	local ftg=ae:GetTarget()
	if chk==0 then
		e:SetCostCheck(false)
		return not ftg or ftg(e,tp,eg,ep,ev,re,r,rp,chk)
	end
```
