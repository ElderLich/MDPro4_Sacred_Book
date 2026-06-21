# Card.GetSummonType

## Signature

```lua
Card.GetSummonType(Card c) -> int
```

## Description

Returns the call / special call of c

## Parameters

- `c` `Card`

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3470`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **26** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.GetSummonType`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Ostinato | `9113513` | [Scripts/c9113513.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c9113513.lua) | 60 |
| Gizmek Yata, the Gleaming Vanguard | `13224603` | [Scripts/c13224603.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c13224603.lua) | 47 |
| Argostars - Lightning Tydeu | `65889305` | [Scripts/c65889305.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c65889305.lua) | 47 |
| Millennium Revelation | `41044418` | [Scripts/c41044418.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c41044418.lua) | 44 |
| Trishula, the Dragon of Icy Imprisonment | `15661378` | [Scripts/c15661378.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c15661378.lua) | 44 |
| Guoglim, Spear of the Ghoti | `2405631` | [Scripts/c2405631.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c2405631.lua) | 43 |
| Metamorphortress | `43959432` | [Scripts/c43959432.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c43959432.lua) | 43 |
| T.G. Recipro Dragonfly | `62560742` | [Scripts/c62560742.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c62560742.lua) | 41 |
| Argostars - Slayer Eteo | `38379052` | [Scripts/c38379052.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c38379052.lua) | 40 |
| Kuebiko | `20087414` | [Scripts/c20087414.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c20087414.lua) | 40 |
| World Legacy - "World Armor" | `83477829` | [Scripts/c83477829.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c83477829.lua) | 40 |
| Statue of Anguish Pattern | `23626223` | [Scripts/c23626223.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c23626223.lua) | 40 |
| Silhouhatte Trick | `24440742` | [Scripts/c24440742.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c24440742.lua) | 39 |
| Exodia, the Legendary Defender | `5008836` | [Scripts/c5008836.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c5008836.lua) | 39 |
| Zoma the Earthbound Spirit | `88001391` | [Scripts/c88001391.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c88001391.lua) | 37 |
| Bujin Hirume | `9418365` | [Scripts/c9418365.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c9418365.lua) | 37 |
| Blink Out | `28279365` | [Scripts/c28279365.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c28279365.lua) | 36 |
| Argostars - Swift Capane | `91284003` | [Scripts/c91284003.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c91284003.lua) | 35 |
| Krystal Avatar | `20960340` | [Scripts/c20960340.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c20960340.lua) | 35 |
| Extraceratops | `38383368` | [Scripts/c38383368.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c38383368.lua) | 35 |
| Dark Lucius LV6 | `12817939` | [Scripts/c12817939.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c12817939.lua) | 32 |
| Cyber Shadow Gardna | `90440725` | [Scripts/c90440725.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c90440725.lua) | 30 |
| Crusadia Krawler | `55838342` | [Scripts/c55838342.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c55838342.lua) | 30 |
| The Ascended of Thunder | `70493141` | [Scripts/c70493141.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c70493141.lua) | 26 |
| ...and 2 more |  |  |  |

## Script Examples

### Ostinato (`9113513`)

Source: [Scripts/c9113513.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c9113513.lua)

```lua
	local tc=e:GetLabelObject()
	local mg=tc:GetMaterial()
	local sumtype=tc:GetSummonType()
	if Duel.Destroy(tc,REASON_EFFECT)~=0
		and bit.band(sumtype,SUMMON_TYPE_FUSION)==SUMMON_TYPE_FUSION and mg:GetCount()>0
```

### Gizmek Yata, the Gleaming Vanguard (`13224603`)

Source: [Scripts/c13224603.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c13224603.lua)

```lua
function c13224603.reccon(e,tp,eg,ep,ev,re,r,rp)
	local c=e:GetHandler()
	return c:IsPreviousLocation(LOCATION_MZONE) and c:GetSummonType()==SUMMON_TYPE_SPECIAL+SUMMON_VALUE_SELF
end
function c13224603.rectg(e,tp,eg,ep,ev,re,r,rp,chk)
```

### Argostars - Lightning Tydeu (`65889305`)

Source: [Scripts/c65889305.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c65889305.lua)

```lua
function s.setcon(e,tp,eg,ep,ev,re,r,rp)
	local c=e:GetHandler()
	return not c:IsStatus(STATUS_BATTLE_DESTROYED) and c:GetSummonType()==SUMMON_TYPE_SPECIAL+SUMMON_VALUE_SELF
end
function s.settg(e,tp,eg,ep,ev,re,r,rp,chk)
```
