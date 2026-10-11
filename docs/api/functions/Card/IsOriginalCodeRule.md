# Card.IsOriginalCodeRule

## Signature

```lua
Card.IsOriginalCodeRule(Card c, int code1, [int code2], [... int]) -> bool
```

## Description

Checks whether c's rule-original card code matches any supplied code.
Nil code arguments are skipped. For double-code cards, the core checks both rule-original codes; otherwise it checks the card's duel code.

## Parameters

- `c` `Card`
- `code1` `int`
- `code2` `int` optional
- `...` `int` optional

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3531`

## Guided Examples

Learn how to use this function in context:

- [Archetypes and Set Codes](/learn/archetypes-and-setcodes)
- [Card Data And Script Wiring](/learn/card-data-and-script-wiring)
- [Common Script Errors And Debugging](/learn/common-script-errors-and-debugging)

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **56** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Card.IsOriginalCodeRule) with `Card.IsOriginalCodeRule`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| A-to-Z-Dragon Buster Cannon | `65172015` | [Scripts/c65172015.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c65172015.lua) | 2 |
| Union Activation | `38527680` | [Scripts/c38527680.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c38527680.lua) | 1 |
| Dual Avatar - Manifested A-Un | `28798938` | [Scripts/c28798938.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c28798938.lua) | 2 |
| Millennium-Eyes Restrict | `41578483` | [Scripts/c41578483.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c41578483.lua) | 2 |
| Majesty Pegasus, the Dracoslayer | `92332424` | [Scripts/c92332424.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92332424.lua) | 1 |
| Number 69: Heraldry Crest - Shatter Stream | `31086840` | [Scripts/c31086840.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c31086840.lua) | 1 |
| Sun God Unification | `77432167` | [Scripts/c77432167.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c77432167.lua) | 1 |
| Photon Change | `42925441` | [Scripts/c42925441.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c42925441.lua) | 1 |
| Penguin Sword | `69792699` | [Scripts/c69792699.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c69792699.lua) | 2 |
| Forge a New Future | `27104921` | [Scripts/c27104921.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c27104921.lua) | 4 |
| Rokket Recharger | `5969957` | [Scripts/c5969957.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c5969957.lua) | 1 |
| The Kaiju Files | `11163040` | [Scripts/c11163040.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c11163040.lua) | 2 |
| Steel-Stringed Sacrifice | `7166709` | [Scripts/c7166709.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c7166709.lua) | 1 |
| The League of Uniform Nomenclature Strikes | `29265962` | [Scripts/c29265962.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c29265962.lua) | 1 |
| Rank-Up-Magic Admiration of the Thousands | `96142517` | [Scripts/c96142517.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c96142517.lua) | 2 |
| War Rock Meteoragon | `10497636` | [Scripts/c10497636.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c10497636.lua) | 2 |
| Nephthys, the Sacred Preserver | `50669347` | [Scripts/c50669347.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c50669347.lua) | 1 |
| Nightmell the Dark Bonder | `66569334` | [Scripts/c66569334.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c66569334.lua) | 1 |
| Solemn Accusation | `78114463` | [Scripts/c78114463.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c78114463.lua) | 2 |
| Exosister Carpedivem | `30802207` | [Scripts/c30802207.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30802207.lua) | 4 |
| Test Panther | `66863374` | [Scripts/c66863374.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c66863374.lua) | 1 |
| Three in One | `50838440` | [Scripts/c50838440.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c50838440.lua) | 2 |
| Fist of Fate | `79868386` | [Scripts/c79868386.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c79868386.lua) | 3 |
| Harpie Lady Elegance | `65664792` | [Scripts/c65664792.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c65664792.lua) | 3 |
| ...and 32 more |  |  |  |

## Script Examples

### A-to-Z-Dragon Buster Cannon (`65172015`)

Source: [Scripts/c65172015.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c65172015.lua)

```lua
end
function c65172015.matfilter(c,sc)
	return c:IsOriginalCodeRule(1561110,91998119) and c:IsAbleToRemoveAsCost() and c:IsCanBeFusionMaterial(sc,SUMMON_TYPE_SPECIAL)
end
function c65172015.fselect(g,tp,sc)
```

### Union Activation (`38527680`)

Source: [Scripts/c38527680.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c38527680.lua)

```lua
end
function s.thfilter(c,code,atk)
	return not c:IsOriginalCodeRule(code) and c:IsAttribute(ATTRIBUTE_LIGHT) and c:IsRace(RACE_MACHINE) and c:IsAttack(atk) and c:IsAbleToHand()
end
function s.target(e,tp,eg,ep,ev,re,r,rp,chk)
```

### Dual Avatar - Manifested A-Un (`28798938`)

Source: [Scripts/c28798938.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c28798938.lua)

```lua
		c:RegisterFlagEffect(85360035,RESET_EVENT+RESETS_STANDARD,0,1)
	end
	if g:IsExists(Card.IsOriginalCodeRule,1,nil,33026283) then
		--atk down
		local e1=Effect.CreateEffect(c)
```
