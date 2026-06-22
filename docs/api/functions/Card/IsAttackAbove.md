# Card.IsAttackAbove

## Signature

```lua
Card.IsAttackAbove(Card c, int atk) -> bool
```

## Description

Checks whether c is a monster or currently treated as one, and whether its current ATK is at least atk.
Unlike Card.IsAttackBelow, this core does not add a separate guard for unknown ATK before comparing.

## Parameters

- `c` `Card`
- `atk` `int`

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3619`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **137** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.IsAttackAbove`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Favorite HERO Flame Wingman](/examples/cards/13243124) | `13243124` | [Scripts/c13243124.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c13243124.lua) | 66 |
| [Ehther the Heavenly Monarch](/examples/cards/96570609) | `96570609` | [Scripts/c96570609.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c96570609.lua) | 65 |
| [Dark End Evaporation Dragon](/examples/cards/62002838) | `62002838` | [Scripts/c62002838.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c62002838.lua) | 63 |
| [Light End Sublimation Dragon](/examples/cards/35614780) | `35614780` | [Scripts/c35614780.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c35614780.lua) | 61 |
| Flame Swordsrealm | `73714736` | [Scripts/c73714736.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c73714736.lua) | 58 |
| Meteonis Drytron | `22398665` | [Scripts/c22398665.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c22398665.lua) | 58 |
| Union Activation | `38527680` | [Scripts/c38527680.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c38527680.lua) | 57 |
| Erebus the Underworld Monarch | `23064604` | [Scripts/c23064604.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c23064604.lua) | 56 |
| Galaxy-Eyes Photon Dragon | `93717133` | [Scripts/c93717133.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93717133.lua) | 56 |
| Drytron Meteonis DA Draconids | `56863746` | [Scripts/c56863746.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c56863746.lua) | 53 |
| Galaxy-Eyes Photon Change Dragon | `54725177` | [Scripts/c54725177.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c54725177.lua) | 53 |
| Borrelcode Dragon | `67288539` | [Scripts/c67288539.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c67288539.lua) | 53 |
| Salamangreat Raging Phoenix | `57134592` | [Scripts/c57134592.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c57134592.lua) | 53 |
| Phara, the Goddess of the Beginning | `82344137` | [Scripts/c82344137.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c82344137.lua) | 52 |
| Altergeist Memorygant | `23790299` | [Scripts/c23790299.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c23790299.lua) | 52 |
| Super Armored Robot Armed Black Iron "C" | `77754169` | [Scripts/c77754169.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c77754169.lua) | 52 |
| Heart of the Blue-Eyes | `54475145` | [Scripts/c54475145.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c54475145.lua) | 51 |
| Tragic Twin Twined Jewels | `81143465` | [Scripts/c81143465.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c81143465.lua) | 51 |
| Servant of Endymion | `92559258` | [Scripts/c92559258.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92559258.lua) | 50 |
| TiSolfachord Beautia | `54387923` | [Scripts/c54387923.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c54387923.lua) | 50 |
| Drytron Meteonis Draconids | `69815951` | [Scripts/c69815951.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c69815951.lua) | 50 |
| Drytron Meteonis Quadrantids | `95209656` | [Scripts/c95209656.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c95209656.lua) | 49 |
| Eidos the Underworld Monarch | `31596518` | [Scripts/c31596518.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c31596518.lua) | 49 |
| Rasterliger | `88000953` | [Scripts/c88000953.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c88000953.lua) | 49 |
| ...and 113 more |  |  |  |

## Script Examples

### Favorite HERO Flame Wingman (`13243124`)

Source: [Scripts/c13243124.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c13243124.lua)

```lua
	local c=e:GetHandler()
	local bc=c:GetBattleTarget()
	return bc and bc:IsFaceup() and bc:IsAttackAbove(2200)
end
function s.atktg(e,tp,eg,ep,ev,re,r,rp,chk)
```

### Ehther the Heavenly Monarch (`96570609`)

Source: [Scripts/c96570609.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c96570609.lua)

```lua
end
function c96570609.spfilter(c,e,tp)
	return c:IsAttackAbove(2400) and c:IsDefense(1000) and c:IsCanBeSpecialSummoned(e,0,tp,false,false)
end
function c96570609.sptg(e,tp,eg,ep,ev,re,r,rp,chk)
```

### Dark End Evaporation Dragon (`62002838`)

Source: [Scripts/c62002838.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c62002838.lua)

```lua
	local c=e:GetHandler()
	if chkc then return chkc:IsLocation(LOCATION_MZONE) and chkc~=c and s.atkfilter(chkc) end
	if chk==0 then return c:IsAttackAbove(500) and c:IsDefenseAbove(500) and Duel.IsExistingTarget(s.atkfilter,tp,LOCATION_MZONE,LOCATION_MZONE,1,c) end
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_FACEUP)
	local tc=Duel.SelectTarget(tp,s.atkfilter,tp,LOCATION_MZONE,LOCATION_MZONE,1,1,c)
```
