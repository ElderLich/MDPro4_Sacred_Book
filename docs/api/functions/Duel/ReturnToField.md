# Duel.ReturnToField

## Signature

```lua
Duel.ReturnToField(Card c, [int pos], [int zone]) -> bool
```

## Description

To return the form c to the field pos, pos default value is the expression before leaving the field, the return value indicates whether the success
C must be a REASON_TEMPORARY reason to leave, and leave the position did not leave that position

## Parameters

- `c` `Card`
- `pos` `int` optional
- `zone` `int` optional - default: 0xff

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4883`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **87** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Duel.ReturnToField`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [PSY-Framelord Omega](/examples/cards/74586817) | `74586817` | [Scripts/c74586817.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74586817.lua) | 64 |
| [Shooting Majestic Star Dragon](/examples/cards/40939228) | `40939228` | [Scripts/c40939228.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c40939228.lua) | 62 |
| [Ecclesia and the Dark Dragon](/examples/cards/78397661) | `78397661` | [Scripts/c78397661.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c78397661.lua) | 62 |
| [PSY-Framelord Zeta](/examples/cards/37192109) | `37192109` | [Scripts/c37192109.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c37192109.lua) | 62 |
| [W:P Fancy Ball](/examples/cards/4993187) | `4993187` | [Scripts/c4993187.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c4993187.lua) | 61 |
| [A Bao A Qu, the Lightless Shadow](/examples/cards/4731783) | `4731783` | [Scripts/c4731783.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c4731783.lua) | 61 |
| Flowering Etoile the Melodious Magnificat | `83793721` | [Scripts/c83793721.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c83793721.lua) | 60 |
| Angelica, Princess of Noble Arms | `36320744` | [Scripts/c36320744.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c36320744.lua) | 59 |
| S:P Little Knight | `29301450` | [Scripts/c29301450.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c29301450.lua) | 58 |
| Sea Stealth Attack | `19089195` | [Scripts/c19089195.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c19089195.lua) | 57 |
| The Weather Painter Moonbow | `95515518` | [Scripts/c95515518.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c95515518.lua) | 57 |
| Ghoti Fury | `65898344` | [Scripts/c65898344.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c65898344.lua) | 56 |
| Galaxy-Eyes Photon Dragon | `93717133` | [Scripts/c93717133.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93717133.lua) | 56 |
| Timebreaker Magician | `80335817` | [Scripts/c80335817.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c80335817.lua) | 54 |
| Sleipnir the Runick Mane | `74659582` | [Scripts/c74659582.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74659582.lua) | 54 |
| Bunny Ear Enthusiast | `39643167` | [Scripts/c39643167.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c39643167.lua) | 54 |
| Galaxy-Eyes Photon Change Dragon | `54725177` | [Scripts/c54725177.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c54725177.lua) | 53 |
| Mekk-Knight Purple Nightfall | `28692962` | [Scripts/c28692962.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c28692962.lua) | 53 |
| Marincess Cascade | `27012990` | [Scripts/c27012990.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c27012990.lua) | 53 |
| Amaze Attraction Thrill Train | `36591747` | [Scripts/c36591747.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c36591747.lua) | 52 |
| Time Thief Redoer | `55285840` | [Scripts/c55285840.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c55285840.lua) | 52 |
| Zefra Metaltron | `85216896` | [Scripts/c85216896.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c85216896.lua) | 52 |
| Cynet Backdoor | `43839002` | [Scripts/c43839002.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c43839002.lua) | 52 |
| Loka Samsara | `2116237` | [Scripts/c2116237.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c2116237.lua) | 51 |
| ...and 63 more |  |  |  |

## Script Examples

### PSY-Framelord Omega (`74586817`)

Source: [Scripts/c74586817.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74586817.lua)

```lua
	while tc do
		if tc==e:GetHandler() then
			Duel.ReturnToField(tc)
		else
			Duel.SendtoHand(tc,tc:GetPreviousControler(),REASON_EFFECT)
```

### Shooting Majestic Star Dragon (`40939228`)

Source: [Scripts/c40939228.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c40939228.lua)

```lua
end
function c40939228.retop(e,tp,eg,ep,ev,re,r,rp)
	Duel.ReturnToField(e:GetLabelObject())
end
```

### Ecclesia and the Dark Dragon (`78397661`)

Source: [Scripts/c78397661.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c78397661.lua)

```lua
end
function s.retop(e,tp,eg,ep,ev,re,r,rp)
	Duel.ReturnToField(e:GetLabelObject())
end
function s.tdfilter(c,tp)
```
