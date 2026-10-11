# Group.SelectSubGroupEach

## Signature

```lua
Group.SelectSubGroupEach(Group g, int tp, table checks, [bool cancelable], [function f], ... any) -> Group|nil
```

## Description

Lets tp select one card for each filter in checks, optionally cancelable. If f is omitted, Auxiliary.TRUE is used for the final group check.

## Parameters

- `g` `Group`
- `tp` `int`
- `checks` `table`
- `cancelable` `bool` optional
- `f` `function` optional
- `...` `any`

## Returns

- `Group|nil` - The selected subgroup, or nil if no valid selection is completed.

## Source

- `Utilities/utility.lua:1356`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **31** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Group.SelectSubGroupEach) with `Group.SelectSubGroupEach`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Astrograph Sorcerer](/examples/cards/76794549) | `76794549` | [Scripts/c76794549.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c76794549.lua) | 1 |
| [Odd-Eyes Revolution Dragon](/examples/cards/16306932) | `16306932` | [Scripts/c16306932.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c16306932.lua) | 1 |
| [Chronograph Sorcerer](/examples/cards/12289247) | `12289247` | [Scripts/c12289247.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c12289247.lua) | 1 |
| Kuribeh | `34419588` | [Scripts/c34419588.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c34419588.lua) | 1 |
| Berserkion the Electromagna Warrior | `42901635` | [Scripts/c42901635.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c42901635.lua) | 2 |
| Summon Reactor ・SK | `89493368` | [Scripts/c89493368.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c89493368.lua) | 1 |
| Kuribah | `44632120` | [Scripts/c44632120.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44632120.lua) | 1 |
| Kuribabylon | `70914287` | [Scripts/c70914287.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c70914287.lua) | 1 |
| Bonding - D2O | `79402185` | [Scripts/c79402185.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c79402185.lua) | 1 |
| D.D. Jet Iron | `15574615` | [Scripts/c15574615.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c15574615.lua) | 2 |
| Valkyrion the Magna Warrior | `75347539` | [Scripts/c75347539.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c75347539.lua) | 1 |
| Arcana Triumph Joker | `93880808` | [Scripts/c93880808.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93880808.lua) | 1 |
| Frost and Flame Dragon | `55589254` | [Scripts/c55589254.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c55589254.lua) | 1 |
| Desert Twister | `81977953` | [Scripts/c81977953.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c81977953.lua) | 1 |
| Sky Scourge Enrise | `11458071` | [Scripts/c11458071.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c11458071.lua) | 1 |
| Orphebull the Harmonious Bullfighter Bard | `97240499` | [Scripts/c97240499.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c97240499.lua) | 1 |
| Sky Scourge Norleras | `48453776` | [Scripts/c48453776.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c48453776.lua) | 1 |
| Cyberdark Impact! | `80033124` | [Scripts/c80033124.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c80033124.lua) | 1 |
| Sophia, Goddess of Rebirth | `4335427` | [Scripts/c4335427.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c4335427.lua) | 1 |
| Five Star Twilight | `6309986` | [Scripts/c6309986.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c6309986.lua) | 1 |
| Machina Force | `58054262` | [Scripts/c58054262.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c58054262.lua) | 1 |
| Mitsurugi Tempest | `49604192` | [Scripts/c49604192.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c49604192.lua) | 1 |
| Sextet Summon | `99162753` | [Scripts/c99162753.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c99162753.lua) | 1 |
| Bonding - DHO | `6890729` | [Scripts/c6890729.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c6890729.lua) | 1 |
| ...and 7 more |  |  |  |

## Script Examples

### Astrograph Sorcerer (`76794549`)

Source: [Scripts/c76794549.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c76794549.lua)

```lua
		and mg:CheckSubGroupEach(c76794549.hnchecks,c76794549.hngoal,e,tp,c) end
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_REMOVE)
	local sg=mg:SelectSubGroupEach(tp,c76794549.hnchecks,false,c76794549.hngoal,e,tp,c)
	sg:AddCard(c)
	Duel.Remove(sg,POS_FACEUP,REASON_COST)
```

### Odd-Eyes Revolution Dragon (`16306932`)

Source: [Scripts/c16306932.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c16306932.lua)

```lua
	local g=Duel.GetReleaseGroup(tp,false,REASON_SPSUMMON):Filter(Card.IsRace,nil,RACE_DRAGON)
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_RELEASE)
	local sg=g:SelectSubGroupEach(tp,c16306932.spchecks,true,aux.mzctcheckrel,tp,REASON_SPSUMMON)
	if sg then
		sg:KeepAlive()
```

### Chronograph Sorcerer (`12289247`)

Source: [Scripts/c12289247.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c12289247.lua)

```lua
		and mg:CheckSubGroupEach(c12289247.hnchecks,c12289247.hngoal,e,tp,c) end
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_REMOVE)
	local sg=mg:SelectSubGroupEach(tp,c12289247.hnchecks,false,c12289247.hngoal,e,tp,c)
	sg:AddCard(c)
	Duel.Remove(sg,POS_FACEUP,REASON_COST)
```
