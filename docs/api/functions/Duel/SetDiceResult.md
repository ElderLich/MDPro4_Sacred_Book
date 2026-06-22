# Duel.SetDiceResult

## Signature

```lua
Duel.SetDiceResult([int res1], [int res2], [int res3], [int res4], [int res5]) -> void
```

## Description

Sets the five stored dice-result slots; missing or out-of-range values are stored as 1.

## Parameters

- `res1` `int` optional
- `res2` `int` optional
- `res3` `int` optional
- `res4` `int` optional
- `res5` `int` optional

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5042`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **2** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Duel.SetDiceResult`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Number 67: Pair-a-Dice Smasher | `35772782` | [Scripts/c35772782.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c35772782.lua) | 34 |
| That Six | `39454112` | [Scripts/c39454112.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c39454112.lua) | 14 |

## Script Examples

### Number 67: Pair-a-Dice Smasher (`35772782`)

Source: [Scripts/c35772782.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c35772782.lua)

```lua
		end
		dc[ac]=7
		Duel.SetDiceResult(table.unpack(dc))
	end
end
```

### That Six (`39454112`)

Source: [Scripts/c39454112.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c39454112.lua)

```lua
		if dc[ac]==1 or dc[ac]==3 or dc[ac]==5 then dc[ac]=6
		else dc[ac]=1 end
		Duel.SetDiceResult(table.unpack(dc))
	end
end
```
