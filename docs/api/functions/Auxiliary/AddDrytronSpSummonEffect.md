# Auxiliary.AddDrytronSpSummonEffect

## Signature

```lua
Auxiliary.AddDrytronSpSummonEffect(Card c, function func) -> void
```

## Description

Adds the shared Drytron ignition effect that Special Summons c from the hand or Graveyard.
The effect uses the common Drytron release cost, target, operation wrapper, and custom activity counter.

## Parameters

- `c` `Card`
- `func` `function`

## Source

- `Utilities/utility.lua:1002`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **5** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Auxiliary.AddDrytronSpSummonEffect) with `Auxiliary.AddDrytronSpSummonEffect`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Drytron Gamma Eltanin | `60037599` | [Scripts/c60037599.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c60037599.lua) | 1 |
| Drytron Delta Altais | `22420202` | [Scripts/c22420202.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c22420202.lua) | 1 |
| Drytron Beta Rastaban | `33543890` | [Scripts/c33543890.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c33543890.lua) | 1 |
| Drytron Alpha Thuban | `97148796` | [Scripts/c97148796.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c97148796.lua) | 1 |
| Drytron Zeta Aldhibah | `96026108` | [Scripts/c96026108.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c96026108.lua) | 1 |

## Script Examples

### Drytron Gamma Eltanin (`60037599`)

Source: [Scripts/c60037599.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c60037599.lua)

```lua
	c:RegisterEffect(e1)
	--spsummon
	local e2=aux.AddDrytronSpSummonEffect(c,c60037599.extraop)
	e2:SetDescription(aux.Stringid(60037599,0))
	e2:SetCategory(CATEGORY_SPECIAL_SUMMON+CATEGORY_GRAVE_SPSUMMON)
```

### Drytron Delta Altais (`22420202`)

Source: [Scripts/c22420202.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c22420202.lua)

```lua
	c:RegisterEffect(e1)
	--spsummon
	local e2=aux.AddDrytronSpSummonEffect(c,c22420202.extraop)
	e2:SetDescription(aux.Stringid(22420202,0))
	e2:SetCategory(CATEGORY_SPECIAL_SUMMON+CATEGORY_DRAW)
```

### Drytron Beta Rastaban (`33543890`)

Source: [Scripts/c33543890.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c33543890.lua)

```lua
	c:RegisterEffect(e1)
	--spsummon
	local e2=aux.AddDrytronSpSummonEffect(c,c33543890.extraop)
	e2:SetDescription(aux.Stringid(33543890,0))
	e2:SetCategory(CATEGORY_SPECIAL_SUMMON+CATEGORY_TOGRAVE)
```
