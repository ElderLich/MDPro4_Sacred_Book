# Card.GetSpecialSummonInfo

## Signature

```lua
Card.GetSpecialSummonInfo(Card c, ... int) -> ...
```

## Description

Returns Special Summon information for c.
Supported fields include SUMMON_INFO_CODE, SUMMON_INFO_CODE2, SUMMON_INFO_TYPE, SUMMON_INFO_LEVEL, SUMMON_INFO_RANK, SUMMON_INFO_ATTRIBUTE, SUMMON_INFO_RACE, SUMMON_INFO_ATTACK, SUMMON_INFO_DEFENSE, SUMMON_INFO_REASON_EFFECT, and SUMMON_INFO_REASON_PLAYER.

## Parameters

- `c` `Card`
- `...` `int`

## Returns

- `...`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3525`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **47** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Card.GetSpecialSummonInfo) with `Card.GetSpecialSummonInfo`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Artmage Pact -Awakening- | `23599634` | [Scripts/c23599634.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c23599634.lua) | 1 |
| Black Garden | `71645242` | [Scripts/c71645242.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c71645242.lua) | 1 |
| Seven Cities of the Golden Land | `95034141` | [Scripts/c95034141.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c95034141.lua) | 1 |
| Crystron Halqifibrax Prism | `65400671` | [Scripts/c65400671.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c65400671.lua) | 1 |
| Allure Queen LV5 | `23756165` | [Scripts/c23756165.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c23756165.lua) | 1 |
| Hyper Rank-Up-Magic Utopiforce | `67517351` | [Scripts/c67517351.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c67517351.lua) | 1 |
| Baelgrill de Nouvelles | `88890658` | [Scripts/c88890658.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c88890658.lua) | 1 |
| Dragonroid | `9069157` | [Scripts/c9069157.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c9069157.lua) | 1 |
| Magicolloidal Sol | `67694706` | [Scripts/c67694706.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c67694706.lua) | 1 |
| World of Prophecy | `29146185` | [Scripts/c29146185.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c29146185.lua) | 1 |
| Mysterion the Dragon Crown | `13735899` | [Scripts/c13735899.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c13735899.lua) | 1 |
| Infernal Strike Fighter | `66122213` | [Scripts/c66122213.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c66122213.lua) | 1 |
| Summer Schoolwork Successful! | `77751766` | [Scripts/c77751766.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c77751766.lua) | 1 |
| Millennium Revelation | `41044418` | [Scripts/c41044418.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c41044418.lua) | 1 |
| Barian Untopia | `30761649` | [Scripts/c30761649.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c30761649.lua) | 1 |
| Balameuniere de Nouvelles | `52495649` | [Scripts/c52495649.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c52495649.lua) | 2 |
| Vulmina, Statue of the Sacred Dragon | `93683815` | [Scripts/c93683815.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c93683815.lua) | 1 |
| Phantasos, the Dream Mirror Friend | `62393472` | [Scripts/c62393472.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c62393472.lua) | 1 |
| Derk, Longing for the Blue Skies | `46708514` | [Scripts/c46708514.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c46708514.lua) | 1 |
| Branded in Central Dogmatika | `14220547` | [Scripts/c14220547.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c14220547.lua) | 2 |
| ZW - Sylphid Wing | `95886782` | [Scripts/c95886782.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c95886782.lua) | 1 |
| Branded Lost | `18973184` | [Scripts/c18973184.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c18973184.lua) | 1 |
| Neiroy, the Dream Mirror Disciple | `18189187` | [Scripts/c18189187.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c18189187.lua) | 1 |
| Chef's Special Recipe | `87955518` | [Scripts/c87955518.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c87955518.lua) | 1 |
| ...and 23 more |  |  |  |

## Script Examples

### Artmage Pact -Awakening- (`23599634`)

Source: [Scripts/c23599634.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c23599634.lua)

```lua
function s.limfilter(c,tp)
	return c:IsSummonPlayer(tp) and c:IsSummonType(SUMMON_TYPE_FUSION)
		and c:GetSpecialSummonInfo(SUMMON_INFO_REASON_EFFECT):IsHasCategory(CATEGORY_FUSION_SUMMON)
end
function s.limcon(e,tp,eg,ep,ev,re,r,rp)
```

### Black Garden (`71645242`)

Source: [Scripts/c71645242.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c71645242.lua)

```lua
end
function c71645242.cfilter(c,tp)
	local code,code2=c:GetSpecialSummonInfo(SUMMON_INFO_CODE,SUMMON_INFO_CODE2)
	return c:IsFaceup() and c:IsControler(tp) and code~=71645242 and code2~=71645242
end
```

### Seven Cities of the Golden Land (`95034141`)

Source: [Scripts/c95034141.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c95034141.lua)

```lua
end
function c95034141.alfilter(c)
	return c:IsRace(RACE_ZOMBIE) and c:IsFaceup() and c:GetSpecialSummonInfo(SUMMON_INFO_REASON_EFFECT)
end
function c95034141.alcon(e,tp,eg,ep,ev,re,r,rp)
```
