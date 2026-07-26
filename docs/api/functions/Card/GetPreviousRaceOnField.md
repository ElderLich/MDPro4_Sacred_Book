# Card.GetPreviousRaceOnField

## Signature

```lua
Card.GetPreviousRaceOnField(Card c) -> int
```

## Description

Returns the Race value recorded for c's previous on-field state.

## Parameters

- `c` `Card`

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3454`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **55** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.GetPreviousRaceOnField`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Teleport Fusion](/examples/cards/36494597) | `36494597` | [Scripts/c36494597.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c36494597.lua) | 64 |
| Despia, Theater of the Branded | `99543666` | [Scripts/c99543666.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c99543666.lua) | 55 |
| Chevreuil, Hunting Scout of the Deep Forest | `13023431` | [Scripts/c13023431.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c13023431.lua) | 54 |
| Melffy Pinny | `34800281` | [Scripts/c34800281.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c34800281.lua) | 53 |
| Arbitration of White | `57964143` | [Scripts/c57964143.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c57964143.lua) | 51 |
| Scrap Garage | `91019775` | [Scripts/c91019775.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c91019775.lua) | 51 |
| Armed Rebeellion | `21056275` | [Scripts/c21056275.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c21056275.lua) | 50 |
| Grenosaurus Giga-Cannon | `34481518` | [Scripts/c34481518.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c34481518.lua) | 49 |
| Sangen Furo | `55484152` | [Scripts/c55484152.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c55484152.lua) | 49 |
| Desperado Barrel Dragon | `76728962` | [Scripts/c76728962.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c76728962.lua) | 48 |
| Transcendosaurus Exaraptor | `56818742` | [Scripts/c56818742.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c56818742.lua) | 48 |
| Celestial Knightlord Parshath | `48589580` | [Scripts/c48589580.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c48589580.lua) | 47 |
| Ragnaraika Hunting Dance | `89824842` | [Scripts/c89824842.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c89824842.lua) | 46 |
| Machina Citadel | `87074380` | [Scripts/c87074380.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c87074380.lua) | 46 |
| Triamid Loading | `64576557` | [Scripts/c64576557.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c64576557.lua) | 45 |
| House Dragonmaid | `41232647` | [Scripts/c41232647.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c41232647.lua) | 44 |
| Salamangreat Fennec | `49094491` | [Scripts/c49094491.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c49094491.lua) | 43 |
| Magikuriboh | `31699677` | [Scripts/c31699677.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c31699677.lua) | 43 |
| Beetrooper Cruel Saturnas | `91300233` | [Scripts/c91300233.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c91300233.lua) | 43 |
| The World Tree | `5973663` | [Scripts/c5973663.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c5973663.lua) | 41 |
| Two-for-One Repair Job | `44459942` | [Scripts/c44459942.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44459942.lua) | 41 |
| Machina Defense Perimeter | `13247801` | [Scripts/c13247801.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c13247801.lua) | 41 |
| Salvagent Driver | `62306203` | [Scripts/c62306203.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c62306203.lua) | 41 |
| Keeper of the Shrine | `66752837` | [Scripts/c66752837.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c66752837.lua) | 40 |
| ...and 31 more |  |  |  |

## Script Examples

### Teleport Fusion (`36494597`)

Source: [Scripts/c36494597.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c36494597.lua)

```lua
end
function s.cfilter(c,tp)
	return c:IsSummonLocation(LOCATION_EXTRA) and c:GetPreviousRaceOnField()&RACE_PSYCHO~=0 and c:IsReason(REASON_BATTLE+REASON_EFFECT)
		and c:IsPreviousLocation(LOCATION_MZONE) and c:IsPreviousControler(tp) and c:IsPreviousPosition(POS_FACEUP)
end
```

### Despia, Theater of the Branded (`99543666`)

Source: [Scripts/c99543666.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c99543666.lua)

```lua
function c99543666.cfilter(c,tp,rp)
	return c:IsPreviousPosition(POS_FACEUP) and c:IsPreviousControler(tp)
		and c:GetPreviousRaceOnField()&RACE_FAIRY~=0 and c:GetPreviousTypeOnField()&TYPE_FUSION==0
		and (c:IsReason(REASON_BATTLE) or (rp==1-tp and c:IsReason(REASON_EFFECT)))
end
```

### Chevreuil, Hunting Scout of the Deep Forest (`13023431`)

Source: [Scripts/c13023431.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c13023431.lua)

```lua
	else
		return bc:GetPreviousPosition()&POS_FACEUP>0 and bc:GetPreviousLocation()&LOCATION_MZONE==LOCATION_MZONE and bc:IsPreviousControler(tp)
			and bc:GetPreviousTypeOnField()&TYPE_MONSTER==TYPE_MONSTER and c:GetPreviousRaceOnField()&RACE_WARRIOR==RACE_WARRIOR
			and bc:GetPreviousAttributeOnField()&ATTRIBUTE_EARTH==ATTRIBUTE_EARTH
	end
```
