# Duel.IsPlayerCanDiscardDeck

## Signature

```lua
Duel.IsPlayerCanDiscardDeck(int player, int count) -> bool
```

## Description

Checks whether player can send count cards from the top of the Deck to the Graveyard.

## Parameters

- `player` `int`
- `count` `int`

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5045`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **107** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Duel.IsPlayerCanDiscardDeck) with `Duel.IsPlayerCanDiscardDeck`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Tearlaments Scheiren | `572850` | [Scripts/c572850.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c572850.lua) | 2 |
| Tearlaments Havnis | `37961969` | [Scripts/c37961969.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c37961969.lua) | 1 |
| Sylvan Dancepione | `21903613` | [Scripts/c21903613.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c21903613.lua) | 2 |
| Tearlaments Merrli | `74078255` | [Scripts/c74078255.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74078255.lua) | 1 |
| Ma'at | `18631392` | [Scripts/c18631392.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c18631392.lua) | 2 |
| Cyberse Clock Dragon | `42717221` | [Scripts/c42717221.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c42717221.lua) | 1 |
| Tearlaments Kitkallos | `92731385` | [Scripts/c92731385.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92731385.lua) | 1 |
| Chaos Ruler, the Chaotic Magical Dragon | `3040496` | [Scripts/c3040496.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c3040496.lua) | 2 |
| Akashic Magician | `28776350` | [Scripts/c28776350.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c28776350.lua) | 2 |
| Speedroid Gum Prize | `70939418` | [Scripts/c70939418.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c70939418.lua) | 1 |
| Kelbek the Ancient Vanguard | `25926710` | [Scripts/c25926710.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c25926710.lua) | 2 |
| Laundry Trap | `79371769` | [Scripts/c79371769.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c79371769.lua) | 1 |
| Alsei, the Sylvan High Protector | `10406322` | [Scripts/c10406322.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c10406322.lua) | 2 |
| The Zombie Vampire | `73082255` | [Scripts/c73082255.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c73082255.lua) | 2 |
| Sylvan Princessprout | `20579538` | [Scripts/c20579538.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c20579538.lua) | 2 |
| Super Quantal Fairy Alphan | `58753372` | [Scripts/c58753372.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c58753372.lua) | 2 |
| Agido the Ancient Sentinel | `62320425` | [Scripts/c62320425.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c62320425.lua) | 4 |
| Tsuchigumo, the Poisonous Mayakashi | `77092311` | [Scripts/c77092311.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c77092311.lua) | 2 |
| Crystal Boon | `85766789` | [Scripts/c85766789.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c85766789.lua) | 1 |
| Minerva, the Athenian Lightsworn | `18843291` | [Scripts/c18843291.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c18843291.lua) | 1 |
| Paleozoic Anomalocaris | `61307542` | [Scripts/c61307542.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c61307542.lua) | 2 |
| Sylvan Princessprite | `33909817` | [Scripts/c33909817.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c33909817.lua) | 2 |
| Virtual World City - Kauwloon | `14886190` | [Scripts/c14886190.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c14886190.lua) | 1 |
| Sylvan Lotuswain | `73136204` | [Scripts/c73136204.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c73136204.lua) | 2 |
| ...and 83 more |  |  |  |

## Script Examples

### Tearlaments Scheiren (`572850`)

Source: [Scripts/c572850.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c572850.lua)

```lua
	if chk==0 then return Duel.GetLocationCount(tp,LOCATION_MZONE)>0
		and c:IsCanBeSpecialSummoned(e,0,tp,false,false)
		and Duel.IsPlayerCanDiscardDeck(tp,3)
		and Duel.IsExistingMatchingCard(c572850.tgfilter,tp,LOCATION_HAND,0,1,c) end
	Duel.SetOperationInfo(0,CATEGORY_DECKDES,nil,0,tp,3)
```

### Tearlaments Havnis (`37961969`)

Source: [Scripts/c37961969.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c37961969.lua)

```lua
	if chk==0 then return Duel.GetLocationCount(tp,LOCATION_MZONE)>0
		and e:GetHandler():IsCanBeSpecialSummoned(e,0,tp,false,false)
		and Duel.IsPlayerCanDiscardDeck(tp,3) end
	Duel.SetOperationInfo(0,CATEGORY_DECKDES,nil,0,tp,3)
	Duel.SetOperationInfo(0,CATEGORY_SPECIAL_SUMMON,e:GetHandler(),1,0,0)
```

### Sylvan Dancepione (`21903613`)

Source: [Scripts/c21903613.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c21903613.lua)

```lua
end
function c21903613.target(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.IsPlayerCanDiscardDeck(tp,1) end
end
function c21903613.spfilter(c,e,tp)
```
