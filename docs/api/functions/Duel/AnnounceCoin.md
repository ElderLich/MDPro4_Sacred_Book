# Duel.AnnounceCoin

## Signature

```lua
Duel.AnnounceCoin(int player) -> int
```

## Description

Lets player choose one of the built-in coin-side options and returns the zero-based option index.

## Parameters

- `player` `int`

## Returns

- `int` - Zero-based option index.

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5035`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **18** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Duel.AnnounceCoin) with `Duel.AnnounceCoin`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Reversal Box | `2606417` | [Scripts/c2606417.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c2606417.lua) | 1 |
| Dark Time Wizard | `40235813` | [Scripts/c40235813.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c40235813.lua) | 1 |
| Goddess of the Two Sides | `50915474` | [Scripts/c50915474.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c50915474.lua) | 1 |
| VIP Whale | `14556954` | [Scripts/c14556954.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c14556954.lua) | 1 |
| Time Wizard of Tomorrow | `26273196` | [Scripts/c26273196.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c26273196.lua) | 1 |
| Prepare to Strike Back | `4483989` | [Scripts/c4483989.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c4483989.lua) | 1 |
| Lucky Chance | `96012004` | [Scripts/c96012004.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c96012004.lua) | 1 |
| Head Judging | `38143903` | [Scripts/c38143903.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c38143903.lua) | 1 |
| Fairy Box | `21598948` | [Scripts/c21598948.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c21598948.lua) | 1 |
| Time Wizard | `71625222` | [Scripts/c71625222.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c71625222.lua) | 1 |
| Kryuel | `82642348` | [Scripts/c82642348.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c82642348.lua) | 1 |
| Goddess of Whim | `67959180` | [Scripts/c67959180.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c67959180.lua) | 1 |
| B.E.S. Covered Core | `15317640` | [Scripts/c15317640.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c15317640.lua) | 1 |
| Gamble | `37313786` | [Scripts/c37313786.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c37313786.lua) | 1 |
| Sasuke Samurai #4 | `64538655` | [Scripts/c64538655.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c64538655.lua) | 1 |
| Fiend Comedian | `81172176` | [Scripts/c81172176.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c81172176.lua) | 1 |
| Abare Ushioni | `89718302` | [Scripts/c89718302.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c89718302.lua) | 1 |
| Jirai Gumo | `94773007` | [Scripts/c94773007.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c94773007.lua) | 1 |

## Script Examples

### Reversal Box (`2606417`)

Source: [Scripts/c2606417.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c2606417.lua)

```lua
	local tc=Duel.GetFirstTarget()
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_COIN)
	local coin=Duel.AnnounceCoin(tp)
	local res=Duel.TossCoin(tp,1)
	if coin~=res and Duel.GetLocationCount(tp,LOCATION_MZONE)>0 then
```

### Dark Time Wizard (`40235813`)

Source: [Scripts/c40235813.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c40235813.lua)

```lua
		local p=1-tp
		Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_COIN)
		local coin=Duel.AnnounceCoin(tp)
		local res=Duel.TossCoin(tp,1)
		if coin==res then
```

### Goddess of the Two Sides (`50915474`)

Source: [Scripts/c50915474.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c50915474.lua)

```lua
function s.atkop(e,tp,eg,ep,ev,re,r,rp)
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_COIN)
	local coin=Duel.AnnounceCoin(tp)
	local res=Duel.TossCoin(tp,1)
	if coin~=res then
```
