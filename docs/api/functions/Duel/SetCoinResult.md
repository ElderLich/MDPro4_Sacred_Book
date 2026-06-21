# Duel.SetCoinResult

## Signature

```lua
Duel.SetCoinResult(int res, ... any) -> void
```

## Description

Forcibly modify the result of casting coins to res
This function is used in the persistent EVENT_TOSS_COIN event

## Parameters

- `res` `int`
- `...` `any`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5041`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **1** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Duel.SetCoinResult`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Proton Blast | `49511705` | [Scripts/c49511705.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c49511705.lua) | 32 |

## Script Examples

### Proton Blast (`49511705`)

Source: [Scripts/c49511705.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c49511705.lua)

```lua
		res[i]=1
	end
	Duel.SetCoinResult(table.unpack(res))
end
```
