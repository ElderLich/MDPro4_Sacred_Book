# Card.GetSynchroType

## Signature

```lua
Card.GetSynchroType(Card c) -> int
```

## Description

Returns c's Synchro Material Type mask used by Synchro Material checks.

## Parameters

- `c` `Card`

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3453`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **1** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Card.GetSynchroType) with `Card.GetSynchroType`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Metaphys Horus | `36898537` | [Scripts/c36898537.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c36898537.lua) | 1 |

## Script Examples

### Metaphys Horus (`36898537`)

Source: [Scripts/c36898537.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c36898537.lua)

```lua
	while tc do
		if not tc:IsSynchroType(TYPE_TUNER) then
			tpe=bit.bor(tpe,tc:GetSynchroType())
		end
		tc=g:GetNext()
```
