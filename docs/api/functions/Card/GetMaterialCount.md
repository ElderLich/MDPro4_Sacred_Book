# Card.GetMaterialCount

## Signature

```lua
Card.GetMaterialCount(Card c) -> int
```

## Description

Returns the number of cards currently recorded as c's materials.

## Parameters

- `c` `Card`

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3571`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **25** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Card.GetMaterialCount) with `Card.GetMaterialCount`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Ashened to Endlessness](/examples/cards/34813443) | `34813443` | [Scripts/c34813443.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c34813443.lua) | 1 |
| Saryuja Skull Dread | `74997493` | [Scripts/c74997493.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74997493.lua) | 3 |
| Dark Alligator | `34479658` | [Scripts/c34479658.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c34479658.lua) | 1 |
| Gold Pride - Pin Baller | `28497830` | [Scripts/c28497830.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c28497830.lua) | 2 |
| Cosmic Quasar Dragon | `37442336` | [Scripts/c37442336.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c37442336.lua) | 1 |
| Ravenous Crocodragon Archethys | `87188910` | [Scripts/c87188910.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c87188910.lua) | 1 |
| Alba-Lenatus the Abyss Dragon | `3410461` | [Scripts/c3410461.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c3410461.lua) | 1 |
| Clorless, Chaos King of Dark World | `22723778` | [Scripts/c22723778.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c22723778.lua) | 1 |
| Wake Up Your Elemental HERO | `32828466` | [Scripts/c32828466.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c32828466.lua) | 1 |
| The Arrival Cyberse @Ignister | `11738489` | [Scripts/c11738489.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c11738489.lua) | 1 |
| Yubel - The Loving Defender Forever | `47172959` | [Scripts/c47172959.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c47172959.lua) | 1 |
| Diabolantis the Menacing Mantis | `24634594` | [Scripts/c24634594.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24634594.lua) | 1 |
| Apollousa, Bow of the Goddess | `4280258` | [Scripts/c4280258.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c4280258.lua) | 1 |
| Frightfur Sabre-Tooth | `80889750` | [Scripts/c80889750.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c80889750.lua) | 1 |
| Tlakalel, His Malevolent Majesty | `82319644` | [Scripts/c82319644.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c82319644.lua) | 1 |
| Shooting Quasar Dragon | `35952884` | [Scripts/c35952884.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c35952884.lua) | 1 |
| Bloom Prima the Melodious Choir | `24672164` | [Scripts/c24672164.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24672164.lua) | 1 |
| Chimera the Illusion Beast | `38264974` | [Scripts/c38264974.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c38264974.lua) | 1 |
| Evolution End Burst | `78217065` | [Scripts/c78217065.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c78217065.lua) | 2 |
| Divine Grace - Northwemko | `61757117` | [Scripts/c61757117.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c61757117.lua) | 1 |
| Chimeratech Overdragon | `64599569` | [Scripts/c64599569.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c64599569.lua) | 2 |
| Synchro Strike | `30123142` | [Scripts/c30123142.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30123142.lua) | 2 |
| Intercept | `59695933` | [Scripts/c59695933.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59695933.lua) | 1 |
| Giganticastle | `63422098` | [Scripts/c63422098.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63422098.lua) | 1 |
| ...and 1 more |  |  |  |

## Script Examples

### Ashened to Endlessness (`34813443`)

Source: [Scripts/c34813443.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c34813443.lua)

```lua
		e1:SetType(EFFECT_TYPE_SINGLE)
		e1:SetCode(EFFECT_UPDATE_ATTACK)
		e1:SetValue(tc:GetMaterialCount()*500)
		e1:SetReset(RESET_EVENT+RESETS_STANDARD)
		tc:RegisterEffect(e1)
```

### Saryuja Skull Dread (`74997493`)

Source: [Scripts/c74997493.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74997493.lua)

```lua
function c74997493.regop(e,tp,eg,ep,ev,re,r,rp)
	local c=e:GetHandler()
	if c:GetMaterialCount()>=2 then
		local e1=Effect.CreateEffect(c)
		e1:SetDescription(aux.Stringid(74997493,0))
```

### Dark Alligator (`34479658`)

Source: [Scripts/c34479658.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c34479658.lua)

```lua
function c34479658.tkcon(e,tp,eg,ep,ev,re,r,rp)
	local c=e:GetHandler()
	return c:IsSummonType(SUMMON_TYPE_ADVANCE) and c:GetMaterialCount()>0
end
function c34479658.tktg(e,tp,eg,ep,ev,re,r,rp,chk)
```
