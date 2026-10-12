# Duel.ClearOperationInfo

## Signature

```lua
Duel.ClearOperationInfo(int ct) -> void
```

## Description

Clears operation info for chain ct; it is a no-op if that Chain Link does not exist.

## Parameters

- `ct` `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5011`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **38** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Duel.ClearOperationInfo) with `Duel.ClearOperationInfo`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Tohushaddoll Grysta](/examples/cards/95072744) | `95072744` | [Scripts/c95072744.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c95072744.lua) | 1 |
| [Barian's Chaos Draw](/examples/cards/97769122) | `97769122` | [Scripts/c97769122.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c97769122.lua) | 1 |
| [Transonic Bird](/examples/cards/34072799) | `34072799` | [Scripts/c34072799.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c34072799.lua) | 1 |
| Chef de Nouvelles | `29251488` | [Scripts/c29251488.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c29251488.lua) | 1 |
| Witchcrafter Genni | `64756282` | [Scripts/c64756282.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c64756282.lua) | 1 |
| Angello Vaalmonica | `3048768` | [Scripts/c3048768.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c3048768.lua) | 1 |
| Dimonno Vaalmonica | `30432463` | [Scripts/c30432463.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c30432463.lua) | 1 |
| Zebufera, Vaalmonican Hallow Heathen | `2815176` | [Scripts/c2815176.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c2815176.lua) | 1 |
| Witchcrafter Pupils | `69964858` | [Scripts/c69964858.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c69964858.lua) | 1 |
| Dinomorphia Kentregina | `48832775` | [Scripts/c48832775.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c48832775.lua) | 1 |
| Darklord Eveningstar | `10136446` | [Scripts/c10136446.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c10136446.lua) | 1 |
| Predaplant Verte Anaconda | `70369116` | [Scripts/c70369116.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c70369116.lua) | 1 |
| Chasma, Dragon Ruler of Auroras | `4965193` | [Scripts/c4965193.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c4965193.lua) | 1 |
| Joker's Wild | `81945678` | [Scripts/c81945678.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c81945678.lua) | 1 |
| Tellarknight Constellar Caduceus | `58858807` | [Scripts/c58858807.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c58858807.lua) | 1 |
| Dinomorphia Reversion | `28292031` | [Scripts/c28292031.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c28292031.lua) | 1 |
| Seventh Ascension | `23153227` | [Scripts/c23153227.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c23153227.lua) | 1 |
| Darklord Tezcatlipoca | `88234365` | [Scripts/c88234365.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c88234365.lua) | 1 |
| Darklord Amdusc | `51728779` | [Scripts/c51728779.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c51728779.lua) | 1 |
| Stars Align across the Milky Way | `20417688` | [Scripts/c20417688.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c20417688.lua) | 1 |
| Ruler of the End of the World | `3739500` | [Scripts/c3739500.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c3739500.lua) | 1 |
| Darklord Ixchel | `52840267` | [Scripts/c52840267.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c52840267.lua) | 1 |
| Traptrix Rafflesia | `6511113` | [Scripts/c6511113.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c6511113.lua) | 1 |
| Kewl Tune Playlist | `40847034` | [Scripts/c40847034.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c40847034.lua) | 1 |
| ...and 14 more |  |  |  |

## Script Examples

### Tohushaddoll Grysta (`95072744`)

Source: [Scripts/c95072744.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c95072744.lua)

```lua
	local tg=te:GetTarget()
	if tg then tg(e,tp,eg,ep,ev,re,r,rp,1) end
	Duel.ClearOperationInfo(0)
end
function s.effop(e,tp,eg,ep,ev,re,r,rp)
```

### Barian's Chaos Draw (`97769122`)

Source: [Scripts/c97769122.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c97769122.lua)

```lua
	te:SetLabelObject(e:GetLabelObject())
	e:SetLabelObject(te)
	Duel.ClearOperationInfo(0)
end
function c97769122.cpop(e,tp,eg,ep,ev,re,r,rp)
```

### Transonic Bird (`34072799`)

Source: [Scripts/c34072799.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c34072799.lua)

```lua
	local tg=te:GetTarget()
	if tg then tg(e,tp,eg,ep,ev,re,r,rp,1) end
	Duel.ClearOperationInfo(0)
end
function c34072799.rsop(e,tp,eg,ep,ev,re,r,rp)
```
