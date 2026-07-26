# Card.GetBattlePosition

## Signature

```lua
Card.GetBattlePosition(Card c) -> int
```

## Description

Returns c's temporary battle-position snapshot.

## Parameters

- `c` `Card`

## Returns

- `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3468`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **24** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.GetBattlePosition`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Loki, Lord of the Aesir | `67098114` | [Scripts/c67098114.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c67098114.lua) | 51 |
| Odin, Father of the Aesir | `93483212` | [Scripts/c93483212.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93483212.lua) | 46 |
| Thor, Lord of the Aesir | `30604579` | [Scripts/c30604579.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30604579.lua) | 45 |
| House Duston | `40343749` | [Scripts/c40343749.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c40343749.lua) | 34 |
| XX-Saber Fulhelmknight | `78422252` | [Scripts/c78422252.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c78422252.lua) | 34 |
| Sphinx Teleia | `51402177` | [Scripts/c51402177.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c51402177.lua) | 33 |
| Umbral Horror Will o' the Wisp | `70546737` | [Scripts/c70546737.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c70546737.lua) | 33 |
| Andro Sphinx | `15013468` | [Scripts/c15013468.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c15013468.lua) | 32 |
| Hyper Psychic Blaster | `95526884` | [Scripts/c95526884.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c95526884.lua) | 30 |
| Psi-Curse | `16678947` | [Scripts/c16678947.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c16678947.lua) | 29 |
| Greed Grado | `3972721` | [Scripts/c3972721.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c3972721.lua) | 29 |
| Bird of Roses | `75252099` | [Scripts/c75252099.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c75252099.lua) | 28 |
| Ally of Justice Field Marshal | `69461394` | [Scripts/c69461394.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c69461394.lua) | 28 |
| Spyder Spider | `80637190` | [Scripts/c80637190.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c80637190.lua) | 27 |
| Shinato, King of a Higher Plane | `86327225` | [Scripts/c86327225.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c86327225.lua) | 26 |
| Earthbound Immortal Cusillu | `33537328` | [Scripts/c33537328.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c33537328.lua) | 24 |
| 8-Claws Scorpion | `14261867` | [Scripts/c14261867.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c14261867.lua) | 24 |
| Winged Sage Falcos | `87523462` | [Scripts/c87523462.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c87523462.lua) | 24 |
| Marshmallon | `31305911` | [Scripts/c31305911.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c31305911.lua) | 21 |
| Reflect Bounder | `2851070` | [Scripts/c2851070.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c2851070.lua) | 20 |
| Legacy Hunter | `87010442` | [Scripts/c87010442.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c87010442.lua) | 20 |
| Great Poseidon Beetle | `75292259` | [Scripts/c75292259.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c75292259.lua) | 13 |
| Twin-Sword Marauder | `40225398` | [Scripts/c40225398.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c40225398.lua) | 13 |
| Ballista of Rampart Smashing | `242146` | [Scripts/c242146.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c242146.lua) | 13 |

## Script Examples

### Loki, Lord of the Aesir (`67098114`)

Source: [Scripts/c67098114.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c67098114.lua)

```lua
	local c=e:GetHandler()
	local pos=c:GetPreviousPosition()
	if c:IsReason(REASON_BATTLE) then pos=c:GetBattlePosition() end
	if rp==1-tp and c:IsPreviousControler(tp) and c:IsReason(REASON_DESTROY)
		and c:IsPreviousLocation(LOCATION_ONFIELD) and bit.band(pos,POS_FACEUP)~=0 then
```

### Odin, Father of the Aesir (`93483212`)

Source: [Scripts/c93483212.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93483212.lua)

```lua
	local c=e:GetHandler()
	local pos=c:GetPreviousPosition()
	if c:IsReason(REASON_BATTLE) then pos=c:GetBattlePosition() end
	if rp==1-tp and c:IsPreviousControler(tp) and c:IsReason(REASON_DESTROY)
		and c:IsPreviousLocation(LOCATION_ONFIELD) and bit.band(pos,POS_FACEUP)~=0 then
```

### Thor, Lord of the Aesir (`30604579`)

Source: [Scripts/c30604579.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c30604579.lua)

```lua
	local c=e:GetHandler()
	local pos=c:GetPreviousPosition()
	if c:IsReason(REASON_BATTLE) then pos=c:GetBattlePosition() end
	if rp==1-tp and c:IsPreviousControler(tp) and c:IsReason(REASON_DESTROY)
		and c:IsPreviousLocation(LOCATION_ONFIELD) and bit.band(pos,POS_FACEUP)~=0 then
```
