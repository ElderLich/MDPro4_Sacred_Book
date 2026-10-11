# Duel.GetFieldCard

## Signature

```lua
Duel.GetFieldCard(int player, int location, int sequence) -> Card|nil
```

## Description

Returns the card at player, location, and sequence, or nil if that slot is empty or invalid.
The binding also returns nil while the card at that slot is in Summoning or Special Summon step status. Field Zone sequence 0 maps to the Field Zone, and Pendulum Zone sequences 0 and 1 only return cards currently marked as Pendulum Zone cards.

## Parameters

- `player` `int`
- `location` `int`
- `sequence` `int`

## Returns

- `Card|nil`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4943`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **75** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Duel.GetFieldCard) with `Duel.GetFieldCard`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Pendulum Evolution](/examples/cards/55795155) | `55795155` | [Scripts/c55795155.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c55795155.lua) | 4 |
| [El Shaddoll Apkallone](/examples/cards/50907446) | `50907446` | [Scripts/c50907446.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c50907446.lua) | 2 |
| [Ghostrick Renovation](/examples/cards/61818176) | `61818176` | [Scripts/c61818176.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c61818176.lua) | 1 |
| [Ursarctic Polari](/examples/cards/27693363) | `27693363` | [Scripts/c27693363.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c27693363.lua) | 1 |
| [Camelot, Realm of Noble Knights and Noble Arms](/examples/cards/15635751) | `15635751` | [Scripts/c15635751.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c15635751.lua) | 1 |
| [Yummy★Snatchy](/examples/cards/30581601) | `30581601` | [Scripts/c30581601.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30581601.lua) | 1 |
| El Shaddoll Meshachrer | `32467459` | [Scripts/c32467459.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c32467459.lua) | 2 |
| Sea Stealth Attack | `19089195` | [Scripts/c19089195.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c19089195.lua) | 1 |
| Favorite Hero | `11881272` | [Scripts/c11881272.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c11881272.lua) | 1 |
| Yummy☆Surprise | `29369059` | [Scripts/c29369059.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c29369059.lua) | 1 |
| Triamid Dancer | `69529337` | [Scripts/c69529337.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c69529337.lua) | 1 |
| Odd-Eyes Pendulum Dragon, Four Heavenly Dragons | `75787708` | [Scripts/c75787708.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c75787708.lua) | 2 |
| Fire King Sanctuary | `65305978` | [Scripts/c65305978.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c65305978.lua) | 1 |
| Numeron Wall | `42352091` | [Scripts/c42352091.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c42352091.lua) | 1 |
| Wind Unicorn Parallel, the Dracoslayer | `39016067` | [Scripts/c39016067.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c39016067.lua) | 2 |
| PenduLuMoon | `66150724` | [Scripts/c66150724.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c66150724.lua) | 4 |
| Thousand Umbral Horror | `2932235` | [Scripts/c2932235.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c2932235.lua) | 1 |
| The Sacred Waters in the Sky | `26684111` | [Scripts/c26684111.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c26684111.lua) | 1 |
| Tenyinfinity | `77946022` | [Scripts/c77946022.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c77946022.lua) | 1 |
| Triamid Master | `32912040` | [Scripts/c32912040.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c32912040.lua) | 1 |
| Odd-Eyes Phantasma Dragon | `21770839` | [Scripts/c21770839.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c21770839.lua) | 2 |
| Dream Mirror Recap | `81038234` | [Scripts/c81038234.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c81038234.lua) | 1 |
| Super Quantal Alphan Spike | `72332074` | [Scripts/c72332074.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c72332074.lua) | 1 |
| Enneacraft Reset | `19504025` | [Scripts/c19504025.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c19504025.lua) | 1 |
| ...and 51 more |  |  |  |

## Script Examples

### Pendulum Evolution (`55795155`)

Source: [Scripts/c55795155.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c55795155.lua)

```lua
	if chk==0 then
		local c=e:GetHandler()
		local lpz=Duel.GetFieldCard(tp,LOCATION_PZONE,0)
		local rpz=Duel.GetFieldCard(tp,LOCATION_PZONE,1)
		if lpz==nil or rpz==nil then return false end
```

### El Shaddoll Apkallone (`50907446`)

Source: [Scripts/c50907446.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c50907446.lua)

```lua
	local mg=g:Filter(c50907446.FShaddollFilter,nil,c)
	local tp=e:GetHandlerPlayer()
	local fc=Duel.GetFieldCard(tp,LOCATION_FZONE,0)
	local exg=nil
	if fc and fc:IsHasEffect(81788994) and fc:IsCanRemoveCounter(tp,0x16,3,REASON_EFFECT) then
```

### Ghostrick Renovation (`61818176`)

Source: [Scripts/c61818176.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c61818176.lua)

```lua
end
function c61818176.target(e,tp,eg,ep,ev,re,r,rp,chk,chkc)
	local tc=Duel.GetFieldCard(tp,LOCATION_FZONE,0)
	if chkc then return false end
	if chk==0 then return tc and tc:IsFaceup() and tc:IsSetCard(0x8d) and tc:IsAbleToHand() and tc:IsCanBeEffectTarget(e) end
```
