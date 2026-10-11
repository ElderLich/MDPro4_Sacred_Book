# Duel.AnnounceType

## Signature

```lua
Duel.AnnounceType(int player) -> int
```

## Description

Lets player choose one of the engine's built-in Monster/Spell/Trap type options and returns the zero-based option index.
The return value is the selected option index, not a TYPE_* bitmask.

## Parameters

- `player` `int`

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:5033`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **23** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Duel.AnnounceType) with `Duel.AnnounceType`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Cosmos Channelling | `91654806` | [Scripts/c91654806.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c91654806.lua) | 1 |
| Vendread Battlelord | `3909436` | [Scripts/c3909436.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c3909436.lua) | 1 |
| Silent Wolf Calupo | `15947754` | [Scripts/c15947754.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c15947754.lua) | 1 |
| Ancient Gear Gadget | `18486927` | [Scripts/c18486927.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c18486927.lua) | 1 |
| SPYGAL Misty | `94096018` | [Scripts/c94096018.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c94096018.lua) | 1 |
| White Rose Cloister | `84335863` | [Scripts/c84335863.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c84335863.lua) | 1 |
| SPYRAL Double Helix | `1322368` | [Scripts/c1322368.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c1322368.lua) | 1 |
| Goddess Verdande's Guidance | `64961254` | [Scripts/c64961254.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c64961254.lua) | 1 |
| Vampire Duke | `58947797` | [Scripts/c58947797.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c58947797.lua) | 1 |
| Card Scanner | `77066768` | [Scripts/c77066768.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c77066768.lua) | 1 |
| Vampire Grace | `40607210` | [Scripts/c40607210.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c40607210.lua) | 1 |
| Vampire Lord | `53839837` | [Scripts/c53839837.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c53839837.lua) | 1 |
| SPYRAL Super Agent | `41091257` | [Scripts/c41091257.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c41091257.lua) | 1 |
| Hazy Flame Sphynx | `1409474` | [Scripts/c1409474.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c1409474.lua) | 1 |
| SPYRAL Tough | `20584712` | [Scripts/c20584712.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c20584712.lua) | 1 |
| Psychic Nightmare | `7582066` | [Scripts/c7582066.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c7582066.lua) | 1 |
| Onikuji | `73820802` | [Scripts/c73820802.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c73820802.lua) | 1 |
| Evigishki Tetrogre | `21496848` | [Scripts/c21496848.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c21496848.lua) | 1 |
| Number 16: Shock Master | `54719828` | [Scripts/c54719828.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c54719828.lua) | 1 |
| Reversal Quiz | `5990062` | [Scripts/c5990062.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c5990062.lua) | 1 |
| Ordeal of a Traveler | `39537362` | [Scripts/c39537362.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c39537362.lua) | 1 |
| Ominous Fortunetelling | `56995655` | [Scripts/c56995655.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c56995655.lua) | 1 |
| Vampire Lady | `26495087` | [Scripts/c26495087.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c26495087.lua) | 1 |

## Script Examples

### Cosmos Channelling (`91654806`)

Source: [Scripts/c91654806.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c91654806.lua)

```lua
	if chk==0 then return e:GetHandler():IsAbleToGrave() and Duel.IsPlayerCanDraw(tp,1) end
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_CARDTYPE)
	e:SetLabel(Duel.AnnounceType(tp))
	Duel.SetOperationInfo(0,CATEGORY_TOGRAVE,e:GetHandler(),0,0,0)
	Duel.SetOperationInfo(0,CATEGORY_DRAW,nil,0,tp,0)
```

### Vendread Battlelord (`3909436`)

Source: [Scripts/c3909436.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c3909436.lua)

```lua
	if chk==0 then return true end
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_CARDTYPE)
	e:SetLabel(Duel.AnnounceType(tp))
end
function c3909436.operation(e,tp,eg,ep,ev,re,r,rp)
```

### Silent Wolf Calupo (`15947754`)

Source: [Scripts/c15947754.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c15947754.lua)

```lua
	if tc then
		Duel.Hint(HINT_SELECTMSG,1-tp,HINTMSG_CARDTYPE)
		local op=Duel.AnnounceType(1-tp)
		if (op==0 and tc:GetOriginalType()&TYPE_MONSTER~=0)
			or (op==1 and tc:GetOriginalType()&TYPE_SPELL~=0)
```
