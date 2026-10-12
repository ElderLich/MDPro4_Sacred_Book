# Effect.GetActivateLocation

## Signature

```lua
Effect.GetActivateLocation(Effect e) -> int
```

## Description

Returns the location from which effect e was activated.

## Parameters

- `e` `Effect`

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libeffect.cpp:658`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **76** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Effect.GetActivateLocation) with `Effect.GetActivateLocation`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Shooting Majestic Star Dragon](/examples/cards/40939228) | `40939228` | [Scripts/c40939228.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c40939228.lua) | 1 |
| [W:P Fancy Ball](/examples/cards/4993187) | `4993187` | [Scripts/c4993187.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c4993187.lua) | 1 |
| Tearlaments Havnis | `37961969` | [Scripts/c37961969.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c37961969.lua) | 1 |
| D/D/D Deviser King Deus Machinex | `46593546` | [Scripts/c46593546.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c46593546.lua) | 1 |
| Heavy Interlock | `20071842` | [Scripts/c20071842.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c20071842.lua) | 1 |
| Fydraulis Harmonia | `70088809` | [Scripts/c70088809.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c70088809.lua) | 1 |
| Rapid Trigger | `67526112` | [Scripts/c67526112.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c67526112.lua) | 1 |
| Kuriboh - Multiply! | `14965712` | [Scripts/c14965712.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c14965712.lua) | 1 |
| Gravekeeper's Trap | `98715423` | [Scripts/c98715423.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c98715423.lua) | 1 |
| Arcana Force EX - The Chaos Ruler | `12686296` | [Scripts/c12686296.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c12686296.lua) | 1 |
| Nerva the Power Patron of Creation | `53589300` | [Scripts/c53589300.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c53589300.lua) | 1 |
| Scareclaw Tri-Heart | `59120809` | [Scripts/c59120809.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c59120809.lua) | 1 |
| Volcanic Inferno | `84138874` | [Scripts/c84138874.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c84138874.lua) | 1 |
| Plundered Power Patron Plane - Vidolia | `51669847` | [Scripts/c51669847.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c51669847.lua) | 1 |
| Titaniklad the Ash Dragon | `41373230` | [Scripts/c41373230.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c41373230.lua) | 1 |
| Dragunity Lord - Georgius | `70522875` | [Scripts/c70522875.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c70522875.lua) | 1 |
| Distrust Paranoia | `81965543` | [Scripts/c81965543.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c81965543.lua) | 1 |
| Blue-Eyes Spirit Dragon | `59822133` | [Scripts/c59822133.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c59822133.lua) | 1 |
| Transcendosaurus Meteorus | `31241087` | [Scripts/c31241087.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c31241087.lua) | 1 |
| Transcendosaurus Gigantozowler | `67745632` | [Scripts/c67745632.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c67745632.lua) | 1 |
| Argostars - Home Stadium | `2674965` | [Scripts/c2674965.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c2674965.lua) | 1 |
| Dragonic Pendulum | `71817640` | [Scripts/c71817640.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c71817640.lua) | 1 |
| Krishnerd Witch | `37006702` | [Scripts/c37006702.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c37006702.lua) | 1 |
| The Zombie Vampire | `73082255` | [Scripts/c73082255.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c73082255.lua) | 1 |
| ...and 52 more |  |  |  |

## Script Examples

### Shooting Majestic Star Dragon (`40939228`)

Source: [Scripts/c40939228.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c40939228.lua)

```lua
		Duel.SetOperationInfo(0,CATEGORY_REMOVE,g,#g,0,0)
	end
	if re:GetActivateLocation()==LOCATION_GRAVE then
		e:SetCategory(e:GetCategory()|CATEGORY_GRAVE_ACTION)
	else
```

### W:P Fancy Ball (`4993187`)

Source: [Scripts/c4993187.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c4993187.lua)

```lua
		Duel.SetOperationInfo(0,CATEGORY_REMOVE,eg,1,0,0)
	end
	if re:GetActivateLocation()==LOCATION_GRAVE then
		e:SetCategory(e:GetCategory()|CATEGORY_GRAVE_ACTION)
	else
```

### Tearlaments Havnis (`37961969`)

Source: [Scripts/c37961969.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c37961969.lua)

```lua
end
function c37961969.tgcon(e,tp,eg,ep,ev,re,r,rp)
	return rp==1-tp and re:IsActiveType(TYPE_MONSTER) and re:GetActivateLocation()==LOCATION_MZONE
end
function c37961969.tgtg(e,tp,eg,ep,ev,re,r,rp,chk)
```
