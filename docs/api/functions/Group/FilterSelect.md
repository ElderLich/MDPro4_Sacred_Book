# Group.FilterSelect

## Signature

```lua
Group.FilterSelect(Group g, int player, function f, int min, int max, [Card|Group|nil ex], ... any) -> Group
```

## Description

Lets player choose min to max cards from g that satisfy filter f, excluding ex, and returns the selected Group.
Extra arguments after ex are passed to f after the Card argument.
This is a selection from an existing Group, not an official Chain target selection.

## How To Use It

Use this when you already have a Group, but only some cards in it should be selectable.

```lua
local sg=g:FilterSelect(tp,s.filter,1,1,nil,e,tp)
if #sg>0 then
    Duel.SendtoHand(sg,nil,REASON_EFFECT)
end
```

This is still an ordinary selection, not an official Chain target selection. Use `Duel.SelectTarget` during targeting effects.

## Related Functions

- [Group.Filter](/api/functions/Group/Filter)
- [Group.Select](/api/functions/Group/Select)
- [Duel.SelectMatchingCard](/api/functions/Duel/SelectMatchingCard)

## Parameters

- `g` `Group`
- `player` `int`
- `f` `function`
- `min` `int`
- `max` `int`
- `ex` `Card|Group|nil` optional
- `...` `any`

## Returns

- `Group`

## Source

- `D:\Programs\GitHub\ygopro-core\libgroup.cpp:914`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **241** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Group.FilterSelect) with `Group.FilterSelect`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Surprise Fusion](/examples/cards/35167375) | `35167375` | [Scripts/c35167375.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c35167375.lua) | 1 |
| [El Shaddoll Apkallone](/examples/cards/50907446) | `50907446` | [Scripts/c50907446.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c50907446.lua) | 3 |
| [Performage Cup Tricker](/examples/cards/6812770) | `6812770` | [Scripts/c6812770.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c6812770.lua) | 1 |
| [Ursarctic Polari](/examples/cards/27693363) | `27693363` | [Scripts/c27693363.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c27693363.lua) | 1 |
| [D/D Count Surveyor](/examples/cards/5997110) | `5997110` | [Scripts/c5997110.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c5997110.lua) | 1 |
| [Nekroz Kaleidoscope](/examples/cards/51124303) | `51124303` | [Scripts/c51124303.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c51124303.lua) | 1 |
| [Ursarctic Polar Star](/examples/cards/62714453) | `62714453` | [Scripts/c62714453.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c62714453.lua) | 1 |
| [Kewl Tune Crackle](/examples/cards/39576656) | `39576656` | [Scripts/c39576656.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c39576656.lua) | 2 |
| Particle Fusion | `39261576` | [Scripts/c39261576.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c39261576.lua) | 1 |
| Ostinato | `9113513` | [Scripts/c9113513.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c9113513.lua) | 4 |
| Trickstar Light Arena | `63492244` | [Scripts/c63492244.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63492244.lua) | 1 |
| Black Dragon Ninja | `56562619` | [Scripts/c56562619.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c56562619.lua) | 1 |
| Frightfur March | `74416026` | [Scripts/c74416026.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74416026.lua) | 1 |
| Power Tool Braver Dragon | `63265554` | [Scripts/c63265554.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63265554.lua) | 1 |
| Alba System Dogmatikalamity | `93053159` | [Scripts/c93053159.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93053159.lua) | 2 |
| Triamid Pulse | `96100333` | [Scripts/c96100333.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c96100333.lua) | 4 |
| Amazement Administrator Arlekino | `94821366` | [Scripts/c94821366.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c94821366.lua) | 1 |
| Exosisters Magnifica | `59242457` | [Scripts/c59242457.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59242457.lua) | 1 |
| R.B. Lambda Cannon | `81794107` | [Scripts/c81794107.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c81794107.lua) | 1 |
| Hyperinvoked Aeon | `33166263` | [Scripts/c33166263.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c33166263.lua) | 1 |
| Psychic Arsenal | `16238373` | [Scripts/c16238373.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c16238373.lua) | 1 |
| Dragunity Arma Leyvaten | `63487632` | [Scripts/c63487632.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63487632.lua) | 1 |
| Kewl Tune Remix | `88170262` | [Scripts/c88170262.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c88170262.lua) | 1 |
| Fydraulis Harmonia | `70088809` | [Scripts/c70088809.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c70088809.lua) | 1 |
| ...and 217 more |  |  |  |

## Script Examples

### Surprise Fusion (`35167375`)

Source: [Scripts/c35167375.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c35167375.lua)

```lua
	local srg=nil
	local chk=Duel.IsExistingMatchingCard(s.cfilter,tp,LOCATION_MZONE,0,1,nil,tp,true)
	srg=rg:FilterSelect(tp,s.cfilter,1,1,nil,tp,chk)
	if srg and srg:GetCount()>0 then
		local rc=srg:GetFirst()
```

### El Shaddoll Apkallone (`50907446`)

Source: [Scripts/c50907446.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c50907446.lua)

```lua
	else
		Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_FMATERIAL)
		g=mg:FilterSelect(tp,c50907446.FShaddollSpFilter1,1,1,nil,c,tp,mg,exg,chkf)
		mg:Sub(g)
	end
```

### Performage Cup Tricker (`6812770`)

Source: [Scripts/c6812770.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c6812770.lua)

```lua
	if tg:GetCount()~=2 or not tg:IsExists(s.xyzfilter2,1,nil) then return end
	Duel.Hint(HINT_SELECTMSG,tp,aux.Stringid(id,4))
	local tg2=tg:FilterSelect(tp,s.xyzfilter2,1,1,nil)
	tg:Sub(tg2)
	local tc=tg2:GetFirst()
```
