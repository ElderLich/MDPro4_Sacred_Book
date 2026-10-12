# Card.CancelCardTarget

## Signature

```lua
Card.CancelCardTarget(Card c, Card target) -> void
```

## Description

Removes target from c's persistent card-target relation list.

## Parameters

- `c` `Card`
- `target` `Card`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3596`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **3** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Card.CancelCardTarget) with `Card.CancelCardTarget`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Trickstar Light Stage | `35371948` | [Scripts/c35371948.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c35371948.lua) | 1 |
| Trickstar Light Arena | `63492244` | [Scripts/c63492244.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c63492244.lua) | 1 |
| Goblin Freefall Squad | `85123771` | [Scripts/c85123771.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c85123771.lua) | 1 |

## Script Examples

### Trickstar Light Stage (`35371948`)

Source: [Scripts/c35371948.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c35371948.lua)

```lua
	local c=e:GetHandler()
	local tc=eg:GetFirst()
	c:CancelCardTarget(tc)
	tc:ResetFlagEffect(35371948)
	local te=e:GetLabelObject()
```

### Trickstar Light Arena (`63492244`)

Source: [Scripts/c63492244.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c63492244.lua)

```lua
	local c=e:GetHandler()
	local tc=eg:GetFirst()
	c:CancelCardTarget(tc)
	tc:ResetFlagEffect(63492244)
	local te=e:GetLabelObject()
```

### Goblin Freefall Squad (`85123771`)

Source: [Scripts/c85123771.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c85123771.lua)

```lua
	local c=e:GetHandler()
	local tc=c:GetFirstCardTarget()
	Card.CancelCardTarget(c,tc)
end
	--to hand
```
