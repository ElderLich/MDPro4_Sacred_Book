# Card.ResetEffect

## Signature

```lua
Card.ResetEffect(Card c, int reset_code, int reset_type) -> void
```

## Description

To reset the type to reset_type, reset the type reset_code manual reset c impact of the impact
The reset_type can only be one of the following types, and the corresponding reset type is
RESET_EVENT An event reset_code is set for the event
RESET_PHASE End of phase Reset the reset_code to phase
RESET_CODE reset the effect of the specified code reset_code for the type of effect code, can only be reset EFFECT_TYPE_SINGLE sustainable type effect
RESET_COPY resets the effect of the copy. Reset_code is copy_id
RESET_CARD The effect of resetting the card reset_code is the card number of the effect owner

## Parameters

- `c` `Card`
- `reset_code` `int`
- `reset_type` `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3550`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **18** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.ResetEffect`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Starving Venemy Dragon](/examples/cards/93729065) | `93729065` | [Scripts/c93729065.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93729065.lua) | 61 |
| Windwitch - Crystal Bell | `25793414` | [Scripts/c25793414.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c25793414.lua) | 57 |
| Odd-Eyes Venom Dragon | `45014450` | [Scripts/c45014450.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c45014450.lua) | 54 |
| Masterflare Hyperion | `63101468` | [Scripts/c63101468.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63101468.lua) | 53 |
| Starving Venom Fusion Dragon | `41209827` | [Scripts/c41209827.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c41209827.lua) | 52 |
| Blackwing - Aurora the Northern Lights | `4068622` | [Scripts/c4068622.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c4068622.lua) | 50 |
| Hundred Eyes Dragon | `95453143` | [Scripts/c95453143.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c95453143.lua) | 49 |
| Supreme King Dragon Starving Venom | `43387895` | [Scripts/c43387895.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c43387895.lua) | 45 |
| Dragon Knight Draco-Equiste | `14017402` | [Scripts/c14017402.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c14017402.lua) | 44 |
| Number 8: Heraldic King Genom-Heritage | `47387961` | [Scripts/c47387961.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c47387961.lua) | 44 |
| CXyz Barian Hope | `67926903` | [Scripts/c67926903.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c67926903.lua) | 41 |
| Elemental HERO Divine Neos | `31111109` | [Scripts/c31111109.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c31111109.lua) | 41 |
| Phantom of Chaos | `30312361` | [Scripts/c30312361.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30312361.lua) | 41 |
| Arcana Call | `99189322` | [Scripts/c99189322.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c99189322.lua) | 34 |
| Neo-Spacian Dark Panther | `43237273` | [Scripts/c43237273.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c43237273.lua) | 34 |
| Pseudo Space | `77584012` | [Scripts/c77584012.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c77584012.lua) | 31 |
| Satellite Cannon | `50400231` | [Scripts/c50400231.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c50400231.lua) | 19 |
| Ape Fighter | `41098335` | [Scripts/c41098335.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c41098335.lua) | 18 |

## Script Examples

### Starving Venemy Dragon (`93729065`)

Source: [Scripts/c93729065.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93729065.lua)

```lua
	local cid=e:GetLabel()
	if cid~=0 then
		c:ResetEffect(cid,RESET_COPY)
		c:ResetEffect(RESET_DISABLE,RESET_EVENT)
	end
```

### Windwitch - Crystal Bell (`25793414`)

Source: [Scripts/c25793414.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c25793414.lua)

```lua
	local cid=e:GetLabel()
	if cid~=0 then
		c:ResetEffect(cid,RESET_COPY)
		c:ResetEffect(RESET_DISABLE,RESET_EVENT)
	end
```

### Odd-Eyes Venom Dragon (`45014450`)

Source: [Scripts/c45014450.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c45014450.lua)

```lua
	local cid=e:GetLabel()
	if cid~=0 then
		c:ResetEffect(cid,RESET_COPY)
		c:ResetEffect(RESET_DISABLE,RESET_EVENT)
	end
```
