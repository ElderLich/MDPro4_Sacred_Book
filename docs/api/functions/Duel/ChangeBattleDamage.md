# Duel.ChangeBattleDamage

## Signature

```lua
Duel.ChangeBattleDamage(int player, int value, [bool check]) -> void
```

## Description

Changes player battle damage for the current battle to value.
When check is true or omitted, existing 0 battle damage is left unchanged.

## Parameters

- `player` `int`
- `value` `int`
- `check` `bool` optional - default: true

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4923`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **3** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Duel.ChangeBattleDamage`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Starving Venemy Dragon](/examples/cards/93729065) | `93729065` | [Scripts/c93729065.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93729065.lua) | 1 |
| Ancient City - Rainbow Ruins | `34487429` | [Scripts/c34487429.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c34487429.lua) | 1 |
| Odd-Eyes Pendulum Dragon | `16178681` | [Scripts/c16178681.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c16178681.lua) | 1 |

## Script Examples

### Starving Venemy Dragon (`93729065`)

Source: [Scripts/c93729065.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93729065.lua)

```lua
	if Duel.SelectYesNo(tp,aux.Stringid(93729065,3)) then
		Duel.Hint(HINT_CARD,0,93729065)
		Duel.ChangeBattleDamage(tp,0)
		e:GetHandler():RegisterFlagEffect(93729066,RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END,0,1)
	end
```

### Ancient City - Rainbow Ruins (`34487429`)

Source: [Scripts/c34487429.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c34487429.lua)

```lua
function c34487429.rdop(e,tp,eg,ep,ev,re,r,rp)
	if Duel.SelectEffectYesNo(tp,e:GetHandler()) then
		Duel.ChangeBattleDamage(tp,math.floor(ev/2))
		e:GetHandler():RegisterFlagEffect(34487429,RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END,0,1)
	end
```

### Odd-Eyes Pendulum Dragon (`16178681`)

Source: [Scripts/c16178681.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c16178681.lua)

```lua
	if Duel.SelectYesNo(tp,aux.Stringid(16178681,2)) then
		Duel.Hint(HINT_CARD,0,16178681)
		Duel.ChangeBattleDamage(tp,0)
		Duel.RegisterFlagEffect(tp,16178681,RESET_PHASE+PHASE_END,0,1)
	end
```
