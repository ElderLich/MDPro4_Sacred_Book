# Auxiliary.sumreg

## Signature

```lua
Auxiliary.sumreg(Effect e, int tp, Group eg, int ep, int ev, Effect re, int r, int rp) -> void
```

## Description

For each card in eg whose original code equals e's label, registers a same-code flag effect that lasts through the End Phase/reset.

## Parameters

- `e` `Effect`
- `tp` `int`
- `eg` `Group`
- `ep` `int`
- `ev` `int`
- `re` `Effect`
- `r` `int`
- `rp` `int`

## Source

- `Utilities/utility.lua:848`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **20** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Auxiliary.sumreg`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Performapal Celestial Magician | `58092907` | [Scripts/c58092907.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c58092907.lua) | 1 |
| Angello Vaalmonica | `3048768` | [Scripts/c3048768.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c3048768.lua) | 1 |
| Dimonno Vaalmonica | `30432463` | [Scripts/c30432463.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30432463.lua) | 1 |
| Performapal Corn | `33103459` | [Scripts/c33103459.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c33103459.lua) | 1 |
| Gizmek Yata, the Gleaming Vanguard | `13224603` | [Scripts/c13224603.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c13224603.lua) | 1 |
| Mayosenju Hitot | `21364070` | [Scripts/c21364070.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c21364070.lua) | 1 |
| Raidraptor - Noir Lanius | `99707692` | [Scripts/c99707692.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c99707692.lua) | 1 |
| Kashtira Riseheart | `31149212` | [Scripts/c31149212.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c31149212.lua) | 1 |
| Predaplant Spider Orchid | `30537973` | [Scripts/c30537973.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30537973.lua) | 1 |
| Performapal Uni | `7714344` | [Scripts/c7714344.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c7714344.lua) | 1 |
| Dark Magician of Chaos | `40737112` | [Scripts/c40737112.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c40737112.lua) | 1 |
| Mayosenju Daibak | `93368494` | [Scripts/c93368494.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93368494.lua) | 1 |
| Mantman the Ultrahuman | `22916418` | [Scripts/c22916418.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c22916418.lua) | 1 |
| Raidraptor - Mimicry Lanius | `96345188` | [Scripts/c96345188.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c96345188.lua) | 1 |
| Raidraptor - Tribute Lanius | `83236601` | [Scripts/c83236601.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c83236601.lua) | 1 |
| Raidraptor - Sharp Lanius | `60950180` | [Scripts/c60950180.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c60950180.lua) | 1 |
| Raidraptor - Wild Vulture | `8785161` | [Scripts/c8785161.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c8785161.lua) | 1 |
| Yosenju Misak | `39853199` | [Scripts/c39853199.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c39853199.lua) | 1 |
| Yosenju Magat | `49249907` | [Scripts/c49249907.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c49249907.lua) | 1 |
| Raidraptor - Vanishing Lanius | `53251824` | [Scripts/c53251824.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c53251824.lua) | 1 |

## Script Examples

### Performapal Celestial Magician (`58092907`)

Source: [Scripts/c58092907.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c58092907.lua)

```lua
		ge1:SetProperty(EFFECT_FLAG_CANNOT_DISABLE)
		ge1:SetLabel(58092907)
		ge1:SetOperation(aux.sumreg)
		Duel.RegisterEffect(ge1,0)
		local ge2=ge1:Clone()
```

### Angello Vaalmonica (`3048768`)

Source: [Scripts/c3048768.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c3048768.lua)

```lua
		ge1:SetLabel(id)
		ge1:SetProperty(EFFECT_FLAG_CANNOT_DISABLE)
		ge1:SetOperation(aux.sumreg)
		Duel.RegisterEffect(ge1,0)
		local ge2=ge1:Clone()
```

### Dimonno Vaalmonica (`30432463`)

Source: [Scripts/c30432463.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30432463.lua)

```lua
		ge1:SetLabel(id)
		ge1:SetProperty(EFFECT_FLAG_CANNOT_DISABLE)
		ge1:SetOperation(aux.sumreg)
		Duel.RegisterEffect(ge1,0)
		local ge2=ge1:Clone()
```
