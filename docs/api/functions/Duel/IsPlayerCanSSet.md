# Duel.IsPlayerCanSSet

## Signature

```lua
Duel.IsPlayerCanSSet(int player, [Card c]) -> bool
```

## Description

Checks whether player can Set Spell/Trap Cards at all, or whether player can Set c as a Spell/Trap Card.

## Parameters

- `player` `int`
- `c` `Card` optional

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5049`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **2** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Duel.IsPlayerCanSSet) with `Duel.IsPlayerCanSSet`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Silent Wolf Calupo | `15947754` | [Scripts/c15947754.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c15947754.lua) | 1 |
| Absolute King Back Jack | `60990740` | [Scripts/c60990740.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c60990740.lua) | 1 |

## Script Examples

### Silent Wolf Calupo (`15947754`)

Source: [Scripts/c15947754.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c15947754.lua)

```lua
	local tc=Duel.GetDecktopGroup(tp,1):GetFirst()
	if c:IsFaceup() and c:IsRelateToEffect(e) and Duel.GetLocationCount(tp,LOCATION_SZONE)>0
		and tc and tc:IsFacedown() and Duel.IsPlayerCanSSet(tp,tc) then
		Duel.DisableShuffleCheck()
		if tc:IsForbidden() then
```

### Absolute King Back Jack (`60990740`)

Source: [Scripts/c60990740.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c60990740.lua)

```lua
	if chk==0 then return Duel.IsPlayerCanDiscardDeck(tp,1)
		and Duel.GetLocationCount(tp,LOCATION_SZONE)>0
		and Duel.IsPlayerCanSSet(tp) end
end
function c60990740.operation(e,tp,eg,ep,ev,re,r,rp)
```
