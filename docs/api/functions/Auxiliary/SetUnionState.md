# Auxiliary.SetUnionState

## Signature

```lua
Auxiliary.SetUnionState(Card c) -> void
```

## Description

Add Union Monster attributes to c

## Parameters

- `c` `Card`

## Source

- `Utilities/utility.lua:312`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **27** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Auxiliary.SetUnionState`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Union Hangar | `66399653` | [Scripts/c66399653.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c66399653.lua) | 48 |
| Buster Blaster | `63676256` | [Scripts/c63676256.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63676256.lua) | 40 |
| Burning Beast | `59364406` | [Scripts/c59364406.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59364406.lua) | 39 |
| Delta Tri | `12079734` | [Scripts/c12079734.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c12079734.lua) | 39 |
| Kiryu | `84814897` | [Scripts/c84814897.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c84814897.lua) | 38 |
| Zombie Tiger | `47693640` | [Scripts/c47693640.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c47693640.lua) | 38 |
| Spirit of the Six Samurai | `65685470` | [Scripts/c65685470.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c65685470.lua) | 38 |
| Armor Breaker | `87798440` | [Scripts/c87798440.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c87798440.lua) | 38 |
| Oilman | `31768112` | [Scripts/c31768112.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c31768112.lua) | 38 |
| Des Dendle | `12965761` | [Scripts/c12965761.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c12965761.lua) | 37 |
| Freezing Beast | `85359414` | [Scripts/c85359414.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c85359414.lua) | 37 |
| Trigon | `48568432` | [Scripts/c48568432.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c48568432.lua) | 37 |
| Second Goblin | `19086954` | [Scripts/c19086954.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c19086954.lua) | 37 |
| Union Driver | `99249638` | [Scripts/c99249638.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c99249638.lua) | 37 |
| Vylon Pentachloro | `47228077` | [Scripts/c47228077.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c47228077.lua) | 37 |
| Protective Soul Ailin | `11678191` | [Scripts/c11678191.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c11678191.lua) | 37 |
| Vylon Tesseract | `84313685` | [Scripts/c84313685.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c84313685.lua) | 36 |
| X-Cross Cannon | `70860415` | [Scripts/c70860415.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c70860415.lua) | 36 |
| Pitch-Dark Dragon | `47415292` | [Scripts/c47415292.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c47415292.lua) | 35 |
| Metallizing Parasite - Lunatite | `7369217` | [Scripts/c7369217.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c7369217.lua) | 35 |
| Metallizing Parasite - Soltite | `87564935` | [Scripts/c87564935.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c87564935.lua) | 35 |
| Union Pilot | `89357740` | [Scripts/c89357740.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c89357740.lua) | 34 |
| Formation Union | `26931058` | [Scripts/c26931058.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c26931058.lua) | 34 |
| Koitsu | `69456283` | [Scripts/c69456283.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c69456283.lua) | 33 |
| ...and 3 more |  |  |  |

## Script Examples

### Union Hangar (`66399653`)

Source: [Scripts/c66399653.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c66399653.lua)

```lua
		local ec=sg:GetFirst()
		if ec and Duel.Equip(tp,ec,tc) then
			aux.SetUnionState(ec)
			local e1=Effect.CreateEffect(e:GetHandler())
			e1:SetType(EFFECT_TYPE_SINGLE)
```

### Buster Blaster (`63676256`)

Source: [Scripts/c63676256.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63676256.lua)

```lua
	end
	if not Duel.Equip(tp,c,tc,false) then return end
	aux.SetUnionState(c)
end
function c63676256.sptg(e,tp,eg,ep,ev,re,r,rp,chk)
```

### Burning Beast (`59364406`)

Source: [Scripts/c59364406.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59364406.lua)

```lua
	end
	if not Duel.Equip(tp,c,tc,false) then return end
	aux.SetUnionState(c)
end
function c59364406.sptg(e,tp,eg,ep,ev,re,r,rp,chk)
```
