# Card.IsRelateToCard

## Signature

```lua
Card.IsRelateToCard(Card c1, Card c2) -> bool
```

## Description

Checks whether c1 currently has a relation to c2.

## Parameters

- `c1` `Card`
- `c2` `Card`

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3564`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **9** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.IsRelateToCard`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Smile Action | `47870325` | [Scripts/c47870325.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c47870325.lua) | 51 |
| Alien Mother | `24104865` | [Scripts/c24104865.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24104865.lua) | 50 |
| Overmind Archfiend | `24221808` | [Scripts/c24221808.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24221808.lua) | 46 |
| Gladiator Beast Darius | `25924653` | [Scripts/c25924653.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c25924653.lua) | 44 |
| Exodius the Ultimate Forbidden Lord | `13893596` | [Scripts/c13893596.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c13893596.lua) | 42 |
| Portable Battery Pack | `61840587` | [Scripts/c61840587.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c61840587.lua) | 41 |
| Future Visions | `87902575` | [Scripts/c87902575.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c87902575.lua) | 38 |
| Elder Entity Norden | `17412721` | [Scripts/c17412721.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c17412721.lua) | 35 |
| Kinka-byo | `45452224` | [Scripts/c45452224.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c45452224.lua) | 34 |

## Script Examples

### Smile Action (`47870325`)

Source: [Scripts/c47870325.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c47870325.lua)

```lua
end
function c47870325.thfilter(c,rc,p)
	return c:IsRelateToCard(rc) and c:IsControler(p) and c:IsAbleToHand()
end
function c47870325.atkop(e,tp,eg,ep,ev,re,r,rp)
```

### Alien Mother (`24104865`)

Source: [Scripts/c24104865.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24104865.lua)

```lua
end
function c24104865.desfilter(c,rc)
	return c:GetFlagEffect(24104865)~=0 and rc:IsRelateToCard(c)
end
function c24104865.desop(e,tp,eg,ep,ev,re,r,rp)
```

### Overmind Archfiend (`24221808`)

Source: [Scripts/c24221808.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24221808.lua)

```lua
end
function c24221808.spfilter(c,rc,e,tp)
	return c:IsRelateToCard(rc) and c:IsCanBeSpecialSummoned(e,0,tp,false,false)
end
function c24221808.spop(e,tp,eg,ep,ev,re,r,rp)
```
