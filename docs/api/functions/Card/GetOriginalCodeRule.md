# Card.GetOriginalCodeRule

## Signature

```lua
Card.GetOriginalCodeRule(Card c) -> int,int|nil
```

## Description

Returns c's rule-original card code.
Double-code cards return two codes: the printed original code and the second rule code. Other cards return only the duel code used by the core.

## Parameters

- `c` `Card`

## Returns

- `int` - Primary rule-original code.
- `int|nil` - Second rule code, when present.

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3438`

## Guided Examples

Learn how to use this function in context:

- [Card Data And Script Wiring](/learn/card-data-and-script-wiring)

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **48** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Card.GetOriginalCodeRule) with `Card.GetOriginalCodeRule`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Starving Venemy Dragon](/examples/cards/93729065) | `93729065` | [Scripts/c93729065.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93729065.lua) | 1 |
| Windwitch - Crystal Bell | `25793414` | [Scripts/c25793414.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c25793414.lua) | 1 |
| Union Activation | `38527680` | [Scripts/c38527680.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c38527680.lua) | 2 |
| Odd-Eyes Venom Dragon | `45014450` | [Scripts/c45014450.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c45014450.lua) | 1 |
| Millennium-Eyes Restrict | `41578483` | [Scripts/c41578483.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c41578483.lua) | 2 |
| Starving Venom Fusion Dragon | `41209827` | [Scripts/c41209827.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c41209827.lua) | 1 |
| Majesty Pegasus, the Dracoslayer | `92332424` | [Scripts/c92332424.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92332424.lua) | 1 |
| Photon Change | `42925441` | [Scripts/c42925441.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c42925441.lua) | 1 |
| Penguin Sword | `69792699` | [Scripts/c69792699.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c69792699.lua) | 2 |
| Donner, Dagger Fur Hire | `8728498` | [Scripts/c8728498.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c8728498.lua) | 2 |
| T.G. Rocket Salamander | `77392987` | [Scripts/c77392987.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c77392987.lua) | 2 |
| Rokket Recharger | `5969957` | [Scripts/c5969957.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c5969957.lua) | 1 |
| The Kaiju Files | `11163040` | [Scripts/c11163040.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c11163040.lua) | 2 |
| Steel-Stringed Sacrifice | `7166709` | [Scripts/c7166709.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c7166709.lua) | 1 |
| War Rock Meteoragon | `10497636` | [Scripts/c10497636.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c10497636.lua) | 2 |
| Nephthys, the Sacred Preserver | `50669347` | [Scripts/c50669347.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c50669347.lua) | 1 |
| Supreme King Dragon Starving Venom | `43387895` | [Scripts/c43387895.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c43387895.lua) | 1 |
| Nightmell the Dark Bonder | `66569334` | [Scripts/c66569334.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c66569334.lua) | 1 |
| Solemn Accusation | `78114463` | [Scripts/c78114463.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c78114463.lua) | 2 |
| Test Panther | `66863374` | [Scripts/c66863374.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c66863374.lua) | 1 |
| Dark Magic Talisman | `71440209` | [Scripts/c71440209.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71440209.lua) | 1 |
| Number 8: Heraldic King Genom-Heritage | `47387961` | [Scripts/c47387961.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c47387961.lua) | 1 |
| Fist of Fate | `79868386` | [Scripts/c79868386.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c79868386.lua) | 2 |
| Harpie Lady Elegance | `65664792` | [Scripts/c65664792.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c65664792.lua) | 3 |
| ...and 24 more |  |  |  |

## Script Examples

### Starving Venemy Dragon (`93729065`)

Source: [Scripts/c93729065.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93729065.lua)

```lua
		e1:SetProperty(EFFECT_FLAG_CANNOT_DISABLE)
		e1:SetCode(EFFECT_CHANGE_CODE)
		e1:SetValue(tc:GetOriginalCodeRule())
		e1:SetReset(RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END)
		c:RegisterEffect(e1)
```

### Windwitch - Crystal Bell (`25793414`)

Source: [Scripts/c25793414.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c25793414.lua)

```lua
	local tc=Duel.GetFirstTarget()
	if tc and c:IsRelateToEffect(e) and c:IsFaceup() and tc:IsRelateToEffect(e) and not tc:IsType(TYPE_TOKEN) then
		local code=tc:GetOriginalCodeRule()
		local cid=0
		local e1=Effect.CreateEffect(c)
```

### Union Activation (`38527680`)

Source: [Scripts/c38527680.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c38527680.lua)

```lua
function s.tgfilter(c,tp)
	return c:IsType(TYPE_NORMAL+TYPE_UNION) and c:IsAttribute(ATTRIBUTE_LIGHT) and c:IsRace(RACE_MACHINE) and c:IsAbleToGrave()
		and Duel.IsExistingMatchingCard(s.thfilter,tp,LOCATION_DECK,0,1,c,c:GetOriginalCodeRule(),c:GetAttack())
end
function s.thfilter(c,code,atk)
```
