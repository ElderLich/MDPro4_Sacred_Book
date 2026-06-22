# Card.ResetFlagEffect

## Signature

```lua
Card.ResetFlagEffect(Card c, int code) -> void
```

## Description

Manually clear the type of c is the code of the identification effect

## Parameters

- `c` `Card`
- `code` `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3554`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **39** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.ResetFlagEffect`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Goyo Emperor](/examples/cards/59255742) | `59255742` | [Scripts/c59255742.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59255742.lua) | 70 |
| [W:P Fancy Ball](/examples/cards/4993187) | `4993187` | [Scripts/c4993187.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c4993187.lua) | 61 |
| Trickstar Light Stage | `35371948` | [Scripts/c35371948.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c35371948.lua) | 60 |
| Trickstar Light Arena | `63492244` | [Scripts/c63492244.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63492244.lua) | 59 |
| LaSolfachord Angelia | `27993919` | [Scripts/c27993919.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c27993919.lua) | 51 |
| TiSolfachord Beautia | `54387923` | [Scripts/c54387923.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c54387923.lua) | 50 |
| Ghost Mourner &amp; Moonlit Chill | `52038441` | [Scripts/c52038441.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c52038441.lua) | 50 |
| Sky Striker Ace - Camellia | `63013339` | [Scripts/c63013339.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63013339.lua) | 48 |
| Tyrant Wing | `57470761` | [Scripts/c57470761.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c57470761.lua) | 48 |
| Time Magic Hammer | `10960419` | [Scripts/c10960419.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c10960419.lua) | 47 |
| Matriarch of Nephthys | `52904476` | [Scripts/c52904476.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c52904476.lua) | 46 |
| Ultimate Divine-Beast | `32247099` | [Scripts/c32247099.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c32247099.lua) | 45 |
| Chronicler of Nephthys | `25397880` | [Scripts/c25397880.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c25397880.lua) | 43 |
| GMX Lab #5 | `74378580` | [Scripts/c74378580.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74378580.lua) | 43 |
| Cerulean Sacred Phoenix of Nephthys | `24175232` | [Scripts/c24175232.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24175232.lua) | 42 |
| Trick Box | `93983867` | [Scripts/c93983867.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93983867.lua) | 42 |
| Speedroid Maliciousmagnet | `62899696` | [Scripts/c62899696.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c62899696.lua) | 40 |
| Superheavy Samurai Stealth Ninja | `50065971` | [Scripts/c50065971.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c50065971.lua) | 38 |
| Defender of Nephthys | `51782995` | [Scripts/c51782995.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c51782995.lua) | 38 |
| Disciple of Nephthys | `98999181` | [Scripts/c98999181.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c98999181.lua) | 37 |
| Shinobaron Shade Peacock | `60823690` | [Scripts/c60823690.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c60823690.lua) | 36 |
| Dark Nephthys | `38107923` | [Scripts/c38107923.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c38107923.lua) | 36 |
| Fire King High Avatar Garunix | `23015896` | [Scripts/c23015896.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c23015896.lua) | 36 |
| Arcana Force EX - The Dark Ruler | `69831560` | [Scripts/c69831560.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c69831560.lua) | 35 |
| ...and 15 more |  |  |  |

## Script Examples

### Goyo Emperor (`59255742`)

Source: [Scripts/c59255742.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59255742.lua)

```lua
		local tg=e1:GetLabelObject()
		for tc in aux.Next(tg) do
			tc:ResetFlagEffect(59255742)
		end
		tg:DeleteGroup()
```

### W:P Fancy Ball (`4993187`)

Source: [Scripts/c4993187.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c4993187.lua)

```lua
	local res=Duel.IsExistingMatchingCard(s.lkfilter,tp,LOCATION_EXTRA,0,1,nil)
	le:Reset()
	c:ResetFlagEffect(id)
	if chk==0 then return res end
	Duel.SetOperationInfo(0,CATEGORY_SPECIAL_SUMMON,nil,1,0,0)
```

### Trickstar Light Stage (`35371948`)

Source: [Scripts/c35371948.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c35371948.lua)

```lua
		c:SetCardTarget(tc)
		e:SetLabelObject(tc)
		c:ResetFlagEffect(35371948)
		tc:ResetFlagEffect(35371948)
		local fid=c:GetFieldID()
```
