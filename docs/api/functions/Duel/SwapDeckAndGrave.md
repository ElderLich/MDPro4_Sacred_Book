# Duel.SwapDeckAndGrave

## Signature

```lua
Duel.SwapDeckAndGrave(int player) -> void
```

## Description

For Exchange of the Spirit-style effects, swaps player's Deck and Graveyard.

## Parameters

- `player` `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5072`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **1** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Duel.SwapDeckAndGrave) with `Duel.SwapDeckAndGrave`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Exchange of the Spirit | `17484499` | [Scripts/c17484499.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c17484499.lua) | 2 |

## Script Examples

### Exchange of the Spirit (`17484499`)

Source: [Scripts/c17484499.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c17484499.lua)

```lua
	local g=Duel.GetFieldGroup(tp,LOCATION_GRAVE,LOCATION_GRAVE)
	if aux.NecroValleyNegateCheck(g) then return end
	Duel.SwapDeckAndGrave(tp)
	Duel.SwapDeckAndGrave(1-tp)
end
```
