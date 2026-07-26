# Duel.Recover

## Signature

```lua
Duel.Recover(int player, int value, int reason, [bool is_step]) -> int
```

## Description

Gives player LP for reason and returns the amount processed.
Effects can reverse recovery into damage; when recovery is reversed, this function returns 0 for recovery. Negative input amounts are clamped to 0 by the local binding.
With is_step=true, finish the damage/recovery batch with Duel.RDComplete.

## How To Use It

Use this during resolution when a player gains LP.

```lua
local gained=Duel.Recover(tp,1000,REASON_EFFECT)
if gained>0 then
    -- follow-up that requires actual recovery
end
```

The return value is the actual recovery applied. If recovery is reversed into damage, the recovery return value is 0. For simultaneous damage/recovery batches, use `is_step=true` and finish with `Duel.RDComplete()`.

## Related Functions

- [Duel.Damage](/api/functions/Duel/Damage)
- [Duel.RDComplete](/api/functions/Duel/RDComplete)
- [Duel.SetOperationInfo](/api/functions/Duel/SetOperationInfo)

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
| [Earthbound Servant Geo Gremlin](/examples/cards/8690387) | `8690387` | [Scripts/c8690387.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c8690387.lua) | 1 |
| Awakening of the Sacred Beasts | `53701259` | [Scripts/c53701259.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c53701259.lua) | 2 |
| GMX - VELOX | `82706696` | [Scripts/c82706696.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c82706696.lua) | 1 |
| Darklord Uprising | `54527349` | [Scripts/c54527349.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c54527349.lua) | 1 |
| D/D/D Vice King Requiem | `25857977` | [Scripts/c25857977.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c25857977.lua) | 1 |
| Supreme King Gate Infinity | `22211622` | [Scripts/c22211622.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c22211622.lua) | 1 |
| Salamangreat Sanctuary | `1295111` | [Scripts/c1295111.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c1295111.lua) | 1 |
| Condemned Darklord | `35306215` | [Scripts/c35306215.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c35306215.lua) | 1 |
| Performapal Corn | `33103459` | [Scripts/c33103459.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c33103459.lua) | 1 |
| Raidraptor - Last Strix | `97219708` | [Scripts/c97219708.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c97219708.lua) | 1 |
| Crossmind Archfiend | `52644170` | [Scripts/c52644170.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c52644170.lua) | 1 |
| Yum☆Yum☆Yummys | `56870908` | [Scripts/c56870908.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c56870908.lua) | 1 |
| Don Thousand's Throne | `93238626` | [Scripts/c93238626.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93238626.lua) | 1 |
| The Chaotic Sacred Beasts | `7894706` | [Scripts/c7894706.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c7894706.lua) | 1 |
| Vesper Girsu | `97345699` | [Scripts/c97345699.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c97345699.lua) | 1 |
| Exosister Irene | `79858629` | [Scripts/c79858629.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c79858629.lua) | 1 |
| Aromalilith Rosemary | `30989084` | [Scripts/c30989084.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30989084.lua) | 1 |
| The Sacred Waters in the Sky | `26684111` | [Scripts/c26684111.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c26684111.lua) | 1 |
| Ancient Fairy Dragon | `25862681` | [Scripts/c25862681.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c25862681.lua) | 1 |
| Sun God Unification | `77432167` | [Scripts/c77432167.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c77432167.lua) | 1 |
| Ebon Sun | `96029570` | [Scripts/c96029570.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c96029570.lua) | 1 |
| R.B. Operation Test | `16066654` | [Scripts/c16066654.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c16066654.lua) | 1 |
| Performapal Odd-Eyes Butler | `56677752` | [Scripts/c56677752.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c56677752.lua) | 1 |
| Gizmek Yata, the Gleaming Vanguard | `13224603` | [Scripts/c13224603.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c13224603.lua) | 1 |
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
