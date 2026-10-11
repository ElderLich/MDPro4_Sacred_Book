# Duel.TossDice

## Signature

```lua
Duel.TossDice(int player, int count1, [int count2]) -> int,...?
```

## Description

Tosses count1 dice for player and, when count2 is supplied, count2 dice for the opponent.
Valid dice results are integers from 1 to 6. Normal script use should keep count1 + count2 at 5 or less; the core rejects count1 &lt;= 0 and count2 &lt; 0.

## Parameters

- `player` `int`
- `count1` `int`
- `count2` `int` optional - default: 0

## Returns

- `int` - First die result.
- `...?` - Additional die results.

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5037`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **61** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Duel.TossDice) with `Duel.TossDice`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Masterking Archfiend | `35606858` | [Scripts/c35606858.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c35606858.lua) | 1 |
| Reversal Box | `2606417` | [Scripts/c2606417.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c2606417.lua) | 1 |
| Hi-Speedroid Clear Wing Rider | `86154370` | [Scripts/c86154370.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c86154370.lua) | 1 |
| Re-dyce-cle | `85704698` | [Scripts/c85704698.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c85704698.lua) | 1 |
| Time Magic Hammer | `10960419` | [Scripts/c10960419.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c10960419.lua) | 1 |
| Astra Ghouls | `69170403` | [Scripts/c69170403.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c69170403.lua) | 1 |
| Evil Lord - Zorc | `73320394` | [Scripts/c73320394.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c73320394.lua) | 1 |
| Shateki | `5574510` | [Scripts/c5574510.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c5574510.lua) | 1 |
| Vaylantz Mad Marquess | `87897777` | [Scripts/c87897777.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c87897777.lua) | 2 |
| Graceful &amp; Skull Dice | `76630812` | [Scripts/c76630812.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c76630812.lua) | 2 |
| Morphtronic Smartfon | `15521027` | [Scripts/c15521027.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c15521027.lua) | 2 |
| Desrook Archfiend | `72192100` | [Scripts/c72192100.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c72192100.lua) | 1 |
| Thunder Ball | `84813516` | [Scripts/c84813516.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c84813516.lua) | 1 |
| Morphtronic Telefon | `38082437` | [Scripts/c38082437.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c38082437.lua) | 2 |
| Speedroid Wheel | `12148078` | [Scripts/c12148078.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c12148078.lua) | 1 |
| Terrorking Archfiend | `35975813` | [Scripts/c35975813.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c35975813.lua) | 1 |
| Number 7: Lucky Straight | `82308875` | [Scripts/c82308875.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c82308875.lua) | 1 |
| Infernalqueen Archfiend | `8581705` | [Scripts/c8581705.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c8581705.lua) | 1 |
| Number 67: Pair-a-Dice Smasher | `35772782` | [Scripts/c35772782.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c35772782.lua) | 1 |
| First Striker Advantage | `58995660` | [Scripts/c58995660.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c58995660.lua) | 1 |
| Musical Sumo Dice Games | `96637156` | [Scripts/c96637156.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c96637156.lua) | 1 |
| Number 85: Crazy Box | `42421606` | [Scripts/c42421606.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c42421606.lua) | 1 |
| Roulette Spider | `36708764` | [Scripts/c36708764.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c36708764.lua) | 1 |
| Dice Dungeon | `11808215` | [Scripts/c11808215.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c11808215.lua) | 1 |
| ...and 37 more |  |  |  |

## Script Examples

### Masterking Archfiend (`35606858`)

Source: [Scripts/c35606858.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c35606858.lua)

```lua
end
function c35606858.dcop(e,tp,eg,ep,ev,re,r,rp)
	local d=Duel.TossDice(tp,1)
	local g=eg:Filter(aux.NecroValleyFilter(c35606858.cfilter),nil,e,tp)
	if g:GetCount()==0 then return end
```

### Reversal Box (`2606417`)

Source: [Scripts/c2606417.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c2606417.lua)

```lua
function s.ctop(e,tp,eg,ep,ev,re,r,rp)
	local c=e:GetHandler()
	local ct=Duel.TossDice(tp,1)
	if c:GetCounter(0x76)+ct>6 then ct=6-c:GetCounter(0x76) end
	if ct>0 then
```

### Hi-Speedroid Clear Wing Rider (`86154370`)

Source: [Scripts/c86154370.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c86154370.lua)

```lua
function c86154370.desop(e,tp,eg,ep,ev,re,r,rp)
	local c=e:GetHandler()
	local dc=Duel.TossDice(tp,1)
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_TODECK)
	local gy=Duel.SelectMatchingCard(tp,c86154370.gyfilter,tp,LOCATION_GRAVE,0,1,dc,nil)
```
