# Card.GetReasonEffect

## Signature

```lua
Card.GetReasonEffect(Card c) -> Effect|nil
```

## Description

Returns c's current reason effect, or nil when no reason effect is recorded.

## Parameters

- `c` `Card`

## Returns

- `Effect|nil`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3462`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **51** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.GetReasonEffect`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Predaplant Bal Teah](/examples/cards/66787942) | `66787942` | [Scripts/c66787942.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c66787942.lua) | 64 |
| Abyss-steam | `63941169` | [Scripts/c63941169.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63941169.lua) | 56 |
| Masked HERO Furnace | `58288218` | [Scripts/c58288218.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c58288218.lua) | 52 |
| Earthbound Servant Geo Gremlina | `33202303` | [Scripts/c33202303.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c33202303.lua) | 52 |
| Numeron Chaos Ritual | `41850466` | [Scripts/c41850466.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c41850466.lua) | 52 |
| Unchained Soul Lord of Yama | `24269961` | [Scripts/c24269961.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24269961.lua) | 51 |
| Armed Rebeellion | `21056275` | [Scripts/c21056275.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c21056275.lua) | 50 |
| Tachyon Cloudragon | `72705654` | [Scripts/c72705654.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c72705654.lua) | 49 |
| Mirage Swordsman | `73936388` | [Scripts/c73936388.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c73936388.lua) | 48 |
| Naturia Mole Cricket | `93454062` | [Scripts/c93454062.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93454062.lua) | 48 |
| Cross Keeper | `40740224` | [Scripts/c40740224.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c40740224.lua) | 48 |
| Amphibious Swarmship Amblowhale | `20665527` | [Scripts/c20665527.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c20665527.lua) | 48 |
| Sacred Fire King Garunix | `66431519` | [Scripts/c66431519.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c66431519.lua) | 47 |
| Redox, Dragon Ruler of Boulders | `90411554` | [Scripts/c90411554.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c90411554.lua) | 47 |
| Predaprimitive | `89176044` | [Scripts/c89176044.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c89176044.lua) | 47 |
| Unchained Ogre Shara | `95136979` | [Scripts/c95136979.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c95136979.lua) | 47 |
| Dream Mirror Recap | `81038234` | [Scripts/c81038234.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c81038234.lua) | 46 |
| The Abyss Dragon Swordsoul | `5141117` | [Scripts/c5141117.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c5141117.lua) | 45 |
| Geistgrinder Golem | `26913989` | [Scripts/c26913989.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c26913989.lua) | 45 |
| Blackwing - Shamal the Sandstorm | `8571567` | [Scripts/c8571567.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c8571567.lua) | 45 |
| Maiden of White | `17947697` | [Scripts/c17947697.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c17947697.lua) | 44 |
| Dillingerous Dragon | `23732205` | [Scripts/c23732205.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c23732205.lua) | 44 |
| Galaxy War Drake | `19316241` | [Scripts/c19316241.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c19316241.lua) | 43 |
| Promethean Princess, Bestower of Flames | `2772337` | [Scripts/c2772337.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c2772337.lua) | 42 |
| ...and 27 more |  |  |  |

## Script Examples

### Predaplant Bal Teah (`66787942`)

Source: [Scripts/c66787942.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c66787942.lua)

```lua
end
function s.spfilter2(c,tp,se)
	return c:IsControler(tp) and (se==nil or c:GetReasonEffect()~=se)
end
function s.spcon2(e,tp,eg,ep,ev,re,r,rp)
```

### Abyss-steam (`63941169`)

Source: [Scripts/c63941169.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63941169.lua)

```lua
		and c:IsPreviousPosition(POS_FACEUP) and c:IsPreviousControler(tp)
		and c:GetPreviousAttributeOnField()&ATTRIBUTE_WATER~=0
		and c:IsPreviousLocation(LOCATION_MZONE) and (se==nil or c:GetReasonEffect()~=se)
end
function s.thcon(e,tp,eg,ep,ev,re,r,rp)
```

### Masked HERO Furnace (`58288218`)

Source: [Scripts/c58288218.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c58288218.lua)

```lua
function s.spfilter(c,tp,se)
	return c:IsSummonPlayer(tp) and not c:IsAttribute(ATTRIBUTE_FIRE) and c:IsSetCard(0x8) and c:IsType(TYPE_FUSION) and c:IsFaceup()
		and (se==nil or c:GetReasonEffect()~=se)
end
function s.spcon(e,tp,eg,ep,ev,re,r,rp)
```
