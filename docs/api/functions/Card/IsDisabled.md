# Card.IsDisabled

## Signature

```lua
Card.IsDisabled(Card c) -> bool
```

## Description

Checks whether c currently has STATUS_DISABLED.

## Parameters

- `c` `Card`

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3625`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **52** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Card.IsDisabled) with `Card.IsDisabled`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Trickstar Light Stage | `35371948` | [Scripts/c35371948.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c35371948.lua) | 2 |
| Trickstar Light Arena | `63492244` | [Scripts/c63492244.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63492244.lua) | 2 |
| Relinquished Fusion | `78063197` | [Scripts/c78063197.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c78063197.lua) | 1 |
| Meklord Astro Mekanikle | `63468625` | [Scripts/c63468625.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63468625.lua) | 1 |
| Union Activation | `38527680` | [Scripts/c38527680.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c38527680.lua) | 1 |
| Quick Summon | `10086952` | [Scripts/c10086952.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c10086952.lua) | 1 |
| Dragunity Arma Leyvaten | `63487632` | [Scripts/c63487632.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63487632.lua) | 1 |
| Groza, Tyrant of Thunder | `45420955` | [Scripts/c45420955.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c45420955.lua) | 1 |
| S-Force Justify | `35334193` | [Scripts/c35334193.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c35334193.lua) | 1 |
| Reversal Box | `2606417` | [Scripts/c2606417.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c2606417.lua) | 1 |
| Meklord Emperor Granel | `4545683` | [Scripts/c4545683.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c4545683.lua) | 1 |
| DoomZ Command "D.O.O.M.D.U.R.G." | `68831625` | [Scripts/c68831625.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c68831625.lua) | 1 |
| Goblin Freefall Squad | `85123771` | [Scripts/c85123771.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c85123771.lua) | 1 |
| Spell Chronicle | `74402414` | [Scripts/c74402414.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74402414.lua) | 1 |
| The Iris Swordsoul | `62849088` | [Scripts/c62849088.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c62849088.lua) | 1 |
| Gold Pride - Pin Baller | `28497830` | [Scripts/c28497830.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c28497830.lua) | 1 |
| Reincarnation Unveiling Mail | `68663427` | [Scripts/c68663427.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c68663427.lua) | 1 |
| Ghostrick or Treat | `27170599` | [Scripts/c27170599.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c27170599.lua) | 1 |
| Inzektor Hopper | `52601736` | [Scripts/c52601736.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c52601736.lua) | 1 |
| Number 3: Cicada King | `4997565` | [Scripts/c4997565.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c4997565.lua) | 1 |
| Vampire Vamp | `82962242` | [Scripts/c82962242.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c82962242.lua) | 1 |
| Deus X-Krawler | `62587693` | [Scripts/c62587693.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c62587693.lua) | 1 |
| Dragunity Arma Mystletainn | `876330` | [Scripts/c876330.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c876330.lua) | 1 |
| Interdimensional Matter Forwarder | `60238002` | [Scripts/c60238002.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c60238002.lua) | 1 |
| ...and 28 more |  |  |  |

## Script Examples

### Trickstar Light Stage (`35371948`)

Source: [Scripts/c35371948.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c35371948.lua)

```lua
	if tc:GetFlagEffectLabel(35371948)==e:GetLabel()
		and c:GetFlagEffectLabel(35371948)==e:GetLabel() then
		return not c:IsDisabled()
	else
		e:Reset()
```

### Trickstar Light Arena (`63492244`)

Source: [Scripts/c63492244.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63492244.lua)

```lua
	if tc:GetFlagEffectLabel(63492244)==e:GetLabel()
		and c:GetFlagEffectLabel(63492244)==e:GetLabel() then
		return not c:IsDisabled()
	else
		e:Reset()
```

### Relinquished Fusion (`78063197`)

Source: [Scripts/c78063197.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c78063197.lua)

```lua
	local m=_G["c"..c:GetCode()]
	return m and c:IsFaceup() and ((c:IsSetCard(0x1110) and c:IsType(TYPE_FUSION)) or c:IsCode(64631466))
		and not c:IsDisabled() and m.can_equip_monster and m.can_equip_monster(c)
end
function c78063197.eqtg(e,tp,eg,ep,ev,re,r,rp,chk,chkc)
```
