# Auxiliary.SynMixHandCheck

## Signature

```lua
Auxiliary.SynMixHandCheck(Group g, int tp, Card syncard) -> bool
```

## Description

Checks whether selected hand Synchro Materials are allowed by a material that grants hand Synchro use, including filter and count limits.

## Parameters

- `g` `Group`
- `tp` `int`
- `syncard` `Card`

## Returns

- `bool` - true if hand Synchro Materials in g are legal.

## Source

- `Utilities/procedure.lua:396`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **8** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Auxiliary.SynMixHandCheck) with `Auxiliary.SynMixHandCheck`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Accel Synchro Stardust Dragon](/examples/cards/30983281) | `30983281` | [Scripts/c30983281.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30983281.lua) | 1 |
| [Yummy★Snatchy](/examples/cards/30581601) | `30581601` | [Scripts/c30581601.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30581601.lua) | 1 |
| Saiba the Soldier Swordsmith | `36608728` | [Scripts/c36608728.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c36608728.lua) | 1 |
| Naturia Blessing | `34813545` | [Scripts/c34813545.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c34813545.lua) | 1 |
| Stand Up Centur-Ion! | `41371602` | [Scripts/c41371602.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c41371602.lua) | 1 |
| Re-dyce-cle | `85704698` | [Scripts/c85704698.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c85704698.lua) | 1 |
| Etude of the Branded | `45675980` | [Scripts/c45675980.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c45675980.lua) | 1 |
| Yang Zing Unleashed | `77783947` | [Scripts/c77783947.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c77783947.lua) | 1 |

## Script Examples

### Accel Synchro Stardust Dragon (`30983281`)

Source: [Scripts/c30983281.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30983281.lua)

```lua
end
function c30983281.syncheck(g,tp,syncard)
	return aux.SynMixHandCheck(g,tp,syncard) and syncard:IsSynchroSummonable(nil,g,#g-1,#g-1)
end
function c30983281.synfilter(c,tp,mg)
```

### Yummy★Snatchy (`30581601`)

Source: [Scripts/c30581601.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30581601.lua)

```lua
end
function s.syncheck(g,tp,syncard)
	return g:IsExists(s.mfilter,1,nil) and aux.SynMixHandCheck(g,tp,syncard) and syncard:IsSynchroSummonable(nil,g,#g-1,#g-1)
end
function s.scfilter(c,tp,mg)
```

### Saiba the Soldier Swordsmith (`36608728`)

Source: [Scripts/c36608728.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c36608728.lua)

```lua
end
function s.syncheck(g,tp,syncard)
	return g:IsExists(s.mfilter,1,nil) and aux.SynMixHandCheck(g,tp,syncard) and syncard:IsSynchroSummonable(nil,g,#g-1,#g-1)
end
function s.scfilter(c,tp,mg)
```
