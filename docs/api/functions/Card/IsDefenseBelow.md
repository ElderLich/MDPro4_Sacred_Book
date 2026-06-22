# Card.IsDefenseBelow

## Signature

```lua
Card.IsDefenseBelow(Card c, int def) -> bool
```

## Description

Checks whether c has known current DEF less than or equal to def.
Link Monsters and non-monsters return false, and unknown or negative DEF also returns false.

## Parameters

- `c` `Card`
- `def` `int`

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3620`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **46** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.IsDefenseBelow`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| D/D/D Super Doom King Bright Armageddon | `72402069` | [Scripts/c72402069.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c72402069.lua) | 52 |
| Boss on Parade | `4909946` | [Scripts/c4909946.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c4909946.lua) | 45 |
| Wynn the Wind Channeler | `86395581` | [Scripts/c86395581.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c86395581.lua) | 44 |
| Aussa the Earth Charmer, Immovable | `97661969` | [Scripts/c97661969.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c97661969.lua) | 43 |
| Eria the Water Charmer, Gentle | `73309655` | [Scripts/c73309655.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c73309655.lua) | 43 |
| Dharc the Dark Charmer, Gloomy | `8264361` | [Scripts/c8264361.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c8264361.lua) | 43 |
| Hiita the Fire Charmer, Ablaze | `48815792` | [Scripts/c48815792.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c48815792.lua) | 43 |
| Wynn the Wind Charmer, Verdant | `30674956` | [Scripts/c30674956.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30674956.lua) | 43 |
| Ace★Spades Speculation | `10796448` | [Scripts/c10796448.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c10796448.lua) | 42 |
| Lyna the Light Charmer, Lustrous | `9839945` | [Scripts/c9839945.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c9839945.lua) | 42 |
| Blackwing - Silverwind the Ascendant | `33236860` | [Scripts/c33236860.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c33236860.lua) | 41 |
| Full Force Virus | `4931121` | [Scripts/c4931121.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c4931121.lua) | 40 |
| Number 84: Pain Gainer | `26556950` | [Scripts/c26556950.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c26556950.lua) | 38 |
| Vengeful Witch | `66100116` | [Scripts/c66100116.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c66100116.lua) | 38 |
| Neo Flamvell Lady | `816427` | [Scripts/c816427.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c816427.lua) | 38 |
| Performapal Call | `22765132` | [Scripts/c22765132.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c22765132.lua) | 38 |
| Curse of the Ancient Turtle | `94749594` | [Scripts/c94749594.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c94749594.lua) | 33 |
| Witch of the Black Forest | `78010363` | [Scripts/c78010363.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c78010363.lua) | 32 |
| Gusto Thunbolt | `28066831` | [Scripts/c28066831.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c28066831.lua) | 32 |
| Makiu, the Magical Mist | `27827272` | [Scripts/c27827272.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c27827272.lua) | 32 |
| Brotherhood of the Fire Fist - Spirit | `1662004` | [Scripts/c1662004.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c1662004.lua) | 31 |
| Dragon's Bind | `16278116` | [Scripts/c16278116.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c16278116.lua) | 30 |
| Whirlwind of Gusto | `91822647` | [Scripts/c91822647.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c91822647.lua) | 29 |
| Throwstone Unit | `76075810` | [Scripts/c76075810.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c76075810.lua) | 28 |
| ...and 22 more |  |  |  |

## Script Examples

### D/D/D Super Doom King Bright Armageddon (`72402069`)

Source: [Scripts/c72402069.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c72402069.lua)

```lua
end
function c72402069.desfilter2(c,atk)
	return c:IsFaceup() and c:IsDefenseBelow(atk)
end
function c72402069.destg(e,tp,eg,ep,ev,re,r,rp,chk,chkc)
```

### Boss on Parade (`4909946`)

Source: [Scripts/c4909946.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c4909946.lua)

```lua
end
function s.spfilter(c,e,tp,ec)
	return c:IsAttack(1200) and c:IsDefenseBelow(1000) and c:IsAttribute(ATTRIBUTE_LIGHT) and c:IsRace(RACE_MACHINE)
		and (Duel.GetMZoneCount(tp,ec)>0
		and c:IsCanBeSpecialSummoned(e,0,tp,false,false)
```

### Wynn the Wind Channeler (`86395581`)

Source: [Scripts/c86395581.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c86395581.lua)

```lua
end
function c86395581.srfilter(c)
	return c:IsAttribute(ATTRIBUTE_WIND) and c:IsDefenseBelow(1500) and not c:IsCode(86395581) and c:IsAbleToHand()
end
function c86395581.srcost(e,tp,eg,ep,ev,re,r,rp,chk)
```
