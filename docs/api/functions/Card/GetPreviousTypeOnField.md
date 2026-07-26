# Card.GetPreviousTypeOnField

## Signature

```lua
Card.GetPreviousTypeOnField(Card c) -> int
```

## Description

Returns the Type value recorded for c's previous on-field state.

## Parameters

- `c` `Card`

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3450`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **72** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.GetPreviousTypeOnField`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Fossil Fusion | `59419719` | [Scripts/c59419719.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59419719.lua) | 60 |
| Supreme King Dragon Lightwurm | `41908872` | [Scripts/c41908872.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c41908872.lua) | 59 |
| Performapal Celestial Magician | `58092907` | [Scripts/c58092907.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c58092907.lua) | 58 |
| Ursarctic Quint Charge | `15758127` | [Scripts/c15758127.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c15758127.lua) | 56 |
| Despia, Theater of the Branded | `99543666` | [Scripts/c99543666.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c99543666.lua) | 55 |
| Anubis the Last Judge | `60411677` | [Scripts/c60411677.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c60411677.lua) | 54 |
| Chevreuil, Hunting Scout of the Deep Forest | `13023431` | [Scripts/c13023431.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c13023431.lua) | 54 |
| World Legacy Collapse | `36197902` | [Scripts/c36197902.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c36197902.lua) | 53 |
| Pendulum Witch | `43502497` | [Scripts/c43502497.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c43502497.lua) | 51 |
| Salamangreat Zebroid X | `44161893` | [Scripts/c44161893.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44161893.lua) | 51 |
| Odd-Eyes Lancer Dragon | `83347294` | [Scripts/c83347294.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c83347294.lua) | 51 |
| Gray Layer | `18616294` | [Scripts/c18616294.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c18616294.lua) | 50 |
| Gussari @Ignister | `55762976` | [Scripts/c55762976.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c55762976.lua) | 49 |
| Peaceful Planet Calarium | `82460246` | [Scripts/c82460246.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c82460246.lua) | 49 |
| Evil HERO Inferno Wing - Backfire | `59893882` | [Scripts/c59893882.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59893882.lua) | 49 |
| Grenosaurus Giga-Cannon | `34481518` | [Scripts/c34481518.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c34481518.lua) | 49 |
| Synchro Overtop | `653675` | [Scripts/c653675.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c653675.lua) | 48 |
| Valiant Shark Lancer | `23672629` | [Scripts/c23672629.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c23672629.lua) | 48 |
| Aluber the Jester of Despia | `62962630` | [Scripts/c62962630.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c62962630.lua) | 47 |
| Sunvine Thrasher | `91557476` | [Scripts/c91557476.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c91557476.lua) | 47 |
| Tenyi Spirit - Shthana | `24557335` | [Scripts/c24557335.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24557335.lua) | 47 |
| Princess Cologne | `75574498` | [Scripts/c75574498.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c75574498.lua) | 46 |
| Voloferniges, the Darkest Dragon Doomrider | `38694052` | [Scripts/c38694052.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c38694052.lua) | 46 |
| Majestic Mirage | `98020526` | [Scripts/c98020526.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c98020526.lua) | 46 |
| ...and 48 more |  |  |  |

## Script Examples

### Fossil Fusion (`59419719`)

Source: [Scripts/c59419719.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59419719.lua)

```lua
end
function c59419719.cfilter(c,tp)
	return c:IsPreviousSetCard(0x149) and c:GetPreviousTypeOnField()&TYPE_FUSION~=0
		and c:IsReason(REASON_BATTLE+REASON_EFFECT) and c:IsPreviousControler(tp) and c:IsPreviousLocation(LOCATION_MZONE)
end
```

### Supreme King Dragon Lightwurm (`41908872`)

Source: [Scripts/c41908872.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c41908872.lua)

```lua
end
function c41908872.thfilter2(c,tp)
	return c:IsReason(REASON_BATTLE+REASON_EFFECT) and bit.band(c:GetPreviousTypeOnField(),TYPE_PENDULUM)~=0
		and c:IsPreviousLocation(LOCATION_MZONE) and c:IsPreviousControler(tp) and c:IsPreviousPosition(POS_FACEUP)
end
```

### Performapal Celestial Magician (`58092907`)

Source: [Scripts/c58092907.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c58092907.lua)

```lua
	return (c:IsReason(REASON_BATTLE) or (c:IsReason(REASON_EFFECT) and rp==1-tp)) and c:IsPreviousLocation(LOCATION_MZONE)
		and c:IsPreviousControler(tp) and c:IsSummonLocation(LOCATION_EXTRA)
		and bit.band(c:GetPreviousTypeOnField(),TYPE_FUSION+TYPE_SYNCHRO+TYPE_XYZ)~=0 and c:IsPreviousPosition(POS_FACEUP)
end
function c58092907.spcon(e,tp,eg,ep,ev,re,r,rp)
```
