# Duel.Recover

## Signature

```lua
Duel.Recover(int player, int value, int reason, [bool is_step]) -> int
```

## Description

Gives player LP for reason and returns the amount processed.
Effects can reverse recovery into damage. With is_step=true, finish the damage/recovery batch with Duel.RDComplete.

## Parameters

- `player` `int`
- `value` `int`
- `reason` `int`
- `is_step` `bool` optional - default: false

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4902`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **267** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Duel.Recover`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Earthbound Servant Geo Gremlin](/examples/cards/8690387) | `8690387` | [Scripts/c8690387.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c8690387.lua) | 61 |
| Awakening of the Sacred Beasts | `53701259` | [Scripts/c53701259.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c53701259.lua) | 57 |
| GMX - VELOX | `82706696` | [Scripts/c82706696.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c82706696.lua) | 56 |
| Darklord Uprising | `54527349` | [Scripts/c54527349.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c54527349.lua) | 54 |
| D/D/D Vice King Requiem | `25857977` | [Scripts/c25857977.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c25857977.lua) | 53 |
| Supreme King Gate Infinity | `22211622` | [Scripts/c22211622.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c22211622.lua) | 53 |
| Salamangreat Sanctuary | `1295111` | [Scripts/c1295111.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c1295111.lua) | 53 |
| Condemned Darklord | `35306215` | [Scripts/c35306215.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c35306215.lua) | 52 |
| Performapal Corn | `33103459` | [Scripts/c33103459.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c33103459.lua) | 51 |
| Raidraptor - Last Strix | `97219708` | [Scripts/c97219708.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c97219708.lua) | 50 |
| Crossmind Archfiend | `52644170` | [Scripts/c52644170.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c52644170.lua) | 50 |
| Yum☆Yum☆Yummys | `56870908` | [Scripts/c56870908.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c56870908.lua) | 49 |
| Don Thousand's Throne | `93238626` | [Scripts/c93238626.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93238626.lua) | 49 |
| The Chaotic Sacred Beasts | `7894706` | [Scripts/c7894706.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c7894706.lua) | 49 |
| Vesper Girsu | `97345699` | [Scripts/c97345699.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c97345699.lua) | 49 |
| Exosister Irene | `79858629` | [Scripts/c79858629.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c79858629.lua) | 49 |
| Aromalilith Rosemary | `30989084` | [Scripts/c30989084.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30989084.lua) | 49 |
| The Sacred Waters in the Sky | `26684111` | [Scripts/c26684111.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c26684111.lua) | 48 |
| Ancient Fairy Dragon | `25862681` | [Scripts/c25862681.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c25862681.lua) | 48 |
| Sun God Unification | `77432167` | [Scripts/c77432167.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c77432167.lua) | 48 |
| Ebon Sun | `96029570` | [Scripts/c96029570.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c96029570.lua) | 48 |
| R.B. Operation Test | `16066654` | [Scripts/c16066654.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c16066654.lua) | 48 |
| Performapal Odd-Eyes Butler | `56677752` | [Scripts/c56677752.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c56677752.lua) | 47 |
| Gizmek Yata, the Gleaming Vanguard | `13224603` | [Scripts/c13224603.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c13224603.lua) | 47 |
| ...and 243 more |  |  |  |

## Script Examples

### Earthbound Servant Geo Gremlin (`8690387`)

Source: [Scripts/c8690387.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c8690387.lua)

```lua
		Duel.Destroy(tc,REASON_EFFECT)
	else
		Duel.Recover(tp,tc:GetAttack(),REASON_EFFECT)
	end
end
```

### Awakening of the Sacred Beasts (`53701259`)

Source: [Scripts/c53701259.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c53701259.lua)

```lua
	local lg=eg:Filter(c53701259.cfilter,nil,1-tp)
	local rnum=lg:GetSum(Card.GetAttack)
	Duel.Recover(tp,rnum,REASON_EFFECT)
end
function c53701259.regcon(e,tp,eg,ep,ev,re,r,rp)
```

### GMX - VELOX (`82706696`)

Source: [Scripts/c82706696.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c82706696.lua)

```lua
function s.recop(e,tp,eg,ep,ev,re,r,rp)
	Duel.Hint(HINT_CARD,0,id)
	Duel.Recover(tp,200,REASON_EFFECT)
end
function s.descon(e,tp,eg,ep,ev,re,r,rp)
```
