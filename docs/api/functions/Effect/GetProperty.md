# Effect.GetProperty

## Signature

```lua
Effect.GetProperty(Effect e) -> int,int
```

## Description

Returns e's two property flag fields, flag1 and flag2.

## Parameters

- `e` `Effect`

## Returns

- `int` - flag1.
- `int` - flag2.

## Source

- `D:\Programs\GitHub\ygopro-core\libeffect.cpp:634`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **28** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Effect.GetProperty`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Barian's Chaos Draw](/examples/cards/97769122) | `97769122` | [Scripts/c97769122.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c97769122.lua) | 63 |
| [Transonic Bird](/examples/cards/34072799) | `34072799` | [Scripts/c34072799.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c34072799.lua) | 61 |
| [Chef de Nouvelles](/examples/cards/29251488) | `29251488` | [Scripts/c29251488.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c29251488.lua) | 60 |
| Angello Vaalmonica | `3048768` | [Scripts/c3048768.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c3048768.lua) | 54 |
| Dimonno Vaalmonica | `30432463` | [Scripts/c30432463.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30432463.lua) | 53 |
| Witchcrafter Genni | `64756282` | [Scripts/c64756282.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c64756282.lua) | 52 |
| Dinomorphia Kentregina | `48832775` | [Scripts/c48832775.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c48832775.lua) | 49 |
| Predaplant Verte Anaconda | `70369116` | [Scripts/c70369116.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c70369116.lua) | 49 |
| Chasma, Dragon Ruler of Auroras | `4965193` | [Scripts/c4965193.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c4965193.lua) | 47 |
| Joker's Wild | `81945678` | [Scripts/c81945678.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c81945678.lua) | 47 |
| Dinomorphia Reversion | `28292031` | [Scripts/c28292031.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c28292031.lua) | 46 |
| Seventh Ascension | `23153227` | [Scripts/c23153227.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c23153227.lua) | 45 |
| Stars Align across the Milky Way | `20417688` | [Scripts/c20417688.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c20417688.lua) | 45 |
| Bait Doll | `7165085` | [Scripts/c7165085.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c7165085.lua) | 45 |
| Traptrix Rafflesia | `6511113` | [Scripts/c6511113.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c6511113.lua) | 42 |
| Double Spell | `24096228` | [Scripts/c24096228.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24096228.lua) | 40 |
| Kewl Tune Loudness War | `41069676` | [Scripts/c41069676.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c41069676.lua) | 38 |
| Numeron Network | `41418852` | [Scripts/c41418852.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c41418852.lua) | 37 |
| Spellbook of the Master | `56981417` | [Scripts/c56981417.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c56981417.lua) | 37 |
| Ghostrick Festival | `35871958` | [Scripts/c35871958.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c35871958.lua) | 36 |
| Fusion Duplication | `43331750` | [Scripts/c43331750.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c43331750.lua) | 34 |
| Trap of Darkness | `79766336` | [Scripts/c79766336.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c79766336.lua) | 33 |
| Transaction Rollback | `6351147` | [Scripts/c6351147.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c6351147.lua) | 32 |
| Fake Feather | `22628574` | [Scripts/c22628574.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c22628574.lua) | 31 |
| ...and 4 more |  |  |  |

## Script Examples

### Barian's Chaos Draw (`97769122`)

Source: [Scripts/c97769122.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c97769122.lua)

```lua
	local te,ceg,cep,cev,cre,cr,crp=g:GetFirst():CheckActivateEffect(true,true,true)
	Duel.SendtoGrave(g,REASON_COST)
	e:SetProperty(te:GetProperty())
	local tg=te:GetTarget()
	if tg then tg(e,tp,ceg,cep,cev,cre,cr,crp,1) end
```

### Transonic Bird (`34072799`)

Source: [Scripts/c34072799.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c34072799.lua)

```lua
	e:SetLabelObject(te)
	Duel.SendtoGrave(g,REASON_COST)
	e:SetProperty(te:GetProperty())
	local tg=te:GetTarget()
	if tg then tg(e,tp,eg,ep,ev,re,r,rp,1) end
```

### Chef de Nouvelles (`29251488`)

Source: [Scripts/c29251488.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c29251488.lua)

```lua
	local te,ceg,cep,cev,cre,cr,crp=g:GetFirst():CheckActivateEffect(false,true,true)
	Duel.Remove(g,POS_FACEUP,REASON_COST)
	e:SetProperty(te:GetProperty())
	local tg=te:GetTarget()
	if tg then tg(e,tp,ceg,cep,cev,cre,cr,crp,1) end
```
