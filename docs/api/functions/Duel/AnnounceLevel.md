# Duel.AnnounceLevel

## Signature

```lua
Duel.AnnounceLevel(int player, [int min], [int max], [int excluded_level1], [... int]) -> int|nil,int|nil
```

## Description

Lets player declare a Level and returns the declared Level plus the zero-based option index.
min and max default to 1 and 12 and are swapped if min is greater than max. Extra level arguments are excluded from the options; if no Levels remain, the binding returns no value.

## Parameters

- `player` `int`
- `min` `int` optional - default: 1
- `max` `int` optional - default: 12
- `excluded_level1` `int` optional
- `...` `int` optional

## Returns

- `int|nil` - Declared Level.
- `int|nil` - Zero-based option index.

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5031`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **24** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Duel.AnnounceLevel) with `Duel.AnnounceLevel`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Brain Controller | `44265115` | [Scripts/c44265115.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c44265115.lua) | 1 |
| Marshalling Field | `63881033` | [Scripts/c63881033.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c63881033.lua) | 1 |
| Sylvan Princessprout | `20579538` | [Scripts/c20579538.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c20579538.lua) | 1 |
| Red Familiar | `8372133` | [Scripts/c8372133.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c8372133.lua) | 1 |
| Wake Up Centur-Ion! | `92907248` | [Scripts/c92907248.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c92907248.lua) | 3 |
| Theorealize Overdrive | `94326720` | [Scripts/c94326720.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c94326720.lua) | 1 |
| Turbo-Tainted Hot Rod GT19 | `16769305` | [Scripts/c16769305.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c16769305.lua) | 1 |
| D/D Lance Soldier | `67322708` | [Scripts/c67322708.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c67322708.lua) | 1 |
| Spore the Fairy Seed | `98888032` | [Scripts/c98888032.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c98888032.lua) | 1 |
| Xyz Align | `60623203` | [Scripts/c60623203.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c60623203.lua) | 1 |
| Assault Blackwing - Kunai the Drizzle | `70456282` | [Scripts/c70456282.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c70456282.lua) | 1 |
| Isolde, Belle of the Underworld | `22657402` | [Scripts/c22657402.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c22657402.lua) | 1 |
| Performapal Lebellman | `3752422` | [Scripts/c3752422.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c3752422.lua) | 1 |
| Magicalibra | `43857222` | [Scripts/c43857222.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c43857222.lua) | 1 |
| Sirenorca | `50074392` | [Scripts/c50074392.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c50074392.lua) | 1 |
| Specimen Inspection | `12292422` | [Scripts/c12292422.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c12292422.lua) | 1 |
| Reasoning | `58577036` | [Scripts/c58577036.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c58577036.lua) | 1 |
| Phonon Pulse Dragon | `67556500` | [Scripts/c67556500.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c67556500.lua) | 1 |
| D/D Berfomet | `19808608` | [Scripts/c19808608.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c19808608.lua) | 1 |
| Speedroid Red-Eyed Dice | `16725505` | [Scripts/c16725505.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c16725505.lua) | 1 |
| BIG Win!? | `84677654` | [Scripts/c84677654.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c84677654.lua) | 1 |
| Falling Current | `26099457` | [Scripts/c26099457.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c26099457.lua) | 1 |
| Extra Gate | `7405310` | [Scripts/c7405310.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c7405310.lua) | 1 |
| Gagaga Magician | `26082117` | [Scripts/c26082117.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c26082117.lua) | 1 |

## Script Examples

### Brain Controller (`44265115`)

Source: [Scripts/c44265115.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c44265115.lua)

```lua
	local lv=g:GetFirst():GetLevel()
	Duel.Hint(HINT_SELECTMSG,tp,aux.Stringid(id,3))
	e:SetLabel(Duel.AnnounceLevel(tp,1,8,lv))
end
function s.lvop(e,tp,eg,ep,ev,re,r,rp)
```

### Marshalling Field (`63881033`)

Source: [Scripts/c63881033.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c63881033.lua)

```lua
	if chk==0 then return Duel.IsExistingMatchingCard(c63881033.filter,tp,LOCATION_MZONE,0,1,nil) end
	Duel.Hint(HINT_SELECTMSG,tp,aux.Stringid(63881033,1))
	local lv=Duel.AnnounceLevel(tp,5,9)
	e:SetLabel(lv)
end
```

### Sylvan Princessprout (`20579538`)

Source: [Scripts/c20579538.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c20579538.lua)

```lua
		and e:GetHandler():IsCanBeSpecialSummoned(e,0,tp,false,false) end
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_LVRANK)
	local lv=Duel.AnnounceLevel(tp,1,8)
	e:SetLabel(lv)
	Duel.SetOperationInfo(0,CATEGORY_SPECIAL_SUMMON,e:GetHandler(),1,0,0)
```
