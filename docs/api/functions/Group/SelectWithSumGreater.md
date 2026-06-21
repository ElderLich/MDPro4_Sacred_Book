# Group.SelectWithSumGreater

## Signature

```lua
Group.SelectWithSumGreater(Group g, int player, function f, int sum, ... any) -> Group
```

## Description

Let the player player select a subset from g so that the sum of the particular function f of the subset is greater than or equal to sum, starting at the fifth argument as an extra parameter

## Parameters

- `g` `Group`
- `player` `int`
- `f` `function`
- `sum` `int`
- `...` `any`

## Returns

- `Group`

## Source

- `D:\Programs\GitHub\ygopro-core\libgroup.cpp:923`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **1** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Group.SelectWithSumGreater`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Ferret Flames | `31044787` | [Scripts/c31044787.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c31044787.lua) | 19 |

## Script Examples

### Ferret Flames (`31044787`)

Source: [Scripts/c31044787.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c31044787.lua)

```lua
	if diff<=0 then return end
	Duel.Hint(HINT_SELECTMSG,1-tp,HINTMSG_TODECK)
	local sg=g:SelectWithSumGreater(1-tp,c31044787.getAttack,diff)
	Duel.SendtoDeck(sg,nil,SEQ_DECKSHUFFLE,REASON_RULE,1-tp)
end
```
