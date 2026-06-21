# Card.IsDefensePos

## Signature

```lua
Card.IsDefensePos(Card c) -> bool
```

## Description

Check whether c is a defensive representation

## Parameters

- `c` `Card`

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3604`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **121** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.IsDefensePos`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Mimighoul Maker | `13204145` | [Scripts/c13204145.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c13204145.lua) | 53 |
| Enneacraft Reverth | `80015408` | [Scripts/c80015408.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c80015408.lua) | 52 |
| Goblin Freefall Squad | `85123771` | [Scripts/c85123771.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c85123771.lua) | 48 |
| Scareclaw Tri-Heart | `59120809` | [Scripts/c59120809.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59120809.lua) | 48 |
| Mermail Abyssbalaen | `75180828` | [Scripts/c75180828.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c75180828.lua) | 46 |
| Ultimate Conductor Tyranno | `18940556` | [Scripts/c18940556.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c18940556.lua) | 45 |
| Junk Berserker | `59771339` | [Scripts/c59771339.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59771339.lua) | 45 |
| Nitro Warrior | `18013090` | [Scripts/c18013090.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c18013090.lua) | 44 |
| Majestic Red Dragon | `67030233` | [Scripts/c67030233.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c67030233.lua) | 43 |
| Superheavy Samurai Helper | `44891812` | [Scripts/c44891812.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44891812.lua) | 43 |
| Sangenpai Transcendent Dragion | `18969888` | [Scripts/c18969888.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c18969888.lua) | 43 |
| Gaming Gamer GG | `15778492` | [Scripts/c15778492.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c15778492.lua) | 43 |
| Twilight Ninja Getsuga, the Shogun | `76930964` | [Scripts/c76930964.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c76930964.lua) | 43 |
| Ace★Spades Speculation | `10796448` | [Scripts/c10796448.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c10796448.lua) | 42 |
| Morphtronic Converter | `90659259` | [Scripts/c90659259.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c90659259.lua) | 42 |
| Karakuri Super Shogun mdl 00N "Bureibu" | `25904894` | [Scripts/c25904894.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c25904894.lua) | 42 |
| Mimighoul Archfiend | `50415441` | [Scripts/c50415441.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c50415441.lua) | 41 |
| Primitive Planet Reichphobia | `56063182` | [Scripts/c56063182.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c56063182.lua) | 41 |
| Morphtronic Slingen | `75775867` | [Scripts/c75775867.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c75775867.lua) | 41 |
| Black Rose Dragon | `73580471` | [Scripts/c73580471.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c73580471.lua) | 40 |
| Number 22: Zombiestein | `73445448` | [Scripts/c73445448.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c73445448.lua) | 40 |
| Scareclaw Reichheart | `82361809` | [Scripts/c82361809.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c82361809.lua) | 39 |
| Superheavy Samurai Soulbuster Gauntlet | `35800511` | [Scripts/c35800511.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c35800511.lua) | 39 |
| Gouki Jet Ogre | `59644128` | [Scripts/c59644128.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59644128.lua) | 39 |
| ...and 97 more |  |  |  |

## Script Examples

### Mimighoul Maker (`13204145`)

Source: [Scripts/c13204145.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c13204145.lua)

```lua
end
function s.posfilter(c)
	return c:IsFacedown() and c:IsDefensePos()
end
function s.postg(e,tp,eg,ep,ev,re,r,rp,chk,chkc)
```

### Enneacraft Reverth (`80015408`)

Source: [Scripts/c80015408.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c80015408.lua)

```lua
end
function s.posfilter(c)
	return c:IsSetCard(0x1d4) and c:IsFacedown() and c:IsDefensePos()
end
function s.sptg(e,tp,eg,ep,ev,re,r,rp,chk)
```

### Goblin Freefall Squad (`85123771`)

Source: [Scripts/c85123771.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c85123771.lua)

```lua
function s.disop(e,tp,eg,ep,ev,re,r,rp)
	local c=e:GetHandler()
	if not c:IsRelateToEffect(e) or c:IsDefensePos() or not c:IsCanChangePosition() then return end
	Duel.ChangePosition(c,POS_FACEUP_DEFENSE,POS_FACEDOWN_DEFENSE,0,0)
	local tc=Duel.GetFirstTarget()
```
