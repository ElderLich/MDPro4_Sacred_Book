# Auxiliary.MustMaterialCheck

## Signature

```lua
Auxiliary.MustMaterialCheck(any v, int tp, int code) -> void
```

## Description

Check if value contains cards or a group affected by player's effect type code
Currently involved codes are:
EFFECT_MUST_BE_SMATERIAL
EFFECT_MUST_BE_XMATERIAL
EFFECT_MUST_BE_FMATERIAL
EFFECT_MUST_BE_LMATERIAL
All are checks for required materials

## Parameters

- `v` `any`
- `tp` `int`
- `code` `int`

## Source

- `Utilities/procedure.lua:2274`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **147** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Auxiliary.MustMaterialCheck`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Astrograph Sorcerer](/examples/cards/76794549) | `76794549` | [Scripts/c76794549.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c76794549.lua) | 71 |
| [Accel Synchro Stardust Dragon](/examples/cards/30983281) | `30983281` | [Scripts/c30983281.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30983281.lua) | 69 |
| [El Shaddoll Apkallone](/examples/cards/50907446) | `50907446` | [Scripts/c50907446.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c50907446.lua) | 68 |
| [Ghostrick Renovation](/examples/cards/61818176) | `61818176` | [Scripts/c61818176.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c61818176.lua) | 65 |
| [Resurgam Xyz](/examples/cards/49082032) | `49082032` | [Scripts/c49082032.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c49082032.lua) | 64 |
| [Converging Wishes](/examples/cards/20007374) | `20007374` | [Scripts/c20007374.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c20007374.lua) | 64 |
| [Shining Draw](/examples/cards/35906693) | `35906693` | [Scripts/c35906693.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c35906693.lua) | 63 |
| [Junoldo the Shadespirit Power Patron](/examples/cards/10266279) | `10266279` | [Scripts/c10266279.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c10266279.lua) | 62 |
| [Flower Cardian Peony with Butterfly](/examples/cards/57261568) | `57261568` | [Scripts/c57261568.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c57261568.lua) | 62 |
| [The Gaze of Timaeus](/examples/cards/22283204) | `22283204` | [Scripts/c22283204.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c22283204.lua) | 62 |
| [Chronograph Sorcerer](/examples/cards/12289247) | `12289247` | [Scripts/c12289247.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c12289247.lua) | 61 |
| [Flower Cardian Willow with Calligrapher](/examples/cards/89818984) | `89818984` | [Scripts/c89818984.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c89818984.lua) | 61 |
| [El Shaddoll Meshachrer](/examples/cards/32467459) | `32467459` | [Scripts/c32467459.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c32467459.lua) | 61 |
| [Jupredo the Shademachine Power Patron](/examples/cards/43871165) | `43871165` | [Scripts/c43871165.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c43871165.lua) | 60 |
| Frightfur Meister | `77522571` | [Scripts/c77522571.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c77522571.lua) | 59 |
| K9-EW Special Release Experiment | `26585784` | [Scripts/c26585784.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c26585784.lua) | 59 |
| Power Patron DoomZ | `81650695` | [Scripts/c81650695.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c81650695.lua) | 58 |
| Rank-Up-Magic Astral Force | `45950291` | [Scripts/c45950291.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c45950291.lua) | 58 |
| K9-X Forced Release | `53792930` | [Scripts/c53792930.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c53792930.lua) | 58 |
| Flame Swordsrealm | `73714736` | [Scripts/c73714736.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c73714736.lua) | 58 |
| Frightfur March | `74416026` | [Scripts/c74416026.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74416026.lua) | 58 |
| Alba System Dogmatikalamity | `93053159` | [Scripts/c93053159.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93053159.lua) | 58 |
| The Phantom Knights' Rank-Up-Magic Requiem | `62104532` | [Scripts/c62104532.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c62104532.lua) | 58 |
| Phantom Knights' Rank-Up-Magic Force | `88504133` | [Scripts/c88504133.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c88504133.lua) | 57 |
| ...and 123 more |  |  |  |

## Script Examples

### Astrograph Sorcerer (`76794549`)

Source: [Scripts/c76794549.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c76794549.lua)

```lua
end
function c76794549.hntg(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return aux.MustMaterialCheck(nil,tp,EFFECT_MUST_BE_FMATERIAL) end
	Duel.SetOperationInfo(0,CATEGORY_SPECIAL_SUMMON,nil,1,tp,LOCATION_EXTRA)
end
```

### Accel Synchro Stardust Dragon (`30983281`)

Source: [Scripts/c30983281.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30983281.lua)

```lua
	if chk==0 then return Duel.IsPlayerCanSpecialSummonCount(tp,2)
		and (not ect1 or ect1>1) and (not ect2 or ect2>1) and (b1 or b2)
		and aux.MustMaterialCheck(nil,tp,EFFECT_MUST_BE_SMATERIAL) end
	local rg=Group.CreateGroup()
	local rc=nil
```

### El Shaddoll Apkallone (`50907446`)

Source: [Scripts/c50907446.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c50907446.lua)

```lua
	local sg=Group.FromCards(c,mc)
	if sg:IsExists(aux.TuneMagicianCheckX,1,nil,sg,EFFECT_TUNE_MAGICIAN_F) then return false end
	if not aux.MustMaterialCheck(sg,tp,EFFECT_MUST_BE_FMATERIAL) then return false end
	if aux.FCheckAdditional and not aux.FCheckAdditional(tp,sg,fc)
		or aux.FGoalCheckAdditional and not aux.FGoalCheckAdditional(tp,sg,fc) then return false end
```
