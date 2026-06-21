# Duel.SelectPosition

## Signature

```lua
Duel.SelectPosition(int player, Card c, int pos) -> int
```

## Description

Let player player select the representation of c and return

## Parameters

- `player` `int`
- `c` `Card`
- `pos` `int`

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5026`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **27** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Duel.SelectPosition`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Ehther the Heavenly Monarch](/examples/cards/96570609) | `96570609` | [Scripts/c96570609.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c96570609.lua) | 65 |
| Mimighoul Maker | `13204145` | [Scripts/c13204145.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c13204145.lua) | 53 |
| Clown Crew Biancaviso | `82159583` | [Scripts/c82159583.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c82159583.lua) | 52 |
| Doodle Beast - Tyranno | `67725394` | [Scripts/c67725394.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c67725394.lua) | 51 |
| Bahalutiya, the Grand Radiance | `53318263` | [Scripts/c53318263.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c53318263.lua) | 49 |
| Fairy Tale Tails | `91957038` | [Scripts/c91957038.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c91957038.lua) | 47 |
| Subterror Final Battle | `74640994` | [Scripts/c74640994.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74640994.lua) | 46 |
| Mimighoul Archfiend | `50415441` | [Scripts/c50415441.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c50415441.lua) | 41 |
| World Legacy Pawns | `89320376` | [Scripts/c89320376.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c89320376.lua) | 41 |
| Tessera the Primal Squire | `67584223` | [Scripts/c67584223.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c67584223.lua) | 40 |
| Spellbook of Fate | `97997309` | [Scripts/c97997309.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c97997309.lua) | 40 |
| Mimighoul Fork | `19338434` | [Scripts/c19338434.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c19338434.lua) | 40 |
| Bettan Bat | `84079032` | [Scripts/c84079032.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c84079032.lua) | 39 |
| Mimighoul Master | `55537983` | [Scripts/c55537983.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c55537983.lua) | 38 |
| Green Ninja | `15198996` | [Scripts/c15198996.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c15198996.lua) | 35 |
| Mausoleum of the Emperor | `80921533` | [Scripts/c80921533.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c80921533.lua) | 35 |
| Samsara Dragon | `33750025` | [Scripts/c33750025.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c33750025.lua) | 35 |
| Eda the Sun Magician | `96352326` | [Scripts/c96352326.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c96352326.lua) | 34 |
| Proof of Pruflas | `85847157` | [Scripts/c85847157.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c85847157.lua) | 34 |
| The Hidden City | `5697558` | [Scripts/c5697558.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c5697558.lua) | 33 |
| Spell Card "Soul Exchange" | `15735108` | [Scripts/c15735108.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c15735108.lua) | 30 |
| Gemini Summoner | `19041767` | [Scripts/c19041767.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c19041767.lua) | 30 |
| Cry Havoc! | `39712330` | [Scripts/c39712330.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c39712330.lua) | 30 |
| Ultimate Offering | `80604091` | [Scripts/c80604091.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c80604091.lua) | 29 |
| ...and 3 more |  |  |  |

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

### Mimighoul Maker (`13204145`)

Source: [Scripts/c13204145.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c13204145.lua)

```lua
			Duel.ChangePosition(tc,POS_FACEUP_ATTACK)
		else
			local pos=Duel.SelectPosition(tp,tc,POS_FACEUP)
			Duel.ChangePosition(tc,pos)
		end
```

### Clown Crew Biancaviso (`82159583`)

Source: [Scripts/c82159583.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c82159583.lua)

```lua
		local s1=tc:IsSummonable(true,nil,1)
		local s2=tc:IsMSetable(true,nil,1)
		if (s1 and s2 and Duel.SelectPosition(tp,tc,POS_FACEUP_ATTACK+POS_FACEDOWN_DEFENSE)==POS_FACEUP_ATTACK) or not s2 then
			Duel.Summon(tp,tc,true,nil,1)
		else
```
