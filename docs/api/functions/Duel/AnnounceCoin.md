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

- Detected in **16** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Duel.AnnounceCoin`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Goddess of the Two Sides | `50915474` | [Scripts/c50915474.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c50915474.lua) | 1 |
| VIP Whale | `14556954` | [Scripts/c14556954.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c14556954.lua) | 1 |
| Time Wizard of Tomorrow | `26273196` | [Scripts/c26273196.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c26273196.lua) | 1 |
| Prepare to Strike Back | `4483989` | [Scripts/c4483989.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c4483989.lua) | 1 |
| Lucky Chance | `96012004` | [Scripts/c96012004.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c96012004.lua) | 1 |
| Head Judging | `38143903` | [Scripts/c38143903.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c38143903.lua) | 1 |
| Fairy Box | `21598948` | [Scripts/c21598948.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c21598948.lua) | 1 |
| Time Wizard | `71625222` | [Scripts/c71625222.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c71625222.lua) | 1 |
| Kryuel | `82642348` | [Scripts/c82642348.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c82642348.lua) | 1 |
| Goddess of Whim | `67959180` | [Scripts/c67959180.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c67959180.lua) | 1 |
| B.E.S. Covered Core | `15317640` | [Scripts/c15317640.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c15317640.lua) | 1 |
| Gamble | `37313786` | [Scripts/c37313786.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c37313786.lua) | 1 |
| Sasuke Samurai #4 | `64538655` | [Scripts/c64538655.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c64538655.lua) | 1 |
| Fiend Comedian | `81172176` | [Scripts/c81172176.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c81172176.lua) | 1 |
| Abare Ushioni | `89718302` | [Scripts/c89718302.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c89718302.lua) | 1 |
| Jirai Gumo | `94773007` | [Scripts/c94773007.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c94773007.lua) | 1 |

## Script Examples

### Goddess of the Two Sides (`50915474`)

Source: [Scripts/c50915474.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c50915474.lua)

```lua
function s.atkop(e,tp,eg,ep,ev,re,r,rp)
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_COIN)
	local coin=Duel.AnnounceCoin(tp)
	local res=Duel.TossCoin(tp,1)
	if coin~=res then
```

### VIP Whale (`14556954`)

Source: [Scripts/c14556954.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c14556954.lua)

```lua
	local c=e:GetHandler()
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_COIN)
	local coin=Duel.AnnounceCoin(tp)
	local res=Duel.TossCoin(tp,1)
	if coin~=res then
```

### Time Wizard of Tomorrow (`26273196`)

Source: [Scripts/c26273196.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c26273196.lua)

```lua
	if g:GetCount()>0 then
		Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_COIN)
		local coin=Duel.AnnounceCoin(tp)
		local res=Duel.TossCoin(tp,1)
		local damp=0
```
