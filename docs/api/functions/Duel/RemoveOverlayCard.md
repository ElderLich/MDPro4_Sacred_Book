# Duel.RemoveOverlayCard

## Signature

```lua
Duel.RemoveOverlayCard(int player, int s, int o, int min, int max, int reason) -> int
```

## Description

Lets player remove between min and max Xyz Materials from the specified own/opponent field locations for reason.
s marks locations on player's own field and o marks locations on the opponent's field, from player's perspective. The return value is the number of materials removed.

## Parameters

- `player` `int`
- `s` `int`
- `o` `int`
- `min` `int`
- `max` `int`
- `reason` `int`

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5018`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **39** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Duel.RemoveOverlayCard`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Goblin's Crazy Beast | `71100270` | [Scripts/c71100270.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71100270.lua) | 1 |
| LeVirtue Dragon | `33113958` | [Scripts/c33113958.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c33113958.lua) | 1 |
| Valiant Shark Lancer | `23672629` | [Scripts/c23672629.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c23672629.lua) | 1 |
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
| Goblin Biker Grand Stampede | `50311058` | [Scripts/c50311058.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c50311058.lua) | 1 |
| Daruma Dropper | `35394356` | [Scripts/c35394356.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c35394356.lua) | 1 |
| Xyz Remora | `43138260` | [Scripts/c43138260.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c43138260.lua) | 1 |
| ...and 15 more |  |  |  |

## Script Examples

### Goblin's Crazy Beast (`71100270`)

Source: [Scripts/c71100270.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71100270.lua)

```lua
	local c=e:GetHandler()
	local tc=Duel.GetFirstTarget()
	if Duel.RemoveOverlayCard(tp,1,1,2,2,REASON_EFFECT)~=0
		and c:IsRelateToEffect(e) and tc:IsRelateToEffect(e) and not tc:IsImmuneToEffect(e) then
		local og=tc:GetOverlayGroup()
```

### LeVirtue Dragon (`33113958`)

Source: [Scripts/c33113958.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c33113958.lua)

```lua
end
function s.thop2(e,tp,eg,ep,ev,re,r,rp)
	if not Duel.CheckRemoveOverlayCard(tp,1,0,1,REASON_EFFECT) or Duel.RemoveOverlayCard(tp,1,0,1,1,REASON_EFFECT)==0 then return end
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_ATOHAND)
	local g=Duel.SelectMatchingCard(tp,aux.NecroValleyFilter(s.thfilter2),tp,LOCATION_GRAVE,0,1,1,nil)
```

### Valiant Shark Lancer (`23672629`)

Source: [Scripts/c23672629.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c23672629.lua)

```lua
function c23672629.desop(e,tp,eg,ep,ev,re,r,rp)
	local tc=Duel.GetFirstTarget()
	if Duel.RemoveOverlayCard(tp,1,0,1,1,REASON_EFFECT)>0 and tc:IsRelateToEffect(e) then
		Duel.Destroy(tc,REASON_EFFECT)
	end
```
