# Duel.GetDiceResult

## Signature

```lua
Duel.GetDiceResult() -> int,int,int,int,int
```

## Description

Returns the five stored dice-result slots for the current dice event.

## Returns

- `int` - First dice result.
- `int` - Second dice result.
- `int` - Third dice result.
- `int` - Fourth dice result.
- `int` - Fifth dice result.

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5040`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **2** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Duel.GetDiceResult) with `Duel.GetDiceResult`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Number 67: Pair-a-Dice Smasher | `35772782` | [Scripts/c35772782.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c35772782.lua) | 1 |
| That Six | `39454112` | [Scripts/c39454112.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c39454112.lua) | 1 |

## Script Examples

### Number 67: Pair-a-Dice Smasher (`35772782`)

Source: [Scripts/c35772782.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c35772782.lua)

```lua
		Duel.Hint(HINT_CARD,0,35772782)
		e:GetHandler():RegisterFlagEffect(35772782,RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END,0,1)
		local dc={Duel.GetDiceResult()}
		local ac=1
		local ct=(ev&0xff)+(ev>>16&0xff)
```

### That Six (`39454112`)

Source: [Scripts/c39454112.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c39454112.lua)

```lua
	if Duel.SelectYesNo(tp,aux.Stringid(39454112,0)) then
		Duel.Hint(HINT_CARD,0,39454112)
		local dc={Duel.GetDiceResult()}
		local ac=1
		local ct=(ev&0xff)+(ev>>16&0xff)
```
