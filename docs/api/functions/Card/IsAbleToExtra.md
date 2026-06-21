# Card.IsAbleToExtra

## Signature

```lua
Card.IsAbleToExtra(Card c) -> bool
```

## Description

Check if c can send extra cards
This function returns false for non-fusion, cohomology, and overdrive cards

## Parameters

- `c` `Card`

## Returns

- `bool`

## Source

- `D:\Programs\GitHub\ygopro-core\libcard.cpp:3586`

## Used By

Generated from the local `Scripts/` folder and `cards.cdb`.

- Detected in **75** indexed script(s).
- Search this function in the [Script Explorer](/tools/script-explorer) with `Card.IsAbleToExtra`.

| Card | ID | Script | Detected Calls |
| --- | ---: | --- | ---: |
| [The Gaze of Timaeus](/examples/cards/22283204) | `22283204` | [Scripts/c22283204.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c22283204.lua) | 62 |
| Plunder Patrollship Jord | `85969517` | [Scripts/c85969517.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c85969517.lua) | 58 |
| Clock Lizard | `51476410` | [Scripts/c51476410.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c51476410.lua) | 58 |
| Exosisters Magnifica | `59242457` | [Scripts/c59242457.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c59242457.lua) | 56 |
| Malefic Paradigm Dragon | `16958382` | [Scripts/c16958382.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c16958382.lua) | 55 |
| Galaxy-Eyes Cipher X Dragon | `28346136` | [Scripts/c28346136.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c28346136.lua) | 54 |
| Madolche Dessert | `51650038` | [Scripts/c51650038.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c51650038.lua) | 53 |
| Lunalight Perfume Dancer | `81196066` | [Scripts/c81196066.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c81196066.lua) | 53 |
| Joyous Melffys | `53054164` | [Scripts/c53054164.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c53054164.lua) | 52 |
| Cynet Circuit | `82886276` | [Scripts/c82886276.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c82886276.lua) | 52 |
| Fusion Substitute | `74335036` | [Scripts/c74335036.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c74335036.lua) | 52 |
| Performage Ball Balancer | `92530005` | [Scripts/c92530005.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c92530005.lua) | 51 |
| Shade the Obscure | `77157846` | [Scripts/c77157846.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c77157846.lua) | 51 |
| Antihuman Intelligence ME-PSY-YA | `58844135` | [Scripts/c58844135.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c58844135.lua) | 51 |
| Artmage Peripeteia -Turmoil- | `17719582` | [Scripts/c17719582.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c17719582.lua) | 50 |
| Sweet Dreams, Nemleria | `44843954` | [Scripts/c44843954.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c44843954.lua) | 50 |
| Gaiarmor Dragonshell | `49816630` | [Scripts/c49816630.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c49816630.lua) | 49 |
| Super All In! | `16780318` | [Scripts/c16780318.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c16780318.lua) | 48 |
| Crimson Dragon Quetzacoatl | `29053656` | [Scripts/c29053656.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c29053656.lua) | 48 |
| Branded Retribution | `17751597` | [Scripts/c17751597.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c17751597.lua) | 48 |
| Salamangreat Burning Shell | `28534130` | [Scripts/c28534130.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c28534130.lua) | 48 |
| Performapal Odd-Eyes Butler | `56677752` | [Scripts/c56677752.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c56677752.lua) | 47 |
| Filia Regis | `70538272` | [Scripts/c70538272.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c70538272.lua) | 47 |
| Junk Warrior/Assault Mode | `23219323` | [Scripts/c23219323.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c23219323.lua) | 47 |
| ...and 51 more |  |  |  |

## Script Examples

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

### Clock Lizard (`51476410`)

Source: [Scripts/c51476410.lua](https://github.com/ElderLich/MDPro3_Sacred_Book/blob/main/Scripts/c51476410.lua)

```lua
end
function c51476410.spfilter3(c,e,tp,chkf,rc)
	if not c:IsType(TYPE_FUSION) or not c:IsAbleToExtra() then return false end
	if Duel.GetLocationCountFromEx(tp,tp,rc,TYPE_FUSION)<=0 then return false end
	local mg=Duel.GetMatchingGroup(c51476410.spfilter0,tp,LOCATION_GRAVE,0,c)
```
