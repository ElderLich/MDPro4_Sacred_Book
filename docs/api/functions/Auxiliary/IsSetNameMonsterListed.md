# Auxiliary.IsSetNameMonsterListed

## Signature

```lua
Auxiliary.IsSetNameMonsterListed(Card c, int setcode) -> bool
```

## Description

Returns true if setcode matches one of the monster set codes registered for c, using the same set-code comparison rules as set membership helpers.

## Parameters

- `c` `Card`
- `setcode` `int`

## Returns

- `bool` - true if c lists a matching monster set code.

## Source

- `Utilities/utility.lua:567`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **5** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Auxiliary.IsSetNameMonsterListed`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Blue-Eyes Toon Ultimate Dragon | `71808988` | [Scripts/c71808988.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71808988.lua) | 1 |
| Break the Destiny | `4008212` | [Scripts/c4008212.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c4008212.lua) | 1 |
| Toon World the Perfect World | `7293697` | [Scripts/c7293697.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c7293697.lua) | 1 |
| Miracle Ejector | `30875635` | [Scripts/c30875635.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30875635.lua) | 1 |
| Elemental HERO Spirit of Neos | `13256226` | [Scripts/c13256226.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c13256226.lua) | 1 |

## Script Examples

### Blue-Eyes Toon Ultimate Dragon (`71808988`)

Source: [Scripts/c71808988.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71808988.lua)

```lua
end
function s.thfilter(c)
	return (c:IsSetCard(0x62) or aux.IsSetNameMonsterListed(c,0x62) or aux.IsCodeListed(c,15259703))
		and c:IsAbleToHand()
end
```

### Break the Destiny (`4008212`)

Source: [Scripts/c4008212.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c4008212.lua)

```lua
function c4008212.thfilter(c)
	return c:IsType(TYPE_SPELL+TYPE_TRAP) and c:IsAbleToHand() and not c:IsCode(4008212)
		and (aux.IsCodeListed(c,76263644) or aux.IsSetNameMonsterListed(c,0xc008))
end
function c4008212.thtg(e,tp,eg,ep,ev,re,r,rp,chk)
```

### Toon World the Perfect World (`7293697`)

Source: [Scripts/c7293697.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c7293697.lua)

```lua
end
function s.thfilter(c)
	return (c:IsSetCard(0x62) or aux.IsSetNameMonsterListed(c,0x62) or aux.IsCodeListed(c,15259703))
		and c:IsAbleToHand()
end
```
