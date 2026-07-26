# Card.IsCanChangePosition

## Signature

```lua
Card.IsCanChangePosition(Card c) -> bool
```

## Description

Checks the core's effect-specific position-change capability for c.
In this MDPro3/YGOPro core, that helper returns false for Link Monsters and true for other cards; it does not perform the broader manual battle-position-change checks.

## Parameters

- `c` `Card`

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3636`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **154** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.IsCanChangePosition`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Power Tool Braver Dragon | `63265554` | [Scripts/c63265554.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63265554.lua) | 58 |
| Mimighoul Maker | `13204145` | [Scripts/c13204145.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c13204145.lua) | 53 |
| Amaze Attraction Thrill Train | `36591747` | [Scripts/c36591747.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c36591747.lua) | 52 |
| Performapal Corn | `33103459` | [Scripts/c33103459.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c33103459.lua) | 51 |
| Arbitration of White | `57964143` | [Scripts/c57964143.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c57964143.lua) | 51 |
| VARefar, the Judge of Ball | `19743887` | [Scripts/c19743887.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c19743887.lua) | 50 |
| Poissonniere de Nouvelles | `46485778` | [Scripts/c46485778.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c46485778.lua) | 49 |
| Epurrely Beauty | `98049934` | [Scripts/c98049934.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c98049934.lua) | 49 |
| Ritual Beast Inheritance | `22501005` | [Scripts/c22501005.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c22501005.lua) | 48 |
| Goblin Freefall Squad | `85123771` | [Scripts/c85123771.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c85123771.lua) | 48 |
| Lancea, Ancestral Dragon of the Ice Mountain | `96402918` | [Scripts/c96402918.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c96402918.lua) | 47 |
| Unchained Malevolent Magistrate Kamura | `68625623` | [Scripts/c68625623.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c68625623.lua) | 47 |
| Cyberse Enchanter | `60279710` | [Scripts/c60279710.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c60279710.lua) | 47 |
| Borrelguard Dragon | `68987122` | [Scripts/c68987122.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c68987122.lua) | 47 |
| Artmage Diactorus | `27184601` | [Scripts/c27184601.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c27184601.lua) | 46 |
| Vanquish Soul Jiaolong | `9091064` | [Scripts/c9091064.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c9091064.lua) | 45 |
| Amaze Attraction Rapid Racing | `55262310` | [Scripts/c55262310.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c55262310.lua) | 45 |
| Gagaga Escape | `9591819` | [Scripts/c9591819.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c9591819.lua) | 45 |
| The Phantom Knights of Umbrage Veil | `85257384` | [Scripts/c85257384.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c85257384.lua) | 44 |
| Number 3: Cicada King | `4997565` | [Scripts/c4997565.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c4997565.lua) | 44 |
| Digital Bug Scaradiator | `12615446` | [Scripts/c12615446.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c12615446.lua) | 44 |
| Riot's Reason | `51612489` | [Scripts/c51612489.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c51612489.lua) | 44 |
| Magikey Beast - Ansyalabolas | `45655875` | [Scripts/c45655875.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c45655875.lua) | 43 |
| Crossroad Sonic Chick | `80054655` | [Scripts/c80054655.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c80054655.lua) | 42 |
| ...and 130 more |  |  |  |

## Script Examples

### Power Tool Braver Dragon (`63265554`)

Source: [Scripts/c63265554.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63265554.lua)

```lua
	local tc=Duel.GetFirstTarget()
	if not tc:IsRelateToEffect(e) then return end
	local b1=tc:IsCanChangePosition()
	local b2=aux.NegateMonsterFilter(tc)
	local op=-1
```

### Mimighoul Maker (`13204145`)

Source: [Scripts/c13204145.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c13204145.lua)

```lua
	local tc=Duel.GetFirstTarget()
	if tc:IsRelateToEffect(e) and tc:IsType(TYPE_MONSTER) then
		if tc:IsPosition(POS_FACEUP_ATTACK) and tc:IsCanChangePosition() then
			Duel.ChangePosition(tc,POS_FACEUP_DEFENCE)
		elseif tc:IsPosition(POS_FACEUP_DEFENCE) and tc:IsCanChangePosition() then
```

### Amaze Attraction Thrill Train (`36591747`)

Source: [Scripts/c36591747.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c36591747.lua)

```lua
function c36591747.sttg(e,tp,eg,ep,ev,re,r,rp,chk)
	local ec=e:GetHandler():GetEquipTarget()
	if chk==0 then return ec and ec:IsCanChangePosition()
		and Duel.IsExistingMatchingCard(c36591747.stfilter,tp,LOCATION_GRAVE,0,1,nil) end
	Duel.SetOperationInfo(0,CATEGORY_POSITION,ec,1,0,0)
```
