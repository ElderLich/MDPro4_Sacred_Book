# Card.GetBaseDefense

## Signature

```lua
Card.GetBaseDefense(Card c) -> int
```

## Description

Returns c's current base DEF. Unknown or negative base DEF values are clamped to 0 by this binding.

## Parameters

- `c` `Card`

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3447`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **76** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.GetBaseDefense`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Gunkan Sushipyard Seaside Supper Spot | `62200831` | [Scripts/c62200831.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c62200831.lua) | 1 |
| Megaroid City | `44139064` | [Scripts/c44139064.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44139064.lua) | 1 |
| Sudden Thunder Swamp | `23611122` | [Scripts/c23611122.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c23611122.lua) | 1 |
| Lunalight Perfume Dancer | `81196066` | [Scripts/c81196066.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c81196066.lua) | 1 |
| Argostars - Giantslaying | `30964246` | [Scripts/c30964246.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30964246.lua) | 1 |
| Brilliant Fusion | `7394770` | [Scripts/c7394770.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c7394770.lua) | 1 |
| Cherubini, Ebon Angel of the Burning Abyss | `58699500` | [Scripts/c58699500.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c58699500.lua) | 1 |
| Update Jammer | `88093706` | [Scripts/c88093706.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c88093706.lua) | 2 |
| Silhouhatte Rabbit | `1528054` | [Scripts/c1528054.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c1528054.lua) | 1 |
| Crystal Aegis | `58371671` | [Scripts/c58371671.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c58371671.lua) | 3 |
| Subterror Final Battle | `74640994` | [Scripts/c74640994.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74640994.lua) | 1 |
| Antidote Nurse | `31539614` | [Scripts/c31539614.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c31539614.lua) | 2 |
| Trivikarma | `7436169` | [Scripts/c7436169.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c7436169.lua) | 3 |
| Despian Proskenion | `18666161` | [Scripts/c18666161.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c18666161.lua) | 2 |
| Apparition | `91392974` | [Scripts/c91392974.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c91392974.lua) | 1 |
| Gunkan Suship Shirauo-class Carrier | `21293424` | [Scripts/c21293424.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c21293424.lua) | 1 |
| Mermail Abyssnerei | `71133680` | [Scripts/c71133680.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71133680.lua) | 2 |
| That's 10! | `97223101` | [Scripts/c97223101.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c97223101.lua) | 1 |
| Heavy Freight Train Derricrane | `13647631` | [Scripts/c13647631.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c13647631.lua) | 1 |
| Pig Iron vs. Pen Peg | `46497537` | [Scripts/c46497537.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c46497537.lua) | 2 |
| Regenesis Dragon | `59323650` | [Scripts/c59323650.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59323650.lua) | 1 |
| Superheavy Samurai Soulbuster Gauntlet | `35800511` | [Scripts/c35800511.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c35800511.lua) | 1 |
| Mimighoul Dungeon | `86809440` | [Scripts/c86809440.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c86809440.lua) | 1 |
| Parallel eXceed | `71278040` | [Scripts/c71278040.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71278040.lua) | 1 |
| ...and 52 more |  |  |  |

## Script Examples

### Gunkan Sushipyard Seaside Supper Spot (`62200831`)

Source: [Scripts/c62200831.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c62200831.lua)

```lua
	if chk==0 then return true end
	local tg=eg:Filter(c62200831.cfilter2,nil,tp)
	local def=tg:GetSum(Card.GetBaseDefense)
	e:SetLabel(def)
end
```

### Megaroid City (`44139064`)

Source: [Scripts/c44139064.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44139064.lua)

```lua
	if tc:IsRelateToBattle() and tc:IsControler(tp) then
		local batk=tc:GetBaseAttack()
		local bdef=tc:GetBaseDefense()
		local e1=Effect.CreateEffect(c)
		e1:SetType(EFFECT_TYPE_SINGLE)
```

### Sudden Thunder Swamp (`23611122`)

Source: [Scripts/c23611122.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c23611122.lua)

```lua
		or bit.band(c:GetOriginalAttribute(),0x7f)~=0
		or c:GetBaseAttack()>0
		or c:GetBaseDefense()>0)
end
function s.activate(e,tp,eg,ep,ev,re,r,rp)
```
