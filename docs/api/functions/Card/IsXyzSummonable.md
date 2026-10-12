# Card.IsXyzSummonable

## Signature

```lua
Card.IsXyzSummonable(Card c, [Group|nil materials], [int minc], [int maxc]) -> bool
```

## Description

Checks whether Xyz Monster c can be Xyz Summoned by the current reason player with an optional material group and min/max constraints.
Use this in effect target and operation branches before calling Duel.XyzSummon. minc and maxc default to 0 when omitted, leaving the registered procedure's own count rules in control.
The core rejects this check during the Damage Step.

## Parameters

- `c` `Card` - Xyz Monster being tested.
- `materials` `Group|nil` optional - Optional material pool or exact material group supplied by the effect.
- `minc` `int` optional - Optional minimum material count override. Defaults to 0.
- `maxc` `int` optional - Optional maximum material count override. Defaults to 0.

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3632`

## Guided Examples

Learn how to use this function in context:

- [Xyz Procedure Guide](/learn/xyz-procedure)

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **32** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Card.IsXyzSummonable) with `Card.IsXyzSummonable`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Barian's Chaos Draw](/examples/cards/97769122) | `97769122` | [Scripts/c97769122.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c97769122.lua) | 2 |
| [Bujinki Ahashima](/examples/cards/71095768) | `71095768` | [Scripts/c71095768.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c71095768.lua) | 2 |
| Supreme King Dragon Lightwurm | `41908872` | [Scripts/c41908872.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c41908872.lua) | 1 |
| Gagaga Girl - Cell Phone Subtraction | `48393693` | [Scripts/c48393693.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c48393693.lua) | 2 |
| Salamangreat Zebroid X | `44161893` | [Scripts/c44161893.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c44161893.lua) | 1 |
| Fire King Sanctuary | `65305978` | [Scripts/c65305978.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c65305978.lua) | 1 |
| Chronomaly Esperanza Glyph | `50797682` | [Scripts/c50797682.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c50797682.lua) | 2 |
| Raise Moon Wings Rapi | `47828069` | [Scripts/c47828069.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c47828069.lua) | 1 |
| Numbers Last Hope | `4606229` | [Scripts/c4606229.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c4606229.lua) | 2 |
| Mathmech Superfactorial | `87804365` | [Scripts/c87804365.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c87804365.lua) | 1 |
| Gazer Shark | `23536866` | [Scripts/c23536866.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c23536866.lua) | 2 |
| Shining Hope Road | `62829077` | [Scripts/c62829077.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c62829077.lua) | 2 |
| Magicolloidal Sol | `67694706` | [Scripts/c67694706.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c67694706.lua) | 1 |
| Magikey Locking | `40493210` | [Scripts/c40493210.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c40493210.lua) | 1 |
| Ryzeal Plasma Hole | `33787730` | [Scripts/c33787730.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c33787730.lua) | 1 |
| Exosister Returnia | `197042` | [Scripts/c197042.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c197042.lua) | 1 |
| Reincarnation Unveiling Mail | `68663427` | [Scripts/c68663427.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c68663427.lua) | 1 |
| Artifacts Unleashed | `56611470` | [Scripts/c56611470.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c56611470.lua) | 2 |
| Hublot the Dark Directory of Death | `29081251` | [Scripts/c29081251.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c29081251.lua) | 1 |
| The Phantom Knights of Umbrage Veil | `85257384` | [Scripts/c85257384.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c85257384.lua) | 1 |
| Full-Armored Xyz | `39733924` | [Scripts/c39733924.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c39733924.lua) | 1 |
| Here There Be Dragons | `4575541` | [Scripts/c4575541.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c4575541.lua) | 1 |
| Pendulum Xyz | `46005939` | [Scripts/c46005939.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c46005939.lua) | 2 |
| K9-ØØ Lupis | `91025875` | [Scripts/c91025875.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c91025875.lua) | 1 |
| ...and 8 more |  |  |  |

## Script Examples

### Barian's Chaos Draw (`97769122`)

Source: [Scripts/c97769122.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c97769122.lua)

```lua
end
function c97769122.xyzfilter(c,mg)
	return c:IsSetCard(0x48) and c:IsXyzSummonable(mg,#mg,#mg)
end
function c97769122.xyztg(e,tp,eg,ep,ev,re,r,rp,chk)
```

### Bujinki Ahashima (`71095768`)

Source: [Scripts/c71095768.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c71095768.lua)

```lua
function c71095768.fselect(g,tp)
	return g:GetClassCount(Card.GetLocation)==g:GetCount() and g:GetClassCount(Card.GetLevel)==1
		and Duel.IsExistingMatchingCard(Card.IsXyzSummonable,tp,LOCATION_EXTRA,0,1,nil,g,2,2)
end
function c71095768.sptg(e,tp,eg,ep,ev,re,r,rp,chk)
```

### Supreme King Dragon Lightwurm (`41908872`)

Source: [Scripts/c41908872.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c41908872.lua)

```lua
end
function c41908872.xyzfilter(c)
	return c:IsSetCard(0x20f8) and c:IsXyzSummonable(nil)
end
function c41908872.thop1(e,tp,eg,ep,ev,re,r,rp)
```
