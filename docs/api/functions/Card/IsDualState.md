# Card.IsDualState

## Signature

```lua
Card.IsDualState(Card c) -> bool
```

## Description

Checks whether c is currently affected by EFFECT_DUAL_STATUS.

## Parameters

- `c` `Card`

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3565`

## Guided Examples

Learn how to use this function in context:

- [Gemini Monsters](/learn/gemini-monsters)

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **9** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Card.IsDualState) with `Card.IsDualState`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Dimer Synthesis | `90965652` | [Scripts/c90965652.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c90965652.lua) | 1 |
| Catalyst Field | `65959844` | [Scripts/c65959844.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c65959844.lua) | 1 |
| Gemini Booster | `18096222` | [Scripts/c18096222.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c18096222.lua) | 1 |
| Unleash Your Power! | `73567374` | [Scripts/c73567374.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c73567374.lua) | 2 |
| Skelesaurus | `89362180` | [Scripts/c89362180.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c89362180.lua) | 1 |
| Super Double Summon | `26120084` | [Scripts/c26120084.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c26120084.lua) | 1 |
| Gemini Trap Hole | `67045174` | [Scripts/c67045174.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c67045174.lua) | 2 |
| Heavy Knight of the Flame | `34761062` | [Scripts/c34761062.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c34761062.lua) | 1 |
| Energy Bravery | `72631243` | [Scripts/c72631243.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c72631243.lua) | 1 |

## Script Examples

### Dimer Synthesis (`90965652`)

Source: [Scripts/c90965652.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c90965652.lua)

```lua
end
function c90965652.tgcheck(g)
	return g:IsExists(Card.IsDualState,1,nil) and g:IsExists(c90965652.atkfilter,1,nil)
end
function c90965652.atktg(e,tp,eg,ep,ev,re,r,rp,chk,chkc)
```

### Catalyst Field (`65959844`)

Source: [Scripts/c65959844.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c65959844.lua)

```lua
end
function c65959844.rmfilter(c)
	return c:IsDualState() and c:IsAbleToRemove()
end
function c65959844.destg(e,tp,eg,ep,ev,re,r,rp,chk,chkc)
```

### Gemini Booster (`18096222`)

Source: [Scripts/c18096222.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c18096222.lua)

```lua
end
function c18096222.dafilter(c)
	return c:IsFaceup() and c:IsType(TYPE_DUAL) and not c:IsDualState()
end
function c18096222.datg(e,tp,eg,ep,ev,re,r,rp,chk,chkc)
```
