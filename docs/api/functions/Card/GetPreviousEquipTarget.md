# Card.GetPreviousEquipTarget

## Signature

```lua
Card.GetPreviousEquipTarget(Card c) -> Card|nil
```

## Description

Returns c's previous Equip target, or nil.
Use this for lost-target and sent-from-field Equip Card triggers after the live equip relationship is gone.

## How To Use It

Use this after an Equip Card has left its equip relationship and the effect needs to know which monster it was previously equipped to.

```lua
local ec=e:GetHandler():GetPreviousEquipTarget()
return e:GetHandler():IsReason(REASON_LOST_TARGET) and ec~=nil
```

This is the usual read for lost-target or sent-from-field Equip Card triggers. It is not a live equip relationship.

## Related Functions

- [Card.GetEquipTarget](/api/functions/Card/GetEquipTarget)
- [Duel.Equip](/api/functions/Duel/Equip)
- [Card.IsReason](/api/functions/Card/IsReason)

## Parameters

- `c` `Card`

## Returns

- `Card|nil`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3575`

## Guided Examples

Learn how to use this function in context:

- [Equip Spells and Equip Cards](/learn/equip-spells)

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **45** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Card.GetPreviousEquipTarget) with `Card.GetPreviousEquipTarget`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Parasite Paranoid | `14457896` | [Scripts/c14457896.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c14457896.lua) | 1 |
| "Infernoble Arms - Almace" | `98319530` | [Scripts/c98319530.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c98319530.lua) | 1 |
| Execution of the Contract | `55976207` | [Scripts/c55976207.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c55976207.lua) | 1 |
| "Infernoble Arms - Durendal" | `37478723` | [Scripts/c37478723.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c37478723.lua) | 1 |
| Gemini Booster | `18096222` | [Scripts/c18096222.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c18096222.lua) | 1 |
| Borrel Regenerator | `6556178` | [Scripts/c6556178.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c6556178.lua) | 1 |
| Grief Tablet | `18046862` | [Scripts/c18046862.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c18046862.lua) | 1 |
| Archfiend's Staff of Despair | `21438286` | [Scripts/c21438286.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c21438286.lua) | 1 |
| Parasomnia Pillow | `44092304` | [Scripts/c44092304.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c44092304.lua) | 2 |
| Prevention Star | `94303232` | [Scripts/c94303232.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c94303232.lua) | 1 |
| Cyberdark Claw | `82562802` | [Scripts/c82562802.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c82562802.lua) | 1 |
| ZW - Sleipnir Mail | `2648201` | [Scripts/c2648201.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c2648201.lua) | 1 |
| Attachment Cybern | `79875526` | [Scripts/c79875526.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c79875526.lua) | 1 |
| Cyberdark Cannon | `45078193` | [Scripts/c45078193.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c45078193.lua) | 1 |
| "Infernoble Arms - Joyeuse" | `90861137` | [Scripts/c90861137.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c90861137.lua) | 1 |
| Dragunity Aklys | `36870345` | [Scripts/c36870345.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c36870345.lua) | 1 |
| "Infernoble Arms - Hauteclere" | `64867422` | [Scripts/c64867422.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c64867422.lua) | 1 |
| Inzektor Giga-Mantis | `94573223` | [Scripts/c94573223.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c94573223.lua) | 1 |
| Spirit Burner | `50418970` | [Scripts/c50418970.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c50418970.lua) | 1 |
| Red-Eyes Baby Dragon | `58257569` | [Scripts/c58257569.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c58257569.lua) | 1 |
| Orb of Yasaka | `74115234` | [Scripts/c74115234.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c74115234.lua) | 1 |
| Iron Chain Snake | `80769747` | [Scripts/c80769747.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c80769747.lua) | 1 |
| U.A. Powered Jersey | `35884610` | [Scripts/c35884610.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c35884610.lua) | 1 |
| Inzektor Giga-Weevil | `21977828` | [Scripts/c21977828.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c21977828.lua) | 1 |
| ...and 21 more |  |  |  |

## Script Examples

### Parasite Paranoid (`14457896`)

Source: [Scripts/c14457896.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c14457896.lua)

```lua
function c14457896.spcon(e,tp,eg,ep,ev,re,r,rp)
	local c=e:GetHandler()
	return c:IsPreviousLocation(LOCATION_SZONE) and c:GetPreviousEquipTarget()
end
function c14457896.spfilter(c,e,tp)
```

### "Infernoble Arms - Almace" (`98319530`)

Source: [Scripts/c98319530.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c98319530.lua)

```lua
function s.thcon(e,tp,eg,ep,ev,re,r,rp)
	local c=e:GetHandler()
	return c:IsReason(REASON_LOST_TARGET) and c:GetPreviousEquipTarget():IsLocation(LOCATION_GRAVE)
end
function s.thfilter(c)
```

### Execution of the Contract (`55976207`)

Source: [Scripts/c55976207.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c55976207.lua)

```lua
function c55976207.descon(e,tp,eg,ep,ev,re,r,rp)
	local c=e:GetHandler()
	local tc=c:GetPreviousEquipTarget()
	return tc and tc:IsReason(REASON_RELEASE) and c:IsReason(REASON_LOST_TARGET)
end
```
