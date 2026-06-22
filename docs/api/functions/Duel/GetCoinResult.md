# Duel.GetCoinResult

## Signature

```lua
Duel.GetCoinResult() -> int...
```

## Description

Returns the stored coin toss results for the current coin-toss event, one result per coin.

## Returns

- `int...` - One value per stored coin result.

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5039`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **3** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Duel.GetCoinResult`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Proton Blast | `49511705` | [Scripts/c49511705.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c49511705.lua) | 32 |
| Origami Goddess | `7930346` | [Scripts/c7930346.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c7930346.lua) | 31 |
| Lucky Chance | `96012004` | [Scripts/c96012004.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c96012004.lua) | 29 |

## Script Examples

### Proton Blast (`49511705`)

Source: [Scripts/c49511705.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c49511705.lua)

```lua
	Duel.Hint(HINT_CARD,0,49511705)
	local ct=0
	local res={Duel.GetCoinResult()}
	for i=1,ev do
		if res[i]==1 then
```

### Origami Goddess (`7930346`)

Source: [Scripts/c7930346.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c7930346.lua)

```lua
function s.coinop(e,tp,eg,ep,ev,re,r,rp)
	local c=e:GetHandler()
	local res={Duel.GetCoinResult()}
	local heads=0
	for _,coin in ipairs(res) do
```

### Lucky Chance (`96012004`)

Source: [Scripts/c96012004.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c96012004.lua)

```lua
end
function c96012004.drcon(e,tp,eg,ep,ev,re,r,rp)
	local res=Duel.GetCoinResult()
	return re==e:GetLabelObject() and res==e:GetLabel()
end
```
