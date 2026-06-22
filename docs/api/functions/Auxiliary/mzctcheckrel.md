# Auxiliary.mzctcheckrel

## Signature

```lua
Auxiliary.mzctcheckrel(Group g, int tp, [int reason]) -> bool
```

## Description

Check if there is space in mzone after tp releases g by reason

## Parameters

- `g` `Group`
- `tp` `int`
- `reason` `int` optional

## Returns

- `bool`

## Source

- `Utilities/utility.lua:1171`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **43** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Auxiliary.mzctcheckrel`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Odd-Eyes Revolution Dragon](/examples/cards/16306932) | `16306932` | [Scripts/c16306932.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c16306932.lua) | 64 |
| [DoSolfachord Coolia](/examples/cards/80776622) | `80776622` | [Scripts/c80776622.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c80776622.lua) | 61 |
| Theia, the Primal Being | `85687952` | [Scripts/c85687952.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c85687952.lua) | 56 |
| Galaxy-Eyes Photon Dragon | `93717133` | [Scripts/c93717133.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93717133.lua) | 56 |
| Raviel, Lord of Phantasms - Shimmering Scraper | `28651380` | [Scripts/c28651380.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c28651380.lua) | 51 |
| Dark Creator | `52768390` | [Scripts/c52768390.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c52768390.lua) | 51 |
| Supreme King Dragon Odd-Eyes | `96733134` | [Scripts/c96733134.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c96733134.lua) | 50 |
| The Bystial Alba Los | `69120785` | [Scripts/c69120785.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c69120785.lua) | 50 |
| Shooting Star Dragon T.G. EX | `63180841` | [Scripts/c63180841.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63180841.lua) | 49 |
| Vampire Voivode | `4918855` | [Scripts/c4918855.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c4918855.lua) | 49 |
| Duke Shade, the Sinister Shadow Lord | `12766474` | [Scripts/c12766474.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c12766474.lua) | 48 |
| Destiny HERO - Plasma | `83965310` | [Scripts/c83965310.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c83965310.lua) | 46 |
| Aron, the Ogdoadic King | `34172284` | [Scripts/c34172284.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c34172284.lua) | 45 |
| Master Peace, the True Dracoslayer | `34079868` | [Scripts/c34079868.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c34079868.lua) | 44 |
| Amunessia, the Ogdoadic Queen | `61160289` | [Scripts/c61160289.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c61160289.lua) | 44 |
| Citadel Whale | `46290741` | [Scripts/c46290741.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c46290741.lua) | 44 |
| Trias Hierarchia | `26866984` | [Scripts/c26866984.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c26866984.lua) | 44 |
| Raviel, Lord of Phantasms | `69890967` | [Scripts/c69890967.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c69890967.lua) | 44 |
| King Beast Barbaros | `63972571` | [Scripts/c63972571.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63972571.lua) | 43 |
| Keurse, the Ogdoadic Light | `62383431` | [Scripts/c62383431.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c62383431.lua) | 42 |
| Ice Master | `32750510` | [Scripts/c32750510.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c32750510.lua) | 42 |
| Evil★Twins Ki-sikil &amp; Lil-la | `62098216` | [Scripts/c62098216.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c62098216.lua) | 41 |
| Stardust Synchron | `37799519` | [Scripts/c37799519.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c37799519.lua) | 41 |
| Aleirtt, the Ogdoadic Dark | `98787535` | [Scripts/c98787535.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c98787535.lua) | 41 |
| ...and 19 more |  |  |  |

## Script Examples

### Odd-Eyes Revolution Dragon (`16306932`)

Source: [Scripts/c16306932.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c16306932.lua)

```lua
	local tp=c:GetControler()
	local g=Duel.GetReleaseGroup(tp,false,REASON_SPSUMMON):Filter(Card.IsRace,nil,RACE_DRAGON)
	return g:CheckSubGroupEach(c16306932.spchecks,aux.mzctcheckrel,tp,REASON_SPSUMMON)
end
function c16306932.hsptg(e,tp,eg,ep,ev,re,r,rp,chk,c)
```

### DoSolfachord Coolia (`80776622`)

Source: [Scripts/c80776622.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c80776622.lua)

```lua
	local tp=c:GetControler()
	local rg=Duel.GetReleaseGroup(tp,false,REASON_SPSUMMON):Filter(c80776622.rfilter,nil,tp)
	return rg:CheckSubGroup(aux.mzctcheckrel,2,2,tp,REASON_SPSUMMON)
end
function c80776622.sptg(e,tp,eg,ep,ev,re,r,rp,chk,c)
```

### Theia, the Primal Being (`85687952`)

Source: [Scripts/c85687952.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c85687952.lua)

```lua
function s.relgoal(sg,tp)
	Duel.SetSelectedCard(sg)
	return sg:CheckWithSumGreater(Card.GetLevel,11) and aux.mzctcheckrel(sg,tp)
end
function s.spcon(e,tp,eg,ep,ev,re,r,rp)
```
