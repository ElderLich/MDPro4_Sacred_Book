# Card.SetTurnCounter

## Signature

```lua
Card.SetTurnCounter(Card c, int counter) -> void
```

## Description

Set c of the round counter (light of the sword, etc.)

## Parameters

- `c` `Card`
- `counter` `int`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3512`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **36** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.SetTurnCounter`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| Future Fusion | `77565204` | [Scripts/c77565204.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c77565204.lua) | 55 |
| Synchro Panic | `83962752` | [Scripts/c83962752.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c83962752.lua) | 54 |
| Performapal Turn Trooper | `220414` | [Scripts/c220414.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c220414.lua) | 50 |
| Ancient Warriors Saga - Three Visits | `11711438` | [Scripts/c11711438.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c11711438.lua) | 49 |
| Photon Change | `42925441` | [Scripts/c42925441.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c42925441.lua) | 48 |
| Cyber Network | `12670770` | [Scripts/c12670770.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c12670770.lua) | 47 |
| Time Magic Hammer | `10960419` | [Scripts/c10960419.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c10960419.lua) | 47 |
| U.A. Penalty Box | `70043345` | [Scripts/c70043345.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c70043345.lua) | 46 |
| SPYRAL MISSION - Recapture | `39373426` | [Scripts/c39373426.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c39373426.lua) | 45 |
| SPYRAL MISSION - Assault | `27642961` | [Scripts/c27642961.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c27642961.lua) | 44 |
| Number 62: Galaxy-Eyes Prime Photon Dragon | `31801517` | [Scripts/c31801517.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c31801517.lua) | 43 |
| Infernoble Knight Astolfo | `95953557` | [Scripts/c95953557.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c95953557.lua) | 42 |
| Seismic Shockwave | `79569173` | [Scripts/c79569173.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c79569173.lua) | 42 |
| SPYRAL MISSION - Rescue | `9212051` | [Scripts/c9212051.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c9212051.lua) | 40 |
| Ledger of Legerdemain | `56256517` | [Scripts/c56256517.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c56256517.lua) | 39 |
| Overdoom Line | `87046457` | [Scripts/c87046457.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c87046457.lua) | 38 |
| Break! Draw! | `63851864` | [Scripts/c63851864.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63851864.lua) | 38 |
| Ancient Warriors Saga - East-by-South Winds | `62528292` | [Scripts/c62528292.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c62528292.lua) | 36 |
| Paradox Fusion | `57355219` | [Scripts/c57355219.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c57355219.lua) | 36 |
| Cocoon of Evolution | `40240595` | [Scripts/c40240595.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c40240595.lua) | 34 |
| Soul Devouring Bamboo Sword | `51670553` | [Scripts/c51670553.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c51670553.lua) | 33 |
| Different Dimension Capsule | `11961740` | [Scripts/c11961740.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c11961740.lua) | 33 |
| Ekibyo Drakmord | `69954399` | [Scripts/c69954399.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c69954399.lua) | 33 |
| Depth Amulet | `8279188` | [Scripts/c8279188.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c8279188.lua) | 32 |
| ...and 12 more |  |  |  |

## Script Examples

### Future Fusion (`77565204`)

Source: [Scripts/c77565204.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c77565204.lua)

```lua
	if chk==0 then return true end
	local c=e:GetHandler()
	c:SetTurnCounter(0)
	local e1=Effect.CreateEffect(c)
	e1:SetType(EFFECT_TYPE_FIELD+EFFECT_TYPE_CONTINUOUS)
```

### Synchro Panic (`83962752`)

Source: [Scripts/c83962752.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c83962752.lua)

```lua
	e1:SetOperation(c83962752.desop)
	e1:SetReset(RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_STANDBY+RESET_SELF_TURN,3)
	c:SetTurnCounter(0)
	c:RegisterEffect(e1)
end
```

### Performapal Turn Trooper (`220414`)

Source: [Scripts/c220414.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c220414.lua)

```lua
			tc=og:GetNext()
		end
		c:SetTurnCounter(0)
		og:KeepAlive()
		local e1=Effect.CreateEffect(c)
```
