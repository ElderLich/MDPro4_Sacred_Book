# Duel.ChangePosition

## Signature

```lua
Duel.ChangePosition(Card|Group targets, int au, [int ad], [int du], [int dd], [bool noflip], [bool setavailable]) -> int
```

## Description

Changing the representation of targets returns the number of actual operations
The attack on the watch side becomes au, the attack on the inside indicates ad,
The side of the garage that becomes du, inside the garrison said to become dd
If noflip = true, the reverse effect will not be triggered (but the effect of inversion will be triggered)
If setavailable = true then the object will become the back side also launched reversal effect

## Parameters

- `targets` `Card|Group`
- `au` `int`
- `ad` `int` optional - default: au
- `du` `int` optional - default: au
- `dd` `int` optional - default: au
- `noflip` `bool` optional - default: false
- `setavailable` `bool` optional - default: false

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4880`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **511** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Duel.ChangePosition`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Salamandra with Chain](/examples/cards/62091148) | `62091148` | [Scripts/c62091148.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c62091148.lua) | 81 |
| [Deftero Enneacraft - "alazoneIA"](/examples/cards/92171126) | `92171126` | [Scripts/c92171126.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92171126.lua) | 68 |
| [Enneacraft - Asta.PIXEA](/examples/cards/28454232) | `28454232` | [Scripts/c28454232.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c28454232.lua) | 64 |
| [Enneacraft - Archa.TAIL](/examples/cards/81237046) | `81237046` | [Scripts/c81237046.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c81237046.lua) | 63 |
| [Enneacraft - Atil.SPIA](/examples/cards/71801447) | `71801447` | [Scripts/c71801447.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71801447.lua) | 62 |
| [Enneacraft - Aiza.LEON](/examples/cards/82359538) | `82359538` | [Scripts/c82359538.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c82359538.lua) | 62 |
| Regenesis Birth | `27781371` | [Scripts/c27781371.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c27781371.lua) | 60 |
| Chaos Hats | `2372506` | [Scripts/c2372506.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c2372506.lua) | 59 |
| Magical Hats | `81210420` | [Scripts/c81210420.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c81210420.lua) | 59 |
| Power Tool Braver Dragon | `63265554` | [Scripts/c63265554.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63265554.lua) | 58 |
| Enneacraft - Atori.MAR | `54842941` | [Scripts/c54842941.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c54842941.lua) | 57 |
| Mimighoul Maker | `13204145` | [Scripts/c13204145.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c13204145.lua) | 53 |
| Ekto Enneacraft - "tromarIA" | `29570824` | [Scripts/c29570824.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c29570824.lua) | 52 |
| Enato Enneacraft - "oknirIA" | `55965529` | [Scripts/c55965529.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c55965529.lua) | 52 |
| Enneacraft Reverth | `80015408` | [Scripts/c80015408.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c80015408.lua) | 52 |
| Amaze Attraction Thrill Train | `36591747` | [Scripts/c36591747.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c36591747.lua) | 52 |
| Scrap-Iron Sacred Statue | `85520170` | [Scripts/c85520170.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c85520170.lua) | 52 |
| Trito Enneacraft - "exapatisIA" | `44716748` | [Scripts/c44716748.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44716748.lua) | 51 |
| Proto Enneacraft - "orgIA" | `56187077` | [Scripts/c56187077.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c56187077.lua) | 51 |
| Performapal Corn | `33103459` | [Scripts/c33103459.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c33103459.lua) | 51 |
| Arbitration of White | `57964143` | [Scripts/c57964143.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c57964143.lua) | 51 |
| First Penguin | `12975671` | [Scripts/c12975671.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c12975671.lua) | 50 |
| VARefar, the Judge of Ball | `19743887` | [Scripts/c19743887.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c19743887.lua) | 50 |
| Poissonniere de Nouvelles | `46485778` | [Scripts/c46485778.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c46485778.lua) | 49 |
| ...and 487 more |  |  |  |

## Script Examples

### Salamandra with Chain (`62091148`)

Source: [Scripts/c62091148.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c62091148.lua)

```lua
			Duel.HintSelection(g)
			local tc2=g:GetFirst()
			Duel.ChangePosition(tc2,POS_FACEDOWN_DEFENSE)
		end
	else
```

### Deftero Enneacraft - "alazoneIA" (`92171126`)

Source: [Scripts/c92171126.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92171126.lua)

```lua
function s.thcost2(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return true end
	Duel.ChangePosition(e:GetHandler(),POS_FACEUP_DEFENSE)
end
function s.thfilter2(c)
```

### Enneacraft - Asta.PIXEA (`28454232`)

Source: [Scripts/c28454232.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c28454232.lua)

```lua
function s.discost(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return true end
	Duel.ChangePosition(e:GetHandler(),POS_FACEUP_DEFENSE)
end
function s.distg(e,tp,eg,ep,ev,re,r,rp,chk)
```
