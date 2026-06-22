# Auxiliary.EnableReviveLimitPendulumSummonable

## Signature

```lua
Auxiliary.EnableReviveLimitPendulumSummonable(Card c, [int loc]) -> void
```

## Description

Enables revive-limit handling for c while also allowing it to be Pendulum Summoned from loc.
The helper stores loc on c's metatable and completes c's procedure when it is successfully Pendulum Summoned.

## Parameters

- `c` `Card`
- `loc` `int` optional - default: 0xff

## Source

- `Utilities/procedure.lua:2097`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **2** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Auxiliary.EnableReviveLimitPendulumSummonable`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Odd-Eyes Revolution Dragon](/examples/cards/16306932) | `16306932` | [Scripts/c16306932.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c16306932.lua) | 64 |
| Odd-Eyes Pendulumgraph Dragon | `66425726` | [Scripts/c66425726.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c66425726.lua) | 49 |

## Script Examples

### Odd-Eyes Revolution Dragon (`16306932`)

Source: [Scripts/c16306932.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c16306932.lua)

```lua
	aux.EnablePendulumAttribute(c)
	--revive limit
	aux.EnableReviveLimitPendulumSummonable(c,LOCATION_HAND)
	--splimit
	local e1=Effect.CreateEffect(c)
```

### Odd-Eyes Pendulumgraph Dragon (`66425726`)

Source: [Scripts/c66425726.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c66425726.lua)

```lua
	aux.EnablePendulumAttribute(c)
	--revive limit
	aux.EnableReviveLimitPendulumSummonable(c,LOCATION_HAND)
	--spsummon condition
	local e0=Effect.CreateEffect(c)
```
