# Duel.GetMatchingGroupCount

## Signature

```lua
Duel.GetMatchingGroupCount([function|nil f], int player, int s, int o, [Card|Group|nil ex], ... any) -> int
```

## Description

Counts cards in the specified locations that satisfy filter f and are not excluded by ex.
Extra arguments after ex are passed to f after the card argument.

## Parameters

- `f` `function|nil` optional
- `player` `int`
- `s` `int`
- `o` `int`
- `ex` `Card|Group|nil` optional
- `...` `any`

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4970`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **589** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Duel.GetMatchingGroupCount`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [D/D/D Alfred the Divine Sage King](/examples/cards/11852093) | `11852093` | [Scripts/c11852093.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c11852093.lua) | 68 |
| [Shooting Majestic Star Dragon](/examples/cards/40939228) | `40939228` | [Scripts/c40939228.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c40939228.lua) | 62 |
| D/D Extra Surveyor | `74387963` | [Scripts/c74387963.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74387963.lua) | 60 |
| Clock Lizard | `51476410` | [Scripts/c51476410.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c51476410.lua) | 58 |
| Phantom Knights' Rank-Up-Magic Force | `88504133` | [Scripts/c88504133.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c88504133.lua) | 57 |
| Endymion, the Mighty Master of Magic | `3611830` | [Scripts/c3611830.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c3611830.lua) | 56 |
| Ursarctic Quint Charge | `15758127` | [Scripts/c15758127.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c15758127.lua) | 56 |
| Kewl Tune Crackle | `39576656` | [Scripts/c39576656.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c39576656.lua) | 56 |
| Theia, the Primal Being | `85687952` | [Scripts/c85687952.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c85687952.lua) | 56 |
| R.B. Shepherd's Crook | `80071619` | [Scripts/c80071619.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c80071619.lua) | 55 |
| Heroic Champion - Magnum Excalibur | `14301396` | [Scripts/c14301396.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c14301396.lua) | 55 |
| Nemleria Louve | `57296396` | [Scripts/c57296396.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c57296396.lua) | 55 |
| Abyss Actor - Mellow Madonna | `78310590` | [Scripts/c78310590.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c78310590.lua) | 54 |
| Traptrix Atypus | `48183890` | [Scripts/c48183890.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c48183890.lua) | 54 |
| Dragunity Arma Gram | `53184342` | [Scripts/c53184342.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c53184342.lua) | 54 |
| Worldsea Dragon Zealantis | `45112597` | [Scripts/c45112597.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c45112597.lua) | 53 |
| Red Hypernova Dragon | `30698243` | [Scripts/c30698243.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30698243.lua) | 53 |
| Fairy Tail - Wiccat | `27632520` | [Scripts/c27632520.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c27632520.lua) | 52 |
| Predaplant Dheadevil | `82370493` | [Scripts/c82370493.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c82370493.lua) | 52 |
| X-Saber Gottoms | `8252010` | [Scripts/c8252010.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c8252010.lua) | 52 |
| Condemned Darklord | `35306215` | [Scripts/c35306215.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c35306215.lua) | 52 |
| Shade the Obscure | `77157846` | [Scripts/c77157846.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c77157846.lua) | 51 |
| Black Luster Soldier - Envoy of the Evening Twilight | `77498348` | [Scripts/c77498348.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c77498348.lua) | 51 |
| X-Krawler Qualiark | `92781606` | [Scripts/c92781606.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92781606.lua) | 51 |
| ...and 565 more |  |  |  |

## Script Examples

### D/D/D Alfred the Divine Sage King (`11852093`)

Source: [Scripts/c11852093.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c11852093.lua)

```lua
	if chkc then return chkc:IsLocation(LOCATION_GRAVE+LOCATION_REMOVED) and chkc:IsControler(tp) and s.tffilter(chkc,tp) end
	local count1=Duel.GetTargetCount(s.tffilter,tp,LOCATION_GRAVE+LOCATION_REMOVED,0,nil,tp)
	local count2=Duel.GetMatchingGroupCount(s.mfilter,tp,LOCATION_MZONE,0,nil)
	if chk==0 then return Duel.GetLocationCount(tp,LOCATION_SZONE)>0 and count1>0 and count2>0 end
	local ct=math.min((Duel.GetLocationCount(tp,LOCATION_SZONE)),count1,count2)
```

### Shooting Majestic Star Dragon (`40939228`)

Source: [Scripts/c40939228.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c40939228.lua)

```lua
end
function c40939228.atkval(e,c)
	return Duel.GetMatchingGroupCount(c40939228.atkfilter,e:GetHandlerPlayer(),LOCATION_GRAVE,0,nil)
end
function c40939228.negcon(e,tp,eg,ep,ev,re,r,rp)
```

### D/D Extra Surveyor (`74387963`)

Source: [Scripts/c74387963.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74387963.lua)

```lua
end
function s.rmtg(e,tp,eg,ep,ev,re,r,rp,chk)
	local ct=Duel.GetMatchingGroupCount(aux.AND(Card.IsFaceup,Card.IsType),tp,0,LOCATION_EXTRA,nil,TYPE_PENDULUM)
	local tg=Duel.GetDecktopGroup(1-tp,ct)
	if chk==0 then return ct>0
```
