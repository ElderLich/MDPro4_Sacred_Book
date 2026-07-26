# Effect.GetActivateSequence

## Signature

```lua
Effect.GetActivateSequence(Effect e) -> int
```

## Description

Returns the sequence where e was activated.

## Parameters

- `e` `Effect`

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libeffect.cpp:659`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **1** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Effect.GetActivateSequence`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Storm Cipher | `89571015` | [Scripts/c89571015.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c89571015.lua) | 1 |

## Script Examples

### Storm Cipher (`89571015`)

Source: [Scripts/c89571015.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c89571015.lua)

```lua
end
function c89571015.immval(e,te)
	return te:IsActivated() and te:GetActivateLocation()==LOCATION_MZONE and te:GetActivateSequence()>4
end
```
