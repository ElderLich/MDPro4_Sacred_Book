# Card.GetMaterial

## Signature

```lua
Card.GetMaterial(Card c) -> Group
```

## Description

Returns a Group containing the cards currently stored as c's material cards.

## Parameters

- `c` `Card` - Card whose stored material list is being read.

## Returns

- `Group` - New Group containing c's stored material cards; the Group is empty if no material cards are stored.

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3570`

## Guided Examples

Learn how to use this function in context:

- [Link Procedure Guide](/learn/link-procedure)
- [Tribute Summon Materials](/learn/tribute-summon-materials)

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **215** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Card.GetMaterial) with `Card.GetMaterial`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Ultra Polymerization](/examples/cards/76647978) | `76647978` | [Scripts/c76647978.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c76647978.lua) | 2 |
| [Destratification Dino Stratiae](/examples/cards/3841104) | `3841104` | [Scripts/c3841104.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c3841104.lua) | 1 |
| Particle Fusion | `39261576` | [Scripts/c39261576.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c39261576.lua) | 1 |
| Ostinato | `9113513` | [Scripts/c9113513.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c9113513.lua) | 1 |
| Magikey Dragon - Andrabime | `71159974` | [Scripts/c71159974.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c71159974.lua) | 1 |
| S:P Little Knight | `29301450` | [Scripts/c29301450.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c29301450.lua) | 1 |
| Dracotail Arthalion | `33760966` | [Scripts/c33760966.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c33760966.lua) | 1 |
| Hi-Speedroid Cork Shooter | `23361526` | [Scripts/c23361526.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c23361526.lua) | 2 |
| X-Saber Pellina | `9978697` | [Scripts/c9978697.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c9978697.lua) | 1 |
| Odd-Eyes Rebellion Dragon Overlord | `98452268` | [Scripts/c98452268.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c98452268.lua) | 1 |
| Nirvana High Paladin | `80896940` | [Scripts/c80896940.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c80896940.lua) | 1 |
| Dual Avatar - Manifested A-Un | `28798938` | [Scripts/c28798938.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c28798938.lua) | 1 |
| Genex Ally Triforce | `52709508` | [Scripts/c52709508.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c52709508.lua) | 1 |
| Genex Ally Triarm | `17760003` | [Scripts/c17760003.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c17760003.lua) | 1 |
| Metaltron XII, the True Dracombatant | `57761191` | [Scripts/c57761191.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c57761191.lua) | 1 |
| Cupid Pitch | `21915012` | [Scripts/c21915012.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c21915012.lua) | 1 |
| Kewl Tune Remix | `88170262` | [Scripts/c88170262.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c88170262.lua) | 1 |
| Salamangreat Blaze Dragon | `9608555` | [Scripts/c9608555.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c9608555.lua) | 1 |
| Borrelcode Dragon | `67288539` | [Scripts/c67288539.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c67288539.lua) | 1 |
| Crystron Halqifibrax Prism | `65400671` | [Scripts/c65400671.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c65400671.lua) | 1 |
| Salamangreat Raging Phoenix | `57134592` | [Scripts/c57134592.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c57134592.lua) | 1 |
| Salamangreat Sunlight Wolf | `87871125` | [Scripts/c87871125.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c87871125.lua) | 1 |
| Dual Avatar Feet - Armored Un-Gyo | `7631534` | [Scripts/c7631534.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c7631534.lua) | 1 |
| Kewl Tune B2B | `65961304` | [Scripts/c65961304.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c65961304.lua) | 1 |
| ...and 191 more |  |  |  |

## Script Examples

### Ultra Polymerization (`76647978`)

Source: [Scripts/c76647978.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c76647978.lua)

```lua
function c76647978.spfilter(c,e,tp)
	if c:IsFaceup() and c:GetFlagEffect(76647978)~=0 and c==e:GetLabelObject() then
		local mg=c:GetMaterial()
		local ct=mg:GetCount()
		return ct>0 and ct<=Duel.GetLocationCount(tp,LOCATION_MZONE)
```

### Destratification Dino Stratiae (`3841104`)

Source: [Scripts/c3841104.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c3841104.lua)

```lua
end
function s.valcheck(e,c)
	local g=c:GetMaterial()
	local atk=0
	for tc in aux.Next(g) do
```

### Particle Fusion (`39261576`)

Source: [Scripts/c39261576.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c39261576.lua)

```lua
function c39261576.atktg(e,tp,eg,ep,ev,re,r,rp,chk,chkc)
	local tc=eg:GetFirst()
	local mat=tc:GetMaterial()
	if chkc then return chkc:IsSetCard(0x1047) and mat:IsContains(chkc) end
	if chk==0 then return mat:IsExists(Card.IsSetCard,1,nil,0x1047) end
```
