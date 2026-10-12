# Card.SetReason

## Signature

```lua
Card.SetReason(Card c, int reason) -> void
```

## Description

Sets c's current reason bitmask to reason.

## Parameters

- `c` `Card`
- `reason` `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3510`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **1** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Card.SetReason) with `Card.SetReason`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Future Fusion | `77565204` | [Scripts/c77565204.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c77565204.lua) | 1 |

## Script Examples

### Future Fusion (`77565204`)

Source: [Scripts/c77565204.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c77565204.lua)

```lua
	for mc in aux.Next(mat) do
		if mc:GetFlagEffect(77565204)>0 then
			mc:SetReason(REASON_EFFECT+REASON_FUSION+REASON_MATERIAL)
		end
	end
```
