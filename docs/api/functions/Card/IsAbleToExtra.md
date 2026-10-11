# Card.IsAbleToExtra

## Signature

```lua
Card.IsAbleToExtra(Card c) -> bool
```

## Description

Checks whether c can be returned to the Extra Deck by the current reason player.

## Parameters

- `c` `Card`

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3641`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **78** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer?format=standard&mode=code&q=Card.IsAbleToExtra) with `Card.IsAbleToExtra`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [Ashtraja Susanoo](/examples/cards/17020474) | `17020474` | [Scripts/c17020474.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c17020474.lua) | 1 |
| [The Gaze of Timaeus](/examples/cards/22283204) | `22283204` | [Scripts/c22283204.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c22283204.lua) | 1 |
| Plunder Patrollship Jord | `85969517` | [Scripts/c85969517.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c85969517.lua) | 1 |
| Clock Lizard | `51476410` | [Scripts/c51476410.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c51476410.lua) | 1 |
| Exosisters Magnifica | `59242457` | [Scripts/c59242457.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59242457.lua) | 1 |
| Malefic Paradigm Dragon | `16958382` | [Scripts/c16958382.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c16958382.lua) | 1 |
| Galaxy-Eyes Cipher X Dragon | `28346136` | [Scripts/c28346136.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c28346136.lua) | 1 |
| Angelechy Problem | `17782288` | [Scripts/c17782288.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c17782288.lua) | 1 |
| Madolche Dessert | `51650038` | [Scripts/c51650038.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c51650038.lua) | 1 |
| Lunalight Perfume Dancer | `81196066` | [Scripts/c81196066.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c81196066.lua) | 2 |
| Joyous Melffys | `53054164` | [Scripts/c53054164.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c53054164.lua) | 1 |
| Cynet Circuit | `82886276` | [Scripts/c82886276.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c82886276.lua) | 1 |
| Fusion Substitute | `74335036` | [Scripts/c74335036.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74335036.lua) | 1 |
| Performage Ball Balancer | `92530005` | [Scripts/c92530005.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92530005.lua) | 1 |
| Shade the Obscure | `77157846` | [Scripts/c77157846.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c77157846.lua) | 1 |
| Antihuman Intelligence ME-PSY-YA | `58844135` | [Scripts/c58844135.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c58844135.lua) | 1 |
| Artmage Peripeteia -Turmoil- | `17719582` | [Scripts/c17719582.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c17719582.lua) | 1 |
| Sweet Dreams, Nemleria | `44843954` | [Scripts/c44843954.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44843954.lua) | 1 |
| Gaiarmor Dragonshell | `49816630` | [Scripts/c49816630.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c49816630.lua) | 1 |
| Super All In! | `16780318` | [Scripts/c16780318.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c16780318.lua) | 1 |
| Crimson Dragon Quetzalcoatl | `29053656` | [Scripts/c29053656.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c29053656.lua) | 1 |
| Branded Retribution | `17751597` | [Scripts/c17751597.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c17751597.lua) | 2 |
| Salamangreat Burning Shell | `28534130` | [Scripts/c28534130.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c28534130.lua) | 1 |
| Performapal Odd-Eyes Butler | `56677752` | [Scripts/c56677752.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c56677752.lua) | 1 |
| ...and 54 more |  |  |  |

## Script Examples

### Ashtraja Susanoo (`17020474`)

Source: [Scripts/c17020474.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c17020474.lua)

```lua
	if chk==0 then return Duel.IsExistingTarget(s.tgfilter,tp,LOCATION_GRAVE+LOCATION_REMOVED,0,1,nil,e,tp) end
	local ct=1
	if c:IsAbleToExtra() then ct=2 end
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_OPERATECARD)
	local g=Duel.SelectTarget(tp,s.tgfilter,tp,LOCATION_GRAVE+LOCATION_REMOVED,0,1,ct,nil,e,tp)
```

### The Gaze of Timaeus (`22283204`)

Source: [Scripts/c22283204.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c22283204.lua)

```lua
	local code=tc:GetCode()
	if tc and tc:IsRelateToChain() and aux.NecroValleyFilter()(tc) and not tc:IsImmuneToEffect(e)
		and (tc:IsAbleToDeck() or tc:IsAbleToExtra()) then
		Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_SPSUMMON)
		local sg=Duel.SelectMatchingCard(tp,s.fusfilter,tp,LOCATION_EXTRA,0,1,1,nil,e,tp,code,tc)
```

### Plunder Patrollship Jord (`85969517`)

Source: [Scripts/c85969517.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c85969517.lua)

```lua
	local c=e:GetHandler()
	if chk==0 then
		if not c:IsAbleToExtra() or Duel.GetMZoneCount(tp,c)<=0
			or Duel.GetMZoneCount(1-tp,c,tp)<=0 or Duel.IsPlayerAffectedByEffect(tp,59822133) then
			return false
```
