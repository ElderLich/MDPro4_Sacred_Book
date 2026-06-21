# Card.ReplaceEffect

## Signature

```lua
Card.ReplaceEffect(Card c, int code, int reset_flag, [int reset_count]) -> int
```

## Description

Replace the effect of c with the effect of the card whose card number is code, and add additional reset conditions
The return value is the code id representing the replacement effect

## Parameters

- `c` `Card`
- `code` `int`
- `reset_flag` `int`
- `reset_count` `int` optional - default: 1

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3567`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **2** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.ReplaceEffect`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Arcana Call | `99189322` | [Scripts/c99189322.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c99189322.lua) | 34 |
| Red Supremacy | `50584941` | [Scripts/c50584941.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c50584941.lua) | 33 |

## Script Examples

### Arcana Call (`99189322`)

Source: [Scripts/c99189322.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c99189322.lua)

```lua
	if Duel.Remove(regc,POS_FACEUP,REASON_EFFECT)==0 or not regc:IsLocation(LOCATION_REMOVED) then return end
	if tc:IsRelateToEffect(e) and tc:IsFaceup() and tc:GetFlagEffect(FLAG_ID_REVERSAL_OF_FATE)~=0 and tc:GetFlagEffect(FLAG_ID_ARCANA_COIN)~=0 then
		local cid=tc:ReplaceEffect(regc:GetOriginalCode(),RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END)
		tc:RegisterFlagEffect(99189322,RESET_EVENT+RESETS_STANDARD+RESET_DISABLE+RESET_PHASE+PHASE_END,0,1)
		local e1=Effect.CreateEffect(e:GetHandler())
```

### Red Supremacy (`50584941`)

Source: [Scripts/c50584941.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c50584941.lua)

```lua
		e1:SetReset(RESET_EVENT+RESETS_STANDARD)
		tc:RegisterEffect(e1)
		tc:ReplaceEffect(code,RESET_EVENT+RESETS_STANDARD)
	end
end
```
