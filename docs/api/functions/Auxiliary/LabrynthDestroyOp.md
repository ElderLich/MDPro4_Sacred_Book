# Auxiliary.LabrynthDestroyOp

## Signature

```lua
Auxiliary.LabrynthDestroyOp(Effect e, int tp, any res) -> void
```

## Description

Shared extra destroy operation for the Labrynth field effect. After a non-hand-activated Welcome Labrynth Normal Trap resolves, it can destroy one card on the field and consumes the field effect's count limit.

## Parameters

- `e` `Effect`
- `tp` `int`
- `res` `any`

## Source

- `Utilities/utility.lua:1099`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **3** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Auxiliary.LabrynthDestroyOp) with `Auxiliary.LabrynthDestroyOp`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Welcome Labrynth | `5380979` | [Scripts/c5380979.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c5380979.lua) | 1 |
| Big Welcome Labrynth | `92714517` | [Scripts/c92714517.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92714517.lua) | 1 |
| Farewelcome Labrynth | `32785578` | [Scripts/c32785578.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c32785578.lua) | 1 |

## Script Examples

### Welcome Labrynth (`5380979`)

Source: [Scripts/c5380979.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c5380979.lua)

```lua
		end
	end
	aux.LabrynthDestroyOp(e,tp,res)
	if e:IsHasType(EFFECT_TYPE_ACTIVATE) then
		local e1=Effect.CreateEffect(c)
```

### Big Welcome Labrynth (`92714517`)

Source: [Scripts/c92714517.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92714517.lua)

```lua
		end
	end
	aux.LabrynthDestroyOp(e,tp,res)
end
function s.checkfilter(c)
```

### Farewelcome Labrynth (`32785578`)

Source: [Scripts/c32785578.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c32785578.lua)

```lua
		end
	end
	aux.LabrynthDestroyOp(e,tp,res)
end
```
