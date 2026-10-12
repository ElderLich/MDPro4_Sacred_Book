# Duel.GetFirstMatchingCard

## Signature

```lua
Duel.GetFirstMatchingCard([function|nil f], int player, int s, int o, [Card|Group|nil ex], [... any]) -> Card|nil
```

## Description

Returns the first card in the specified locations that satisfies f and is not excluded by ex.
f may be nil. ex may be a Card, a Group, or nil, and extra arguments after ex are passed to f. Returns nil when no matching card is found.

## Parameters

- `f` `function|nil` optional
- `player` `int`
- `s` `int`
- `o` `int`
- `ex` `Card|Group|nil` optional
- `...` `any` optional

## Returns

- `Card|nil`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4971`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **85** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Duel.GetFirstMatchingCard) with `Duel.GetFirstMatchingCard`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| D/D/D Deviser King Deus Machinex | `46593546` | [Scripts/c46593546.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c46593546.lua) | 2 |
| Scrap-Iron Sacred Statue | `85520170` | [Scripts/c85520170.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c85520170.lua) | 1 |
| Majesty Pegasus, the Dracoslayer | `92332424` | [Scripts/c92332424.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c92332424.lua) | 2 |
| Charming Resort Staff | `64753157` | [Scripts/c64753157.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c64753157.lua) | 1 |
| Yosenju Oroshi Channeling | `61884774` | [Scripts/c61884774.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c61884774.lua) | 2 |
| Synchro Overtop | `653675` | [Scripts/c653675.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c653675.lua) | 1 |
| Synchro World | `36742774` | [Scripts/c36742774.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c36742774.lua) | 1 |
| Super Quantal Alphan Spike | `72332074` | [Scripts/c72332074.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c72332074.lua) | 1 |
| Imsety, Glory of Horus | `84941194` | [Scripts/c84941194.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c84941194.lua) | 1 |
| Number 53: Heart-eartH | `23998625` | [Scripts/c23998625.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c23998625.lua) | 1 |
| Advanced Crystal Beast Cobalt Eagle | `45236142` | [Scripts/c45236142.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c45236142.lua) | 1 |
| Abyss Actor - Wild Hope | `51391183` | [Scripts/c51391183.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c51391183.lua) | 1 |
| Performage Shadow Maker | `69655484` | [Scripts/c69655484.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c69655484.lua) | 1 |
| Performapal Odd-Eyes Light Phoenix | `59762399` | [Scripts/c59762399.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c59762399.lua) | 2 |
| Ahrima, the Wicked Warden | `86377375` | [Scripts/c86377375.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c86377375.lua) | 1 |
| The Earth - Hex-Sealed Fusion | `88696724` | [Scripts/c88696724.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c88696724.lua) | 1 |
| The Light - Hex-Sealed Fusion | `15717011` | [Scripts/c15717011.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c15717011.lua) | 1 |
| The Dark - Hex-Sealed Fusion | `52101615` | [Scripts/c52101615.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c52101615.lua) | 1 |
| Aleister the Invoker | `86120751` | [Scripts/c86120751.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c86120751.lua) | 1 |
| Tindangle Trinity | `11375683` | [Scripts/c11375683.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c11375683.lua) | 1 |
| Euler's Circuit | `9547962` | [Scripts/c9547962.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c9547962.lua) | 1 |
| Vampire Takeover | `22900598` | [Scripts/c22900598.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c22900598.lua) | 1 |
| Dragunity Remus | `26577155` | [Scripts/c26577155.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c26577155.lua) | 1 |
| Wightprincess | `90243945` | [Scripts/c90243945.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c90243945.lua) | 1 |
| ...and 61 more |  |  |  |

## Script Examples

### D/D/D Deviser King Deus Machinex (`46593546`)

Source: [Scripts/c46593546.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c46593546.lua)

```lua
	if chkc then return chkc:IsControler(tp) and chkc:IsLocation(LOCATION_MZONE+LOCATION_GRAVE) and c46593546.sptgfilter(chkc) end
	local c=e:GetHandler()
	local tc=Duel.GetFirstMatchingCard(nil,tp,LOCATION_PZONE,0,c)
	if chk==0 then return tc and Duel.GetMZoneCount(tp)>0 and tc:IsCanBeSpecialSummoned(e,0,tp,false,false)
		and Duel.IsExistingTarget(c46593546.sptgfilter,tp,LOCATION_MZONE+LOCATION_GRAVE,0,1,nil) end
```

### Scrap-Iron Sacred Statue (`85520170`)

Source: [Scripts/c85520170.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c85520170.lua)

```lua
end
function s.spop(e,tp,eg,ep,ev,re,r,rp)
	local tg=Duel.GetFirstMatchingCard(s.spfilter,tp,LOCATION_EXTRA,0,nil,e,tp)
	if tg then
		Duel.SpecialSummon(tg,0,tp,tp,false,false,POS_FACEUP)
```

### Majesty Pegasus, the Dracoslayer (`92332424`)

Source: [Scripts/c92332424.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c92332424.lua)

```lua
function c92332424.srtg(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then
		local oc=Duel.GetFirstMatchingCard(nil,tp,LOCATION_PZONE,0,e:GetHandler())
		return Duel.IsExistingMatchingCard(c92332424.srfilter,tp,LOCATION_DECK,0,1,nil,oc)
	end
```
