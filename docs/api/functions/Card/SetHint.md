# Card.SetHint

## Signature

```lua
Card.SetHint(Card c, int type, int value) -> void
```

## Description

Sends a client card-hint message for c with hint type and value; types at or above CHINT_DESC_ADD are ignored.

## Parameters

- `c` `Card`
- `type` `int`
- `value` `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3655`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **8** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.SetHint`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Nephe Shaddoll Fusion | `60226558` | [Scripts/c60226558.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c60226558.lua) | 55 |
| Tualatin | `27769400` | [Scripts/c27769400.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c27769400.lua) | 37 |
| Maple Maiden | `73104892` | [Scripts/c73104892.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c73104892.lua) | 36 |
| Mirror Resonator | `40159926` | [Scripts/c40159926.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c40159926.lua) | 31 |
| Genomix Fighter | `42155488` | [Scripts/c42155488.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c42155488.lua) | 31 |
| Cloak and Dagger | `8323633` | [Scripts/c8323633.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c8323633.lua) | 29 |
| Prohibition | `43711255` | [Scripts/c43711255.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c43711255.lua) | 25 |
| Final Countdown | `95308449` | [Scripts/c95308449.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c95308449.lua) | 19 |

## Script Examples

### Nephe Shaddoll Fusion (`60226558`)

Source: [Scripts/c60226558.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c60226558.lua)

```lua
		e1:SetReset(RESET_EVENT+RESETS_STANDARD)
		c:RegisterEffect(e1)
		c:SetHint(CHINT_ATTRIBUTE,att)
	end
end
```

### Tualatin (`27769400`)

Source: [Scripts/c27769400.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c27769400.lua)

```lua
	Duel.Destroy(g,REASON_EFFECT)
	if c:IsRelateToEffect(e) then
		c:SetHint(CHINT_ATTRIBUTE,rc)
		local e1=Effect.CreateEffect(c)
		e1:SetType(EFFECT_TYPE_FIELD)
```

### Maple Maiden (`73104892`)

Source: [Scripts/c73104892.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c73104892.lua)

```lua
		e1:SetReset(RESET_EVENT+RESETS_STANDARD+RESET_DISABLE)
		c:RegisterEffect(e1)
		c:SetHint(CHINT_ATTRIBUTE,att)
	end
end
```
