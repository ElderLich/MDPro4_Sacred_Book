# Duel.IsPlayerCanSpecialSummon

## Signature

```lua
Duel.IsPlayerCanSpecialSummon(int player, [int sumtype], [int sumpos], [int target_player], [Card c]) -> bool
```

## Description

With only player, checks whether player is allowed to perform a Special Summon and still has Special Summon count available.
With the optional card-specific arguments, checks whether player can Special Summon c to target_player in sumpos with sumtype, using the current reason effect.

## Parameters

- `player` `int`
- `sumtype` `int` optional
- `sumpos` `int` optional
- `target_player` `int` optional
- `c` `Card` optional

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5050`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **28** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Duel.IsPlayerCanSpecialSummon) with `Duel.IsPlayerCanSpecialSummon`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Yummy★Snatchy](/examples/cards/30581601) | `30581601` | [Scripts/c30581601.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30581601.lua) | 1 |
| Saiba the Soldier Swordsmith | `36608728` | [Scripts/c36608728.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c36608728.lua) | 1 |
| Naturia Blessing | `34813545` | [Scripts/c34813545.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c34813545.lua) | 1 |
| Masterking Archfiend | `35606858` | [Scripts/c35606858.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c35606858.lua) | 1 |
| Stand Up Centur-Ion! | `41371602` | [Scripts/c41371602.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c41371602.lua) | 1 |
| Super Koi Koi | `66171432` | [Scripts/c66171432.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c66171432.lua) | 1 |
| Re-dyce-cle | `85704698` | [Scripts/c85704698.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c85704698.lua) | 1 |
| Destined Duel | `48128081` | [Scripts/c48128081.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c48128081.lua) | 1 |
| The Kaiju Files | `11163040` | [Scripts/c11163040.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c11163040.lua) | 1 |
| Interrupted Kaiju Slumber | `99330325` | [Scripts/c99330325.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c99330325.lua) | 2 |
| Super Quantal Alphan Spike | `72332074` | [Scripts/c72332074.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c72332074.lua) | 1 |
| Etude of the Branded | `45675980` | [Scripts/c45675980.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c45675980.lua) | 1 |
| Crystal Boon | `85766789` | [Scripts/c85766789.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c85766789.lua) | 1 |
| Transforming Sphere | `66094973` | [Scripts/c66094973.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c66094973.lua) | 1 |
| Dark Magical Curtain | `41350417` | [Scripts/c41350417.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c41350417.lua) | 1 |
| Mimikuril | `74879881` | [Scripts/c74879881.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74879881.lua) | 1 |
| Gunkan Suship Ikura | `61027400` | [Scripts/c61027400.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c61027400.lua) | 1 |
| Yang Zing Unleashed | `77783947` | [Scripts/c77783947.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c77783947.lua) | 1 |
| Monster Gate | `43040603` | [Scripts/c43040603.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c43040603.lua) | 2 |
| Last Turn | `28566710` | [Scripts/c28566710.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c28566710.lua) | 1 |
| Lullaby of Obedience | `39238953` | [Scripts/c39238953.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c39238953.lua) | 1 |
| Cynet Storm | `42461852` | [Scripts/c42461852.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c42461852.lua) | 2 |
| Illusion Balloons | `62161698` | [Scripts/c62161698.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c62161698.lua) | 1 |
| One or Eight | `74202664` | [Scripts/c74202664.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74202664.lua) | 1 |
| ...and 4 more |  |  |  |

## Script Examples

### Yummy★Snatchy (`30581601`)

Source: [Scripts/c30581601.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30581601.lua)

```lua
function s.sctg(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then
		if not Duel.IsPlayerCanSpecialSummon(tp) then return false end
		local mg=Duel.GetSynchroMaterial(tp)
		if mg:IsExists(Card.GetHandSynchro,1,nil) then
```

### Saiba the Soldier Swordsmith (`36608728`)

Source: [Scripts/c36608728.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c36608728.lua)

```lua
function s.sctg(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then
		if not Duel.IsPlayerCanSpecialSummon(tp) then return false end
		local mg=Duel.GetSynchroMaterial(tp)
		if mg:IsExists(Card.GetHandSynchro,1,nil) then
```

### Naturia Blessing (`34813545`)

Source: [Scripts/c34813545.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c34813545.lua)

```lua
function c34813545.sctg(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then
		if not Duel.IsPlayerCanSpecialSummon(tp) then return false end
		local mg=Duel.GetSynchroMaterial(tp)
		if mg:IsExists(Card.GetHandSynchro,1,nil) then
```
