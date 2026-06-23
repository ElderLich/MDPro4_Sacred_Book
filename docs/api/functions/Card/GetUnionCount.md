# Card.GetUnionCount

## Signature

```lua
Card.GetUnionCount(Card c) -> int,int
```

## Description

Returns two values for c: the number of modern Union cards equipped to it, then the number of old Union cards equipped to it.
The local core counts equipped cards with TYPE_UNION plus EFFECT_UNION_STATUS or EFFECT_OLDUNION_STATUS.

## Parameters

- `c` `Card` - Monster whose equipped Union cards should be counted.

## Returns

- `int` - Number of equipped modern Union cards.
- `int` - Number of equipped old Union cards.

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3523`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **19** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.GetUnionCount`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Buster Blaster | `63676256` | [Scripts/c63676256.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63676256.lua) | 40 |
| Burning Beast | `59364406` | [Scripts/c59364406.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59364406.lua) | 39 |
| Kiryu | `84814897` | [Scripts/c84814897.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c84814897.lua) | 38 |
| Zombie Tiger | `47693640` | [Scripts/c47693640.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c47693640.lua) | 38 |
| Spirit of the Six Samurai | `65685470` | [Scripts/c65685470.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c65685470.lua) | 38 |
| Armor Breaker | `87798440` | [Scripts/c87798440.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c87798440.lua) | 38 |
| Oilman | `31768112` | [Scripts/c31768112.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c31768112.lua) | 38 |
| Des Dendle | `12965761` | [Scripts/c12965761.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c12965761.lua) | 37 |
| Freezing Beast | `85359414` | [Scripts/c85359414.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c85359414.lua) | 37 |
| Trigon | `48568432` | [Scripts/c48568432.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c48568432.lua) | 37 |
| Second Goblin | `19086954` | [Scripts/c19086954.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c19086954.lua) | 37 |
| Vylon Pentachloro | `47228077` | [Scripts/c47228077.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c47228077.lua) | 37 |
| Protective Soul Ailin | `11678191` | [Scripts/c11678191.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c11678191.lua) | 37 |
| Vylon Tesseract | `84313685` | [Scripts/c84313685.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c84313685.lua) | 36 |
| Pitch-Dark Dragon | `47415292` | [Scripts/c47415292.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c47415292.lua) | 35 |
| Metallizing Parasite - Lunatite | `7369217` | [Scripts/c7369217.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c7369217.lua) | 35 |
| Metallizing Parasite - Soltite | `87564935` | [Scripts/c87564935.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c87564935.lua) | 35 |
| Koitsu | `69456283` | [Scripts/c69456283.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c69456283.lua) | 33 |
| Doitsu | `57062206` | [Scripts/c57062206.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c57062206.lua) | 33 |

## Script Examples

### Buster Blaster (`63676256`)

Source: [Scripts/c63676256.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63676256.lua)

```lua
c63676256.old_union=true
function c63676256.filter(c)
	return c:IsFaceup() and c:GetUnionCount()==0
end
function c63676256.eqtg(e,tp,eg,ep,ev,re,r,rp,chk,chkc)
```

### Burning Beast (`59364406`)

Source: [Scripts/c59364406.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59364406.lua)

```lua
end
function c59364406.filter(c)
	return c:IsFaceup() and c:IsCode(85359414) and c:GetUnionCount()==0
end
function c59364406.eqtg(e,tp,eg,ep,ev,re,r,rp,chk,chkc)
```

### Kiryu (`84814897`)

Source: [Scripts/c84814897.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c84814897.lua)

```lua
end
function c84814897.filter(c)
	return c:IsFaceup() and c:IsCode(11321183) and c:GetUnionCount()==0
end
function c84814897.eqtg(e,tp,eg,ep,ev,re,r,rp,chk,chkc)
```
