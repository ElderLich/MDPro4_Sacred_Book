# Card.SetReason

## Signature

```lua
Card.SetReason(Card c, int reason) -> bool
```

## Description

Set the reason for card c arriving at its current position to reason

## Parameters

- `c` `Card`
- `reason` `int`

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3458`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **1** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.SetReason`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Future Fusion | `77565204` | [Scripts/c77565204.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c77565204.lua) | 55 |

## Script Examples

### Future Fusion (`77565204`)

Source: [Scripts/c77565204.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c77565204.lua)

```lua
	for mc in aux.Next(mat) do
		if mc:GetFlagEffect(77565204)>0 then
			mc:SetReason(REASON_EFFECT+REASON_FUSION+REASON_MATERIAL)
		end
	end
```
