# Duel.Overlay

## Signature

```lua
Duel.Overlay(Card c, Card|Group ocard, [bool adjust]) -> void
```

## Description

Overlays ocard under c as Xyz Material.
This moves a Card or Group under c; it does not by itself perform a proper Xyz Summon or mark the monster's procedure complete.
By default the field is adjusted after the overlay. Pass adjust=false only when a larger procedure will adjust afterward.

## How To Use It

Use this when a procedure or effect turns cards into Xyz Materials under an Xyz Monster.

The first argument is the Xyz Monster that will receive the materials. The second argument can be one Card or a Group:

```lua
Duel.Overlay(xyzc,mg)
```

Leave `adjust` omitted for normal scripts. Pass `false` only inside a larger procedure that will adjust the field afterward.

## Related Functions

- [Duel.GetOverlayGroup](/api/functions/Duel/GetOverlayGroup)
- [Duel.RemoveOverlayCard](/api/functions/Duel/RemoveOverlayCard)
- [Card.GetOverlayGroup](/api/functions/Card/GetOverlayGroup)

## Parameters

- `c` `Card` - Card that will receive the Xyz Materials.
- `ocard` `Card|Group` - Card or Group to overlay under c.
- `adjust` `bool` optional - Whether to adjust the field after overlaying. Defaults to true.

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5014`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **260** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Duel.Overlay) with `Duel.Overlay`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Performage Cup Tricker](/examples/cards/6812770) | `6812770` | [Scripts/c6812770.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c6812770.lua) | 2 |
| [Ghostrick Renovation](/examples/cards/61818176) | `61818176` | [Scripts/c61818176.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c61818176.lua) | 2 |
| [Resurgam Xyz](/examples/cards/49082032) | `49082032` | [Scripts/c49082032.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c49082032.lua) | 2 |
| [Shining Draw](/examples/cards/35906693) | `35906693` | [Scripts/c35906693.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c35906693.lua) | 2 |
| Jupredo the Shademachine Power Patron | `43871165` | [Scripts/c43871165.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c43871165.lua) | 1 |
| K9-EW Special Release Experiment | `26585784` | [Scripts/c26585784.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c26585784.lua) | 2 |
| Power Patron DoomZ | `81650695` | [Scripts/c81650695.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c81650695.lua) | 2 |
| Rank-Up-Magic Astral Force | `45950291` | [Scripts/c45950291.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c45950291.lua) | 2 |
| Number 101: Silent Honor ARK - Soul Asylum | `2419596` | [Scripts/c2419596.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c2419596.lua) | 1 |
| The Phantom Knights' Rank-Up-Magic Requiem | `62104532` | [Scripts/c62104532.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c62104532.lua) | 2 |
| K9-X Forced Release | `53792930` | [Scripts/c53792930.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c53792930.lua) | 2 |
| Phantom Knights' Rank-Up-Magic Force | `88504133` | [Scripts/c88504133.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c88504133.lua) | 2 |
| Super Quantal Mech Ship Magnacarrier | `10424147` | [Scripts/c10424147.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c10424147.lua) | 4 |
| DoomZ XII Zero - Drastea | `92472273` | [Scripts/c92472273.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92472273.lua) | 1 |
| D/D/D Deviser King Deus Machinex | `46593546` | [Scripts/c46593546.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c46593546.lua) | 1 |
| Exosisters Magnifica | `59242457` | [Scripts/c59242457.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59242457.lua) | 2 |
| Number 38: Hope Harbinger Dragon Titanic Galaxy | `63767246` | [Scripts/c63767246.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63767246.lua) | 1 |
| Purrely | `25550531` | [Scripts/c25550531.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c25550531.lua) | 2 |
| Odd-Eyes Rebellion Dragon Overlord | `98452268` | [Scripts/c98452268.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c98452268.lua) | 2 |
| Darktellarknight Batlamyus | `64414267` | [Scripts/c64414267.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c64414267.lua) | 2 |
| Number 4: Stealth Kragen | `67557908` | [Scripts/c67557908.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c67557908.lua) | 1 |
| Purrely Sharely!? | `10780049` | [Scripts/c10780049.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c10780049.lua) | 2 |
| Purrelyeap!? | `82983267` | [Scripts/c82983267.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c82983267.lua) | 2 |
| Gunkan Sushipyard Seaside Supper Spot | `62200831` | [Scripts/c62200831.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c62200831.lua) | 1 |
| ...and 236 more |  |  |  |

## Script Examples

### Performage Cup Tricker (`6812770`)

Source: [Scripts/c6812770.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c6812770.lua)

```lua
			Duel.SendtoGrave(og,REASON_RULE)
		end
		Duel.Overlay(tc,Group.FromCards(c))
	end
end
```

### Ghostrick Renovation (`61818176`)

Source: [Scripts/c61818176.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c61818176.lua)

```lua
		local mg=tc:GetOverlayGroup()
		if mg:GetCount()~=0 then
			Duel.Overlay(sc,mg)
		end
		sc:SetMaterial(Group.FromCards(tc))
```

### Resurgam Xyz (`49082032`)

Source: [Scripts/c49082032.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c49082032.lua)

```lua
		local mg=tc:GetOverlayGroup()
		if mg:GetCount()~=0 then
			Duel.Overlay(sc,mg)
		end
		sc:SetMaterial(Group.FromCards(tc))
```
