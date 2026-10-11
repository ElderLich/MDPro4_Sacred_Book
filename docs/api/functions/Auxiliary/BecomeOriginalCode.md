# Auxiliary.BecomeOriginalCode

## Signature

```lua
Auxiliary.BecomeOriginalCode(Card c, Card tc, [int reset]) -> Effect
```

## Description

Registers an EFFECT_CHANGE_CODE effect on c so its code becomes tc's original rule code until reset; reset defaults to standard event reset through the End Phase.

## Parameters

- `c` `Card`
- `tc` `Card`
- `reset` `int` optional - defult: RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END

## Returns

- `Effect`

## Source

- `Utilities/utility.lua:2010`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **1** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Auxiliary.BecomeOriginalCode) with `Auxiliary.BecomeOriginalCode`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Phantom of Chaos | `30312361` | [Scripts/c30312361.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30312361.lua) | 1 |

## Script Examples

### Phantom of Chaos (`30312361`)

Source: [Scripts/c30312361.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30312361.lua)

```lua
		local code=tc:GetOriginalCode()
		local ba=tc:GetBaseAttack()
		local e1=aux.BecomeOriginalCode(c,tc)
		local e2=Effect.CreateEffect(c)
		e2:SetType(EFFECT_TYPE_SINGLE)
```
