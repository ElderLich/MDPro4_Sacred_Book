# Auxiliary.EnableUnionAttribute

## Signature

```lua
Auxiliary.EnableUnionAttribute(Card c, function filter) -> void
```

## Description

add effect to modern union monsters

## Parameters

- `c` `Card`
- `filter` `function`

## Source

- `Utilities/utility.lua:348`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **21** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Auxiliary.EnableUnionAttribute`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Union Driver | `99249638` | [Scripts/c99249638.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c99249638.lua) | 37 |
| Y-Yare Head | `6355563` | [Scripts/c6355563.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c6355563.lua) | 35 |
| Z-Zillion Tank | `33744268` | [Scripts/c33744268.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c33744268.lua) | 35 |
| Union Pilot | `89357740` | [Scripts/c89357740.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c89357740.lua) | 34 |
| Armored Cybern | `67159705` | [Scripts/c67159705.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c67159705.lua) | 31 |
| A-Assault Core | `30012506` | [Scripts/c30012506.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30012506.lua) | 28 |
| B-Buster Drake | `77411244` | [Scripts/c77411244.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c77411244.lua) | 28 |
| C-Crush Wyvern | `3405259` | [Scripts/c3405259.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c3405259.lua) | 28 |
| Heavy Mech Support Armor | `39890958` | [Scripts/c39890958.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c39890958.lua) | 26 |
| Squeaknight | `38783169` | [Scripts/c38783169.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c38783169.lua) | 23 |
| Machina Peacekeeper | `78349103` | [Scripts/c78349103.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c78349103.lua) | 23 |
| Unauthorized Bootup Device | `81951640` | [Scripts/c81951640.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c81951640.lua) | 22 |
| Machina Gearframe | `42940404` | [Scripts/c42940404.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c42940404.lua) | 22 |
| Valkyrie Chariot | `19190082` | [Scripts/c19190082.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c19190082.lua) | 18 |
| Fortune Chariot | `39299733` | [Scripts/c39299733.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c39299733.lua) | 14 |
| Leng Ling | `70298454` | [Scripts/c70298454.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c70298454.lua) | 7 |
| Z-Metal Tank | `64500000` | [Scripts/c64500000.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c64500000.lua) | 7 |
| Torque Tune Gear | `79538761` | [Scripts/c79538761.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c79538761.lua) | 7 |
| Heavy Mech Support Platform | `23265594` | [Scripts/c23265594.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c23265594.lua) | 7 |
| Y-Dragon Head | `65622692` | [Scripts/c65622692.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c65622692.lua) | 7 |
| W-Wing Catapult | `96300057` | [Scripts/c96300057.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c96300057.lua) | 7 |

## Script Examples

### Union Driver (`99249638`)

Source: [Scripts/c99249638.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c99249638.lua)

```lua
--ユニオン・ドライバー
function c99249638.initial_effect(c)
	aux.EnableUnionAttribute(c,aux.TRUE)
	--reequip
	local e4=Effect.CreateEffect(c)
```

### Y-Yare Head (`6355563`)

Source: [Scripts/c6355563.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c6355563.lua)

```lua
local s,id,o=GetID()
function s.initial_effect(c)
	aux.EnableUnionAttribute(c,s.filter)
	--
	local e1=Effect.CreateEffect(c)
```

### Z-Zillion Tank (`33744268`)

Source: [Scripts/c33744268.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c33744268.lua)

```lua
local s,id,o=GetID()
function s.initial_effect(c)
	aux.EnableUnionAttribute(c,s.filter)
	--
	local e1=Effect.CreateEffect(c)
```
