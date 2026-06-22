# Duel.ChangeTargetParam

## Signature

```lua
Duel.ChangeTargetParam(int chainc, int param) -> void
```

## Description

Changes target parameter data for Chain Link count to param.

## Parameters

- `chainc` `int`
- `param` `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4926`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **1** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Duel.ChangeTargetParam`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Engraver of the Mark | `50078320` | [Scripts/c50078320.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c50078320.lua) | 38 |

## Script Examples

### Engraver of the Mark (`50078320`)

Source: [Scripts/c50078320.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c50078320.lua)

```lua
		ac=Duel.AnnounceCard(tp,table.unpack(afilter))
	end
	Duel.ChangeTargetParam(ev,ac)
end
function c50078320.desfilter(c)
```
