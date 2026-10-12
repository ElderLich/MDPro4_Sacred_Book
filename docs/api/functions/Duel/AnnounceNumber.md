# Duel.AnnounceNumber

## Signature

```lua
Duel.AnnounceNumber(int player, int number1, [int number2], [... int]) -> int,int
```

## Description

Lets player choose one of the supplied numbers.
Returns the selected number and the core's 0-based option index for that number.

## Parameters

- `player` `int`
- `number1` `int`
- `number2` `int` optional
- `...` `int` optional

## Returns

- `int` - Selected number.
- `int` - 0-based option index selected by the core.

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5034`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **82** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Duel.AnnounceNumber) with `Duel.AnnounceNumber`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Chef de Nouvelles | `29251488` | [Scripts/c29251488.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c29251488.lua) | 1 |
| Isolde, Two Tales of the Noble Knights | `59934749` | [Scripts/c59934749.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c59934749.lua) | 1 |
| Mixeroid | `71340250` | [Scripts/c71340250.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c71340250.lua) | 1 |
| Phantom Knights' Rank-Up-Magic Force | `88504133` | [Scripts/c88504133.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c88504133.lua) | 1 |
| Miscellaneousaurus | `38572779` | [Scripts/c38572779.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c38572779.lua) | 1 |
| Magellanica, the Deep Sea City | `26534688` | [Scripts/c26534688.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c26534688.lua) | 1 |
| Sylvan Dancepione | `21903613` | [Scripts/c21903613.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c21903613.lua) | 1 |
| Sleepy Scapegoats | `3129527` | [Scripts/c3129527.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c3129527.lua) | 1 |
| Witchcrafter Masterpiece | `55072170` | [Scripts/c55072170.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c55072170.lua) | 1 |
| Gagaga Utopic Tactics | `75956913` | [Scripts/c75956913.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c75956913.lua) | 1 |
| Token Support | `53545926` | [Scripts/c53545926.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c53545926.lua) | 1 |
| Dawn Angel Kambi | `12500059` | [Scripts/c12500059.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c12500059.lua) | 1 |
| Reversal Box | `2606417` | [Scripts/c2606417.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c2606417.lua) | 1 |
| Galaxy Photon Dragon | `85747929` | [Scripts/c85747929.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c85747929.lua) | 1 |
| Zexal Catapult | `95664204` | [Scripts/c95664204.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c95664204.lua) | 1 |
| The Agent of Destruction - Venus | `99054885` | [Scripts/c99054885.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c99054885.lua) | 1 |
| Puzzlomino, the Drop-n-Deleter | `84271823` | [Scripts/c84271823.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c84271823.lua) | 1 |
| Shamanite Shamanknight | `16237004` | [Scripts/c16237004.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c16237004.lua) | 1 |
| Cosmic Tree Irmistil | `74139959` | [Scripts/c74139959.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c74139959.lua) | 1 |
| Hollowrokket Dragon | `51548207` | [Scripts/c51548207.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c51548207.lua) | 1 |
| Junk Meister | `73218792` | [Scripts/c73218792.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c73218792.lua) | 1 |
| Mythical Institution | `94599451` | [Scripts/c94599451.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c94599451.lua) | 1 |
| Spell Power Attainment | `39123673` | [Scripts/c39123673.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c39123673.lua) | 1 |
| Division | `42427230` | [Scripts/c42427230.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c42427230.lua) | 1 |
| ...and 58 more |  |  |  |

## Script Examples

### Chef de Nouvelles (`29251488`)

Source: [Scripts/c29251488.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c29251488.lua)

```lua
		local ct={1,2,3}
		Duel.Hint(HINT_SELECTMSG,tp,aux.Stringid(id,5))
		local ac=Duel.AnnounceNumber(tp,table.unpack(ct))
		local e1=Effect.CreateEffect(e:GetHandler())
		e1:SetType(EFFECT_TYPE_SINGLE)
```

### Isolde, Two Tales of the Noble Knights (`59934749`)

Source: [Scripts/c59934749.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c59934749.lua)

```lua
	lvt[pc]=nil
	Duel.Hint(HINT_SELECTMSG,tp,aux.Stringid(59934749,2))
	local lv=Duel.AnnounceNumber(tp,table.unpack(lvt))
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_TOGRAVE)
	aux.GCheckAdditional=aux.dncheck
```

### Mixeroid (`71340250`)

Source: [Scripts/c71340250.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c71340250.lua)

```lua
	lvt[pc]=nil
	Duel.Hint(HINT_SELECTMSG,tp,aux.Stringid(71340250,2))
	local lv=Duel.AnnounceNumber(tp,table.unpack(lvt))
	local rg1=Group.CreateGroup()
	if lv>1 then
```
