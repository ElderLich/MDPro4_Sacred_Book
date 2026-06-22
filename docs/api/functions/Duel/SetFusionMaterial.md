# Duel.SetFusionMaterial

## Signature

```lua
Duel.SetFusionMaterial(Group g) -> void
```

## Description

Replaces the core's current Fusion Material set with the cards in g.

## Parameters

- `g` `Group`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4990`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **5** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Duel.SetFusionMaterial`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [El Shaddoll Apkallone](/examples/cards/50907446) | `50907446` | [Scripts/c50907446.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c50907446.lua) | 68 |
| [El Shaddoll Meshachrer](/examples/cards/32467459) | `32467459` | [Scripts/c32467459.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c32467459.lua) | 61 |
| Alba System Dogmatikalamity | `93053159` | [Scripts/c93053159.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93053159.lua) | 58 |
| Dragon Master Magia | `12381100` | [Scripts/c12381100.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c12381100.lua) | 57 |
| Invoked Transcendence Aeon | `33166263` | [Scripts/c33166263.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c33166263.lua) | 55 |

## Script Examples

### El Shaddoll Apkallone (`50907446`)

Source: [Scripts/c50907446.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c50907446.lua)

```lua
		g:Merge(sg)
	end
	Duel.SetFusionMaterial(g)
end
```

### El Shaddoll Meshachrer (`32467459`)

Source: [Scripts/c32467459.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c32467459.lua)

```lua
		fc:RemoveCounter(tp,0x16,3,REASON_EFFECT)
	end
	Duel.SetFusionMaterial(g)
end
```

### Alba System Dogmatikalamity (`93053159`)

Source: [Scripts/c93053159.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93053159.lua)

```lua
			end
			g:Merge(sg)
			Duel.SetFusionMaterial(g)
		end
end
```
