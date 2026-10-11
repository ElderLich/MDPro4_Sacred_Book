# Duel.ShuffleExtra

## Signature

```lua
Duel.ShuffleExtra(int player) -> void
```

## Description

Shuffles player's Extra Deck.

## Parameters

- `player` `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4916`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **37** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Duel.ShuffleExtra) with `Duel.ShuffleExtra`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Kewl Tune Crackle](/examples/cards/39576656) | `39576656` | [Scripts/c39576656.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c39576656.lua) | 2 |
| Hyperinvoked Aeon | `33166263` | [Scripts/c33166263.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c33166263.lua) | 1 |
| Future Fusion | `77565204` | [Scripts/c77565204.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c77565204.lua) | 1 |
| Number 78: Number Archive | `29085954` | [Scripts/c29085954.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c29085954.lua) | 1 |
| Fydraulis Harmonia | `70088809` | [Scripts/c70088809.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c70088809.lua) | 1 |
| Meklord Astro Dragon Triskelion | `4837861` | [Scripts/c4837861.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c4837861.lua) | 1 |
| Zaborg the Mega Monarch | `87602890` | [Scripts/c87602890.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c87602890.lua) | 1 |
| Topologic Blaster Dragon | `30064423` | [Scripts/c30064423.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30064423.lua) | 1 |
| True King Lithosagym, the Disaster | `30539496` | [Scripts/c30539496.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30539496.lua) | 1 |
| Aegaion the Sea Castrum | `10678778` | [Scripts/c10678778.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c10678778.lua) | 1 |
| Number 1: Infection Buzzking | `10666000` | [Scripts/c10666000.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c10666000.lua) | 1 |
| Sacred Spirit Sword Aiwass | `63926180` | [Scripts/c63926180.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63926180.lua) | 1 |
| Abyss Script - Fire Dragon's Lair | `50179591` | [Scripts/c50179591.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c50179591.lua) | 1 |
| Trishula, the Dragon of Icy Imprisonment | `15661378` | [Scripts/c15661378.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c15661378.lua) | 1 |
| White Relic of Dogmatika | `48654323` | [Scripts/c48654323.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c48654323.lua) | 1 |
| Silverrokket Dragon | `32476603` | [Scripts/c32476603.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c32476603.lua) | 1 |
| Ilios the Black Sun Dragon | `19438484` | [Scripts/c19438484.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c19438484.lua) | 1 |
| Branded in Central Dogmatika | `14220547` | [Scripts/c14220547.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c14220547.lua) | 1 |
| Pride of the Plunder Patroll | `17016131` | [Scripts/c17016131.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c17016131.lua) | 1 |
| Number 89: Diablosis the Mind Hacker | `95474755` | [Scripts/c95474755.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c95474755.lua) | 1 |
| Banquet of Millions | `48814566` | [Scripts/c48814566.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c48814566.lua) | 1 |
| Galaxy Hundred | `897409` | [Scripts/c897409.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c897409.lua) | 2 |
| Dogmatikamatrix | `35569555` | [Scripts/c35569555.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c35569555.lua) | 1 |
| Mimighoul Charm | `55733143` | [Scripts/c55733143.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c55733143.lua) | 1 |
| ...and 13 more |  |  |  |

## Script Examples

### Kewl Tune Crackle (`39576656`)

Source: [Scripts/c39576656.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c39576656.lua)

```lua
			end
		end
		Duel.ShuffleExtra(1-tp)
	end
end
```

### Hyperinvoked Aeon (`33166263`)

Source: [Scripts/c33166263.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c33166263.lua)

```lua
			local rg=g:FilterSelect(tp,Card.IsAbleToRemove,1,3,nil)
			Duel.Remove(rg,POS_FACEUP,REASON_EFFECT)
			Duel.ShuffleExtra(1-tp)
		end
	end
```

### Future Fusion (`77565204`)

Source: [Scripts/c77565204.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c77565204.lua)

```lua
		e:SetLabel(code)
		e:SetLabelObject(mat)
		Duel.ShuffleExtra(tp)
	end
end
```
