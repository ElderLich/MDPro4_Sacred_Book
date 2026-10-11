# Duel.ReturnToField

## Signature

```lua
Duel.ReturnToField(Card c, [int pos], [int zone]) -> bool|nil
```

## Description

Returns a card temporarily removed from the field to its previous controller and previous location.
pos defaults to the previous position and zone defaults to 0xff. If c was not removed for REASON_TEMPORARY, the binding returns no Lua value; otherwise it yields and returns whether the move succeeded.
Use this only for temporary removal lifecycles, not as a generic way to place cards on the field.

## How To Use It

Use this to close a real temporary-banish lifecycle. The card should have left the field with `Duel.Remove(..., REASON_EFFECT+REASON_TEMPORARY)` or an equivalent temporary removal reason.

```lua
if Duel.Remove(tc,0,REASON_EFFECT+REASON_TEMPORARY)>0 then
    e1:SetLabelObject(tc)
end

local rc=e:GetLabelObject()
if rc then
    Duel.ReturnToField(rc)
end
```

Do not use this as a generic field-placement helper. Use `Duel.SpecialSummon`, `Duel.SSet`, `Duel.MSet`, `Duel.Equip`, or `Duel.MoveToField` for ordinary placement actions.

## Related Functions

- [Duel.Remove](/api/functions/Duel/Remove)
- [Card.IsReason](/api/functions/Card/IsReason)
- [Duel.MoveToField](/api/functions/Duel/MoveToField)

## Parameters

- `c` `Card`
- `pos` `int` optional - default: previous position
- `zone` `int` optional - default: 0xff

## Returns

- `bool|nil` - Success flag, or nil if c was not temporarily removed from the field.

## Source

- `D:\Programs\GitHub\ygopro-core\libduel.cpp:4883`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **91** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Duel.ReturnToField) with `Duel.ReturnToField`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [PSY-Framelord Omega](/examples/cards/74586817) | `74586817` | [Scripts/c74586817.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74586817.lua) | 1 |
| [Shooting Majestic Star Dragon](/examples/cards/40939228) | `40939228` | [Scripts/c40939228.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c40939228.lua) | 1 |
| [PSY-Framelord Zeta](/examples/cards/37192109) | `37192109` | [Scripts/c37192109.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c37192109.lua) | 1 |
| [W:P Fancy Ball](/examples/cards/4993187) | `4993187` | [Scripts/c4993187.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c4993187.lua) | 1 |
| [A Bao A Qu, the Lightless Shadow](/examples/cards/4731783) | `4731783` | [Scripts/c4731783.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c4731783.lua) | 1 |
| [Cerynemesia, Mystical Beast of the Forest](/examples/cards/43632709) | `43632709` | [Scripts/c43632709.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c43632709.lua) | 1 |
| Flowering Etoile the Melodious Magnificat | `83793721` | [Scripts/c83793721.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c83793721.lua) | 2 |
| Angelica, Princess of Noble Arms | `36320744` | [Scripts/c36320744.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c36320744.lua) | 1 |
| Ecclesia and the Dark Dragon | `78397661` | [Scripts/c78397661.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c78397661.lua) | 1 |
| S:P Little Knight | `29301450` | [Scripts/c29301450.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c29301450.lua) | 2 |
| Sea Stealth Attack | `19089195` | [Scripts/c19089195.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c19089195.lua) | 1 |
| The Weather Painter Moonbow | `95515518` | [Scripts/c95515518.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c95515518.lua) | 1 |
| Ghoti Fury | `65898344` | [Scripts/c65898344.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c65898344.lua) | 2 |
| Galaxy-Eyes Photon Dragon | `93717133` | [Scripts/c93717133.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93717133.lua) | 1 |
| Timebreaker Magician | `80335817` | [Scripts/c80335817.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c80335817.lua) | 2 |
| Sleipnir the Runick Mane | `74659582` | [Scripts/c74659582.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74659582.lua) | 1 |
| Bunny Ear Enthusiast | `39643167` | [Scripts/c39643167.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c39643167.lua) | 1 |
| Galaxy-Eyes Photon Change Dragon | `54725177` | [Scripts/c54725177.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c54725177.lua) | 1 |
| Mekk-Knight Purple Nightfall | `28692962` | [Scripts/c28692962.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c28692962.lua) | 1 |
| Destiny HERO - Doom Overlord | `62542673` | [Scripts/c62542673.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c62542673.lua) | 1 |
| Marincess Cascade | `27012990` | [Scripts/c27012990.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c27012990.lua) | 1 |
| Amaze Attraction Thrill Train | `36591747` | [Scripts/c36591747.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c36591747.lua) | 1 |
| Time Thief Redoer | `55285840` | [Scripts/c55285840.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c55285840.lua) | 1 |
| Zefra Metaltron | `85216896` | [Scripts/c85216896.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c85216896.lua) | 1 |
| ...and 67 more |  |  |  |

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

### PSY-Framelord Zeta (`37192109`)

Source: [Scripts/c37192109.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c37192109.lua)

```lua
	local tc=sg:GetFirst()
	while tc do
		Duel.ReturnToField(tc)
		tc=sg:GetNext()
	end
```
