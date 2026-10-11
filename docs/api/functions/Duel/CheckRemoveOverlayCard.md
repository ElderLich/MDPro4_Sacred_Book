# Duel.CheckRemoveOverlayCard

## Signature

```lua
Duel.CheckRemoveOverlayCard(int player, int s, int o, int count, int reason) -> bool
```

## Description

Checks whether player can remove at least count Xyz Materials from the specified own/opponent field locations for reason.
s marks locations on player's own field and o marks locations on the opponent's field, from player's perspective. Applicable replacement effects can satisfy the check.

## Parameters

- `player` `int`
- `s` `int`
- `o` `int`
- `count` `int`
- `reason` `int`

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5017`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **46** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Duel.CheckRemoveOverlayCard) with `Duel.CheckRemoveOverlayCard`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Goblin's Crazy Beast | `71100270` | [Scripts/c71100270.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71100270.lua) | 1 |
| LeVirtue Dragon | `33113958` | [Scripts/c33113958.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c33113958.lua) | 2 |
| Valiant Shark Lancer | `23672629` | [Scripts/c23672629.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c23672629.lua) | 1 |
| Garbage Golem | `28968609` | [Scripts/c28968609.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c28968609.lua) | 1 |
| Unbreakable Xyz Barrier | `96004535` | [Scripts/c96004535.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c96004535.lua) | 1 |
| Tally-ho! Springans | `9175957` | [Scripts/c9175957.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c9175957.lua) | 1 |
| Mansion of the Dreadful Dolls | `36890111` | [Scripts/c36890111.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c36890111.lua) | 1 |
| Baromet the Sacred Sheep Shrub | `62967433` | [Scripts/c62967433.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c62967433.lua) | 1 |
| Goblin Bikers Gone Bonkers | `46014517` | [Scripts/c46014517.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c46014517.lua) | 2 |
| Xyz Force | `31398842` | [Scripts/c31398842.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c31398842.lua) | 1 |
| Ryzeal Duo Drive | `7511613` | [Scripts/c7511613.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c7511613.lua) | 1 |
| Mikanko Shinbu - Noble Twins | `84550369` | [Scripts/c84550369.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c84550369.lua) | 1 |
| Xyz Poseidon Splash | `16938770` | [Scripts/c16938770.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c16938770.lua) | 1 |
| Spright Sprind | `72329844` | [Scripts/c72329844.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c72329844.lua) | 1 |
| Battlin' Boxer King Dempsey | `46804536` | [Scripts/c46804536.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c46804536.lua) | 1 |
| Springans Captain Sargas | `29601381` | [Scripts/c29601381.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c29601381.lua) | 1 |
| Migratory Zereort | `87640391` | [Scripts/c87640391.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c87640391.lua) | 1 |
| Time Thief Bezel Ship | `82496097` | [Scripts/c82496097.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c82496097.lua) | 1 |
| Constellar Castor | `33302589` | [Scripts/c33302589.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c33302589.lua) | 1 |
| Xyz Lay | `43150717` | [Scripts/c43150717.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c43150717.lua) | 1 |
| Goblin Biker Clatter Sploder | `51473858` | [Scripts/c51473858.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c51473858.lua) | 1 |
| Goblin Biker Troika Griare | `44241999` | [Scripts/c44241999.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44241999.lua) | 2 |
| Goblin Biker Grand Stampede | `50311058` | [Scripts/c50311058.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c50311058.lua) | 2 |
| Daruma Dropper | `35394356` | [Scripts/c35394356.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c35394356.lua) | 1 |
| ...and 22 more |  |  |  |

## Script Examples

### Goblin's Crazy Beast (`71100270`)

Source: [Scripts/c71100270.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71100270.lua)

```lua
function c71100270.xmtg(e,tp,eg,ep,ev,re,r,rp,chk,chkc)
	if chkc then return chkc:IsLocation(LOCATION_ONFIELD) and c71100270.filter(chkc) end
	if chk==0 then return Duel.CheckRemoveOverlayCard(tp,1,1,2,REASON_EFFECT)
		and Duel.IsExistingTarget(c71100270.filter,tp,LOCATION_ONFIELD,LOCATION_ONFIELD,1,nil) end
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_XMATERIAL)
```

### LeVirtue Dragon (`33113958`)

Source: [Scripts/c33113958.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c33113958.lua)

```lua
end
function s.thtg2(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.CheckRemoveOverlayCard(tp,1,0,1,REASON_EFFECT) and Duel.IsExistingMatchingCard(s.thfilter2,tp,LOCATION_GRAVE,0,1,nil) end
	Duel.SetOperationInfo(0,CATEGORY_TOHAND,nil,1,tp,LOCATION_GRAVE)
end
```

### Valiant Shark Lancer (`23672629`)

Source: [Scripts/c23672629.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c23672629.lua)

```lua
	if chkc then return chkc:IsLocation(LOCATION_MZONE) and chkc:IsControler(1-tp) end
	if chk==0 then return Duel.IsExistingTarget(aux.TRUE,tp,0,LOCATION_MZONE,1,nil)
		and Duel.CheckRemoveOverlayCard(tp,1,0,1,REASON_EFFECT) end
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_DESTROY)
	local g=Duel.SelectTarget(tp,aux.TRUE,tp,0,LOCATION_MZONE,1,1,nil)
```
