# Duel.Equip

## Signature

```lua
Duel.Equip(int player, Card c1, Card c2, [bool up], [bool is_step]) -> bool
```

## Description

Equips c1 to c2 for player and returns true if the equip succeeds.
up defaults to true and makes the Equip Card face-up. When is_step is true, call Duel.EquipComplete after all step equips have been created.
Register or rely on an EFFECT_EQUIP_LIMIT so the card can legally remain equipped to that monster.

## How To Use It

Use this after both the Equip Card and the monster it will equip to are still valid.

A self-equip effect usually creates an Equip Limit after the equip succeeds so the card stays attached only to the intended monster:

```lua
local tc=Duel.GetFirstTarget()
local c=e:GetHandler()
if tc and tc:IsRelateToEffect(e) and c:IsRelateToEffect(e) and Duel.Equip(tp,c,tc) then
    local e1=Effect.CreateEffect(c)
    e1:SetType(EFFECT_TYPE_SINGLE)
    e1:SetCode(EFFECT_EQUIP_LIMIT)
    e1:SetProperty(EFFECT_FLAG_CANNOT_DISABLE)
    e1:SetValue(function(e,ec) return ec==tc end)
    e1:SetReset(RESET_EVENT+RESETS_STANDARD)
    c:RegisterEffect(e1)
end
```

When several cards are equipped as one procedure with `is_step=true`, call `Duel.EquipComplete()` after the final successful step.

## Related Functions

- [Card.CheckEquipTarget](/api/functions/Card/CheckEquipTarget)
- [Duel.EquipComplete](/api/functions/Duel/EquipComplete)
- [Auxiliary.AddEquipSpellEffect](/api/functions/Auxiliary/AddEquipSpellEffect)

## Parameters

- `player` `int`
- `c1` `Card`
- `c2` `Card`
- `up` `bool` optional - default: true
- `is_step` `bool` optional - default: false

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4904`

## Guided Examples

Learn how to use this function in context:

- [Methods for Affecting Cards](/learn/affecting-cards)
- [Equip Spells and Equip Cards](/learn/equip-spells)
- [Functions That Move Cards Across Locations](/learn/moving-cards)
- [Union Monsters](/learn/union-monsters)

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **664** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Duel.Equip) with `Duel.Equip`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Salamandra with Chain](/examples/cards/62091148) | `62091148` | [Scripts/c62091148.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c62091148.lua) | 1 |
| [Fiendsmith's Sequence](/examples/cards/49867899) | `49867899` | [Scripts/c49867899.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c49867899.lua) | 1 |
| [Spirit Illusion](/examples/cards/71939275) | `71939275` | [Scripts/c71939275.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c71939275.lua) | 1 |
| [Pere-Zenet Em Heru](/examples/cards/46273941) | `46273941` | [Scripts/c46273941.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c46273941.lua) | 1 |
| [Am Duazenet](/examples/cards/45151304) | `45151304` | [Scripts/c45151304.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c45151304.lua) | 1 |
| [Converging Wishes](/examples/cards/20007374) | `20007374` | [Scripts/c20007374.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c20007374.lua) | 1 |
| [Graydle Split](/examples/cards/75361204) | `75361204` | [Scripts/c75361204.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c75361204.lua) | 1 |
| [Shining Draw](/examples/cards/35906693) | `35906693` | [Scripts/c35906693.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c35906693.lua) | 1 |
| [Plunder Patroll Shipshape Ships Shipping](/examples/cards/44227727) | `44227727` | [Scripts/c44227727.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c44227727.lua) | 1 |
| Red-Eyes Slash Dragon | `21140872` | [Scripts/c21140872.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c21140872.lua) | 1 |
| Power Patron DoomZ | `81650695` | [Scripts/c81650695.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c81650695.lua) | 1 |
| Power Tool Braver Dragon | `63265554` | [Scripts/c63265554.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c63265554.lua) | 1 |
| Meklord Astro Mekanikle | `63468625` | [Scripts/c63468625.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c63468625.lua) | 1 |
| Amazement Administrator Arlekino | `94821366` | [Scripts/c94821366.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c94821366.lua) | 1 |
| DoomZ XII Zero - Drastea | `92472273` | [Scripts/c92472273.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c92472273.lua) | 1 |
| Tails of the Fairy Tails | `82119326` | [Scripts/c82119326.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c82119326.lua) | 1 |
| Seven Stars Slash - Army Annihilator Hagun | `65114115` | [Scripts/c65114115.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c65114115.lua) | 1 |
| Zoroa, the Magistus Verethragna | `37260677` | [Scripts/c37260677.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c37260677.lua) | 1 |
| Emperor Charles the Great | `97864322` | [Scripts/c97864322.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c97864322.lua) | 1 |
| Inzektor Picofalena | `97273514` | [Scripts/c97273514.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c97273514.lua) | 1 |
| Favorite Hero | `11881272` | [Scripts/c11881272.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c11881272.lua) | 1 |
| Amaze Attraction Wonder Wheel | `93473606` | [Scripts/c93473606.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c93473606.lua) | 1 |
| Heroic Champion - Magnum Excalibur | `14301396` | [Scripts/c14301396.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c14301396.lua) | 1 |
| Nephe Shaddoll Fusion | `60226558` | [Scripts/c60226558.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c60226558.lua) | 1 |
| ...and 640 more |  |  |  |

## Script Examples

### Salamandra with Chain (`62091148`)

Source: [Scripts/c62091148.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c62091148.lua)

```lua
	if not c:IsRelateToEffect(e) or c:IsStatus(STATUS_LEAVE_CONFIRMED) then return end
	local tc=Duel.GetFirstTarget()
	if tc:IsRelateToEffect(e) and tc:IsFaceup() and Duel.Equip(tp,c,tc) then
		local e1=Effect.CreateEffect(c)
		e1:SetType(EFFECT_TYPE_EQUIP)
```

### Fiendsmith's Sequence (`49867899`)

Source: [Scripts/c49867899.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c49867899.lua)

```lua
			return
		end
		if not Duel.Equip(tp,c,tc) then return end
		local e1=Effect.CreateEffect(c)
		e1:SetType(EFFECT_TYPE_SINGLE)
```

### Spirit Illusion (`71939275`)

Source: [Scripts/c71939275.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c71939275.lua)

```lua
	local tc=Duel.GetFirstTarget()
	if c:IsRelateToEffect(e) and tc:IsRelateToEffect(e) and tc:IsFaceup() then
		Duel.Equip(tp,c,tc)
	end
end
```
