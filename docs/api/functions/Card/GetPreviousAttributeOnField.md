# Card.GetPreviousAttributeOnField

## Signature

```lua
Card.GetPreviousAttributeOnField(Card c) -> int
```

## Description

Returns the Attribute value recorded for c's previous on-field state.

## Parameters

- `c` `Card`

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3502`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **26** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Card.GetPreviousAttributeOnField) with `Card.GetPreviousAttributeOnField`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Stars Align Above the Shrine](/examples/cards/15306543) | `15306543` | [Scripts/c15306543.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c15306543.lua) | 1 |
| Abyss-steam | `63941169` | [Scripts/c63941169.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c63941169.lua) | 1 |
| Chevreuil, Hunting Scout of the Deep Forest | `13023431` | [Scripts/c13023431.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c13023431.lua) | 1 |
| Salamangreat Raging Phoenix | `57134592` | [Scripts/c57134592.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c57134592.lua) | 1 |
| Zaborg the Mega Monarch | `87602890` | [Scripts/c87602890.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c87602890.lua) | 1 |
| Sangen Furo | `55484152` | [Scripts/c55484152.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c55484152.lua) | 1 |
| Desperado Barrel Dragon | `76728962` | [Scripts/c76728962.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c76728962.lua) | 1 |
| Valiant Shark Lancer | `23672629` | [Scripts/c23672629.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c23672629.lua) | 1 |
| Aussa the Earth Channeler | `62803464` | [Scripts/c62803464.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c62803464.lua) | 1 |
| Machina Citadel | `87074380` | [Scripts/c87074380.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c87074380.lua) | 1 |
| Wynn the Wind Channeler | `86395581` | [Scripts/c86395581.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c86395581.lua) | 1 |
| Two-for-One Repair Job | `44459942` | [Scripts/c44459942.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c44459942.lua) | 1 |
| Darkest Diabolos, Lord of the Lair | `50383626` | [Scripts/c50383626.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c50383626.lua) | 1 |
| Magmacho Dragon | `50951254` | [Scripts/c50951254.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c50951254.lua) | 1 |
| Crusher Run | `88667504` | [Scripts/c88667504.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c88667504.lua) | 1 |
| Exodia, the Legendary Defender | `5008836` | [Scripts/c5008836.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c5008836.lua) | 1 |
| Infinitrack Road Roller | `5205146` | [Scripts/c5205146.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c5205146.lua) | 1 |
| Cataclysmic Scorching Sunburner | `39505816` | [Scripts/c39505816.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c39505816.lua) | 1 |
| Shinobird Power Spot | `9553721` | [Scripts/c9553721.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c9553721.lua) | 1 |
| Cataclysmic Cryonic Coldo | `19420830` | [Scripts/c19420830.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c19420830.lua) | 1 |
| Cataclysmic Crusted Calcifida | `9028399` | [Scripts/c9028399.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c9028399.lua) | 1 |
| Prayers of the Voiceless Voice | `52472775` | [Scripts/c52472775.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c52472775.lua) | 1 |
| Cataclysmic Circumpolar Chilblainia | `62850093` | [Scripts/c62850093.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c62850093.lua) | 1 |
| Piwraithe the Ghost Pirate | `83682209` | [Scripts/c83682209.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c83682209.lua) | 1 |
| ...and 2 more |  |  |  |

## Script Examples

### Stars Align Above the Shrine (`15306543`)

Source: [Scripts/c15306543.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c15306543.lua)

```lua
end
function s.cfilter(c,tp)
	return c:IsPreviousPosition(POS_FACEUP) and bit.band(c:GetPreviousAttributeOnField(),ATTRIBUTE_WIND)~=0 and c:IsPreviousControler(tp)
		and c:IsPreviousLocation(LOCATION_MZONE) and c:IsControler(tp)
end
```

### Abyss-steam (`63941169`)

Source: [Scripts/c63941169.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c63941169.lua)

```lua
	return c:IsReason(REASON_BATTLE+REASON_EFFECT)
		and c:IsPreviousPosition(POS_FACEUP) and c:IsPreviousControler(tp)
		and c:GetPreviousAttributeOnField()&ATTRIBUTE_WATER~=0
		and c:IsPreviousLocation(LOCATION_MZONE) and (se==nil or c:GetReasonEffect()~=se)
end
```

### Chevreuil, Hunting Scout of the Deep Forest (`13023431`)

Source: [Scripts/c13023431.lua](https://github.com/ElderLich/MDPro4_Sacred_Book/blob/main/Scripts/c13023431.lua)

```lua
		return bc:GetPreviousPosition()&POS_FACEUP>0 and bc:GetPreviousLocation()&LOCATION_MZONE==LOCATION_MZONE and bc:IsPreviousControler(tp)
			and bc:GetPreviousTypeOnField()&TYPE_MONSTER==TYPE_MONSTER and c:GetPreviousRaceOnField()&RACE_WARRIOR==RACE_WARRIOR
			and bc:GetPreviousAttributeOnField()&ATTRIBUTE_EARTH==ATTRIBUTE_EARTH
	end
end
```
