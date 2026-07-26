# Card.IsControlerCanBeChanged

## Signature

```lua
Card.IsControlerCanBeChanged(Card c, [bool ignore_mzone], [int zone]) -> bool
```

## Description

Checks whether control of c can currently move to the other player.
The card must be in the Monster Zone and must not be affected by EFFECT_CANNOT_CHANGE_CONTROL. Unless ignore_mzone is true, the opponent must also have an available Monster Zone in zone.

## Parameters

- `c` `Card`
- `ignore_mzone` `bool` optional - default: false
- `zone` `int` optional - default: 0xff

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3630`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **125** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.IsControlerCanBeChanged`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Goyo Emperor](/examples/cards/59255742) | `59255742` | [Scripts/c59255742.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59255742.lua) | 70 |
| [Tellusion the Magna Warrior](/examples/cards/24431911) | `24431911` | [Scripts/c24431911.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24431911.lua) | 62 |
| Enlilgirsu, the Orcust Mekk-Knight | `74820316` | [Scripts/c74820316.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74820316.lua) | 56 |
| R.B. Lambda Blade | `17188206` | [Scripts/c17188206.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c17188206.lua) | 56 |
| Eternal Bond | `45283341` | [Scripts/c45283341.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c45283341.lua) | 53 |
| Phara, the Goddess of the Beginning | `82344137` | [Scripts/c82344137.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c82344137.lua) | 52 |
| Possessed Resonance - Wynn | `60516416` | [Scripts/c60516416.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c60516416.lua) | 52 |
| Borreload Dragon | `31833038` | [Scripts/c31833038.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c31833038.lua) | 50 |
| Fabled Levilazebul | `21281085` | [Scripts/c21281085.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c21281085.lua) | 50 |
| Primite Howl | `41488249` | [Scripts/c41488249.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c41488249.lua) | 49 |
| Vanquish Soul Hollie Sue | `93156774` | [Scripts/c93156774.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93156774.lua) | 48 |
| Amaze Attraction Viking Vortex | `97182396` | [Scripts/c97182396.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c97182396.lua) | 47 |
| Hecahands Xeno | `94410955` | [Scripts/c94410955.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c94410955.lua) | 46 |
| Chaotic Elements | `92221402` | [Scripts/c92221402.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92221402.lua) | 46 |
| Number S38: Titanic Galaxy | `16110708` | [Scripts/c16110708.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c16110708.lua) | 45 |
| Predaplant Longinephila | `44994712` | [Scripts/c44994712.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44994712.lua) | 45 |
| SPYRAL MISSION - Recapture | `39373426` | [Scripts/c39373426.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c39373426.lua) | 45 |
| Ancient Warriors Saga - Deception and Betrayal | `45115956` | [Scripts/c45115956.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c45115956.lua) | 45 |
| Time Thief Double Barrel | `91135480` | [Scripts/c91135480.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c91135480.lua) | 44 |
| Borreload Liberator Dragon | `27096833` | [Scripts/c27096833.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c27096833.lua) | 44 |
| Metaphys Horus | `36898537` | [Scripts/c36898537.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c36898537.lua) | 44 |
| Tragoedia | `98777036` | [Scripts/c98777036.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c98777036.lua) | 44 |
| Number 46: Dragluon | `2978414` | [Scripts/c2978414.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c2978414.lua) | 44 |
| Number F0: Utopic Future Zexal | `41522092` | [Scripts/c41522092.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c41522092.lua) | 43 |
| ...and 101 more |  |  |  |

## Script Examples

### Goyo Emperor (`59255742`)

Source: [Scripts/c59255742.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59255742.lua)

```lua
end
function c59255742.filter(c,tp)
	return c:IsSummonPlayer(1-tp) and c:IsControlerCanBeChanged(true)
end
function c59255742.target(e,tp,eg,ep,ev,re,r,rp,chk)
```

### Tellusion the Magna Warrior (`24431911`)

Source: [Scripts/c24431911.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24431911.lua)

```lua
	local tc=Duel.GetFirstTarget()
	if tc:IsRelateToChain() and tc:IsLocation(LOCATION_MZONE) then
		if e:GetLabel()==1 and tc:IsControlerCanBeChanged()
			and Duel.SelectYesNo(tp,aux.Stringid(id,3)) then
			Duel.GetControl(tc,tp)
```

### Enlilgirsu, the Orcust Mekk-Knight (`74820316`)

Source: [Scripts/c74820316.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74820316.lua)

```lua
end
function s.gcfilter2(c)
	return c:IsFaceup() and c:IsControlerCanBeChanged()
end
function s.thtg(e,tp,eg,ep,ev,re,r,rp,chk,chkc)
```
