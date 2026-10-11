# Card.IsCanBeDisabledByEffect

## Signature

```lua
Card.IsCanBeDisabledByEffect(Card c, Effect e, [bool isMonsterEffect]) -> bool
```

## Description

Checks whether c's effects can be negated by e.
Cards that are already negated, have no original effects, or are unaffected by e cannot be negated.
The optional third parameter indicates whether this is a monster effect.

## Parameters

- `c` `Card`
- `e` `Effect`
- `isMonsterEffect` `bool` optional

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3702`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **108** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Card.IsCanBeDisabledByEffect) with `Card.IsCanBeDisabledByEffect`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [El Shaddoll Apkallone](/examples/cards/50907446) | `50907446` | [Scripts/c50907446.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c50907446.lua) | 1 |
| [DoSolfachord Coolia](/examples/cards/80776622) | `80776622` | [Scripts/c80776622.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c80776622.lua) | 1 |
| [Transonic Bird](/examples/cards/34072799) | `34072799` | [Scripts/c34072799.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c34072799.lua) | 1 |
| Sacred Beasts Combined Assault | `50147815` | [Scripts/c50147815.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c50147815.lua) | 1 |
| Dracotail Mululu | `7375867` | [Scripts/c7375867.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c7375867.lua) | 1 |
| Cyber Dragon, the Luminous Mech Dragon | `66664203` | [Scripts/c66664203.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c66664203.lua) | 1 |
| Power Tool Braver Dragon | `63265554` | [Scripts/c63265554.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c63265554.lua) | 1 |
| Radiant Typhoon Mandate | `53813120` | [Scripts/c53813120.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c53813120.lua) | 1 |
| Unchained Soul Rage Abominator | `21419436` | [Scripts/c21419436.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c21419436.lua) | 1 |
| Weaver of Fairy Tails | `78021082` | [Scripts/c78021082.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c78021082.lua) | 1 |
| Borrelshroud Dragon | `66452432` | [Scripts/c66452432.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c66452432.lua) | 1 |
| S-Force Justify | `35334193` | [Scripts/c35334193.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c35334193.lua) | 1 |
| Icejade Erosion | `53742162` | [Scripts/c53742162.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c53742162.lua) | 1 |
| Scourge of the White Forest | `93723936` | [Scripts/c93723936.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c93723936.lua) | 1 |
| Reversal Box | `2606417` | [Scripts/c2606417.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c2606417.lua) | 1 |
| Stellarnova Binding | `69678646` | [Scripts/c69678646.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c69678646.lua) | 1 |
| The Chaotic Phantasmal Sacred Beasts | `7894706` | [Scripts/c7894706.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c7894706.lua) | 1 |
| Dragunity Knight - Areus | `34528176` | [Scripts/c34528176.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c34528176.lua) | 1 |
| Epurrely Beauty | `98049934` | [Scripts/c98049934.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c98049934.lua) | 1 |
| Magikey Mechmusket - Batosbuster | `19489718` | [Scripts/c19489718.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c19489718.lua) | 1 |
| Angel of Blue Tears | `91706817` | [Scripts/c91706817.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c91706817.lua) | 1 |
| Diabrocken the Ominous Specter | `6083904` | [Scripts/c6083904.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c6083904.lua) | 1 |
| The Three Champions of Swordsoul | `74405783` | [Scripts/c74405783.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74405783.lua) | 1 |
| Kewl Tune RS | `15665977` | [Scripts/c15665977.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c15665977.lua) | 1 |
| ...and 84 more |  |  |  |

## Script Examples

### El Shaddoll Apkallone (`50907446`)

Source: [Scripts/c50907446.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c50907446.lua)

```lua
	local c=e:GetHandler()
	local tc=Duel.GetFirstTarget()
	if tc:IsFaceup() and tc:IsRelateToEffect(e) and tc:IsCanBeDisabledByEffect(e,false) then
		Duel.NegateRelatedChain(tc,RESET_TURN_SET)
		local e1=Effect.CreateEffect(c)
```

### DoSolfachord Coolia (`80776622`)

Source: [Scripts/c80776622.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c80776622.lua)

```lua
end
function c80776622.disfilter(c,e)
	return c:IsFaceup() and c:IsRelateToEffect(e) and c:IsCanBeDisabledByEffect(e,false)
end
function c80776622.disop(e,tp,eg,ep,ev,re,r,rp)
```

### Transonic Bird (`34072799`)

Source: [Scripts/c34072799.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c34072799.lua)

```lua
	local c=e:GetHandler()
	local tc=Duel.GetFirstTarget()
	if tc:IsFaceup() and tc:IsRelateToEffect(e) and tc:IsCanBeDisabledByEffect(e,false) then
		Duel.NegateRelatedChain(tc,RESET_TURN_SET)
		local e1=Effect.CreateEffect(c)
```
