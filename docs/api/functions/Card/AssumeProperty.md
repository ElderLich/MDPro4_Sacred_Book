# Card.AssumeProperty

## Signature

```lua
Card.AssumeProperty(Card c, int assume_type, int assume_value) -> void
```

## Description

Use the value of assume_type c as assume_value (genome fighter)
Assume_type is the following type
ASSUME_CODE card number
The ASSUME_TYPE type
ASSUME_LEVEL class
ASSUME_RANK class
ASSUME_ATTRIBUTE property
ASSUME_RACE race
ASSUME_ATTACK Attack power
ASSUME_DEFENSE Defense

## Parameters

- `c` `Card`
- `assume_type` `int`
- `assume_value` `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3660`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **2** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.AssumeProperty`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Genomix Fighter | `42155488` | [Scripts/c42155488.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c42155488.lua) | 31 |
| Mono Synchron | `56897896` | [Scripts/c56897896.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c56897896.lua) | 11 |

## Script Examples

### Genomix Fighter (`42155488`)

Source: [Scripts/c42155488.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c42155488.lua)

```lua
end
function c42155488.syncheck(e,c)
	c:AssumeProperty(ASSUME_RACE,e:GetLabel())
end
```

### Mono Synchron (`56897896`)

Source: [Scripts/c56897896.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c56897896.lua)

```lua
function c56897896.syncheck(e,c)
	if c~=e:GetHandler() then
		c:AssumeProperty(ASSUME_LEVEL,1)
	end
end
```
