# Card.ResetFlagEffect

## Signature

```lua
Card.ResetFlagEffect(Card c, int code) -> void
```

## Description

Resets all flag effects on c with code.
This clears matching card markers manually; it does not affect player markers registered with Duel.RegisterFlagEffect.

## How To Use It

Use this to clear all card markers with the matching code before their natural reset would remove them.

```lua
c:ResetFlagEffect(id)
```

This is a manual clear for flag effects, not a replacement for choosing the right reset mask when the marker is registered.

## Related Functions

- [Card.RegisterFlagEffect](/api/functions/Card/RegisterFlagEffect)
- [Card.GetFlagEffect](/api/functions/Card/GetFlagEffect)

## Parameters

- `c` `Card` - Card whose matching flag effects are reset.
- `code` `int` - Flag-effect code to clear.

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3609`

## Guided Examples

Learn how to use this function in context:

- [Reset Flags And Effect Duration](/learn/reset-flags-and-duration)

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **39** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Card.ResetFlagEffect) with `Card.ResetFlagEffect`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Goyo Emperor](/examples/cards/59255742) | `59255742` | [Scripts/c59255742.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c59255742.lua) | 1 |
| [W:P Fancy Ball](/examples/cards/4993187) | `4993187` | [Scripts/c4993187.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c4993187.lua) | 1 |
| Trickstar Light Stage | `35371948` | [Scripts/c35371948.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c35371948.lua) | 3 |
| Trickstar Light Arena | `63492244` | [Scripts/c63492244.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c63492244.lua) | 3 |
| LaSolfachord Angelia | `27993919` | [Scripts/c27993919.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c27993919.lua) | 1 |
| TiSolfachord Beautia | `54387923` | [Scripts/c54387923.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c54387923.lua) | 1 |
| Ghost Mourner &amp; Moonlit Chill | `52038441` | [Scripts/c52038441.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c52038441.lua) | 1 |
| Sky Striker Ace - Camellia | `63013339` | [Scripts/c63013339.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c63013339.lua) | 1 |
| Tyrant Wing | `57470761` | [Scripts/c57470761.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c57470761.lua) | 1 |
| Time Magic Hammer | `10960419` | [Scripts/c10960419.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c10960419.lua) | 1 |
| Matriarch of Nephthys | `52904476` | [Scripts/c52904476.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c52904476.lua) | 1 |
| Ultimate Divine-Beast | `32247099` | [Scripts/c32247099.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c32247099.lua) | 1 |
| Chronicler of Nephthys | `25397880` | [Scripts/c25397880.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c25397880.lua) | 1 |
| GMX Lab #5 | `74378580` | [Scripts/c74378580.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c74378580.lua) | 2 |
| Cerulean Sacred Phoenix of Nephthys | `24175232` | [Scripts/c24175232.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c24175232.lua) | 1 |
| Trick Box | `93983867` | [Scripts/c93983867.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c93983867.lua) | 1 |
| Speedroid Maliciousmagnet | `62899696` | [Scripts/c62899696.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c62899696.lua) | 2 |
| Superheavy Samurai Stealth Ninja | `50065971` | [Scripts/c50065971.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c50065971.lua) | 1 |
| Defender of Nephthys | `51782995` | [Scripts/c51782995.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c51782995.lua) | 1 |
| Disciple of Nephthys | `98999181` | [Scripts/c98999181.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c98999181.lua) | 1 |
| Shinobaron Shade Peacock | `60823690` | [Scripts/c60823690.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c60823690.lua) | 1 |
| Dark Nephthys | `38107923` | [Scripts/c38107923.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c38107923.lua) | 1 |
| Fire King High Avatar Garunix | `23015896` | [Scripts/c23015896.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c23015896.lua) | 1 |
| Arcana Force EX - The Dark Ruler | `69831560` | [Scripts/c69831560.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c69831560.lua) | 1 |
| ...and 15 more |  |  |  |

## Script Examples

### Goyo Emperor (`59255742`)

Source: [Scripts/c59255742.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c59255742.lua)

```lua
		local tg=e1:GetLabelObject()
		for tc in aux.Next(tg) do
			tc:ResetFlagEffect(59255742)
		end
		tg:DeleteGroup()
```

### W:P Fancy Ball (`4993187`)

Source: [Scripts/c4993187.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c4993187.lua)

```lua
	local res=Duel.IsExistingMatchingCard(s.lkfilter,tp,LOCATION_EXTRA,0,1,nil)
	le:Reset()
	c:ResetFlagEffect(id)
	if chk==0 then return res end
	Duel.SetOperationInfo(0,CATEGORY_SPECIAL_SUMMON,nil,1,0,0)
```

### Trickstar Light Stage (`35371948`)

Source: [Scripts/c35371948.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c35371948.lua)

```lua
		c:SetCardTarget(tc)
		e:SetLabelObject(tc)
		c:ResetFlagEffect(35371948)
		tc:ResetFlagEffect(35371948)
		local fid=c:GetFieldID()
```
