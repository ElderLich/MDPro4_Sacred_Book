# Auxiliary.CreateChecks

## Signature

```lua
Auxiliary.CreateChecks(function f, table list) -> table
```

## Description

Returns a table of one-card check functions where each function calls f(c, list\[i\]).

## Parameters

- `f` `function`
- `list` `table`

## Returns

- `table`

## Source

- `Utilities/utility.lua:1307`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **30** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Auxiliary.CreateChecks`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Astrograph Sorcerer](/examples/cards/76794549) | `76794549` | [Scripts/c76794549.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c76794549.lua) | 71 |
| [Odd-Eyes Revolution Dragon](/examples/cards/16306932) | `16306932` | [Scripts/c16306932.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c16306932.lua) | 64 |
| [Chronograph Sorcerer](/examples/cards/12289247) | `12289247` | [Scripts/c12289247.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c12289247.lua) | 61 |
| Kuribeh | `34419588` | [Scripts/c34419588.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c34419588.lua) | 57 |
| Berserkion the Electromagna Warrior | `42901635` | [Scripts/c42901635.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c42901635.lua) | 56 |
| Summon Reactor ・SK | `89493368` | [Scripts/c89493368.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c89493368.lua) | 48 |
| Kuribah | `44632120` | [Scripts/c44632120.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44632120.lua) | 45 |
| Kuribabylon | `70914287` | [Scripts/c70914287.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c70914287.lua) | 43 |
| Bonding - D2O | `79402185` | [Scripts/c79402185.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c79402185.lua) | 43 |
| D.D. Jet Iron | `15574615` | [Scripts/c15574615.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c15574615.lua) | 42 |
| Valkyrion the Magna Warrior | `75347539` | [Scripts/c75347539.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c75347539.lua) | 42 |
| Arcana Triumph Joker | `93880808` | [Scripts/c93880808.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93880808.lua) | 41 |
| Frost and Flame Dragon | `55589254` | [Scripts/c55589254.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c55589254.lua) | 40 |
| Desert Twister | `81977953` | [Scripts/c81977953.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c81977953.lua) | 40 |
| Orphebull the Harmonious Bullfighter Bard | `97240499` | [Scripts/c97240499.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c97240499.lua) | 38 |
| Cyberdark Impact! | `80033124` | [Scripts/c80033124.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c80033124.lua) | 37 |
| Sophia, Goddess of Rebirth | `4335427` | [Scripts/c4335427.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c4335427.lua) | 35 |
| Five Star Twilight | `6309986` | [Scripts/c6309986.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c6309986.lua) | 35 |
| Machina Force | `58054262` | [Scripts/c58054262.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c58054262.lua) | 35 |
| Mitsurugi Tempest | `49604192` | [Scripts/c49604192.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c49604192.lua) | 34 |
| Sextet Summon | `99162753` | [Scripts/c99162753.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c99162753.lua) | 32 |
| Utopic Onomatopoeia | `8512558` | [Scripts/c8512558.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c8512558.lua) | 31 |
| Bonding - DHO | `6890729` | [Scripts/c6890729.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c6890729.lua) | 31 |
| Bonding - H2O | `45898858` | [Scripts/c45898858.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c45898858.lua) | 30 |
| ...and 6 more |  |  |  |

## Script Examples

### Astrograph Sorcerer (`76794549`)

Source: [Scripts/c76794549.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c76794549.lua)

```lua
	end
end
c76794549.hnchecks=aux.CreateChecks(Card.IsSetCard,{0x10f2,0x2073,0x2017,0x1046})
function c76794549.checkop(e,tp,eg,ep,ev,re,r,rp)
	local tc=eg:GetFirst()
```

### Odd-Eyes Revolution Dragon (`16306932`)

Source: [Scripts/c16306932.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c16306932.lua)

```lua
	c:RegisterEffect(e8)
end
c16306932.spchecks=aux.CreateChecks(Card.IsType,{TYPE_FUSION,TYPE_SYNCHRO,TYPE_XYZ})
function c16306932.psplimit(e,c,tp,sumtp,sumpos)
	return not c:IsRace(RACE_DRAGON) and bit.band(sumtp,SUMMON_TYPE_PENDULUM)==SUMMON_TYPE_PENDULUM
```

### Chronograph Sorcerer (`12289247`)

Source: [Scripts/c12289247.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c12289247.lua)

```lua
	end
end
c12289247.hnchecks=aux.CreateChecks(Card.IsSetCard,{0x10f2,0x2073,0x2017,0x1046})
function c12289247.spcfilter(c,tp)
	return c:IsReason(REASON_BATTLE+REASON_EFFECT)
```
