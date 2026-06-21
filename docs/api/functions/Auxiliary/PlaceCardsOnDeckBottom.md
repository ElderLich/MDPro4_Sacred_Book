# Auxiliary.PlaceCardsOnDeckBottom

## Signature

```lua
Auxiliary.PlaceCardsOnDeckBottom(int p, Group g, [int reason]) -> int
```

## Description

Sends g to the top of the Deck by reason, lets p order cards that reached either Deck, moves them to the bottom, and returns the number of operated cards.

## Parameters

- `p` `int`
- `g` `Group`
- `reason` `int` optional - Defaults to REASON_EFFECT.

## Returns

- `int` - The number of operated cards.

## Source

- `Utilities/utility.lua:1617`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **28** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Auxiliary.PlaceCardsOnDeckBottom`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [A Bao A Qu, the Lightless Shadow](/examples/cards/4731783) | `4731783` | [Scripts/c4731783.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c4731783.lua) | 61 |
| Tearlaments Scheiren | `572850` | [Scripts/c572850.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c572850.lua) | 59 |
| Tearlaments Havnis | `37961969` | [Scripts/c37961969.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c37961969.lua) | 58 |
| R.B. Shepherd's Crook | `80071619` | [Scripts/c80071619.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c80071619.lua) | 55 |
| Anubis the Last Judge | `60411677` | [Scripts/c60411677.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c60411677.lua) | 54 |
| Psychic Arsenal | `16238373` | [Scripts/c16238373.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c16238373.lua) | 54 |
| Tearlaments Merrli | `74078255` | [Scripts/c74078255.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74078255.lua) | 54 |
| Possessed Resonance - Wynn | `60516416` | [Scripts/c60516416.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c60516416.lua) | 52 |
| Rahamu, Envoy of the Sacred Tome | `53904087` | [Scripts/c53904087.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c53904087.lua) | 51 |
| Yummyusment★Acroquey | `93360904` | [Scripts/c93360904.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93360904.lua) | 51 |
| Saryuja Skull Dread | `74997493` | [Scripts/c74997493.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74997493.lua) | 51 |
| Skull Archfiend of Chaos | `24088928` | [Scripts/c24088928.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24088928.lua) | 49 |
| Volcanic Inferno | `84138874` | [Scripts/c84138874.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c84138874.lua) | 48 |
| Ryzeal Cross | `6798031` | [Scripts/c6798031.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c6798031.lua) | 46 |
| Yummyusment☆Mignon | `66975205` | [Scripts/c66975205.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c66975205.lua) | 46 |
| The Chaos Creator | `90488465` | [Scripts/c90488465.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c90488465.lua) | 46 |
| Dark Spirit's Mastery | `14386013` | [Scripts/c14386013.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c14386013.lua) | 45 |
| Favorite Contact | `75047173` | [Scripts/c75047173.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c75047173.lua) | 44 |
| Nouvelles Restaurant "At Table" | `15388353` | [Scripts/c15388353.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c15388353.lua) | 44 |
| Floowandereeze and the Unexplored Winds | `55521751` | [Scripts/c55521751.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c55521751.lua) | 40 |
| Raidraptor - Roost | `64049553` | [Scripts/c64049553.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c64049553.lua) | 38 |
| Flowerdino | `10851853` | [Scripts/c10851853.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c10851853.lua) | 35 |
| Link Bound | `51335426` | [Scripts/c51335426.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c51335426.lua) | 35 |
| Saryuja's Shackles | `11434258` | [Scripts/c11434258.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c11434258.lua) | 31 |
| ...and 4 more |  |  |  |

## Script Examples

### A Bao A Qu, the Lightless Shadow (`4731783`)

Source: [Scripts/c4731783.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c4731783.lua)

```lua
		local rg=Duel.GetFieldGroup(p,LOCATION_HAND,0):Select(p,dc,dc,nil)
		Duel.ShuffleHand(p)
		aux.PlaceCardsOnDeckBottom(p,rg)
	end
end
```

### Tearlaments Scheiren (`572850`)

Source: [Scripts/c572850.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c572850.lua)

```lua
				Duel.HintSelection(cg)
			end
			aux.PlaceCardsOnDeckBottom(tp,mat1,REASON_EFFECT+REASON_MATERIAL+REASON_FUSION)
			Duel.BreakEffect()
			Duel.SpecialSummon(tc,SUMMON_TYPE_FUSION,tp,tp,false,false,POS_FACEUP)
```

### Tearlaments Havnis (`37961969`)

Source: [Scripts/c37961969.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c37961969.lua)

```lua
				Duel.HintSelection(cg)
			end
			aux.PlaceCardsOnDeckBottom(tp,mat1,REASON_EFFECT+REASON_MATERIAL+REASON_FUSION)
			Duel.BreakEffect()
			Duel.SpecialSummon(tc,SUMMON_TYPE_FUSION,tp,tp,false,false,POS_FACEUP)
```
