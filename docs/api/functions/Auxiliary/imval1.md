# Auxiliary.imval1

## Signature

```lua
Auxiliary.imval1(Effect e, Card c) -> bool
```

## Description

Default value helper for EFFECT_CANNOT_BE_BATTLE_TARGET; it returns true when c is not immune to e.

## Parameters

- `e` `Effect`
- `c` `Card`

## Returns

- `bool`

## Source

- `Utilities/utility.lua:820`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **51** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Auxiliary.imval1`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Duel Link Dragon, the Duel Dragon | `60025883` | [Scripts/c60025883.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c60025883.lua) | 59 |
| The Winged Dragon of Ra - Sphere Mode | `10000080` | [Scripts/c10000080.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c10000080.lua) | 51 |
| Ultimaya Tzolkin | `1686814` | [Scripts/c1686814.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c1686814.lua) | 49 |
| Rokket Recharger | `5969957` | [Scripts/c5969957.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c5969957.lua) | 47 |
| Performapal Miss Director | `92932860` | [Scripts/c92932860.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92932860.lua) | 46 |
| Princess Cologne | `75574498` | [Scripts/c75574498.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c75574498.lua) | 46 |
| Selene, Queen of the Master Magicians | `45819647` | [Scripts/c45819647.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c45819647.lua) | 46 |
| Appliancer Celtopus | `78225596` | [Scripts/c78225596.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c78225596.lua) | 45 |
| Gullveig of the Nordic Ascendant | `90207654` | [Scripts/c90207654.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c90207654.lua) | 44 |
| Performage Trapeze Witch | `33206889` | [Scripts/c33206889.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c33206889.lua) | 44 |
| Brotherhood of the Fire Fist - Peacock | `20265095` | [Scripts/c20265095.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c20265095.lua) | 43 |
| Ancient Warriors - Virtuous Liu Xuan | `40428851` | [Scripts/c40428851.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c40428851.lua) | 42 |
| Poseidra, the Storming Atlantean | `99193444` | [Scripts/c99193444.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c99193444.lua) | 42 |
| Raidraptor Replica | `54423935` | [Scripts/c54423935.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c54423935.lua) | 42 |
| Meizen the Battle Ninja | `11825276` | [Scripts/c11825276.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c11825276.lua) | 41 |
| Ghostrick Socuteboss | `32224143` | [Scripts/c32224143.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c32224143.lua) | 40 |
| Ancient Warriors - Masterful Sun Mou | `40140448` | [Scripts/c40140448.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c40140448.lua) | 39 |
| Yuki-Onna, the Ice Mayakashi | `66870733` | [Scripts/c66870733.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c66870733.lua) | 39 |
| Shinobi Insect Hagakuremino | `70709488` | [Scripts/c70709488.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c70709488.lua) | 39 |
| Earthbound Immortal Wiraqocha Rasca | `41181774` | [Scripts/c41181774.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c41181774.lua) | 38 |
| Rescue-ACE Hydrant | `37617348` | [Scripts/c37617348.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c37617348.lua) | 38 |
| Earthbound Immortal Uru | `15187079` | [Scripts/c15187079.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c15187079.lua) | 38 |
| Raidraptor - Rudder Strix | `6552938` | [Scripts/c6552938.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c6552938.lua) | 37 |
| Otoshidamashi | `14957440` | [Scripts/c14957440.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c14957440.lua) | 36 |
| ...and 27 more |  |  |  |

## Script Examples

### Duel Link Dragon, the Duel Dragon (`60025883`)

Source: [Scripts/c60025883.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c60025883.lua)

```lua
	e2:SetRange(LOCATION_MZONE)
	e2:SetCondition(c60025883.tgcon)
	e2:SetValue(aux.imval1)
	c:RegisterEffect(e2)
	local e3=e2:Clone()
```

### The Winged Dragon of Ra - Sphere Mode (`10000080`)

Source: [Scripts/c10000080.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c10000080.lua)

```lua
	e7:SetCode(EFFECT_CANNOT_BE_BATTLE_TARGET)
	e7:SetRange(LOCATION_MZONE)
	e7:SetValue(aux.imval1)
	c:RegisterEffect(e7)
	local e8=e7:Clone()
```

### Ultimaya Tzolkin (`1686814`)

Source: [Scripts/c1686814.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c1686814.lua)

```lua
	e4:SetRange(LOCATION_MZONE)
	e4:SetCondition(c1686814.tgcon)
	e4:SetValue(aux.imval1)
	c:RegisterEffect(e4)
	local e5=e4:Clone()
```
