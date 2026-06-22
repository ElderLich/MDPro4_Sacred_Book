# Duel.IsPlayerCanSendtoDeck

## Signature

```lua
Duel.IsPlayerCanSendtoDeck(int player, Card c) -> bool
```

## Description

Checks whether player can send cards to the Deck at all, or whether player can send c to the Deck.

## Parameters

- `player` `int`
- `c` `Card`

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5058`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **1** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Duel.IsPlayerCanSendtoDeck`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Ferret Flames | `31044787` | [Scripts/c31044787.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c31044787.lua) | 19 |

## Script Examples

### Ferret Flames (`31044787`)

Source: [Scripts/c31044787.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c31044787.lua)

```lua
end
function c31044787.filter(c,tp)
	return c:IsFaceup() and c:GetAttack()>0 and Duel.IsPlayerCanSendtoDeck(tp,c)
end
function c31044787.condition(e,tp,eg,ep,ev,re,r,rp)
```
