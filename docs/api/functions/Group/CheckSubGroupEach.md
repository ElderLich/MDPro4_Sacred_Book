# Group.CheckSubGroupEach

## Signature

```lua
Group.CheckSubGroupEach(Group g, table checks, [function f], ... any) -> bool
```

## Description

Checks whether g can supply one card for each filter in checks. If f is omitted, only the per-position checks are required.

## Parameters

- `g` `Group`
- `checks` `table`
- `f` `function` optional
- `...` `any`

## Returns

- `bool` - true if one card can satisfy each check.

## Source

- `Utilities/utility.lua:1338`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **33** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Group.CheckSubGroupEach`.

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
| Realm Resonance | `36920182` | [Scripts/c36920182.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c36920182.lua) | 42 |
| Valkyrion the Magna Warrior | `75347539` | [Scripts/c75347539.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c75347539.lua) | 42 |
| Arcana Triumph Joker | `93880808` | [Scripts/c93880808.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93880808.lua) | 41 |
| Frost and Flame Dragon | `55589254` | [Scripts/c55589254.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c55589254.lua) | 40 |
| Desert Twister | `81977953` | [Scripts/c81977953.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c81977953.lua) | 40 |
| Sky Scourge Enrise | `11458071` | [Scripts/c11458071.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c11458071.lua) | 39 |
| Orphebull the Harmonious Bullfighter Bard | `97240499` | [Scripts/c97240499.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c97240499.lua) | 38 |
| Sky Scourge Norleras | `48453776` | [Scripts/c48453776.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c48453776.lua) | 38 |
| Cyberdark Impact! | `80033124` | [Scripts/c80033124.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c80033124.lua) | 37 |
| Sophia, Goddess of Rebirth | `4335427` | [Scripts/c4335427.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c4335427.lua) | 35 |
| Five Star Twilight | `6309986` | [Scripts/c6309986.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c6309986.lua) | 35 |
| Machina Force | `58054262` | [Scripts/c58054262.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c58054262.lua) | 35 |
| Mitsurugi Tempest | `49604192` | [Scripts/c49604192.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c49604192.lua) | 34 |
| Sextet Summon | `99162753` | [Scripts/c99162753.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c99162753.lua) | 32 |
| ...and 9 more |  |  |  |

## Script Examples

### Astrograph Sorcerer (`76794549`)

Source: [Scripts/c76794549.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c76794549.lua)

```lua
	if chk==0 then return c:IsAbleToRemoveAsCost()
		and Duel.IsExistingMatchingCard(c76794549.hnfilter,tp,LOCATION_EXTRA,0,1,nil,e,tp,nil)
		and mg:CheckSubGroupEach(c76794549.hnchecks,c76794549.hngoal,e,tp,c) end
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_REMOVE)
	local sg=mg:SelectSubGroupEach(tp,c76794549.hnchecks,false,c76794549.hngoal,e,tp,c)
```

### Odd-Eyes Revolution Dragon (`16306932`)

Source: [Scripts/c16306932.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c16306932.lua)

```lua
	local tp=c:GetControler()
	local g=Duel.GetReleaseGroup(tp,false,REASON_SPSUMMON):Filter(Card.IsRace,nil,RACE_DRAGON)
	return g:CheckSubGroupEach(c16306932.spchecks,aux.mzctcheckrel,tp,REASON_SPSUMMON)
end
function c16306932.hsptg(e,tp,eg,ep,ev,re,r,rp,chk,c)
```

### Chronograph Sorcerer (`12289247`)

Source: [Scripts/c12289247.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c12289247.lua)

```lua
	if chk==0 then return c:IsAbleToRemoveAsCost()
		and Duel.IsExistingMatchingCard(c12289247.hnfilter,tp,LOCATION_EXTRA,0,1,nil,e,tp)
		and mg:CheckSubGroupEach(c12289247.hnchecks,c12289247.hngoal,e,tp,c) end
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_REMOVE)
	local sg=mg:SelectSubGroupEach(tp,c12289247.hnchecks,false,c12289247.hngoal,e,tp,c)
```
