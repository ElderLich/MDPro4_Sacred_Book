# Duel.ChangeTargetPlayer

## Signature

```lua
Duel.ChangeTargetPlayer(int chainc, int player) -> void
```

## Description

Changes the target player recorded for Chain Link count.

## Parameters

- `chainc` `int`
- `player` `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4925`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **1** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Duel.ChangeTargetPlayer`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Mystical Refpanel | `35563539` | [Scripts/c35563539.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c35563539.lua) | 1 |

## Script Examples

### Mystical Refpanel (`35563539`)

Source: [Scripts/c35563539.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c35563539.lua)

```lua
function c35563539.activate(e,tp,eg,ep,ev,re,r,rp)
	local p=Duel.GetChainInfo(ev,CHAININFO_TARGET_PLAYER)
	Duel.ChangeTargetPlayer(ev,1-p)
end
```
