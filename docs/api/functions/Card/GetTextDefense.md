# Card.GetTextDefense

## Signature

```lua
Card.GetTextDefense(Card c) -> int
```

## Description

Returns c's printed/stored DEF value, or 0 while c has no-Level status.

## Parameters

- `c` `Card`

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3496`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **18** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Card.GetTextDefense) with `Card.GetTextDefense`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Duel Link Dragon, the Duel Dragon | `60025883` | [Scripts/c60025883.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c60025883.lua) | 1 |
| Allure Queen LV5 | `23756165` | [Scripts/c23756165.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c23756165.lua) | 1 |
| Nibiru, the Primal Being | `27204311` | [Scripts/c27204311.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c27204311.lua) | 2 |
| The Atmosphere | `14466224` | [Scripts/c14466224.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c14466224.lua) | 1 |
| Ancient Chant | `78665705` | [Scripts/c78665705.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c78665705.lua) | 1 |
| Nightmell the Dark Bonder | `66569334` | [Scripts/c66569334.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c66569334.lua) | 2 |
| Guardian of Felgrand | `33460840` | [Scripts/c33460840.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c33460840.lua) | 1 |
| The Tyrant Neptune | `88071625` | [Scripts/c88071625.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c88071625.lua) | 1 |
| Inzektor Exa-Beetle | `44505297` | [Scripts/c44505297.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44505297.lua) | 1 |
| Exodia, the Legendary Defender | `5008836` | [Scripts/c5008836.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c5008836.lua) | 1 |
| Phantasmal Summoning Beast | `53134520` | [Scripts/c53134520.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c53134520.lua) | 1 |
| Allure Queen LV7 | `50140163` | [Scripts/c50140163.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c50140163.lua) | 1 |
| World Legacy Clash | `93236220` | [Scripts/c93236220.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93236220.lua) | 2 |
| Inzektor Exa-Stag | `26211048` | [Scripts/c26211048.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c26211048.lua) | 1 |
| Berserker Crush | `15471265` | [Scripts/c15471265.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c15471265.lua) | 1 |
| Branded Disciple | `34536828` | [Scripts/c34536828.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c34536828.lua) | 1 |
| Spirit Sculptor | `19307353` | [Scripts/c19307353.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c19307353.lua) | 3 |
| Small World | `89558743` | [Scripts/c89558743.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c89558743.lua) | 2 |

## Script Examples

### Duel Link Dragon, the Duel Dragon (`60025883`)

Source: [Scripts/c60025883.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c60025883.lua)

```lua
	local tc=e:GetLabelObject()
	local atk=tc:GetTextAttack()
	local def=tc:GetTextDefense()
	local lv=tc:GetOriginalLevel()
	local race=tc:GetOriginalRace()
```

### Allure Queen LV5 (`23756165`)

Source: [Scripts/c23756165.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c23756165.lua)

```lua
	if tc:IsFaceup() and tc:IsRelateToEffect(e) then
		local atk=tc:GetTextAttack()
		local def=tc:GetTextDefense()
		if atk<0 then atk=0 end
		if def<0 then def=0 end
```

### Nibiru, the Primal Being (`27204311`)

Source: [Scripts/c27204311.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c27204311.lua)

```lua
		and Duel.IsPlayerCanSpecialSummonCount(tp,2)
		and e:GetHandler():IsCanBeSpecialSummoned(e,0,tp,false,false)
		and Duel.IsPlayerCanSpecialSummonMonster(tp,27204312,0,TYPES_TOKEN_MONSTER,g:GetSum(c27204311.adfilter,Card.GetTextAttack),g:GetSum(c27204311.adfilter,Card.GetTextDefense),11,RACE_ROCK,ATTRIBUTE_LIGHT,POS_FACEUP,1-tp) end
	Duel.SetOperationInfo(0,CATEGORY_TOKEN,nil,1,0,0)
	Duel.SetOperationInfo(0,CATEGORY_SPECIAL_SUMMON,e:GetHandler(),2,0,0)
```
