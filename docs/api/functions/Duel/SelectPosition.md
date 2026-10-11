# Duel.SelectPosition

## Signature

```lua
Duel.SelectPosition(int player, Card c, int positions) -> int
```

## Description

Lets player choose one of the allowed positions for c and returns the selected POS_* value.

## Parameters

- `player` `int`
- `c` `Card`
- `positions` `int`

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5026`

## Guided Examples

Learn how to use this function in context:

- [Tokens And Summon Choices](/learn/tokens-and-summon-choices)

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **28** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Duel.SelectPosition) with `Duel.SelectPosition`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Ehther the Heavenly Monarch](/examples/cards/96570609) | `96570609` | [Scripts/c96570609.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c96570609.lua) | 1 |
| Quick Summon | `10086952` | [Scripts/c10086952.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c10086952.lua) | 2 |
| Mimighoul Maker | `13204145` | [Scripts/c13204145.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c13204145.lua) | 1 |
| Clown Crew Biancaviso | `82159583` | [Scripts/c82159583.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c82159583.lua) | 1 |
| Doodle Beast - Tyranno | `67725394` | [Scripts/c67725394.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c67725394.lua) | 1 |
| Bahalutiya, the Grand Radiance | `53318263` | [Scripts/c53318263.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c53318263.lua) | 1 |
| Fairy Tale Tails | `91957038` | [Scripts/c91957038.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c91957038.lua) | 1 |
| Subterror Final Battle | `74640994` | [Scripts/c74640994.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74640994.lua) | 1 |
| Mimighoul Archfiend | `50415441` | [Scripts/c50415441.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c50415441.lua) | 1 |
| World Legacy Pawns | `89320376` | [Scripts/c89320376.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c89320376.lua) | 1 |
| Tessera the Primal Squire | `67584223` | [Scripts/c67584223.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c67584223.lua) | 1 |
| Spellbook of Fate | `97997309` | [Scripts/c97997309.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c97997309.lua) | 1 |
| Mimighoul Fork | `19338434` | [Scripts/c19338434.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c19338434.lua) | 1 |
| Bettan Bat | `84079032` | [Scripts/c84079032.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c84079032.lua) | 1 |
| Mimighoul Master | `55537983` | [Scripts/c55537983.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c55537983.lua) | 1 |
| Samsara Dragon | `33750025` | [Scripts/c33750025.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c33750025.lua) | 1 |
| Green Ninja | `15198996` | [Scripts/c15198996.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c15198996.lua) | 1 |
| Mausoleum of the Emperor | `80921533` | [Scripts/c80921533.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c80921533.lua) | 1 |
| Eda the Sun Magician | `96352326` | [Scripts/c96352326.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c96352326.lua) | 1 |
| Proof of Pruflas | `85847157` | [Scripts/c85847157.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c85847157.lua) | 1 |
| The Hidden City | `5697558` | [Scripts/c5697558.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c5697558.lua) | 2 |
| Spell Card "Soul Exchange" | `15735108` | [Scripts/c15735108.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c15735108.lua) | 1 |
| Gemini Summoner | `19041767` | [Scripts/c19041767.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c19041767.lua) | 1 |
| Cry Havoc! | `39712330` | [Scripts/c39712330.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c39712330.lua) | 1 |
| ...and 4 more |  |  |  |

## Script Examples

### Ehther the Heavenly Monarch (`96570609`)

Source: [Scripts/c96570609.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c96570609.lua)

```lua
	if c:IsMSetable(true,nil,1) then pos=pos+POS_FACEDOWN_DEFENSE end
	if pos==0 then return end
	if Duel.SelectPosition(tp,c,pos)==POS_FACEUP_ATTACK then
		Duel.Summon(tp,c,true,nil,1)
	else
```

### Quick Summon (`10086952`)

Source: [Scripts/c10086952.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c10086952.lua)

```lua
			(ne==se
				or not tc:IsMSetable(true,ne)
				or Duel.SelectPosition(tp,tc,POS_FACEUP_ATTACK+POS_FACEDOWN_DEFENSE)==POS_FACEUP_ATTACK) then
			Duel.Summon(tp,tc,true,ne)
		else Duel.MSet(tp,tc,true,ne) end
```

### Mimighoul Maker (`13204145`)

Source: [Scripts/c13204145.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c13204145.lua)

```lua
			Duel.ChangePosition(tc,POS_FACEUP_ATTACK)
		else
			local pos=Duel.SelectPosition(tp,tc,POS_FACEUP)
			Duel.ChangePosition(tc,pos)
		end
```
