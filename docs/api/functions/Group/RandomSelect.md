# Group.RandomSelect

## Signature

```lua
Group.RandomSelect(Group g, int player, int count) -> Group
```

## Description

Returns a new Group containing count randomly chosen cards from g.
count is clamped to g's size. The player argument is written to the random-selection message but does not influence the random choice.

## Parameters

- `g` `Group`
- `player` `int`
- `count` `int`

## Returns

- `Group`

## Source

- `D:\Programs\GitHub\ygopro-core\libgroup.cpp:917`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **142** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Group.RandomSelect) with `Group.RandomSelect`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Deftero Enneacraft - "alazoneIA"](/examples/cards/92171126) | `92171126` | [Scripts/c92171126.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92171126.lua) | 2 |
| [Enneacraft - Asta.PIXEA](/examples/cards/28454232) | `28454232` | [Scripts/c28454232.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c28454232.lua) | 1 |
| [PSY-Framelord Omega](/examples/cards/74586817) | `74586817` | [Scripts/c74586817.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74586817.lua) | 1 |
| Erebus the Underworld Monarch | `23064604` | [Scripts/c23064604.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c23064604.lua) | 1 |
| Genex Ally Triarm | `17760003` | [Scripts/c17760003.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c17760003.lua) | 1 |
| Number 78: Number Archive | `29085954` | [Scripts/c29085954.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c29085954.lua) | 1 |
| Mimighoul Maker | `13204145` | [Scripts/c13204145.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c13204145.lua) | 1 |
| Ekto Enneacraft - "tromarIA" | `29570824` | [Scripts/c29570824.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c29570824.lua) | 1 |
| Enato Enneacraft - "oknirIA" | `55965529` | [Scripts/c55965529.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c55965529.lua) | 1 |
| Psychic Omnibuster | `70659412` | [Scripts/c70659412.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c70659412.lua) | 1 |
| X-Saber Gottoms | `8252010` | [Scripts/c8252010.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c8252010.lua) | 1 |
| Trito Enneacraft - "exapatisIA" | `44716748` | [Scripts/c44716748.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44716748.lua) | 1 |
| Proto Enneacraft - "orgIA" | `56187077` | [Scripts/c56187077.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c56187077.lua) | 1 |
| Black Luster Soldier - Envoy of the Evening Twilight | `77498348` | [Scripts/c77498348.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c77498348.lua) | 1 |
| Infernoid Piaty | `25811989` | [Scripts/c25811989.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c25811989.lua) | 1 |
| Smile Action | `47870325` | [Scripts/c47870325.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c47870325.lua) | 1 |
| Abyss Actor - Liberty Dramatist | `65477143` | [Scripts/c65477143.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c65477143.lua) | 1 |
| Dinomist Rex | `63251695` | [Scripts/c63251695.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63251695.lua) | 1 |
| Hi-Speedroid Rubber Band Shooter | `72813401` | [Scripts/c72813401.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c72813401.lua) | 1 |
| Evening Twilight Knight | `32013448` | [Scripts/c32013448.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c32013448.lua) | 1 |
| Grapha, Dragon Lord of Dark World | `34230233` | [Scripts/c34230233.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c34230233.lua) | 1 |
| Stellarknight Triverr | `42589641` | [Scripts/c42589641.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c42589641.lua) | 1 |
| Spell Shattering Sword | `77456448` | [Scripts/c77456448.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c77456448.lua) | 1 |
| Awakening of the Possessed - Gagigobyte | `74426895` | [Scripts/c74426895.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74426895.lua) | 1 |
| ...and 118 more |  |  |  |

## Script Examples

### Deftero Enneacraft - "alazoneIA" (`92171126`)

Source: [Scripts/c92171126.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92171126.lua)

```lua
		Duel.ConfirmCards(1-tp,sg)
		Duel.Hint(HINT_SELECTMSG,1-tp,HINTMSG_ATOHAND)
		local tg=sg:RandomSelect(1-tp,1)
		Duel.ShuffleDeck(tp)
		tg:GetFirst():SetStatus(STATUS_TO_HAND_WITHOUT_CONFIRM,true)
```

### Enneacraft - Asta.PIXEA (`28454232`)

Source: [Scripts/c28454232.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c28454232.lua)

```lua
		local g=Duel.GetMatchingGroup(Card.IsAbleToRemove,tp,0,LOCATION_HAND,nil,POS_FACEDOWN)
		if g:GetCount()>0 then
			local sg=g:RandomSelect(tp,1)
			Duel.Remove(sg,POS_FACEDOWN,REASON_EFFECT)
		end
```

### PSY-Framelord Omega (`74586817`)

Source: [Scripts/c74586817.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74586817.lua)

```lua
	local g=Duel.GetFieldGroup(1-tp,LOCATION_HAND,0)
	if g:GetCount()==0 or not c:IsRelateToEffect(e) or c:IsFacedown() then return end
	local rs=g:RandomSelect(1-tp,1)
	local rg=Group.FromCards(c,rs:GetFirst())
	if Duel.Remove(rg,POS_FACEUP,REASON_EFFECT+REASON_TEMPORARY)~=0 then
```
