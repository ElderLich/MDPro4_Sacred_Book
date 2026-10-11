# Card.AssumeProperty

## Signature

```lua
Card.AssumeProperty(Card c, int assume_type, int assume_value) -> void
```

## Description

Temporarily assumes one property of c for core checks.
assume_type is one of ASSUME_CODE, ASSUME_TYPE, ASSUME_LEVEL, ASSUME_RANK, ASSUME_ATTRIBUTE, ASSUME_RACE, ASSUME_ATTACK, or ASSUME_DEFENSE.

## Parameters

- `c` `Card`
- `assume_type` `int`
- `assume_value` `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3715`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **2** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Card.AssumeProperty) with `Card.AssumeProperty`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Genomix Fighter | `42155488` | [Scripts/c42155488.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c42155488.lua) | 1 |
| Mono Synchron | `56897896` | [Scripts/c56897896.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c56897896.lua) | 1 |

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
